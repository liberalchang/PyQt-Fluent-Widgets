# coding:utf-8
"""
Vispy Canvas 画布层模块

负责创建和管理 Vispy SceneCanvas，处理 OpenGL 上下文、相机控制、主题管理。
"""
from typing import Dict, Optional, Union
import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

try:
    from vispy import scene, app as vispy_app
    from vispy.scene import SceneCanvas
    from vispy.scene.visuals import Line
    VISPY_AVAILABLE = True
except ImportError:
    VISPY_AVAILABLE = False
    SceneCanvas = QWidget  # 降级为普通Widget

from .vispy_visuals import VisualEntry


def initialize_vispy():
    """初始化Vispy后端"""
    if VISPY_AVAILABLE:
        try:
            # 设置 PySide6 后端
            vispy_app.use_app('pyside6')
        except Exception as e:
            print(f"Failed to set vispy backend: {e}")


class VispyCanvasBase:
    """Vispy Canvas 基类
    
    管理 SceneCanvas、相机、网格、主题等基础功能。
    """
    
    def __init__(self, camera_mode: str = 'turntable'):
        """初始化画布和场景
        
        Args:
            camera_mode: 相机模式 ('panzoom', 'turntable', 'arcball', 'fly')
        """
        if not VISPY_AVAILABLE:
            self.canvas = None
            self.view = None
            self.native_widget = None
            self.entries = {}
            return
        
        # 初始化 Vispy 后端
        initialize_vispy()
        
        # 创建 Canvas
        self.canvas = SceneCanvas(keys='interactive', show=False)
        self.native_widget = self.canvas.native
        self.canvas.bgcolor = '#F5F5F5'  # 默认亮色主题
        self.native_widget.setAttribute(Qt.WA_AlwaysStackOnTop, False)
        
        # 创建 ViewBox
        self.view = self.canvas.central_widget.add_view()
        self.view.camera = camera_mode
        
        # Visual 元素管理
        self.entries: Dict[str, VisualEntry] = {}
        self._visual_id_counter = 0
        
        # 网格
        self.grid = None
        
    def set_theme(self, is_dark: bool) -> None:
        """设置主题（亮色/暗色）
        
        Args:
            is_dark: 是否为暗色主题
        """
        if not VISPY_AVAILABLE or not self.canvas:
            return
        
        self.canvas.bgcolor = '#202020' if is_dark else '#F5F5F5'
        self.canvas.update()
        
    def add_visual(self, visual_entry: VisualEntry) -> str:
        """添加 Visual 元素
        
        Args:
            visual_entry: Visual 元素对象
            
        Returns:
            唯一标识符
        """
        visual_id = visual_entry.visual_id
        self.entries[visual_id] = visual_entry
        return visual_id
        
    def remove_visual(self, visual_id: str) -> bool:
        """移除指定 Visual 元素
        
        Args:
            visual_id: Visual 元素 ID
            
        Returns:
            是否成功移除
        """
        if visual_id in self.entries:
            self.entries[visual_id].destroy()
            del self.entries[visual_id]
            if self.canvas:
                self.canvas.update()
            return True
        return False
        
    def set_visible(self, visual_id: str, visible: bool) -> bool:
        """设置 Visual 元素可见性
        
        Args:
            visual_id: Visual 元素 ID
            visible: 是否可见
            
        Returns:
            是否成功设置
        """
        if visual_id in self.entries:
            self.entries[visual_id].set_visible(visible)
            if self.canvas:
                self.canvas.update()
            return True
        return False
        
    def update_visual(self, visual_id: str, **kwargs) -> bool:
        """更新 Visual 元素数据
        
        Args:
            visual_id: Visual 元素 ID
            **kwargs: 更新参数
            
        Returns:
            是否成功更新
        """
        if visual_id in self.entries:
            self.entries[visual_id].update_data(**kwargs)
            if self.canvas:
                self.canvas.update()
            return True
        return False
        
    def clear_all(self) -> None:
        """清空所有 Visual 元素"""
        for entry in self.entries.values():
            entry.destroy()
        self.entries.clear()
        if self.canvas:
            self.canvas.update()
        
    def auto_range(self) -> None:
        """自动调整相机以适应场景范围"""
        if not VISPY_AVAILABLE or not self.view or not self.entries:
            return
        
        try:
            # 收集所有可见元素的边界
            bounds_list = []
            for entry in self.entries.values():
                if entry.visible:
                    bounds = entry.bounds
                    if bounds is not None:
                        bounds_list.append(bounds)
            
            if not bounds_list:
                return
            
            # 计算总边界
            all_bounds = np.array(bounds_list)
            min_bounds = all_bounds[:, 0, :].min(axis=0)
            max_bounds = all_bounds[:, 1, :].max(axis=0)
            
            # 检查是否包含 NaN/Inf
            if not (np.isfinite(min_bounds).all() and np.isfinite(max_bounds).all()):
                return
            
            center = (min_bounds + max_bounds) / 2
            extent = np.linalg.norm(max_bounds - min_bounds)
            
            if not np.isfinite(extent) or extent == 0:
                extent = 1.0
            
            # 转换为tuple（相机需要tuple格式）
            self.view.camera.center = tuple(center.tolist())
            self.view.camera.distance = extent * 1.5
            
            # 设置 scale_factor（确保平移操作灵敏度）
            if hasattr(self.view.camera, 'scale_factor'):
                self.view.camera.scale_factor = extent
                
        except Exception as e:
            print(f"Error in auto_range: {e}")
    
    def _generate_visual_id(self) -> str:
        """生成唯一的 Visual ID"""
        self._visual_id_counter += 1
        return f"visual_{self._visual_id_counter}"


