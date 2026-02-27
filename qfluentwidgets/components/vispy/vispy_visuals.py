# coding:utf-8
"""
Vispy Visual 图形元素封装模块

提供统一的 Visual 元素接口，封装 Vispy 的各种可视化对象。
"""
from typing import Union, Optional
import numpy as np
from abc import ABC, abstractmethod

try:
    from vispy.scene import visuals
    from vispy.visuals.transforms import MatrixTransform
    VISPY_AVAILABLE = True
except ImportError:
    VISPY_AVAILABLE = False


class VisualEntry(ABC):
    """Visual 元素基类
    
    所有场景图形元素的基础接口，提供统一的可见性、数据更新、销毁等操作。
    """
    
    def __init__(self, parent_view, visual_id: str):
        """初始化 Visual 对象
        
        Args:
            parent_view: Vispy ViewBox 对象
            visual_id: 唯一标识符
        """
        self.view = parent_view
        self.visual_id = visual_id
        self.visible = True
        self.visual = None
        
    @abstractmethod
    def set_visible(self, visible: bool) -> None:
        """设置可见性"""
        pass
        
    @abstractmethod
    def update_data(self, **kwargs) -> None:
        """更新数据"""
        pass
        
    @abstractmethod
    def destroy(self) -> None:
        """销毁 Visual 对象"""
        pass
        
    @property
    @abstractmethod
    def bounds(self) -> np.ndarray:
        """返回边界框 [[min_x, min_y, min_z], [max_x, max_y, max_z]]"""
        pass


# ==================== 2D Visual 元素 ====================

class LineEntry(VisualEntry):
    """2D/3D 折线元素"""
    
    def __init__(self, parent_view, visual_id: str, pos: np.ndarray, 
                 color: Union[str, tuple] = 'white', width: float = 1.0):
        """
        Args:
            pos: 形状 (N, 2) 或 (N, 3)，点坐标
            color: 颜色
            width: 线宽
        """
        super().__init__(parent_view, visual_id)
        
        if not VISPY_AVAILABLE:
            return
            
        self.pos = pos
        self.color = color
        self.width = width
        
        self.visual = visuals.Line(
            pos=pos,
            color=color,
            width=width,
            parent=parent_view.scene
        )
        
    def set_visible(self, visible: bool) -> None:
        self.visible = visible
        if self.visual:
            self.visual.visible = visible
            
    def update_data(self, **kwargs) -> None:
        if not self.visual:
            return
            
        if 'pos' in kwargs:
            self.pos = kwargs['pos']
        if 'color' in kwargs:
            self.color = kwargs['color']
        if 'width' in kwargs:
            self.width = kwargs['width']
            
        self.visual.set_data(pos=self.pos, color=self.color, width=self.width)
        
    def destroy(self) -> None:
        if self.visual:
            self.visual.parent = None
            
    @property
    def bounds(self) -> np.ndarray:
        if self.pos is None or len(self.pos) == 0:
            return np.array([[0, 0, 0], [0, 0, 0]])
        mins = self.pos.min(axis=0)
        maxs = self.pos.max(axis=0)
        # 补齐到3D
        if len(mins) == 2:
            mins = np.append(mins, 0)
            maxs = np.append(maxs, 0)
        return np.array([mins, maxs])


