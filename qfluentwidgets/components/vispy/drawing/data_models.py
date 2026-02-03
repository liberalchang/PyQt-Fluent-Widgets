# coding:utf-8
"""
数据模型模块

定义交互式绘图框架中所有图元的数据结构，包括：
- StyleData: 样式数据（线宽、颜色、填充等）
- PrimitiveData: 图元基类
- 各种具体图元数据类（LineData、BezierData等）
"""
from dataclasses import dataclass, field
from typing import Optional, Tuple
from abc import ABC
import numpy as np
import uuid
import math


@dataclass
class StyleData:
    """样式数据类
    
    定义图元的视觉样式属性。
    """
    # 线条相关
    lineWidth: float = 1.0                          # 线宽
    lineColor: Tuple[float, float, float, float] = (1.0, 1.0, 1.0, 1.0)  # 线条颜色 (R,G,B,A)
    
    # 填充相关（适用于闭合图形）
    filled: bool = True                             # 是否填充
    fillColor: Tuple[float, float, float, float] = (0.5, 0.5, 0.5, 0.8)  # 填充颜色 (R,G,B,A)
    
    # 边缘线条相关（适用于闭合图形）
    showBorder: bool = True                         # 是否显示边缘线条
    borderColor: Tuple[float, float, float, float] = (1.0, 1.0, 1.0, 1.0)  # 边缘线条颜色 (R,G,B,A)
    borderWidth: float = 1.0                        # 边缘线条宽度
    
    # 点相关
    pointSize: float = 6.0                          # 点大小（直径）
    
    def copy(self) -> 'StyleData':
        """创建样式数据的副本"""
        return StyleData(
            lineWidth=self.lineWidth,
            lineColor=self.lineColor,
            filled=self.filled,
            fillColor=self.fillColor,
            showBorder=self.showBorder,
            borderColor=self.borderColor,
            borderWidth=self.borderWidth,
            pointSize=self.pointSize
        )


@dataclass
class PrimitiveData(ABC):
    """图元数据基类
    
    所有图元数据类的基类，包含通用属性。
    """
    id: str = field(default_factory=lambda: str(uuid.uuid4()))  # 唯一标识符
    name: str = ""                                  # 图元名称
    layer_id: str = ""                              # 所属图层ID
    type_name: str = ""                             # 类型名称（用于分组）
    style: StyleData = field(default_factory=StyleData)  # 样式数据
    visible: bool = True                            # 是否可见
    locked: bool = False                            # 是否锁定（锁定后不可编辑）
    with_handles: bool = False                      # 是否创建控制端点（Handle）
    userData: Optional[dict] = None                 # 用户自定义数据
    
    def __post_init__(self):
        """初始化后处理"""
        if self.userData is None:
            self.userData = {}
        if not self.name:
            self.name = f"{self.type_name}_{self.id[:8]}"


@dataclass
class PointData(PrimitiveData):
    """点数据类
    
    表示单个点图元，可以作为端点或控制点。
    """
    x: float = 0.0                                   # X坐标
    y: float = 0.0                                   # Y坐标
    radius: float = 3.0                              # 点的显示半径
    
    def __post_init__(self):
        self.type_name = "point"
        super().__post_init__()
        
    @property
    def bounds(self) -> np.ndarray:
        """返回边界框 [[min_x, min_y], [max_x, max_y]]"""
        return np.array([[self.x - self.radius, self.y - self.radius], 
                        [self.x + self.radius, self.y + self.radius]])


@dataclass
class LineData(PrimitiveData):
    """线条数据类
    
    表示直线或折线（多段线）。
    """
    points: np.ndarray = field(default_factory=lambda: np.array([[0, 0], [1, 1]], dtype=np.float32))  # 形状 (N, 2)
    
    def __post_init__(self):
        self.type_name = "line"
        super().__post_init__()
        
    @property
    def bounds(self) -> np.ndarray:
        """返回边界框 [[min_x, min_y], [max_x, max_y]]"""
        if len(self.points) == 0:
            return np.array([[0, 0], [0, 0]])
        mins = self.points.min(axis=0)
        maxs = self.points.max(axis=0)
        return np.array([mins, maxs])


