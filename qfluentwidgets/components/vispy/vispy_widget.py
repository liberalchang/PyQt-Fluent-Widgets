# coding:utf-8
"""
Vispy Widget 控件层模块

提供 VispyWidget2D 和 VispyWidget3D 控件，集成主题管理和数据接口。
"""
from typing import Union, Tuple, Optional
import numpy as np
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

try:
    from vispy import app as vispy_app
    VISPY_AVAILABLE = True
except ImportError:
    VISPY_AVAILABLE = False

from .vispy_canvas import VispyCanvas2D, VispyCanvas3D
from .vispy_visuals import (
    LineEntry, MarkersEntry, RectangleEntry, EllipseEntry,
    PolygonEntry, ImageEntry, TextEntry, MeshEntry,
    SurfacePlotEntry, VolumeEntry, AxesEntry, GridLinesEntry
)
from qfluentwidgets.common.style_sheet import isDarkTheme


class VispyWidget2D(QWidget):
    """2D Vispy 图形控件
    
    提供 2D 图形绘制功能，支持折线、散点、矩形、椭圆、多边形、图像等元素。
    """
    
    # 信号
    visualAdded = Signal(str)  # visual_id
    visualRemoved = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        if not VISPY_AVAILABLE:
            self._init_fallback_ui()
            return
        
        # 创建布局
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        
        # 创建 2D Canvas
        self.canvas = VispyCanvas2D()
        
        if self.canvas.native_widget:
            self.vBoxLayout.addWidget(self.canvas.native_widget)
        
        # 初始化主题
        self.set_theme(isDarkTheme())
        
    def _init_fallback_ui(self):
        """Vispy 不可用时的降级 UI"""
        self.vBoxLayout = QVBoxLayout(self)
        label = QLabel("Vispy 未安装，无法渲染图形\n请使用: pip install 'PySide6-Fluent-Widgets[full]'", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: #666; font-size: 14px;")
        self.vBoxLayout.addWidget(label)
        self.canvas = None
        
    def set_theme(self, is_dark: bool) -> None:
        """设置主题
        
        Args:
            is_dark: 是否为暗色主题
        """
        if self.canvas:
            self.canvas.set_theme(is_dark)
    
    # ==================== 2D 绘图接口 ====================
    
    def add_line(self, pos: np.ndarray, color: Union[str, tuple] = 'white',
                 width: float = 1.0) -> str:
        """添加 2D 折线/曲线
        
        Args:
            pos: 形状 (N, 2)，N 个点的 x/y 坐标
            color: 颜色，如 'red' 或 (1, 0, 0, 1)
            width: 线宽
            
        Returns:
            visual_id
        """
        if not self.canvas:
            return ""
        
        visual_id = self.canvas._generate_visual_id()
        entry = LineEntry(self.canvas.view, visual_id, pos, color, width)
        self.canvas.add_visual(entry)
        self.visualAdded.emit(visual_id)
        return visual_id
    
    def add_markers(self, pos: np.ndarray, colors: Union[str, np.ndarray] = 'white',
                    sizes: Union[float, np.ndarray] = 5.0, symbol: str = 'o') -> str:
        """添加 2D 散点标记
        
        Args:
            pos: 形状 (N, 2)，N 个点的 x/y 坐标
            colors: 单一颜色或每个点的颜色数组
            sizes: 统一大小或每个点的大小
            symbol: 符号类型：'o', 's', '^', 'd' 等
            
        Returns:
            visual_id
        """
        if not self.canvas:
            return ""
        
        visual_id = self.canvas._generate_visual_id()
        entry = MarkersEntry(self.canvas.view, visual_id, pos, colors, sizes, symbol)
        self.canvas.add_visual(entry)
        self.visualAdded.emit(visual_id)
        return visual_id
    
    def add_rectangle(self, pos: tuple, size: tuple, color: Union[str, tuple] = 'white',
                      border_color: Optional[Union[str, tuple]] = None) -> str:
        """添加 2D 矩形
        
        Args:
            pos: 左上角坐标 (x, y)
            size: 尺寸 (width, height)
            color: 填充颜色
            border_color: 边框颜色
            
        Returns:
            visual_id
        """
        if not self.canvas:
            return ""
        
        visual_id = self.canvas._generate_visual_id()
        entry = RectangleEntry(self.canvas.view, visual_id, pos, size, color, border_color)
        self.canvas.add_visual(entry)
        self.visualAdded.emit(visual_id)
        return visual_id
    
    def add_ellipse(self, center: tuple, radius: Union[float, tuple],
                    color: Union[str, tuple] = 'white') -> str:
        """添加 2D 椭圆/圆形
        
        Args:
            center: 中心点 (x, y)
            radius: 半径（圆）或 (rx, ry)（椭圆）
            color: 填充颜色
            
        Returns:
            visual_id
        """
        if not self.canvas:
            return ""
        
        visual_id = self.canvas._generate_visual_id()
        entry = EllipseEntry(self.canvas.view, visual_id, center, radius, color)
        self.canvas.add_visual(entry)
        self.visualAdded.emit(visual_id)
        return visual_id
    
    def add_polygon(self, pos: np.ndarray, color: Union[str, tuple] = 'white',
                    border_color: Optional[Union[str, tuple]] = None) -> str:
        """添加 2D 多边形
        
        Args:
            pos: 形状 (N, 2)，N 个顶点的 x/y 坐标
            color: 填充颜色
            border_color: 边框颜色
            
        Returns:
            visual_id
        """
        if not self.canvas:
            return ""
        
        visual_id = self.canvas._generate_visual_id()
        entry = PolygonEntry(self.canvas.view, visual_id, pos, color, border_color)
        self.canvas.add_visual(entry)
        self.visualAdded.emit(visual_id)
        return visual_id
    
    def add_image(self, data: np.ndarray, pos: tuple = (0, 0),
                  interpolation: str = 'nearest') -> str:
        """添加 2D 图像
        
        Args:
            data: 图像数据 (H, W) 或 (H, W, 3/4)
            pos: 左下角位置
            interpolation: 插值方式
            
        Returns:
            visual_id
        """
        if not self.canvas:
            return ""
        
        visual_id = self.canvas._generate_visual_id()
        entry = ImageEntry(self.canvas.view, visual_id, data, pos, interpolation)
        self.canvas.add_visual(entry)
        self.visualAdded.emit(visual_id)
        return visual_id
    
    def add_text(self, text: str, pos: tuple, font_size: float = 12,
                 color: Union[str, tuple] = 'white') -> str:
        """添加 2D 文本标注
        
        Args:
            text: 文本内容
            pos: 位置 (x, y)
            font_size: 字体大小
            color: 文本颜色
            
        Returns:
            visual_id
        """
        if not self.canvas:
            return ""
        
        visual_id = self.canvas._generate_visual_id()
        entry = TextEntry(self.canvas.view, visual_id, text, pos, font_size, color)
        self.canvas.add_visual(entry)
        self.visualAdded.emit(visual_id)
        return visual_id
    
    # ==================== 通用管理接口 ====================
    
    def remove_visual(self, visual_id: str) -> bool:
        """移除指定 Visual 元素
        
        Args:
            visual_id: Visual 元素 ID
            
        Returns:
            是否成功移除
        """
        if not self.canvas:
            return False
        
        result = self.canvas.remove_visual(visual_id)
        if result:
            self.visualRemoved.emit(visual_id)
        return result
    
    def update_visual(self, visual_id: str, **kwargs) -> bool:
        """更新 Visual 元素数据
        
        Args:
            visual_id: Visual 元素 ID
            **kwargs: 更新参数
            
        Returns:
            是否成功更新
        """
        if not self.canvas:
            return False
        
        return self.canvas.update_visual(visual_id, **kwargs)
    
    def set_visible(self, visual_id: str, visible: bool) -> bool:
        """设置 Visual 元素可见性
        
        Args:
            visual_id: Visual 元素 ID
            visible: 是否可见
            
        Returns:
            是否成功设置
        """
        if not self.canvas:
            return False
        
        return self.canvas.set_visible(visual_id, visible)
    
    def clear_all(self) -> None:
        """清空所有 Visual 元素"""
        if self.canvas:
            self.canvas.clear_all()
    
    def auto_range(self) -> None:
        """自动调整相机范围"""
        if self.canvas:
            self.canvas.auto_range()
            self.canvas.update_grid()


class VispyWidget3D(QWidget):
    """3D Vispy 图形控件
    
    提供 3D 图形绘制功能，支持点云、网格、曲面、体数据等元素。
    """
    
    # 信号
    visualAdded = Signal(str)
    visualRemoved = Signal(str)
    
    def __init__(self, parent=None, camera_mode: str = 'turntable'):
        """
        Args:
            camera_mode: 相机模式 ('turntable', 'arcball', 'fly')
        """
        super().__init__(parent)
        
        if not VISPY_AVAILABLE:
            self._init_fallback_ui()
            return
        
        # 创建布局
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        
        # 创建 3D Canvas
        self.canvas = VispyCanvas3D(camera_mode=camera_mode)
        
        if self.canvas.native_widget:
            self.vBoxLayout.addWidget(self.canvas.native_widget)
        
        # 初始化主题
        self.set_theme(isDarkTheme())
        
    def _init_fallback_ui(self):
        """Vispy 不可用时的降级 UI"""
        self.vBoxLayout = QVBoxLayout(self)
        label = QLabel("Vispy 未安装，无法渲染图形\n请使用: pip install 'PySide6-Fluent-Widgets[full]'", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: #666; font-size: 14px;")
        self.vBoxLayout.addWidget(label)
        self.canvas = None
        
    def set_theme(self, is_dark: bool) -> None:
        """设置主题
        
        Args:
            is_dark: 是否为暗色主题
        """
        if self.canvas:
            self.canvas.set_theme(is_dark)
    
    # ==================== 3D 绘图接口 ====================
    
    def add_points(self, xyz: np.ndarray, colors: Union[str, np.ndarray] = 'white',
                   sizes: Union[float, np.ndarray] = 5.0, symbol: str = 'disc') -> str:
        """添加 3D 散点/点云
        
        Args:
            xyz: 形状 (N, 3)，N 个点的 x/y/z 坐标
            colors: 单一颜色或每个点的颜色数组
            sizes: 统一大小或每个点的大小
            symbol: 符号类型（大数据量自动切换为 'square'）
            
        Returns:
            visual_id
        """
        if not self.canvas:
            return ""
        
        visual_id = self.canvas._generate_visual_id()
        entry = MarkersEntry(self.canvas.view, visual_id, xyz, colors, sizes, symbol)
        self.canvas.add_visual(entry)
        self.visualAdded.emit(visual_id)
        return visual_id
    
    def add_line3d(self, pos: np.ndarray, color: Union[str, tuple] = 'white',
                   width: float = 1.0) -> str:
        """添加 3D 折线/曲线
        
        Args:
            pos: 形状 (N, 3)，N 个点的 x/y/z 坐标
            color: 颜色
            width: 线宽
            
        Returns:
            visual_id
        """
        if not self.canvas:
            return ""
        
        visual_id = self.canvas._generate_visual_id()
        entry = LineEntry(self.canvas.view, visual_id, pos, color, width)
        self.canvas.add_visual(entry)
        self.visualAdded.emit(visual_id)
        return visual_id
    
    def add_mesh(self, vertices: np.ndarray, faces: np.ndarray,
                 color: Union[str, tuple] = 'white', shading: str = 'smooth') -> str:
        """添加 3D 网格模型
        
        Args:
            vertices: 形状 (N, 3)，顶点坐标
            faces: 形状 (M, 3)，面索引
            color: 网格颜色
            shading: 着色方式：'flat', 'smooth'
            
        Returns:
            visual_id
        """
        if not self.canvas:
            return ""
        
        visual_id = self.canvas._generate_visual_id()
        entry = MeshEntry(self.canvas.view, visual_id, vertices, faces, color, shading)
        self.canvas.add_visual(entry)
        self.visualAdded.emit(visual_id)
        return visual_id
    
    def add_surface(self, x: np.ndarray, y: np.ndarray, z: np.ndarray,
                    color: Union[str, tuple] = 'white', shading: str = 'smooth') -> str:
        """添加 3D 曲面图
        
        Args:
            x: X 坐标网格
            y: Y 坐标网格
            z: Z 值网格（高度）
            color: 曲面颜色
            shading: 着色方式
            
        Returns:
            visual_id
        """
        if not self.canvas:
            return ""
        
        visual_id = self.canvas._generate_visual_id()
        entry = SurfacePlotEntry(self.canvas.view, visual_id, x, y, z, color, shading)
        self.canvas.add_visual(entry)
        self.visualAdded.emit(visual_id)
        return visual_id
    
    def add_volume(self, data: np.ndarray, method: str = 'mip',
                   threshold: Optional[float] = None) -> str:
        """添加 3D 体数据
        
        Args:
            data: 形状 (D, H, W)，3D 体数据
            method: 渲染方式：'mip', 'iso', 'translucent'
            threshold: 阈值（用于 iso 模式）
            
        Returns:
            visual_id
        """
        if not self.canvas:
            return ""
        
        visual_id = self.canvas._generate_visual_id()
        entry = VolumeEntry(self.canvas.view, visual_id, data, method, threshold)
        self.canvas.add_visual(entry)
        self.visualAdded.emit(visual_id)
        return visual_id
    
    def add_axes(self, size: float = 1.0) -> str:
        """添加 3D 坐标轴
        
        Args:
            size: 轴长度
            
        Returns:
            visual_id
        """
        if not self.canvas:
            return ""
        
        visual_id = self.canvas._generate_visual_id()
        entry = AxesEntry(self.canvas.view, visual_id, size)
        self.canvas.add_visual(entry)
        self.visualAdded.emit(visual_id)
        return visual_id
    
    def add_gridlines(self, scale: tuple = (1, 1, 1),
                      color: Union[str, tuple] = (0.5, 0.5, 0.5, 0.3)) -> str:
        """添加 3D 网格线
        
        Args:
            scale: 网格间距 (dx, dy, dz)
            color: 网格颜色
            
        Returns:
            visual_id
        """
        if not self.canvas:
            return ""
        
        visual_id = self.canvas._generate_visual_id()
        entry = GridLinesEntry(self.canvas.view, visual_id, scale, color)
        self.canvas.add_visual(entry)
        self.visualAdded.emit(visual_id)
        return visual_id
    
    def add_text3d(self, text: str, pos: tuple, font_size: float = 12,
                   color: Union[str, tuple] = 'white', rotation: tuple = (0, 0, 0)) -> str:
        """添加 3D 文本标注
        
        Args:
            text: 文本内容
            pos: 位置 (x, y, z)
            font_size: 字体大小
            color: 文本颜色
            rotation: 旋转角度
            
        Returns:
            visual_id
        """
        if not self.canvas:
            return ""
        
        visual_id = self.canvas._generate_visual_id()
        entry = TextEntry(self.canvas.view, visual_id, text, pos, font_size, color, rotation)
        self.canvas.add_visual(entry)
        self.visualAdded.emit(visual_id)
        return visual_id
    
    # ==================== 通用管理接口 ====================
    
    def remove_visual(self, visual_id: str) -> bool:
        """移除指定 Visual 元素"""
        if not self.canvas:
            return False
        
        result = self.canvas.remove_visual(visual_id)
        if result:
            self.visualRemoved.emit(visual_id)
        return result
    
    def update_visual(self, visual_id: str, **kwargs) -> bool:
        """更新 Visual 元素数据"""
        if not self.canvas:
            return False
        
        return self.canvas.update_visual(visual_id, **kwargs)
    
    def set_visible(self, visual_id: str, visible: bool) -> bool:
        """设置 Visual 元素可见性"""
        if not self.canvas:
            return False
        
        return self.canvas.set_visible(visual_id, visible)
    
    def clear_all(self) -> None:
        """清空所有 Visual 元素"""
        if self.canvas:
            self.canvas.clear_all()
    
    def auto_range(self) -> None:
        """自动调整相机范围"""
        if self.canvas:
            self.canvas.auto_range()
            self.canvas.update_grid()
    
    def set_view(self, mode: str) -> None:
        """设置相机视角
        
        Args:
            mode: 'free', 'top', 'front', 'side'
        """
        if self.canvas:
            self.canvas.set_view(mode)
