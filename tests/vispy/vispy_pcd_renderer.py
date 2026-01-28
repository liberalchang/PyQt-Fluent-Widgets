# -*- coding: utf-8 -*-
"""
Vispy PCD渲染器模块

使用vispy库实现3D点云可视化。
"""
import numpy as np
from typing import List, Optional, Tuple, Dict, Union
from pathlib import Path
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor

try:
    from vispy import scene, app as vispy_app
    from vispy.scene import SceneCanvas
    from vispy.scene.visuals import Markers, Line, Image, Mesh
    from vispy.visuals.transforms import MatrixTransform
    VISPY_AVAILABLE = True
except ImportError:
    VISPY_AVAILABLE = False
    SceneCanvas = QWidget  # 降级为普通Widget

from app.common.logger import logger
from app.core.managers.signal_manager import signalManager
from app.core.utils.pcd_loader import PCDLoader
from app.core.utils.image_loader import ImageLoader
from app.core.utils.stl_loader import STLLoader


def initialize_vispy():
    """初始化Vispy后端"""
    if VISPY_AVAILABLE:
        try:
            # 优先使用 PySide6
            vispy_app.use_app('pyside6')
            logger.info("Vispy backend set to PySide6")
        except Exception as e:
            logger.warning(f"Failed to set vispy backend: {e}")


class VispyPointCloudEntry:
    """单个点云实体"""
    def __init__(self, parent_view, data: dict, file_path: str, color: QColor = QColor(255, 255, 255)):
        self.view = parent_view
        self.file_path = file_path
        self.data = data
        self.xyz = data['xyz']
        self.base_color = color
        self.visible = True
        self.point_size = 3
        self.color_mode = 'single'
        
        self.markers = Markers(parent=self.view.scene)
        self.markers.interactive = False

        if VISPY_AVAILABLE and self.markers is not None:
            # 设置为不透明渲染，开启深度测试并关闭混合，避免点重叠时的透明度叠加导致“阴影”效果
            #- opaque （预设）
            # - 用于配置该可视对象的 OpenGL 渲染为“不透明”。
            # - 典型效果是禁用颜色混合、启用深度测试，让前后遮挡按真实几何关系呈现，而不会出现半透明叠加导致的区域变暗。
            # - depth_test=True
            # - 开启深度测试（Z-Buffer）。
            # - 片元在写入前会与当前深度缓冲比较，仅距离摄像机更近的片元会通过测试并显示，实现正确的遮挡关系。
            # - blend=False
            # - 关闭颜色混合（Blending）。
            # - 片元颜色直接写入帧缓冲，不与已有颜色做透明度叠加，可避免密集重叠点产生的“阴影”观感。
            self.markers.set_gl_state('opaque', depth_test=True, blend=False)

        self.update_visual()

    def update_visual(self, color_mode: str = None):
        if not self.visible:
            self.markers.visible = False
            return
            
        if color_mode is not None:
            self.color_mode = color_mode
            
        self.markers.visible = True
        colors = self._get_colors(self.color_mode)
        
        # 自适应选择 symbol (Adaptive Symbol)
        # < 50w 点: disc (圆形，边缘平滑，美观但Shader开销稍大)
        # >= 50w 点: square (方形，最基础形态，渲染性能最高)
        # 大数据量下，像素级的小点形状差异难以察觉，但方形能显著降低Fragment Shader压力
        symbol = 'disc'
        if len(self.xyz) > 500000:
            symbol = 'square'
        
        self.markers.set_data(
            pos=self.xyz,
            face_color=colors,
            edge_width=0,
            size=self.point_size,
            symbol=symbol
        )

    def _get_colors(self, mode: str):
        count = len(self.xyz)
        
        if mode == 'rgb':
            has_rgb = 'rgb' in self.data
            logger.info(f"[_get_colors] mode={mode}, has_rgb={has_rgb}")
            if has_rgb:
                rgb_val = self.data['rgb']
                logger.info(f"[_get_colors] RGB shape: {rgb_val.shape}, dtype: {rgb_val.dtype}, range: [{rgb_val.min():.2f}, {rgb_val.max():.2f}]")
                logger.info(f"[_get_colors] First pixel: {rgb_val[0]}")
                
                # 强制转换为 float32 并返回
                rgb = rgb_val.astype(np.float32)
                return np.column_stack((rgb, np.ones(count, dtype=np.float32)))
            else:
                logger.warning("[_get_colors] Mode is RGB but 'rgb' data is missing!")

        elif mode == 'intensity' and 'intensity' in self.data:
            intensity = self.data['intensity']
            # 简单的归一化映射到灰度/热力图
            if len(intensity) > 0:
                i_min, i_max = intensity.min(), intensity.max()
                if i_max > i_min:
                    norm = (intensity - i_min) / (i_max - i_min)
                else:
                    norm = np.zeros_like(intensity)
                # 使用 viridis 风格或其他 (这里简单用灰度)
                # return np.column_stack((norm, norm, norm, np.ones(count)))
                
                # 热力图风格 (R=Intensity, G=0, B=1-Intensity)
                return np.column_stack((norm, np.zeros_like(norm), 1-norm, np.ones(count, dtype=np.float32)))
                
        elif mode == 'height':
            z = self.xyz[:, 2]
            if len(z) > 0:
                z_min, z_max = z.min(), z.max()
                if z_max > z_min:
                    norm = (z - z_min) / (z_max - z_min)
                else:
                    norm = np.zeros_like(z)
                # 彩虹色映射 (简单实现)
                return np.column_stack((norm, 1-np.abs(norm-0.5)*2, 1-norm, np.ones(count, dtype=np.float32)))
        
        # 默认使用单一颜色
        r, g, b, a = self.base_color.redF(), self.base_color.greenF(), self.base_color.blueF(), 1.0
        return (r, g, b, a)

    def set_visible(self, visible: bool):
        self.visible = visible
        self.markers.visible = visible

    def set_color(self, color: QColor):
        self.base_color = color
        
    def set_size(self, size: int):
        self.point_size = size
        self.update_visual()

    def destroy(self):
        self.markers.parent = None