class MarkersEntry(VisualEntry):
    """2D/3D 散点标记元素"""
    
    def __init__(self, parent_view, visual_id: str, pos: np.ndarray,
                 colors: Union[str, np.ndarray] = 'white',
                 sizes: Union[float, np.ndarray] = 5.0,
                 symbol: str = 'o',
                 edge_color: Union[str, np.ndarray, None] = None,
                 edge_width: float = 0.0):
        """
        Args:
            pos: 形状 (N, 2) 或 (N, 3)，点坐标
            colors: 单一颜色或每个点的颜色数组（填充颜色）
            sizes: 统一大小或每个点的大小
            symbol: 符号类型 ('o', 's', '^', 'd' 等)
            edge_color: 边缘颜色
            edge_width: 边缘宽度
        """
        super().__init__(parent_view, visual_id)
        
        if not VISPY_AVAILABLE:
            return
            
        self.pos = pos
        self.colors = colors
        self.sizes = sizes
        self.symbol = symbol
        self.edge_color = edge_color
        self.edge_width = edge_width
        
        # 大数据量优化
        if len(pos) > 500000 and symbol == 'disc':
            symbol = 'square'
        
        self.visual = visuals.Markers(
            pos=pos,
            face_color=colors,
            size=sizes,
            symbol=symbol,
            edge_color=edge_color,
            edge_width=edge_width,
            parent=parent_view.scene
        )
        
        # OpenGL 状态优化
        if VISPY_AVAILABLE:
            self.visual.set_gl_state('opaque', depth_test=True, blend=False)
        
    def set_visible(self, visible: bool) -> None:
        self.visible = visible
        if self.visual:
            self.visual.visible = visible
            
    def update_data(self, **kwargs) -> None:
        if not self.visual:
            return
            
        if 'pos' in kwargs:
            self.pos = kwargs['pos']
        if 'colors' in kwargs:
            self.colors = kwargs['colors']
        if 'sizes' in kwargs:
            self.sizes = kwargs['sizes']
        if 'edge_color' in kwargs:
            self.edge_color = kwargs['edge_color']
        if 'edge_width' in kwargs:
            self.edge_width = kwargs['edge_width']
            
        self.visual.set_data(
            pos=self.pos, 
            face_color=self.colors, 
            size=self.sizes,
            edge_color=self.edge_color,
            edge_width=self.edge_width
        )
        
    def destroy(self) -> None:
        if self.visual:
            self.visual.parent = None
            
    @property
    def bounds(self) -> np.ndarray:
        if self.pos is None or len(self.pos) == 0:
            return np.array([[0, 0, 0], [0, 0, 0]])
        mins = self.pos.min(axis=0)
        maxs = self.pos.max(axis=0)
        if len(mins) == 2:
            mins = np.append(mins, 0)
            maxs = np.append(maxs, 0)
        return np.array([mins, maxs])


class RectangleEntry(VisualEntry):
    """2D 矩形元素"""
    
    def __init__(self, parent_view, visual_id: str, pos: tuple, size: tuple,
                 color: Union[str, tuple] = 'white',
                 border_color: Optional[Union[str, tuple]] = None):
        """
        Args:
            pos: 左上角坐标 (x, y)
            size: 尺寸 (width, height)
            color: 填充颜色
            border_color: 边框颜色
        """
        super().__init__(parent_view, visual_id)
        
        if not VISPY_AVAILABLE:
            return
            
        self.pos = pos
        self.size = size
        self.color = color
        self.border_color = border_color
        
        self.visual = visuals.Rectangle(
            center=(pos[0] + size[0]/2, pos[1] + size[1]/2),
            width=size[0],
            height=size[1],
            color=color,
            border_color=border_color if border_color else color,
            parent=parent_view.scene
        )
        
    def set_visible(self, visible: bool) -> None:
        self.visible = visible
        if self.visual:
            self.visual.visible = visible
            
    def update_data(self, **kwargs) -> None:
        if not self.visual:
            return
            
        if 'pos' in kwargs:
            self.pos = kwargs['pos']
        if 'size' in kwargs:
            self.size = kwargs['size']
        if 'color' in kwargs:
            self.color = kwargs['color']
        if 'border_color' in kwargs:
            self.border_color = kwargs['border_color']
            
        self.visual.center = (self.pos[0] + self.size[0]/2, self.pos[1] + self.size[1]/2)
        self.visual.width = self.size[0]
        self.visual.height = self.size[1]
        self.visual.color = self.color
        if self.border_color:
            self.visual.border_color = self.border_color
        
    def destroy(self) -> None:
        if self.visual:
            self.visual.parent = None
            
    @property
    def bounds(self) -> np.ndarray:
        x, y = self.pos
        w, h = self.size
        return np.array([[x, y, 0], [x + w, y + h, 0]])


