# -*- coding: utf-8 -*-
"""
STL文件加载器模块

使用Open3D库加载STL文件 (ASCII/Binary)。
"""
import numpy as np
from typing import Dict, Any, Optional
from app.common.logger import logger

try:
    import open3d as o3d
    OPEN3D_AVAILABLE = True
except ImportError:
    OPEN3D_AVAILABLE = False
    logger.error("Open3D not available. STL loading will not work.")

class STLLoader:
    """STL文件加载器"""
    
    @staticmethod
    def load(file_path: str) -> Dict[str, Any]:
        """
        加载STL文件
        
        Args:
            file_path: STL文件路径
            
        Returns:
            Dict containing:
            - vertices: (N, 3) float32 array
            - faces: (M, 3) int32 array (optional)
            - normals: (N, 3) float32 array (optional)
            
        Raises:
            RuntimeError: If Open3D is not installed
            ValueError: If file is empty or invalid
            Exception: For other loading errors
        """
        if not OPEN3D_AVAILABLE:
            error_msg = "Open3D is not installed. Cannot load STL file."
            logger.error(error_msg)
            raise RuntimeError(error_msg)
            
        logger.info(f"Loading STL file: {file_path}")
        
        # Open3D 自动检测文件格式 (ASCII/Binary)
        
        # 处理 Windows 下 Open3D 中文路径加载问题
        import os
        import tempfile
        import shutil
        
        # 预先检查文件大小
        try:
            file_size = os.path.getsize(file_path)
            # Binary STL header (80) + count (4) = 84 bytes. If size <= 84, it's likely empty.
            # ASCII "solid " is 6 bytes.
            if file_size <= 84:
                # 进一步检查是否为纯 header 的空 binary STL
                if file_size == 84:
                    with open(file_path, 'rb') as f:
                        f.seek(80)
                        count = int.from_bytes(f.read(4), byteorder='little')
                        if count == 0:
                            raise ValueError("STL file is empty (0 triangles defined).")
                elif file_size == 0:
                     raise ValueError("File is empty (0 bytes).")
        except OSError as e:
            logger.error(f"Failed to check file size: {e}")
            # Continue trying to load via Open3D regardless
        
        load_path = str(file_path)
        is_temp = False
        
        # 如果路径包含非 ASCII 字符，创建一个纯 ASCII 的临时文件链接/副本进行加载
        if not all(ord(c) < 128 for c in load_path):
            try:
                fd, temp_path = tempfile.mkstemp(suffix='.stl')
                os.close(fd)
                os.remove(temp_path) # mkstemp 创建了文件，需要删除以便 link/copy
                
                # 优先尝试硬链接 (速度快，秒级)
                try:
                    os.link(load_path, temp_path)
                except OSError:
                    # 跨驱动器无法硬链接，回退到复制 (速度较慢)
                    logger.info(f"Copying STL to temp file for ASCII path compatibility: {temp_path}")
                    shutil.copy2(load_path, temp_path)
                    
                load_path = temp_path
                is_temp = True
            except Exception as e:
                logger.warning(f"Failed to create temp ASCII path for {file_path}: {e}")
                # 回退到原始路径尝试
                load_path = str(file_path)
                is_temp = False

        try:
            # 禁用 Assimp 警告输出到控制台 (Open3D 可能会直接打印)
            # o3d.utility.set_verbosity_level(o3d.utility.VerbosityLevel.Error)
            
            mesh = o3d.io.read_triangle_mesh(load_path)
        except Exception as e:
            raise RuntimeError(f"Open3D failed to read mesh: {e}")
        finally:
            # 清理临时文件
            if is_temp and os.path.exists(load_path):
                try:
                    os.remove(load_path)
                except:
                    pass
        
        if not mesh.has_vertices():
            logger.warning(f"STL file has no vertices: {file_path}")
            raise ValueError("STL file has no vertices (empty mesh).")
            
        # 确保计算法线以获得更好的渲染效果
        if not mesh.has_vertex_normals():
            mesh.compute_vertex_normals()
            
        vertices = np.asarray(mesh.vertices, dtype=np.float32)
        faces = np.asarray(mesh.triangles, dtype=np.int32)
        normals = np.asarray(mesh.vertex_normals, dtype=np.float32) if mesh.has_vertex_normals() else None
        
        logger.info(f"Loaded STL: {len(vertices)} vertices, {len(faces)} faces")
        
        result = {
            'vertices': vertices,
            'faces': faces,
            'normals': normals
        }
        return result