class VispyMeshEntry:
    """单个网格实体 (STL)"""
    def __init__(self, parent_view, data: dict, file_path: str, color: QColor = QColor(200, 200, 200)):
        self.view = parent_view
        self.file_path = file_path
        self.data = data
        self.vertices = data['vertices']
        self.faces = data['faces']
        self.base_color = color
        self.visible = True
        
        # 创建 Mesh visual
        self.mesh = Mesh(vertices=self.vertices, faces=self.faces, 
                         color=self.base_color.name(), shading='smooth', parent=self.view.scene)
        
        if VISPY_AVAILABLE:
             self.mesh.set_gl_state('opaque', depth_test=True, blend=False)

    @property
    def xyz(self):
        return self.vertices

    def update_visual(self, color_mode: str = None):
        # Mesh 目前只支持单一颜色，忽略 color_mode
        if not self.visible:
            self.mesh.visible = False
            return
            
        self.mesh.visible = True
        self.mesh.color = self.base_color.name()

    def set_visible(self, visible: bool):
        self.visible = visible
        self.mesh.visible = visible

    def set_color(self, color: QColor):
        self.base_color = color
        self.update_visual()
        
    def set_size(self, size: int):
        pass

    def destroy(self):
        self.mesh.parent = None


class VispyImageEntry:
    """单个图片实体 (3D平面纹理)"""
    def __init__(self, parent_view, image_data: np.ndarray, file_path: str, x_offset: float, scale: float = 0.1):
        """
        初始化图片实体
        
        Args:
            scale: 图片缩放比例。默认0.1表示缩小10倍。
                   数值越小图片越小 (e.g. 0.01 = 缩小100倍)。
                   理论上只要大于0即可，无硬性下限，但过小会导致不可见。
        """
        self.view = parent_view
        self.file_path = file_path
        self.visible = True
        self.scale = scale
        
        # image_data: (H, W, 4)
        self.height, self.width = image_data.shape[:2]
        self.x_offset = x_offset
        
        self.scaled_width = self.width * scale
        self.scaled_height = self.height * scale
        
        # 创建 Image visual
        # method='auto' 会根据数据类型自动选择
        # 尝试使用 'auto' (通常是 subpixel)，如果失败 (如缺少 vispy 数据文件)，尝试 'impostor' 降级渲染
        # 如果依然失败，尝试 interpolation='nearest' (最邻近插值，不依赖 spatial-filters.npy)
        try:
            self.image_visual = Image(image_data, parent=self.view.scene, method='auto')
        except Exception as e1:
            logger.warning(f"Failed to create Image visual with method='auto': {e1}. Retrying with method='impostor'...")
            try:
                # 降级尝试 1: impostor 模式
                self.image_visual = Image(image_data, parent=self.view.scene, method='impostor')
            except Exception as e2:
                logger.warning(f"Failed to create Image visual with method='impostor': {e2}. Retrying with interpolation='nearest'...")
                try:
                    # 降级尝试 2: nearest 插值 (通常不需要加载 filter kernel)
                    self.image_visual = Image(image_data, parent=self.view.scene, interpolation='nearest')
                except Exception as e3:
                    logger.error(f"All Image visual creation methods failed. Last error: {e3}")
                    raise e3
        
        # 变换位置
        # 目标: XZ平面, Y=0
        # 初始: Image在XY平面 (0,0) -> (W, H)
        # 旋转: 绕X轴旋转90度 -> (x, y, z) -> (x, -z, y) ?
        # 也就是原y轴映射到z轴
        
        transform = MatrixTransform()
        transform.scale((scale, scale, 1))
        transform.rotate(90, (1, 0, 0))
        transform.translate((x_offset, 0, 0))
        
        self.image_visual.transform = transform
        
        # 边界 (用于调整相机)
        # 假设高度映射到 Z
        self.xyz = np.array([
            [x_offset, 0, 0],
            [x_offset + self.scaled_width, 0, 0],
            [x_offset, 0, self.scaled_height],
            [x_offset + self.scaled_width, 0, self.scaled_height]
        ])

    def set_visible(self, visible: bool):
        self.visible = visible
        self.image_visual.visible = visible

    def destroy(self):
        self.image_visual.parent = None


