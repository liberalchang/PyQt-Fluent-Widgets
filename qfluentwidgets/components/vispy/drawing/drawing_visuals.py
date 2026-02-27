# coding:utf-8
"""
绘图 Visual 元素模块

扩展 vispy_visuals 模块，添加交互式绘图需要的新图元类型：
- BezierCurveEntry: 贝塞尔曲线
- ArcEntry: 圆弧
- StyledPolygonEntry: 带样式控制的多边形
- StyledRectangleEntry: 带样式控制的矩形
- StyledEllipseEntry: 带样式控制的圆形/椭圆
"""
from typing import Union
import numpy as np

try:
    from vispy.scene import visuals
    VISPY_AVAILABLE = True
except ImportError:
    VISPY_AVAILABLE = False

from ..vispy_visuals import VisualEntry


class BezierCurveEntry(VisualEntry):
    """贝塞尔曲线元素
    
    支持二阶和三阶贝塞尔曲线，通过采样转换为线条渲染。
    """
    
    def __init__(self, parent_view, visual_id: str, control_points: np.ndarray,
                 degree: int = 2, color: Union[str, tuple] = 'white', 
                 width: float = 1.0, num_samples: int = 50):
        """
        Args:
            parent_view: Vispy ViewBox 对象
            visual_id: 唯一标识符
            control_points: 控制点，形状 (3, 2) 或 (4, 2)
            degree: 阶数，2=二阶，3=三阶
            color: 颜色
            width: 线宽
            num_samples: 采样点数量
        """
        super().__init__(parent_view, visual_id)
        
        if not VISPY_AVAILABLE:
            return
            
        self.control_points = control_points
        self.degree = degree
        self.color = color
        self.width = width
        self.num_samples = num_samples
        
        # 生成采样点
        self.sampled_points = self._sample_bezier()
        
        # 使用 Line visual 渲染
        self.visual = visuals.Line(
            pos=self.sampled_points,
            color=color,
            width=width,
            parent=parent_view.scene
        )
        
    def _sample_bezier(self) -> np.ndarray:
        """采样贝塞尔曲线
        
        Returns:
            采样点数组，形状 (num_samples, 2)
        """
        t_values = np.linspace(0, 1, self.num_samples)
        n = len(self.control_points) - 1
        
        if n < 1:
            return np.array(self.control_points, dtype=np.float32)
            
        # 使用通用公式计算任意阶贝塞尔曲线
        # B(t) = sum(C(n,i) * (1-t)^(n-i) * t^i * Pi)
        
        points = np.zeros((self.num_samples, 2))
        
        # 预计算组合数
        import math
        combinations = [math.comb(n, i) for i in range(n + 1)]
        
        for i in range(n + 1):
            # 计算基函数值 (num_samples,)
            basis = combinations[i] * ((1 - t_values) ** (n - i)) * (t_values ** i)
            # 累加点坐标
            points += np.outer(basis, self.control_points[i])
            
        return points.astype(np.float32)
        
    def set_visible(self, visible: bool) -> None:
        self.visible = visible
        if self.visual:
            self.visual.visible = visible
            
    def update_data(self, **kwargs) -> None:
        if not self.visual:
            return
            
        if 'control_points' in kwargs:
            self.control_points = kwargs['control_points']
            self.sampled_points = self._sample_bezier()
            
        if 'degree' in kwargs:
            self.degree = kwargs['degree']
            self.sampled_points = self._sample_bezier()
            
        if 'num_samples' in kwargs:
            self.num_samples = kwargs['num_samples']
            self.sampled_points = self._sample_bezier()
            
        if 'color' in kwargs:
            self.color = kwargs['color']
        if 'width' in kwargs:
            self.width = kwargs['width']
            
        # 更新 visual
        self.visual.set_data(pos=self.sampled_points, color=self.color, width=self.width)
        
    def destroy(self) -> None:
        if self.visual:
            self.visual.parent = None
            
    @property
    def bounds(self) -> np.ndarray:
        if self.control_points is None or len(self.control_points) == 0:
            return np.array([[0, 0, 0], [0, 0, 0]])
        mins = self.control_points.min(axis=0)
        maxs = self.control_points.max(axis=0)
        # 补齐到3D
        if len(mins) == 2:
            mins = np.append(mins, 0)
            maxs = np.append(maxs, 0)
        return np.array([mins, maxs])