class EllipseEntry(VisualEntry):
    """2D 椭圆/圆形元素"""
    
    def __init__(self, parent_view, visual_id: str, center: tuple,
                 radius: Union[float, tuple], color: Union[str, tuple] = 'white'):
        """
        Args:
            center: 中心点 (x, y)
            radius: 半径（圆）或 (rx, ry)（椭圆）
            color: 填充颜色
        """
        super().__init__(parent_view, visual_id)
        
        if not VISPY_AVAILABLE:
            return
            
        self.center = center
        self.radius = radius if isinstance(radius, tuple) else (radius, radius)
        self.color = color
        
        self.visual = visuals.Ellipse(
            center=center,
            radius=self.radius,
            color=color,
            parent=parent_view.scene
        )
        
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
            radius = kwargs['radius']
            self.radius = radius if isinstance(radius, tuple) else (radius, radius)
        if 'color' in kwargs:
            self.color = kwargs['color']
            
        self.visual.center = self.center
        self.visual.radius = self.radius
        self.visual.color = self.color
        
    def destroy(self) -> None:
        if self.visual:
            self.visual.parent = None
            
    @property
    def bounds(self) -> np.ndarray:
        cx, cy = self.center
        rx, ry = self.radius
        return np.array([[cx - rx, cy - ry, 0], [cx + rx, cy + ry, 0]])


class PolygonEntry(VisualEntry):
    """2D 多边形元素"""
    
    def __init__(self, parent_view, visual_id: str, pos: np.ndarray,
                 color: Union[str, tuple] = 'white',
                 border_color: Optional[Union[str, tuple]] = None):
        """
        Args:
            pos: 形状 (N, 2)，顶点坐标
            color: 填充颜色
            border_color: 边框颜色
        """
        super().__init__(parent_view, visual_id)
        
        if not VISPY_AVAILABLE:
            return
            
        self.pos = pos
        self.color = color
        self.border_color = border_color
        
        self.visual = visuals.Polygon(
            pos=pos,
            color=color,
            border_color=border_color if border_color else color,
            parent=parent_view.scene
        )
        
    def set_visible(self, visible: bool) -> None:
        self.visible = visible
        if self.visual:
            self.visual.visible = visible
            
    def update_data(self, **kwargs) -> None:
        if not self.visual:
            return
            
        if 'pos' in kwargs:
            self.pos = kwargs['pos']
        if 'color' in kwargs:
            self.color = kwargs['color']
        if 'border_color' in kwargs:
            self.border_color = kwargs['border_color']
            
        # Polygon 需要重新创建
        self.visual.parent = None
        self.visual = visuals.Polygon(
            pos=self.pos,
            color=self.color,
            border_color=self.border_color if self.border_color else self.color,
            parent=self.view.scene
        )
        
    def destroy(self) -> None:
        if self.visual:
            self.visual.parent = None
            
    @property
    def bounds(self) -> np.ndarray:
        if self.pos is None or len(self.pos) == 0:
            return np.array([[0, 0, 0], [0, 0, 0]])
        mins = self.pos.min(axis=0)
        maxs = self.pos.max(axis=0)
        return np.array([[mins[0], mins[1], 0], [maxs[0], maxs[1], 0]])