class VispyPcdRenderer(QWidget):
    """基于Vispy的PCD渲染器"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        if not VISPY_AVAILABLE:
            logger.error("Vispy not available! PCD rendering will not work.")
            self._init_fallback_ui()
            return
        
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        
        # 创建vispy画布
        self.canvas = SceneCanvas(keys='interactive', show=False)
        self.native_widget = self.canvas.native
        self.canvas.bgcolor = '#F5F5F5'
        self.native_widget.setAttribute(Qt.WA_AlwaysStackOnTop, False)
        
        self.view = self.canvas.central_widget.add_view()
        self.view.camera = 'turntable'
        self.view.camera.fov = 45
        self.view.camera.distance = 100
        
        # 坐标轴和网格
        scene.visuals.XYZAxis(parent=self.view.scene)
        self._init_grid()
        
        self.vBoxLayout.addWidget(self.native_widget)
        
        # 数据管理
        self.entries: Dict[str, VispyPointCloudEntry] = {}
        self.image_entries: Dict[str, VispyImageEntry] = {}
        self.image_x_offset = 0.0
        
        self.current_point_size = 3
        self.current_color_mode = "single"  # single, intensity, height, rgb
        self.load_mode = "auto" # auto, downsample, full
        
        logger.info("VispyPcdRenderer initialized successfully")

    def _init_grid(self, size: float = 100.0, spacing: float = 10.0):
        # 使用 Line 绘制动态网格，而不是无限大的 GridLines
        # 初始化一个默认的小网格，后续会根据点云范围更新
        self.grid = scene.visuals.Line(pos=np.array([[0,0,0], [0,0,0]]), color=(0.6, 0.6, 0.6, 0.4), method='gl', connect='segments', parent=self.view.scene)
        self.grid.interactive = False
        self._update_grid_extent(np.array([-50, -50, 0]), np.array([50, 50, 0]))

    def _update_grid_extent(self, mn: np.ndarray, mx: np.ndarray):
        """根据点云范围更新网格大小"""
        if not VISPY_AVAILABLE or self.grid is None:
            return
            
        try:
            # 计算网格尺寸和间距
            # 处理 NaN/Inf
            mn = np.nan_to_num(mn, nan=0.0, posinf=100.0, neginf=-100.0)
            mx = np.nan_to_num(mx, nan=0.0, posinf=100.0, neginf=-100.0)

            size_x = float(max(1.0, mx[0] - mn[0]))
            size_y = float(max(1.0, mx[1] - mn[1]))
            size = float(max(size_x, size_y))
            # 动态调整间距，大约显示20个格子
            spacing = max(1.0, size / 20.0)
            
            # 稍微扩大一点范围，避免点云正好在边缘
            size *= 1.2
            half = size / 2.0
            
            # 中心点
            center_x = (mn[0] + mx[0]) / 2.0
            center_y = (mn[1] + mx[1]) / 2.0
            
            # 计算线条数量
            nx = max(1, int(np.ceil(size / spacing)))
            
            # 生成线条坐标
            # 这里简化为以中心点为中心的正方形网格
            xs = np.linspace(center_x - half, center_x + half, nx + 1)
            ys = np.linspace(center_y - half, center_y + half, nx + 1)
            
            segs = []
            # Y方向线条 (X固定)
            for x in xs:
                segs.append([float(x), center_y - half, 0.0])
                segs.append([float(x), center_y + half, 0.0])
                
            # X方向线条 (Y固定)
            for y in ys:
                segs.append([center_x - half, float(y), 0.0])
                segs.append([center_x + half, float(y), 0.0])
                
            pos = np.array(segs, dtype=np.float32)
            self.grid.set_data(pos=pos)
            
        except Exception as e:
            logger.error(f"Error updating grid extent: {e}")

    def _update_scene_bounds(self):
        """更新整个场景的边界和网格"""
        if not self.entries and not self.image_entries:
            return
            
        try:
            mins = []
            maxs = []
            for entry in self.entries.values():
                if entry.visible and len(entry.xyz) > 0:
                    mins.append(entry.xyz.min(axis=0))
                    maxs.append(entry.xyz.max(axis=0))
            
            for entry in self.image_entries.values():
                if entry.visible:
                    # VispyImageEntry.xyz is 4x3 array of corners
                    mins.append(entry.xyz.min(axis=0))
                    maxs.append(entry.xyz.max(axis=0))

            if not mins:
                return

            mn = np.min(np.stack(mins, axis=0), axis=0)
            mx = np.max(np.stack(maxs, axis=0), axis=0)
            
            self._update_grid_extent(mn, mx)
            
        except Exception as e:
            logger.error(f"Error calculating scene bounds: {e}")

    def set_theme(self, is_dark: bool):
        if not VISPY_AVAILABLE: return
        self.canvas.bgcolor = '#202020' if is_dark else '#F5F5F5'
        self.canvas.update()

    def _init_fallback_ui(self):
        from PySide6.QtWidgets import QLabel
        self.vBoxLayout = QVBoxLayout(self)
        label = QLabel("Vispy未安装，无法渲染PCD点云\n请使用: pip install vispy", self)
        label.setAlignment(Qt.AlignCenter)
        self.vBoxLayout.addWidget(label)

    def add_image_file(self, file_path: str) -> bool:
        """加载图片文件"""
        if not VISPY_AVAILABLE: return False
        
        # 1. 如果文件已存在，先移除旧的 (实现重新加载)
        if file_path in self.image_entries:
            logger.info(f"Image already loaded, reloading: {file_path}")
            self.remove_file(file_path)
            # 注意: remove_file 会销毁对象并从字典移除
            
        try:
            data = ImageLoader.load(file_path)
            if data is None:
                signalManager.emit("pcdRendererError", file_path, "Failed to load image data")
                return False
                
            entry = VispyImageEntry(self.view, data, file_path, self.image_x_offset, scale=0.01)
            self.image_entries[file_path] = entry
            
            # 更新下一个图片的起始位置 (x + scaled_width)
            self.image_x_offset += entry.scaled_width
            
            self._update_scene_bounds()
            self.canvas.update()
            
            # 通知加载成功 (虽然不是PCD，但可以复用信号或添加新信号)
            # 这里暂时不发信号，或者发一个通用信号
            logger.info(f"Loaded image {file_path}, offset={entry.x_offset}, width={entry.width}")
            return True
            
        except Exception as e:
            logger.error(f"Error loading image {file_path}: {e}")
            signalManager.emit("pcdRendererError", file_path, str(e))
            return False

    def add_pcd_file(self, file_path: str, color: QColor = None) -> bool:
        if not VISPY_AVAILABLE: return False
        
        # 1. 如果文件已存在，先移除旧的 (实现重新加载)
        if file_path in self.entries:
            logger.info(f"File already loaded, reloading: {file_path}")
            self.remove_file(file_path)
            # 注意: remove_file 会销毁对象并从字典移除
            
        try:
            # 确定加载步长
            step = 1
            if self.load_mode == "downsample":
                step = 5  # 简单写死降采样 1/5
            
            data = PCDLoader.load(file_path, step=step)
            points = data['xyz']
            
            if len(points) == 0:
                signalManager.emit("pcdRendererError", file_path, "No points found")
                return False
                
            # 自动分配颜色
            if color is None:
                import random
                color = QColor(random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
                
            entry = VispyPointCloudEntry(self.view, data, file_path, color)
            entry.point_size = self.current_point_size
            
            # 智能颜色模式选择：如果包含RGB且当前模式为默认(single)，则优先显示RGB
            mode = self.current_color_mode
            if mode == 'single' and 'rgb' in data:
                mode = 'rgb'
                logger.info(f"PCD文件 {Path(file_path).name} 包含RGB数据，初始加载自动切换为 [RGB彩色] 模式，而非使用随机单色")
            elif mode == 'single':
                logger.info(f"PCD文件 {Path(file_path).name} 未包含RGB数据，初始加载使用 [单色] 模式 (颜色: {color.name()})")
            
            entry.update_visual(mode)
            
            self.entries[file_path] = entry
            
            # 自动调整相机 (如果是第一个文件)
            if len(self.entries) == 1:
                self._auto_adjust_camera(points)
            
            # 更新网格范围
            self._update_scene_bounds()
                
            signalManager.emit("pcdRendererLoaded", file_path, len(points))
            return True
            
        except Exception as e:
            logger.error(f"Error loading PCD {file_path}: {e}")
            signalManager.emit("pcdRendererError", file_path, str(e))
            return False

    def add_stl_file(self, file_path: str, color: QColor = None) -> bool:
        """加载STL文件"""
        if not VISPY_AVAILABLE: return False
        
        if file_path in self.entries:
            logger.info(f"File already loaded, reloading: {file_path}")
            self.remove_file(file_path)
            
        try:
            data = STLLoader.load(file_path)
            # STLLoader now raises exceptions for failures/empty files, so data is never None here.
                
            vertices = data['vertices']
            # STLLoader ensures vertices exist, but safe to keep basic check or rely on loader.
            
            if color is None:
                import random
                color = QColor(random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            
            entry = VispyMeshEntry(self.view, data, file_path, color)
            self.entries[file_path] = entry
            
            if len(self.entries) == 1:
                self._auto_adjust_camera(vertices)
                
            self._update_scene_bounds()
            
            signalManager.emit("pcdRendererLoaded", file_path, len(vertices))
            return True
            
        except Exception as e:
            logger.error(f"Error loading STL {file_path}: {e}")
            signalManager.emit("pcdRendererError", file_path, str(e))
            return False

    def remove_file(self, file_path: str):
        """移除文件 (PCD或图片)"""
        if file_path in self.entries:
            self.entries[file_path].destroy()
            del self.entries[file_path]
            self._update_scene_bounds()
            self.canvas.update()
        elif file_path in self.image_entries:
            self.image_entries[file_path].destroy()
            del self.image_entries[file_path]
            self._update_scene_bounds()
            self.canvas.update()

    def set_file_visible(self, file_path: str, visible: bool):
        if file_path in self.entries:
            self.entries[file_path].set_visible(visible)
            self._update_scene_bounds()
            self.canvas.update()
        elif file_path in self.image_entries:
            self.image_entries[file_path].set_visible(visible)
            self._update_scene_bounds()
            self.canvas.update()
            
    def set_file_color(self, file_path: str, color: QColor):
        if file_path in self.entries:
            self.entries[file_path].set_color(color)
            self.entries[file_path].update_visual(self.current_color_mode)
            self.canvas.update()

    def clear_all(self):
        for entry in self.entries.values():
            entry.destroy()
        self.entries.clear()
        
        for entry in self.image_entries.values():
            entry.destroy()
        self.image_entries.clear()
        self.image_x_offset = 0.0
        
        self._update_scene_bounds()
        self.canvas.update()

    def set_point_size(self, size: int):
        self.current_point_size = size
        for entry in self.entries.values():
            entry.set_size(size)
        self.canvas.update()

    def set_color_mapping(self, mode: str):
        """
        设置颜色映射模式
        
        支持的模式说明：
        1. 强度 (Intensity): 根据激光雷达的反射强度显示颜色。通常用于区分不同材质（如车道线、路牌反射率较高）。
           映射方式：归一化强度值 -> 颜色渐变 (如黑->白 或 热力图)。
           
        2. 高度 (Height): 根据点云的 Z 轴高度显示颜色。用于观察地形起伏或物体高度。
           映射方式：Z值归一化 -> 彩虹色 (蓝->绿->红)。
           
        3. RGB: 使用点云文件中自带的 RGB 颜色信息。
           来源：通常由相机与激光雷达融合生成，或者是彩色激光雷达数据。
           注意：如果文件不包含 RGB 字段，此模式无效（通常回退到单色）。
           
        4. 单色 (Single/Monochrome): 所有点使用统一的单一颜色。
           用途：当需要同时查看多个点云文件时，用不同单色区分不同文件（如 红色=基准，白色=当前）。
        
        Args:
            mode: 模式名称 ("强度", "高度", "RGB", "单色" 或 英文 keys)
        """
        # mode: 强度, 高度, RGB, 单色
        mapping = {
            "强度": "intensity", "intensity": "intensity",
            "高度": "height", "height": "height",
            "RGB": "rgb", "rgb": "rgb",
            "单色": "single", "single": "single"
        }
        target_mode = mapping.get(mode, "single")
        self.current_color_mode = target_mode
        
        for entry in self.entries.values():
            entry.update_visual(target_mode)
        self.canvas.update()

    def set_load_mode(self, mode: str):
        # mode: 自动, 降采样, 完整加载
        mapping = {
            "自动": "auto", "auto": "auto",
            "降采样": "downsample", "downsample": "downsample",
            "完整加载": "full", "full": "full"
        }
        self.load_mode = mapping.get(mode, "auto")
        # 注意：更改加载模式不影响已加载的文件，只影响后续加载

    def set_view_mode(self, mode: str):
        if not VISPY_AVAILABLE: return
        
        if "顶" in mode or "top" in mode.lower():
            self.view.camera.elevation = 90
            self.view.camera.azimuth = 0
        elif "前" in mode or "front" in mode.lower():
            self.view.camera.elevation = 0
            self.view.camera.azimuth = 0
        elif "侧" in mode or "side" in mode.lower():
            self.view.camera.elevation = 0
            self.view.camera.azimuth = 90
        else:  # 自由视角
            self.view.camera.elevation = 30
            self.view.camera.azimuth = 45
        
        self.canvas.update()

    def _auto_adjust_camera(self, points: np.ndarray):
        if len(points) == 0: return
        min_bounds = points.min(axis=0)
        max_bounds = points.max(axis=0)
        
        # 检查是否包含 NaN/Inf
        if not (np.isfinite(min_bounds).all() and np.isfinite(max_bounds).all()):
            logger.warning("Point cloud bounds contain NaN or Inf, skipping camera adjustment.")
            return

        center = (min_bounds + max_bounds) / 2
        extent = np.linalg.norm(max_bounds - min_bounds)
        
        # 检查 extent 是否为 NaN (如果 min/max 包含 Inf，相减可能得到 NaN)
        if not np.isfinite(extent) or extent == 0:
             extent = 1.0 # Fallback
             
        self.view.camera.center = center
        self.view.camera.distance = extent * 1.5
        # 关键修复：设置 scale_factor，确保平移操作的灵敏度与场景尺度匹配
        # 如果不设置，scale_factor 默认为 1，在查看大尺寸 PCD 时会导致 Shift+拖拽 平移极其缓慢
        self.view.camera.scale_factor = extent