class ArcEntry(VisualEntry):
    """圆弧元素
    
    通过参数方程采样生成圆弧上的点，使用线条渲染。
    """
    
    def __init__(self, parent_view, visual_id: str, center: tuple, radius: float,
                 start_angle: float, end_angle: float, color: Union[str, tuple] = 'white',
                 width: float = 1.0, num_samples: int = 50):
        """
        Args:
            parent_view: Vispy ViewBox 对象
            visual_id: 唯一标识符
            center: 中心点 (x, y)
            radius: 半径
            start_angle: 起始角度（度数）
            end_angle: 结束角度（度数）
            color: 颜色
            width: 线宽
            num_samples: 采样点数量
        """
        super().__init__(parent_view, visual_id)
        
        if not VISPY_AVAILABLE:
            return
            
        self.center = center
        self.radius = radius
        self.start_angle = start_angle
        self.end_angle = end_angle
        self.color = color
        self.width = width
        self.num_samples = num_samples
        
        # 生成采样点
        self.sampled_points = self._sample_arc()
        
        # 使用 Line visual 渲染
        self.visual = visuals.Line(
            pos=self.sampled_points,
            color=color,
            width=width,
            parent=parent_view.scene
        )
        
    def _sample_arc(self) -> np.ndarray:
        """采样圆弧
        
        Returns:
            采样点数组，形状 (num_samples, 2)
        """
        # 转换为弧度
        start_rad = np.deg2rad(self.start_angle)
        end_rad = np.deg2rad(self.end_angle)
        
        # 生成角度序列
        angles = np.linspace(start_rad, end_rad, self.num_samples)
        
        # 计算点坐标
        cx, cy = self.center
        x = cx + self.radius * np.cos(angles)
        y = cy + self.radius * np.sin(angles)
        
        points = np.column_stack([x, y])
        return points.astype(np.float32)
        
    def set_visible(self, visible: bool) -> None:
        self.visible = visible
        if self.visual:
            self.visual.visible = visible
            
    def update_data(self, **kwargs) -> None:
        if not self.visual:
            return
            
        if 'center' in kwargs:
            self.center = kwargs['center']
        if 'radius' in kwargs:
            self.radius = kwargs['radius']
        if 'start_angle' in kwargs:
            self.start_angle = kwargs['start_angle']
        if 'end_angle' in kwargs:
            self.end_angle = kwargs['end_angle']
        if 'num_samples' in kwargs:
            self.num_samples = kwargs['num_samples']
            
        # 重新采样
        self.sampled_points = self._sample_arc()
        
        if 'color' in kwargs:
            self.color = kwargs['color']
        if 'width' in kwargs:
            self.width = kwargs['width']
            
        # 更新 visual
        self.visual.set_data(pos=self.sampled_points, color=self.color, width=self.width)
        
    def destroy(self) -> None:
        if self.visual:
            self.visual.parent = None
            
    @property
    def bounds(self) -> np.ndarray:
        cx, cy = self.center
        r = self.radius
        return np.array([[cx - r, cy - r, 0], [cx + r, cy + r, 0]])


