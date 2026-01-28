# -*- coding: utf-8 -*-
"""
PCD文件加载工具模块
"""
import numpy as np
from typing import Dict, Optional, Tuple
from pathlib import Path
import zlib
import struct
from app.common.logger import logger

class PCDLoader:
    """PCD文件加载器 (支持 ASCII, Binary, Binary Compressed)"""
    
    @staticmethod
    def load(file_path: str, step: int = 1) -> Dict[str, np.ndarray]:
        """
        加载PCD文件
        
        Args:
            file_path: 文件路径
            step: 降采样步长 (1=全量, >1=降采样)
            
        Returns:
            Dict containing:
                'xyz': np.ndarray (N, 3) float32
                'rgb': np.ndarray (N, 3) float32 (0-1), optional
                'intensity': np.ndarray (N,) float32, optional
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        # 读取头信息
        header = PCDLoader._read_header(path)
        data_type = header['data_type']
        fields = header['fields']
        points_count = header['points']
        
        if points_count == 0:
            return {'xyz': np.empty((0, 3), dtype=np.float32)}

        # 针对 binary_compressed 格式，必须使用 Open3D 加载
        if data_type == 'binary_compressed':
            try:
                # 仅引入必要的 Open3D 模块，避免全量引入触发无关依赖（如 plotly, jinja2 等）
                # 注意：Open3D 0.16+ 默认导入会触发懒加载，这里我们尝试只使用 IO 功能
                import open3d as o3d
                # 显式设置不使用可视化功能（如果支持），减少依赖触发
                if hasattr(o3d, "visualization"):
                    pass # 仅作为占位，实际无法完全禁用，但表明意图

                import os
                import tempfile
                import shutil
                
                load_path = str(file_path)
                is_temp = False
                
                # Open3D on Windows 可能会因为中文路径导致编码错误 (utf-8 codec can't decode byte ...)
                # 如果路径包含非 ASCII 字符，创建一个纯 ASCII 的临时文件链接/副本进行加载
                if not all(ord(c) < 128 for c in load_path):
                    try:
                        fd, temp_path = tempfile.mkstemp(suffix='.pcd')
                        os.close(fd)
                        os.remove(temp_path) # mkstemp 创建了文件，需要删除以便 link/copy
                        
                        # 优先尝试硬链接 (速度快，秒级)
                        try:
                            os.link(load_path, temp_path)
                        except OSError:
                            # 跨驱动器无法硬链接，回退到复制 (速度较慢)
                            logger.info(f"Copying PCD to temp file for ASCII path compatibility: {temp_path}")
                            shutil.copy2(load_path, temp_path)
                            
                        load_path = temp_path
                        is_temp = True
                    except Exception as e:
                        logger.warning(f"Failed to create temp ASCII path for {file_path}: {e}")
                        # 回退到原始路径尝试
                        load_path = str(file_path)
                        is_temp = False

                try:
                    pcd = o3d.io.read_point_cloud(load_path)
                finally:
                    # 清理临时文件
                    if is_temp and os.path.exists(load_path):
                        try:
                            os.remove(load_path)
                        except:
                            pass
                
                # 转换 XYZ
                xyz = np.asarray(pcd.points, dtype=np.float32)
                
                # 降采样
                if step > 1:
                    xyz = xyz[::step]
                    
                result = {'xyz': xyz}
                
                # 转换 RGB
                if pcd.has_colors():
                    rgb = np.asarray(pcd.colors, dtype=np.float32)
                    if step > 1:
                        rgb = rgb[::step]
                    result['rgb'] = rgb
                
                return result
                
            except ImportError as e:
                error_msg = f"Failed to import Open3D: {e}. Open3D is required to load binary_compressed PCD files. Please install it using: pip install open3d"
                logger.error(error_msg)
                raise RuntimeError(error_msg)
            except Exception as e:
                logger.error(f"Open3D failed to load PCD: {e}")
                raise e

        # 原生加载逻辑 (作为 fallback 或用于 ASCII/Binary)
        
        # 读取数据
        data = PCDLoader._read_data(path, header)
        
        # 解析字段
        result = PCDLoader._parse_fields(data, fields, header['sizes'], header['types'], points_count)
        
        # 降采样
        if step > 1:
            for key in result:
                result[key] = result[key][::step]
                
        return result

    @staticmethod
    def _lzf_decompress(data, out_len):
        """
        Pure Python LZF decompression implementation.
        """
        i = 0
        o = 0
        output = bytearray(out_len)
        data_len = len(data)
        
        while i < data_len:
            ctrl = data[i]
            i += 1
            
            if ctrl < 32:
                # Literal run
                length = ctrl + 1
                if o + length > out_len:
                    length = out_len - o
                
                output[o:o+length] = data[i:i+length]
                o += length
                i += length
            else:
                # Back reference
                length = ctrl >> 5
                ref = o - ((ctrl & 0x1f) << 8) - 1
                
                if length == 7:
                    length += data[i]
                    i += 1
                
                ref -= data[i]
                i += 1
                
                length += 2
                
                if o + length > out_len:
                    length = out_len - o
                    
                if ref < 0:
                    pass
                
                # Copy from reference
                if o - ref >= length:
                    output[o:o+length] = output[ref:ref+length]
                else:
                    # Overlapping copy
                    for k in range(length):
                        output[o+k] = output[ref+k]
                
                o += length
                
        return output

    @staticmethod
    def _read_header(path: Path) -> dict:
        header = {
            'fields': [], 'sizes': [], 'types': [], 'counts': [],
            'width': 0, 'height': 1, 'points': 0, 'data_type': 'ascii',
            'header_len': 0
        }
        
        with path.open('rb') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                
                line_str = line.decode('utf-8', errors='ignore').strip()
                if not line_str or line_str.startswith('#'):
                    continue
                
                parts = line_str.split()
                key = parts[0].upper()
                
                if key == 'FIELDS':
                    header['fields'] = parts[1:]
                elif key == 'SIZE':
                    header['sizes'] = [int(x) for x in parts[1:]]
                elif key == 'TYPE':
                    header['types'] = parts[1:]
                elif key == 'COUNT':
                    header['counts'] = [int(x) for x in parts[1:]]
                elif key == 'WIDTH':
                    header['width'] = int(parts[1])
                elif key == 'HEIGHT':
                    header['height'] = int(parts[1])
                elif key == 'POINTS':
                    header['points'] = int(parts[1])
                elif key == 'DATA':
                    header['data_type'] = parts[1].lower()
                    header['header_len'] = f.tell()
                    break
        
        # 补全默认值
        if not header['counts']:
            header['counts'] = [1] * len(header['fields'])
        
        return header

    @staticmethod
    def _read_data(path: Path, header: dict) -> bytes:
        if header['data_type'] == 'ascii':
            # ASCII 读取特殊处理，直接返回行列表
            with path.open('r', encoding='utf-8', errors='ignore') as f:
                f.seek(header['header_len'])
                return f.read().splitlines()
        
        elif header['data_type'] == 'binary':
            with path.open('rb') as f:
                f.seek(header['header_len'])
                return f.read()
                
        elif header['data_type'] == 'binary_compressed':
            # This branch should now only be reached if someone bypassed the check above,
            # or if we decide to re-enable internal support later.
            # But based on current requirements, we throw an error if Open3D failed/missing above.
            # However, for robustness, if we are here it means we fell through (which shouldn't happen for binary_compressed).
            # We'll just return empty or raise.
            raise RuntimeError("Internal binary_compressed loader is disabled. Please install Open3D.")
        
        return b''

    @staticmethod
    def _parse_fields(raw_data, fields, sizes, types, count) -> dict:
        result = {}
        
        # 映射字段索引
        try:
            x_idx = fields.index('x')
            y_idx = fields.index('y')
            z_idx = fields.index('z')
        except ValueError:
            return {'xyz': np.empty((0, 3), dtype=np.float32)}

        # 构造 dtype
        dtype_list = []
        used_field_names = set()
        
        for i, field in enumerate(fields):
            type_char = types[i].upper()
            size = sizes[i]
            
            if type_char == 'F':
                np_type = np.float32 if size == 4 else np.float64
            elif type_char == 'I':
                np_type = {1: np.int8, 2: np.int16, 4: np.int32}.get(size, np.int32)
            elif type_char == 'U':
                np_type = {1: np.uint8, 2: np.uint16, 4: np.uint32}.get(size, np.uint32)
            else:
                np_type = np.float32
            
            # 处理重复字段名 (如 padding 字段 '_')，Numpy 要求结构化数组字段名唯一
            unique_field = field
            rename_count = 0
            while unique_field in used_field_names:
                rename_count += 1
                unique_field = f"{field}_{rename_count}"
            
            used_field_names.add(unique_field)
            dtype_list.append((unique_field, np_type))

        if isinstance(raw_data, list): # ASCII
            data_array = np.genfromtxt(raw_data, dtype=dtype_list)
        else: # Binary
            # 检查数据长度是否对齐
            dtype_obj = np.dtype(dtype_list)
            itemsize = dtype_obj.itemsize
            
            if len(raw_data) % itemsize != 0:
                remainder = len(raw_data) % itemsize
                logger.warning(f"PCD binary data length ({len(raw_data)}) is not a multiple of item size ({itemsize}). Trimming {remainder} bytes.")
                raw_data = raw_data[:-remainder]
            
            try:
                data_array = np.frombuffer(raw_data, dtype=dtype_list)
            except Exception as e:
                logger.error(f"Failed to load PCD binary buffer: {e}")
                return {'xyz': np.empty((0, 3), dtype=np.float32)}

        # 检查点数是否符合预期
        if len(data_array) != count:
            logger.warning(f"PCD points count mismatch: header says {count}, but loaded {len(data_array)}")

        # 确保数据点数量不超过 count
        if len(data_array) > count:
            data_array = data_array[:count]

        # 提取坐标
        x = data_array['x'].astype(np.float32)
        y = data_array['y'].astype(np.float32)
        z = data_array['z'].astype(np.float32)
        result['xyz'] = np.column_stack((x, y, z))

        # 提取 RGB
        if 'rgb' in fields:
            rgb_raw = data_array['rgb']
            rgb_int = rgb_raw.view(np.uint32) if rgb_raw.dtype == np.float32 else rgb_raw.astype(np.uint32)
            
            r = ((rgb_int >> 16) & 0xFF) / 255.0
            g = ((rgb_int >> 8) & 0xFF) / 255.0
            b = ((rgb_int) & 0xFF) / 255.0
            result['rgb'] = np.column_stack((r, g, b))
            
        elif 'r' in fields and 'g' in fields and 'b' in fields:
            r = data_array['r'].astype(np.float32) / 255.0
            g = data_array['g'].astype(np.float32) / 255.0
            b = data_array['b'].astype(np.float32) / 255.0
            result['rgb'] = np.column_stack((r, g, b))

        # 提取强度
        if 'intensity' in fields:
            result['intensity'] = data_array['intensity'].astype(np.float32)

        return result