class ImageEntry(VisualEntry):
    """2D 图像元素"""
    
    def __init__(self, parent_view, visual_id: str, data: np.ndarray,
                 pos: tuple = (0, 0), interpolation: str = 'nearest'):
        """
        Args:
            data: 图像数据 (H, W) 或 (H, W, 3/4)
            pos: 左下角位置 (x, y)
            interpolation: 插值方式
        """
        super().__init__(parent_view, visual_id)
        
        if not VISPY_AVAILABLE:
            return
            
        self.data = data
        self.pos = pos
        self.interpolation = interpolation
        
        try:
            self.visual = visuals.Image(
                data=data,
                interpolation=interpolation,
                parent=parent_view.scene
            )
        except Exception:
            # 降级尝试
            try:
                self.visual = visuals.Image(
                    data=data,
                    method='impostor',
                    parent=parent_view.scene
                )
            except Exception:
                self.visual = visuals.Image(
                    data=data,
                    interpolation='nearest',
                    parent=parent_view.scene
                )
        
        # 设置位置
        if pos != (0, 0):
            transform = MatrixTransform()
            transform.translate((pos[0], pos[1], 0))
            self.visual.transform = transform
        
    def set_visible(self, visible: bool) -> None:
        self.visible = visible
        if self.visual:
            self.visual.visible = visible
            
    def update_data(self, **kwargs) -> None:
        if not self.visual:
            return
            
        if 'data' in kwargs:
            self.data = kwargs['data']
            self.visual.set_data(self.data)
        if 'pos' in kwargs:
            self.pos = kwargs['pos']
            transform = MatrixTransform()
            transform.translate((self.pos[0], self.pos[1], 0))
            self.visual.transform = transform
        
    def destroy(self) -> None:
        if self.visual:
            self.visual.parent = None
            
    @property
    def bounds(self) -> np.ndarray:
        if self.data is None:
            return np.array([[0, 0, 0], [0, 0, 0]])
        h, w = self.data.shape[:2]
        x, y = self.pos
        return np.array([[x, y, 0], [x + w, y + h, 0]])


class TextEntry(VisualEntry):
    """2D/3D 文本标注元素"""
    
    def __init__(self, parent_view, visual_id: str, text: str, pos: tuple,
                 font_size: float = 12, color: Union[str, tuple] = 'white',
                 rotation: Optional[tuple] = None):
        """
        Args:
            text: 文本内容
            pos: 位置 (x, y) 或 (x, y, z)
            font_size: 字体大小
            color: 文本颜色
            rotation: 旋转角度 (用于3D)
        """
        super().__init__(parent_view, visual_id)
        
        if not VISPY_AVAILABLE:
            return
            
        self.text = text
        self.pos = pos
        self.font_size = font_size
        self.color = color
        self.rotation = rotation
        
        self.visual = visuals.Text(
            text=text,
            pos=pos,
            font_size=font_size,
            color=color,
            parent=parent_view.scene
        )
        
        if rotation and len(pos) == 3:
            transform = MatrixTransform()
            transform.rotate(rotation[0], (1, 0, 0))
            transform.rotate(rotation[1], (0, 1, 0))
            transform.rotate(rotation[2], (0, 0, 1))
            self.visual.transform = transform
        
    def set_visible(self, visible: bool) -> None:
        self.visible = visible
        if self.visual:
            self.visual.visible = visible
            
    def update_data(self, **kwargs) -> None:
        if not self.visual:
            return
            
        if 'text' in kwargs:
            self.text = kwargs['text']
            self.visual.text = self.text
        if 'pos' in kwargs:
            self.pos = kwargs['pos']
            self.visual.pos = self.pos
        if 'font_size' in kwargs:
            self.font_size = kwargs['font_size']
            self.visual.font_size = self.font_size
        if 'color' in kwargs:
            self.color = kwargs['color']
            self.visual.color = self.color
        
    def destroy(self) -> None:
        if self.visual:
            self.visual.parent = None
            
    @property
    def bounds(self) -> np.ndarray:
        # 文本边界简化处理
        pos = list(self.pos) + [0] * (3 - len(self.pos))
        offset = self.font_size * 0.5
        return np.array([
            [pos[0] - offset, pos[1] - offset, pos[2]],
            [pos[0] + offset, pos[1] + offset, pos[2]]
        ])


# ==================== 3D Visual 元素 ====================