class VispyCanvas2D(VispyCanvasBase):
    """2D Vispy Canvas
    
    相机模式为 PanZoomCamera（平移、缩放）
    官方默认操作：
    - LMB（左键）: 平移视图
    - RMB 或滚轮: 缩放视图
    """
    
    def __init__(self):
        """初始化 2D 画布"""
        super().__init__(camera_mode='panzoom')
        
        if not VISPY_AVAILABLE:
            return
        
        # 初始化 2D 网格
        self._init_grid()
        
    def _init_grid(self):
        """初始化 2D 网格"""
        if not VISPY_AVAILABLE:
            return
        
        # 创建简单的 2D 网格线
        size = 100.0
        spacing = 10.0
        
        # 生成网格线段
        lines = []
        num_lines = int(size / spacing)
        
        # 垂直线
        for i in range(-num_lines, num_lines + 1):
            x = i * spacing
            lines.append([[x, -size, 0], [x, size, 0]])
        
        # 水平线
        for i in range(-num_lines, num_lines + 1):
            y = i * spacing
            lines.append([[-size, y, 0], [size, y, 0]])
        
        # 连接所有线段
        pos = []
        for line in lines:
            pos.extend(line)
        
        pos = np.array(pos, dtype=np.float32)
        
        self.grid = Line(
            pos=pos,
            color=(0.6, 0.6, 0.6, 0.4),
            method='gl',
            connect='segments',
            parent=self.view.scene
        )
        self.grid.interactive = False
        
    def update_grid(self, scale: tuple = (1, 1)):
        """更新网格范围和间距
        
        Args:
            scale: 网格间距 (dx, dy)
        """
        if not VISPY_AVAILABLE or not self.grid:
            return
        
        try:
            # 根据当前场景范围动态调整网格
            if self.entries:
                bounds_list = []
                for entry in self.entries.values():
                    if entry.visible:
                        bounds = entry.bounds
                        if bounds is not None:
                            bounds_list.append(bounds)
                
                if bounds_list:
                    all_bounds = np.array(bounds_list)
                    min_bounds = all_bounds[:, 0, :2]
                    max_bounds = all_bounds[:, 1, :2]
                    
                    mn = min_bounds.min(axis=0)
                    mx = max_bounds.max(axis=0)
                    
                    # 处理 NaN/Inf
                    mn = np.nan_to_num(mn, nan=0.0, posinf=100.0, neginf=-100.0)
                    mx = np.nan_to_num(mx, nan=0.0, posinf=100.0, neginf=-100.0)
                    
                    size = max(float(mx[0] - mn[0]), float(mx[1] - mn[1]), 1.0) * 1.2
                    spacing = max(1.0, size / 20.0)
                    
                    center = (mn + mx) / 2
                    
                    # 重新生成网格
                    lines = []
                    num_lines = int(size / spacing / 2)
                    
                    for i in range(-num_lines, num_lines + 1):
                        x = center[0] + i * spacing
                        lines.append([[x, center[1] - size/2, 0], [x, center[1] + size/2, 0]])
                    
                    for i in range(-num_lines, num_lines + 1):
                        y = center[1] + i * spacing
                        lines.append([[center[0] - size/2, y, 0], [center[0] + size/2, y, 0]])
                    
                    pos = []
                    for line in lines:
                        pos.extend(line)
                    
                    pos = np.array(pos, dtype=np.float32)
                    self.grid.set_data(pos=pos)
                    
        except Exception as e:
            print(f"Error updating 2D grid: {e}")