class StyledPolygonEntry(VisualEntry):
    """带样式控制的多边形元素
    
    支持独立的填充和边缘线条控制。
    """
    
    def __init__(self, parent_view, visual_id: str, vertices: np.ndarray,
                 fill_color: Union[str, tuple] = (0.5, 0.5, 0.5, 0.8),
                 border_color: Union[str, tuple] = (1, 1, 1, 1),
                 border_width: float = 1.0,
                 filled: bool = True,
                 show_border: bool = True):
        """
        Args:
            parent_view: Vispy ViewBox 对象
            visual_id: 唯一标识符
            vertices: 顶点，形状 (N, 2)
            fill_color: 填充颜色
            border_color: 边缘线条颜色
            border_width: 边缘线条宽度
            filled: 是否填充
            show_border: 是否显示边缘线条
        """
        super().__init__(parent_view, visual_id)
        
        if not VISPY_AVAILABLE:
            return
            
        self.vertices = vertices
        self.fill_color = fill_color
        self.border_color = border_color
        self.border_width = border_width
        self.filled = filled
        self.show_border = show_border
        
        # 创建填充 visual
        self.fill_visual = None
        if self.filled:
            self.fill_visual = visuals.Polygon(
                pos=vertices,
                color=fill_color,
                border_color=None,
                parent=parent_view.scene
            )
            
        # 创建边缘线条 visual（闭合）
        self.border_visual = None
        if self.show_border:
            # 闭合多边形：添加第一个点到末尾
            closed_vertices = np.vstack([vertices, vertices[0:1]])
            self.border_visual = visuals.Line(
                pos=closed_vertices,
                color=border_color,
                width=border_width,
                parent=parent_view.scene
            )
            
        self.visual = self.fill_visual if self.fill_visual else self.border_visual
        
    def set_visible(self, visible: bool) -> None:
        self.visible = visible
        if self.fill_visual:
            self.fill_visual.visible = visible
        if self.border_visual:
            self.border_visual.visible = visible
            
    def update_data(self, **kwargs) -> None:
        if 'vertices' in kwargs:
            self.vertices = kwargs['vertices']
            
        if 'fill_color' in kwargs:
            self.fill_color = kwargs['fill_color']
        if 'border_color' in kwargs:
            self.border_color = kwargs['border_color']
        if 'border_width' in kwargs:
            self.border_width = kwargs['border_width']
        if 'filled' in kwargs:
            self.filled = kwargs['filled']
        if 'show_border' in kwargs:
            self.show_border = kwargs['show_border']
            
        # 更新或重新创建 visual
        if self.filled:
            if self.fill_visual is None:
                self.fill_visual = visuals.Polygon(
                    pos=self.vertices,
                    color=self.fill_color,
                    border_color=None,
                    parent=self.view.scene
                )
            else:
                # 重新创建 polygon（vispy Polygon 不支持直接更新）
                self.fill_visual.parent = None
                self.fill_visual = visuals.Polygon(
                    pos=self.vertices,
                    color=self.fill_color,
                    border_color=None,
                    parent=self.view.scene
                )
        else:
            if self.fill_visual:
                self.fill_visual.parent = None
                self.fill_visual = None
                
        if self.show_border:
            closed_vertices = np.vstack([self.vertices, self.vertices[0:1]])
            if self.border_visual is None:
                self.border_visual = visuals.Line(
                    pos=closed_vertices,
                    color=self.border_color,
                    width=self.border_width,
                    parent=self.view.scene
                )
            else:
                self.border_visual.set_data(
                    pos=closed_vertices,
                    color=self.border_color,
                    width=self.border_width
                )
        else:
            if self.border_visual:
                self.border_visual.parent = None
                self.border_visual = None
                
        self.visual = self.fill_visual if self.fill_visual else self.border_visual
        
    def destroy(self) -> None:
        if self.fill_visual:
            self.fill_visual.parent = None
            self.fill_visual = None
        if self.border_visual:
            self.border_visual.parent = None
            self.border_visual = None
            
    @property
    def bounds(self) -> np.ndarray:
        if self.vertices is None or len(self.vertices) == 0:
            return np.array([[0, 0, 0], [0, 0, 0]])
        mins = self.vertices.min(axis=0)
        maxs = self.vertices.max(axis=0)
        return np.array([[mins[0], mins[1], 0], [maxs[0], maxs[1], 0]])