@dataclass
class BezierData(PrimitiveData):
    """贝塞尔曲线数据类
    
    支持二阶（Quadratic，3个控制点）和三阶（Cubic，4个控制点）贝塞尔曲线。
    """
    control_points: np.ndarray = field(default_factory=lambda: np.array([[0, 0], [0.5, 1], [1, 0]], dtype=np.float32))  # 控制点
    degree: int = 2                                 # 阶数：2=二阶，3=三阶
    
    def __post_init__(self):
        self.type_name = "bezier"
        super().__post_init__()
        # 验证控制点数量
        if self.degree == 2 and len(self.control_points) < 3:
            raise ValueError("二阶贝塞尔曲线至少需要3个控制点")
        elif self.degree == 3 and len(self.control_points) < 4:
            raise ValueError("三阶贝塞尔曲线至少需要4个控制点")
        # 如果控制点数量超过要求，只使用前面的点
            
    @property
    def bounds(self) -> np.ndarray:
        """返回边界框"""
        if len(self.control_points) == 0:
            return np.array([[0, 0], [0, 0]])
        mins = self.control_points.min(axis=0)
        maxs = self.control_points.max(axis=0)
        return np.array([mins, maxs])
        
    def evaluate(self, t: float) -> np.ndarray:
        """计算贝塞尔曲线上参数t处的点
        
        Args:
            t: 参数，范围[0, 1]
            
        Returns:
            点坐标 (x, y)
        """
        if self.degree == 2:
            # 二阶贝塞尔：B(t) = (1-t)²P₀ + 2(1-t)tP₁ + t²P₂
            p0, p1, p2 = self.control_points[:3]
            return (1-t)**2 * p0 + 2*(1-t)*t * p1 + t**2 * p2
        elif self.degree == 3:
            # 三阶贝塞尔：B(t) = (1-t)³P₀ + 3(1-t)²tP₁ + 3(1-t)t²P₂ + t³P₃
            p0, p1, p2, p3 = self.control_points[:4]
            return (1-t)**3 * p0 + 3*(1-t)**2*t * p1 + 3*(1-t)*t**2 * p2 + t**3 * p3
        else:
            # 高阶贝塞尔通用公式 (De Casteljau's algorithm 或 Bernstein polynomials)
            # 为简化实现，如果控制点数足够，支持任意阶数
            # 但这里我们只实现最常用的，对于不支持的阶数，尝试降级处理或报错
            # 这里实现一个通用的 Bernstein 多项式求值
            n = len(self.control_points) - 1
            if n != self.degree and n > 0:
                 # 如果控制点数量与degree不符，以控制点数量为准
                 n = len(self.control_points) - 1
            
            point = np.zeros(2)
            for i in range(n + 1):
                # Binomial coefficient: nCk = n! / (k! * (n-k)!)
                coeff = math.comb(n, i)
                # Bernstein basis: B_{i,n}(t) = C(n,i) * t^i * (1-t)^(n-i)
                basis = coeff * (t**i) * ((1-t)**(n-i))
                point += basis * self.control_points[i]
            return point
            
    def sample(self, num_points: int = 50) -> np.ndarray:
        """采样贝塞尔曲线上的点
        
        Args:
            num_points: 采样点数量
            
        Returns:
            采样点数组，形状 (num_points, 2)
        """
        t_values = np.linspace(0, 1, num_points)
        points = np.array([self.evaluate(t) for t in t_values])
        return points


@dataclass
class ArcData(PrimitiveData):
    """圆弧数据类
    
    表示圆弧，通过中心、半径和起止角度定义。
    """
    center: Tuple[float, float] = (0.0, 0.0)        # 中心点 (x, y)
    radius: float = 1.0                             # 半径
    start_angle: float = 0.0                        # 起始角度（度数）
    end_angle: float = 90.0                         # 结束角度（度数）
    
    def __post_init__(self):
        self.type_name = "arc"
        super().__post_init__()
        
    @property
    def bounds(self) -> np.ndarray:
        """返回边界框（简化为圆的边界框）"""
        cx, cy = self.center
        r = self.radius
        return np.array([[cx - r, cy - r], [cx + r, cy + r]])
        
    def sample(self, num_points: int = 50) -> np.ndarray:
        """采样圆弧上的点
        
        Args:
            num_points: 采样点数量
            
        Returns:
            采样点数组，形状 (num_points, 2)
        """
        # 转换为弧度
        start_rad = np.deg2rad(self.start_angle)
        end_rad = np.deg2rad(self.end_angle)
        
        # 生成角度序列
        angles = np.linspace(start_rad, end_rad, num_points)
        
        # 计算点坐标
        cx, cy = self.center
        x = cx + self.radius * np.cos(angles)
        y = cy + self.radius * np.sin(angles)
        
        return np.column_stack([x, y])


@dataclass
class CircleData(PrimitiveData):
    """圆形数据类
    
    表示圆形或椭圆。
    """
    center: Tuple[float, float] = (0.0, 0.0)        # 中心点 (x, y)
    radius: Tuple[float, float] = (1.0, 1.0)        # 半径 (rx, ry)，相等时为圆形
    
    def __post_init__(self):
        self.type_name = "circle"
        super().__post_init__()
        
    @property
    def bounds(self) -> np.ndarray:
        """返回边界框"""
        cx, cy = self.center
        rx, ry = self.radius
        return np.array([[cx - rx, cy - ry], [cx + rx, cy + ry]])
        
    @property
    def is_circle(self) -> bool:
        """是否为正圆"""
        return abs(self.radius[0] - self.radius[1]) < 1e-6