class VispyCanvas3D(VispyCanvasBase):
    """3D Vispy Canvas
    
    相机模式为 TurntableCamera（固定轴旋转）或 ArcballCamera（自由旋转）
    """
    
    def __init__(self, camera_mode: str = 'turntable'):
        """初始化 3D 画布
        
        Args:
            camera_mode: 相机模式 ('turntable', 'arcball', 'fly')
        """
        super().__init__(camera_mode=camera_mode)
        
        if not VISPY_AVAILABLE:
            return
        
        # 设置 3D 相机参数
        self.view.camera.fov = 45
        self.view.camera.distance = 100
        
        # 初始化 3D 网格
        self._init_grid()
        
    def _init_grid(self):
        """初始化 3D 网格"""
        if not VISPY_AVAILABLE:
            return
        
        # 创建简单的 3D 网格线（XY 平面）
        size = 100.0
        spacing = 10.0
        
        lines = []
        num_lines = int(size / spacing)
        
        # X 方向线（Y 固定）
        for i in range(-num_lines, num_lines + 1):
            y = i * spacing
            lines.append([[-size, y, 0], [size, y, 0]])
        
        # Y 方向线（X 固定）
        for i in range(-num_lines, num_lines + 1):
            x = i * spacing
            lines.append([[x, -size, 0], [x, size, 0]])
        
        pos = []
        for line in lines:
            pos.extend(line)
        
        pos = np.array(pos, dtype=np.float32)
        
        self.grid = Line(
            pos=pos,
            color=(0.6, 0.6, 0.6, 0.4),
            method='gl',
            connect='segments',
            parent=self.view.scene
        )
        self.grid.interactive = False
        
    def update_grid(self, scale: tuple = (1, 1, 1)):
        """更新网格范围和间距
        
        Args:
            scale: 网格间距 (dx, dy, dz)
        """
        if not VISPY_AVAILABLE or not self.grid:
            return
        
        try:
            # 根据当前场景范围动态调整网格
            if self.entries:
                bounds_list = []
                for entry in self.entries.values():
                    if entry.visible:
                        bounds = entry.bounds
                        if bounds is not None:
                            bounds_list.append(bounds)
                
                if bounds_list:
                    all_bounds = np.array(bounds_list)
                    mn = all_bounds[:, 0, :].min(axis=0)
                    mx = all_bounds[:, 1, :].max(axis=0)
                    
                    # 处理 NaN/Inf
                    mn = np.nan_to_num(mn, nan=0.0, posinf=100.0, neginf=-100.0)
                    mx = np.nan_to_num(mx, nan=0.0, posinf=100.0, neginf=-100.0)
                    
                    size_x = float(max(1.0, mx[0] - mn[0]))
                    size_y = float(max(1.0, mx[1] - mn[1]))
                    size = float(max(size_x, size_y)) * 1.2
                    spacing = max(1.0, size / 20.0)
                    
                    center_x = (mn[0] + mx[0]) / 2.0
                    center_y = (mn[1] + mx[1]) / 2.0
                    
                    # 重新生成网格
                    lines = []
                    num_lines = int(size / spacing / 2)
                    
                    for i in range(-num_lines, num_lines + 1):
                        x = center_x + i * spacing
                        lines.append([[x, center_y - size/2, 0], [x, center_y + size/2, 0]])
                    
                    for i in range(-num_lines, num_lines + 1):
                        y = center_y + i * spacing
                        lines.append([[center_x - size/2, y, 0], [center_x + size/2, y, 0]])
                    
                    pos = []
                    for line in lines:
                        pos.extend(line)
                    
                    pos = np.array(pos, dtype=np.float32)
                    self.grid.set_data(pos=pos)
                    
        except Exception as e:
            print(f"Error updating 3D grid: {e}")
    
    def set_view(self, mode: str) -> None:
        """设置相机视角
        
        Args:
            mode: 视角模式 ('free', 'top', 'front', 'side')
        """
        if not VISPY_AVAILABLE or not self.view:
            return
        
        if mode == 'top':
            self.view.camera.elevation = 90
            self.view.camera.azimuth = 0
        elif mode == 'front':
            self.view.camera.elevation = 0
            self.view.camera.azimuth = 0
        elif mode == 'side':
            self.view.camera.elevation = 0
            self.view.camera.azimuth = 90
        else:  # 'free'
            self.view.camera.elevation = 30
            self.view.camera.azimuth = 45
        
        if self.canvas:
            self.canvas.update()