class MeshEntry(VisualEntry):
    """3D 网格模型元素"""
    
    def __init__(self, parent_view, visual_id: str, vertices: np.ndarray,
                 faces: np.ndarray, color: Union[str, tuple] = 'white',
                 shading: str = 'smooth'):
        """
        Args:
            vertices: 形状 (N, 3)，顶点坐标
            faces: 形状 (M, 3)，面索引
            color: 网格颜色
            shading: 着色方式 ('flat', 'smooth')
        """
        super().__init__(parent_view, visual_id)
        
        if not VISPY_AVAILABLE:
            return
            
        self.vertices = vertices
        self.faces = faces
        self.color = color
        self.shading = shading
        
        self.visual = visuals.Mesh(
            vertices=vertices,
            faces=faces,
            color=color,
            shading=shading,
            parent=parent_view.scene
        )
        
        if VISPY_AVAILABLE:
            self.visual.set_gl_state('opaque', depth_test=True, blend=False)
        
    def set_visible(self, visible: bool) -> None:
        self.visible = visible
        if self.visual:
            self.visual.visible = visible
            
    def update_data(self, **kwargs) -> None:
        if not self.visual:
            return
            
        if 'vertices' in kwargs:
            self.vertices = kwargs['vertices']
        if 'faces' in kwargs:
            self.faces = kwargs['faces']
        if 'color' in kwargs:
            self.color = kwargs['color']
            
        self.visual.set_data(vertices=self.vertices, faces=self.faces)
        self.visual.color = self.color
        
    def destroy(self) -> None:
        if self.visual:
            self.visual.parent = None
            
    @property
    def bounds(self) -> np.ndarray:
        if self.vertices is None or len(self.vertices) == 0:
            return np.array([[0, 0, 0], [0, 0, 0]])
        mins = self.vertices.min(axis=0)
        maxs = self.vertices.max(axis=0)
        return np.array([mins, maxs])


class SurfacePlotEntry(VisualEntry):
    """3D 曲面图元素"""
    
    def __init__(self, parent_view, visual_id: str, x: np.ndarray, y: np.ndarray,
                 z: np.ndarray, color: Union[str, tuple] = 'white',
                 shading: str = 'smooth'):
        """
        Args:
            x: X 坐标网格
            y: Y 坐标网格
            z: Z 值网格（高度）
            color: 曲面颜色
            shading: 着色方式
        """
        super().__init__(parent_view, visual_id)
        
        if not VISPY_AVAILABLE:
            return
            
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.shading = shading
        
        self.visual = visuals.SurfacePlot(
            x=x,
            y=y,
            z=z,
            color=color,
            shading=shading,
            parent=parent_view.scene
        )
        
    def set_visible(self, visible: bool) -> None:
        self.visible = visible
        if self.visual:
            self.visual.visible = visible
            
    def update_data(self, **kwargs) -> None:
        if not self.visual:
            return
            
        if 'x' in kwargs:
            self.x = kwargs['x']
        if 'y' in kwargs:
            self.y = kwargs['y']
        if 'z' in kwargs:
            self.z = kwargs['z']
            
        self.visual.set_data(x=self.x, y=self.y, z=self.z)
        
    def destroy(self) -> None:
        if self.visual:
            self.visual.parent = None
            
    @property
    def bounds(self) -> np.ndarray:
        if self.z is None:
            return np.array([[0, 0, 0], [0, 0, 0]])
        x_min, x_max = self.x.min(), self.x.max()
        y_min, y_max = self.y.min(), self.y.max()
        z_min, z_max = self.z.min(), self.z.max()
        return np.array([[x_min, y_min, z_min], [x_max, y_max, z_max]])