class StyledRectangleEntry(VisualEntry):
    """带样式控制的矩形元素"""
    
    def __init__(self, parent_view, visual_id: str, pos: tuple, size: tuple,
                 fill_color: Union[str, tuple] = (0.5, 0.5, 0.5, 0.8),
                 border_color: Union[str, tuple] = (1, 1, 1, 1),
                 border_width: float = 1.0,
                 filled: bool = True,
                 show_border: bool = True):
        """
        Args:
            pos: 左上角位置 (x, y)
            size: 尺寸 (width, height)
        """
        super().__init__(parent_view, visual_id)
        
        if not VISPY_AVAILABLE:
            return
            
        self.pos = pos
        self.size = size
        self.fill_color = fill_color
        self.border_color = border_color
        self.border_width = border_width
        self.filled = filled
        self.show_border = show_border
        
        # 创建填充 visual
        self.fill_visual = None
        if self.filled:
            self.fill_visual = visuals.Rectangle(
                center=(pos[0] + size[0]/2, pos[1] + size[1]/2),
                width=size[0],
                height=size[1],
                color=fill_color,
                border_color=None,
                parent=parent_view.scene
            )
            
        # 创建边缘线条 visual
        self.border_visual = None
        if self.show_border:
            # 矩形四个角的点（闭合）
            x, y = pos
            w, h = size
            vertices = np.array([
                [x, y], [x + w, y], [x + w, y + h], [x, y + h], [x, y]
            ], dtype=np.float32)
            self.border_visual = visuals.Line(
                pos=vertices,
                color=border_color,
                width=border_width,
                parent=parent_view.scene
            )
            
        self.visual = self.fill_visual if self.fill_visual else self.border_visual
        
    def set_visible(self, visible: bool) -> None:
        self.visible = visible
        if self.fill_visual:
            self.fill_visual.visible = visible
        if self.border_visual:
            self.border_visual.visible = visible
            
    def update_data(self, **kwargs) -> None:
        if 'pos' in kwargs:
            self.pos = kwargs['pos']
        if 'size' in kwargs:
            self.size = kwargs['size']
        if 'fill_color' in kwargs:
            self.fill_color = kwargs['fill_color']
        if 'border_color' in kwargs:
            self.border_color = kwargs['border_color']
        if 'border_width' in kwargs:
            self.border_width = kwargs['border_width']
        if 'filled' in kwargs:
            self.filled = kwargs['filled']
        if 'show_border' in kwargs:
            self.show_border = kwargs['show_border']
            
        # 更新填充 visual
        if self.filled:
            if self.fill_visual is None:
                self.fill_visual = visuals.Rectangle(
                    center=(self.pos[0] + self.size[0]/2, self.pos[1] + self.size[1]/2),
                    width=self.size[0],
                    height=self.size[1],
                    color=self.fill_color,
                    border_color=None,
                    parent=self.view.scene
                )
            else:
                self.fill_visual.center = (self.pos[0] + self.size[0]/2, self.pos[1] + self.size[1]/2)
                self.fill_visual.width = self.size[0]
                self.fill_visual.height = self.size[1]
                self.fill_visual.color = self.fill_color
        else:
            if self.fill_visual:
                self.fill_visual.parent = None
                self.fill_visual = None
                
        # 更新边缘线条 visual
        if self.show_border:
            x, y = self.pos
            w, h = self.size
            vertices = np.array([
                [x, y], [x + w, y], [x + w, y + h], [x, y + h], [x, y]
            ], dtype=np.float32)
            
            if self.border_visual is None:
                self.border_visual = visuals.Line(
                    pos=vertices,
                    color=self.border_color,
                    width=self.border_width,
                    parent=self.view.scene
                )
            else:
                self.border_visual.set_data(
                    pos=vertices,
                    color=self.border_color,
                    width=self.border_width
                )
        else:
            if self.border_visual:
                self.border_visual.parent = None
                self.border_visual = None
                
        self.visual = self.fill_visual if self.fill_visual else self.border_visual
        
    def destroy(self) -> None:
        if self.fill_visual:
            self.fill_visual.parent = None
            self.fill_visual = None
        if self.border_visual:
            self.border_visual.parent = None
            self.border_visual = None
            
    @property
    def bounds(self) -> np.ndarray:
        x, y = self.pos
        w, h = self.size
        return np.array([[x, y, 0], [x + w, y + h, 0]])