@dataclass
class RectangleData(PrimitiveData):
    """矩形数据类
    
    表示轴对齐的矩形。
    """
    pos: Tuple[float, float] = (0.0, 0.0)           # 左上角位置 (x, y)
    size: Tuple[float, float] = (1.0, 1.0)          # 尺寸 (width, height)
    
    def __post_init__(self):
        self.type_name = "rectangle"
        super().__post_init__()
        
    @property
    def bounds(self) -> np.ndarray:
        """返回边界框"""
        x, y = self.pos
        w, h = self.size
        return np.array([[x, y], [x + w, y + h]])
        
    @property
    def center(self) -> Tuple[float, float]:
        """返回中心点"""
        x, y = self.pos
        w, h = self.size
        return (x + w / 2, y + h / 2)
        
    def contains_point(self, point: Tuple[float, float]) -> bool:
        """判断点是否在矩形内
        
        Args:
            point: 点坐标 (x, y)
            
        Returns:
            是否在矩形内
        """
        px, py = point
        x, y = self.pos
        w, h = self.size
        return x <= px <= x + w and y <= py <= y + h


@dataclass
class PolygonData(PrimitiveData):
    """多边形数据类
    
    表示任意多边形。
    """
    vertices: np.ndarray = field(default_factory=lambda: np.array([[0, 0], [1, 0], [0.5, 1]], dtype=np.float32))  # 顶点，形状 (N, 2)
    
    def __post_init__(self):
        self.type_name = "polygon"
        super().__post_init__()
        
    @property
    def bounds(self) -> np.ndarray:
        """返回边界框"""
        if len(self.vertices) == 0:
            return np.array([[0, 0], [0, 0]])
        mins = self.vertices.min(axis=0)
        maxs = self.vertices.max(axis=0)
        return np.array([mins, maxs])
        
    def contains_point(self, point: Tuple[float, float]) -> bool:
        """判断点是否在多边形内（射线法）
        
        Args:
            point: 点坐标 (x, y)
            
        Returns:
            是否在多边形内
        """
        px, py = point
        n = len(self.vertices)
        inside = False
        
        p1x, p1y = self.vertices[0]
        for i in range(1, n + 1):
            p2x, p2y = self.vertices[i % n]
            if py > min(p1y, p2y):
                if py <= max(p1y, p2y):
                    if px <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (py - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or px <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
            
        return inside


@dataclass
class MarkersData(PrimitiveData):
    """标记点数据类
    
    表示散点标记。
    """
    positions: np.ndarray = field(default_factory=lambda: np.array([[0, 0]], dtype=np.float32))  # 点位置，形状 (N, 2)
    sizes: np.ndarray = field(default_factory=lambda: np.array([5.0]))  # 点大小，形状 (N,) 或标量
    symbol: str = 'o'                               # 符号类型：'o', 's', '^', 'd' 等
    
    def __post_init__(self):
        self.type_name = "markers"
        super().__post_init__()
        
    @property
    def bounds(self) -> np.ndarray:
        """返回边界框"""
        if len(self.positions) == 0:
            return np.array([[0, 0], [0, 0]])
            
        # 考虑点的大小
        if np.isscalar(self.sizes):
            max_size = float(self.sizes)
        else:
            max_size = float(np.max(self.sizes)) if len(self.sizes) > 0 else 0.0
            
        radius = max_size / 2.0
        
        mins = self.positions.min(axis=0) - radius
        maxs = self.positions.max(axis=0) + radius
        return np.array([mins, maxs])


@dataclass
class ImageData(PrimitiveData):
    """图像数据类
    
    表示位图图像。
    """
    data: Optional[np.ndarray] = None               # 图像数据，形状 (H, W) 或 (H, W, 3/4)
    pos: Tuple[float, float] = (0.0, 0.0)           # 左下角位置 (x, y)
    interpolation: str = 'nearest'                  # 插值方式
    image_path: Optional[str] = None                # 图像文件路径（可选，用于记录来源）
    
    def __post_init__(self):
        self.type_name = "image"
        super().__post_init__()
        
    @property
    def bounds(self) -> np.ndarray:
        """返回边界框"""
        if self.data is None:
            return np.array([[0, 0], [0, 0]])
        h, w = self.data.shape[:2]
        x, y = self.pos
        return np.array([[x, y], [x + w, y + h]])
        
    @property
    def size(self) -> Tuple[int, int]:
        """返回图像尺寸 (width, height)"""
        if self.data is None:
            return (0, 0)
        h, w = self.data.shape[:2]
        return (w, h)