class VolumeEntry(VisualEntry):
    """3D 体数据元素"""
    
    def __init__(self, parent_view, visual_id: str, data: np.ndarray,
                 method: str = 'mip', threshold: Optional[float] = None):
        """
        Args:
            data: 形状 (D, H, W)，3D 体数据
            method: 渲染方式 ('mip', 'iso', 'translucent')
            threshold: 阈值（用于 iso 模式）
        """
        super().__init__(parent_view, visual_id)
        
        if not VISPY_AVAILABLE:
            return
            
        self.data = data
        self.method = method
        self.threshold = threshold
        
        self.visual = visuals.Volume(
            data=data,
            method=method,
            threshold=threshold,
            parent=parent_view.scene
        )
        
    def set_visible(self, visible: bool) -> None:
        self.visible = visible
        if self.visual:
            self.visual.visible = visible
            
    def update_data(self, **kwargs) -> None:
        if not self.visual:
            return
            
        if 'data' in kwargs:
            self.data = kwargs['data']
            self.visual.set_data(self.data)
        if 'method' in kwargs:
            self.method = kwargs['method']
            self.visual.method = self.method
        if 'threshold' in kwargs:
            self.threshold = kwargs['threshold']
            self.visual.threshold = self.threshold
        
    def destroy(self) -> None:
        if self.visual:
            self.visual.parent = None
            
    @property
    def bounds(self) -> np.ndarray:
        if self.data is None:
            return np.array([[0, 0, 0], [0, 0, 0]])
        d, h, w = self.data.shape
        return np.array([[0, 0, 0], [w, h, d]])


class AxesEntry(VisualEntry):
    """3D 坐标轴元素"""
    
    def __init__(self, parent_view, visual_id: str, size: float = 1.0):
        """
        Args:
            size: 轴长度
        """
        super().__init__(parent_view, visual_id)
        
        if not VISPY_AVAILABLE:
            return
            
        self.size = size
        
        # 使用 XYZAxis
        from vispy.scene.visuals import XYZAxis
        self.visual = XYZAxis(parent=parent_view.scene)
        
        # 缩放
        if size != 1.0:
            transform = MatrixTransform()
            transform.scale((size, size, size))
            self.visual.transform = transform
        
    def set_visible(self, visible: bool) -> None:
        self.visible = visible
        if self.visual:
            self.visual.visible = visible
            
    def update_data(self, **kwargs) -> None:
        if not self.visual:
            return
            
        if 'size' in kwargs:
            self.size = kwargs['size']
            transform = MatrixTransform()
            transform.scale((self.size, self.size, self.size))
            self.visual.transform = transform
        
    def destroy(self) -> None:
        if self.visual:
            self.visual.parent = None
            
    @property
    def bounds(self) -> np.ndarray:
        s = self.size
        return np.array([[0, 0, 0], [s, s, s]])


class GridLinesEntry(VisualEntry):
    """3D 网格线元素"""
    
    def __init__(self, parent_view, visual_id: str, scale: tuple = (1, 1, 1),
                 color: Union[str, tuple] = (0.5, 0.5, 0.5, 0.3)):
        """
        Args:
            scale: 网格间距 (dx, dy, dz)
            color: 网格颜色
        """
        super().__init__(parent_view, visual_id)
        
        if not VISPY_AVAILABLE:
            return
            
        self.scale = scale
        self.color = color
        
        # 使用 GridLines
        self.visual = visuals.GridLines(
            scale=scale,
            color=color,
            parent=parent_view.scene
        )
        
    def set_visible(self, visible: bool) -> None:
        self.visible = visible
        if self.visual:
            self.visual.visible = visible
            
    def update_data(self, **kwargs) -> None:
        if not self.visual:
            return
            
        # GridLines 不支持动态更新，需要重新创建
        if 'scale' in kwargs or 'color' in kwargs:
            if 'scale' in kwargs:
                self.scale = kwargs['scale']
            if 'color' in kwargs:
                self.color = kwargs['color']
                
            self.visual.parent = None
            self.visual = visuals.GridLines(
                scale=self.scale,
                color=self.color,
                parent=self.view.scene
            )
        
    def destroy(self) -> None:
        if self.visual:
            self.visual.parent = None
            
    @property
    def bounds(self) -> np.ndarray:
        # 网格线无明确边界，返回原点附近区域
        s = max(self.scale)
        return np.array([[-s, -s, -s], [s, s, s]])