class StyledEllipseEntry(VisualEntry):
    """带样式控制的圆形/椭圆元素"""
    
    def __init__(self, parent_view, visual_id: str, center: tuple, radius: Union[float, tuple],
                 fill_color: Union[str, tuple] = (0.5, 0.5, 0.5, 0.8),
                 border_color: Union[str, tuple] = (1, 1, 1, 1),
                 border_width: float = 1.0,
                 filled: bool = True,
                 show_border: bool = True,
                 num_samples: int = 64):
        """
        Args:
            center: 中心点 (x, y)
            radius: 半径（圆）或 (rx, ry)（椭圆）
        """
        super().__init__(parent_view, visual_id)
        
        if not VISPY_AVAILABLE:
            return
            
        self.center = center
        self.radius = radius if isinstance(radius, tuple) else (radius, radius)
        self.fill_color = fill_color
        self.border_color = border_color
        self.border_width = border_width
        self.filled = filled
        self.show_border = show_border
        self.num_samples = num_samples
        
        # 创建填充 visual
        self.fill_visual = None
        if self.filled:
            self.fill_visual = visuals.Ellipse(
                center=center,
                radius=self.radius,
                color=fill_color,
                border_color=None,
                parent=parent_view.scene
            )
            
        # 创建边缘线条 visual（使用采样点）
        self.border_visual = None
        if self.show_border:
            vertices = self._sample_ellipse()
            self.border_visual = visuals.Line(
                pos=vertices,
                color=border_color,
                width=border_width,
                parent=parent_view.scene
            )
            
        self.visual = self.fill_visual if self.fill_visual else self.border_visual
        
    def _sample_ellipse(self) -> np.ndarray:
        """采样椭圆边缘点（闭合）"""
        angles = np.linspace(0, 2*np.pi, self.num_samples + 1)
        cx, cy = self.center
        rx, ry = self.radius
        x = cx + rx * np.cos(angles)
        y = cy + ry * np.sin(angles)
        return np.column_stack([x, y]).astype(np.float32)
        
    def set_visible(self, visible: bool) -> None:
        self.visible = visible
        if self.fill_visual:
            self.fill_visual.visible = visible
        if self.border_visual:
            self.border_visual.visible = visible
            
    def update_data(self, **kwargs) -> None:
        if 'center' in kwargs:
            self.center = kwargs['center']
        if 'radius' in kwargs:
            radius = kwargs['radius']
            self.radius = radius if isinstance(radius, tuple) else (radius, radius)
        if 'fill_color' in kwargs:
            self.fill_color = kwargs['fill_color']
        if 'border_color' in kwargs:
            self.border_color = kwargs['border_color']
        if 'border_width' in kwargs:
            self.border_width = kwargs['border_width']
        if 'filled' in kwargs:
            self.filled = kwargs['filled']
        if 'show_border' in kwargs:
            self.show_border = kwargs['show_border']
            
        # 更新填充 visual
        if self.filled:
            if self.fill_visual is None:
                self.fill_visual = visuals.Ellipse(
                    center=self.center,
                    radius=self.radius,
                    color=self.fill_color,
                    border_color=None,
                    parent=self.view.scene
                )
            else:
                self.fill_visual.center = self.center
                self.fill_visual.radius = self.radius
                self.fill_visual.color = self.fill_color
        else:
            if self.fill_visual:
                self.fill_visual.parent = None
                self.fill_visual = None
                
        # 更新边缘线条 visual
        if self.show_border:
            vertices = self._sample_ellipse()
            if self.border_visual is None:
                self.border_visual = visuals.Line(
                    pos=vertices,
                    color=self.border_color,
                    width=self.border_width,
                    parent=self.view.scene
                )
            else:
                self.border_visual.set_data(
                    pos=vertices,
                    color=self.border_color,
                    width=self.border_width
                )
        else:
            if self.border_visual:
                self.border_visual.parent = None
                self.border_visual = None
                
        self.visual = self.fill_visual if self.fill_visual else self.border_visual
        
    def destroy(self) -> None:
        if self.fill_visual:
            self.fill_visual.parent = None
            self.fill_visual = None
        if self.border_visual:
            self.border_visual.parent = None
            self.border_visual = None
            
    @property
    def bounds(self) -> np.ndarray:
        cx, cy = self.center
        rx, ry = self.radius
        return np.array([[cx - rx, cy - ry, 0], [cx + rx, cy + ry, 0]])
