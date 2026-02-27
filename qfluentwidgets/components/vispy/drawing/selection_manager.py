# coding:utf-8
"""
选择管理器模块

实现图元的选择功能：
- 点选检测：鼠标点击选中图元
- 框选检测：拖拽矩形框选中多个图元
- 高亮渲染：为选中的图元添加高亮效果
"""
from typing import List, Set, Optional
import numpy as np
from PySide6.QtCore import QObject, Signal

try:
    from vispy.scene import visuals  # noqa: F401
    VISPY_AVAILABLE = True
except ImportError:
    VISPY_AVAILABLE = False

from .layer_manager import LayerManager, Primitive
from .coordinate_system import CoordinateSystem
from .data_models import LineData, RectangleData, CircleData, PolygonData, BezierData, ArcData


class SelectionManager(QObject):
    """选择管理器类
    
    管理图元的选择状态，提供点选和框选功能。
    """
    
    # 信号
    selectionChanged = Signal(list)  # 选中的图元ID列表
    
    def __init__(self, layer_manager: LayerManager, coordinate_system: CoordinateSystem, 
                 parent_view=None):
        """初始化选择管理器
        
        Args:
            layer_manager: 图层管理器
            coordinate_system: 坐标系统
            parent_view: vispy ViewBox 对象
        """
        super().__init__()
        self.layer_manager = layer_manager
        self.coordinate_system = coordinate_system
        self.parent_view = parent_view
        
        self._selected_ids: Set[str] = set()    # 当前选中的图元ID集合
        self._highlight_visuals: dict = {}       # 高亮 visual 对象缓存
        self._selection_threshold = 5.0          # 点选阈值（像素）
        
    def selectPrimitive(self, primitive_id: str, append: bool = False) -> bool:
        """选中图元
        
        Args:
            primitive_id: 图元ID
            append: 是否追加到当前选择（True）还是替换当前选择（False）
            
        Returns:
            是否成功选中
        """
        primitive = self.layer_manager.getPrimitive(primitive_id)
        if primitive is None or primitive.data.locked:
            return False
            
        if not append:
            # 清除之前的选择
            self.clearSelection()
            
        # 添加到选中集合
        self._selected_ids.add(primitive_id)
        primitive.selected = True
        
        # 创建高亮效果
        self._createHighlight(primitive)
        
        # 发送信号
        self.selectionChanged.emit(list(self._selected_ids))
        return True
        
    def deselectPrimitive(self, primitive_id: str) -> bool:
        """取消选中图元
        
        Args:
            primitive_id: 图元ID
            
        Returns:
            是否成功取消选中
        """
        if primitive_id not in self._selected_ids:
            return False
            
        primitive = self.layer_manager.getPrimitive(primitive_id)
        if primitive:
            primitive.selected = False
            
        self._selected_ids.remove(primitive_id)
        
        # 移除高亮效果
        self._removeHighlight(primitive_id)
        
        # 发送信号
        self.selectionChanged.emit(list(self._selected_ids))
        return True
        
    def clearSelection(self) -> None:
        """清除所有选择"""
        for primitive_id in list(self._selected_ids):
            primitive = self.layer_manager.getPrimitive(primitive_id)
            if primitive:
                primitive.selected = False
            self._removeHighlight(primitive_id)
            
        self._selected_ids.clear()
        self.selectionChanged.emit([])
        
    def getSelectedPrimitives(self) -> List[str]:
        """获取当前选中的图元ID列表
        
        Returns:
            图元ID列表
        """
        return list(self._selected_ids)
        
    def isSelected(self, primitive_id: str) -> bool:
        """判断图元是否被选中
        
        Args:
            primitive_id: 图元ID
            
        Returns:
            是否被选中
        """
        return primitive_id in self._selected_ids
        
    def pickPrimitive(self, world_x: float, world_y: float) -> Optional[str]:
        """点选检测：查找鼠标点击位置的图元
        
        Args:
            world_x: 世界坐标 X
            world_y: 世界坐标 Y
            
        Returns:
            选中的图元ID，如果没有选中返回 None
        """
        # 计算选择阈值（世界坐标）
        threshold = self.coordinate_system.distanceScreenToWorld(self._selection_threshold)
        
        # 从上层到下层遍历图元（逆序）
        layers = self.layer_manager.getAllLayers()
        for layer in reversed(layers):
            if not layer.visible or layer.locked:
                continue
                
            primitives = layer.getAllPrimitives()
            # 逆序遍历同层图元（后绘制的在上层）
            for primitive in reversed(primitives):
                if not primitive.data.visible or primitive.data.locked:
                    continue
                    
                if self._hitTest(primitive, world_x, world_y, threshold):
                    return primitive.id
                    
        return None
        
    def boxSelect(self, world_x1: float, world_y1: float, 
                  world_x2: float, world_y2: float, append: bool = False) -> List[str]:
        """框选检测：选中矩形框内的所有图元
        
        Args:
            world_x1, world_y1: 矩形框第一个角的世界坐标
            world_x2, world_y2: 矩形框第二个角的世界坐标
            append: 是否追加到当前选择
            
        Returns:
            选中的图元ID列表
        """
        if not append:
            self.clearSelection()
            
        # 归一化矩形框
        min_x = min(world_x1, world_x2)
        max_x = max(world_x1, world_x2)
        min_y = min(world_y1, world_y2)
        max_y = max(world_y1, world_y2)
        
        selected_ids = []
        
        # 遍历所有可见图元
        for primitive in self.layer_manager.getAllPrimitives():
            if not primitive.data.visible or primitive.data.locked:
                continue
                
            # 检测边界框是否与选择框相交
            bounds = primitive.data.bounds
            if self._boxIntersects(bounds, min_x, min_y, max_x, max_y):
                if self.selectPrimitive(primitive.id, append=True):
                    selected_ids.append(primitive.id)
                    
        return selected_ids
        
    def _hitTest(self, primitive: Primitive, x: float, y: float, threshold: float) -> bool:
        """碰撞检测：判断点是否在图元上
        
        Args:
            primitive: 图元对象
            x, y: 点的世界坐标
            threshold: 检测阈值
            
        Returns:
            是否命中
        """
        data = primitive.data
        type_name = data.type_name
        
        # 线条类型：点到线段的距离
        if type_name == "line":
            return self._hitTestLine(data, x, y, threshold)
            
        # 贝塞尔曲线：采样后检测
        elif type_name == "bezier":
            return self._hitTestBezier(data, x, y, threshold)
            
        # 圆弧：采样后检测
        elif type_name == "arc":
            return self._hitTestArc(data, x, y, threshold)
            
        # 圆形：点到圆心的距离
        elif type_name == "circle":
            return self._hitTestCircle(data, x, y, threshold)
            
        # 矩形：点在矩形内
        elif type_name == "rectangle":
            return self._hitTestRectangle(data, x, y)
            
        # 多边形：点在多边形内
        elif type_name == "polygon":
            return self._hitTestPolygon(data, x, y)
            
        # 标记点：点到标记的距离
        elif type_name == "markers":
            return self._hitTestMarkers(data, x, y, threshold)
            
        # 图像：点在图像边界内
        elif type_name == "image":
            bounds = data.bounds
            return bounds[0][0] <= x <= bounds[1][0] and bounds[0][1] <= y <= bounds[1][1]
            
        return False
        
    def _hitTestLine(self, data: LineData, x: float, y: float, threshold: float) -> bool:
        """线条碰撞检测"""
        points = data.points
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            dist = self._pointToSegmentDistance(x, y, p1[0], p1[1], p2[0], p2[1])
            if dist < threshold:
                return True
        return False
        
    def _hitTestBezier(self, data: BezierData, x: float, y: float, threshold: float) -> bool:
        """贝塞尔曲线碰撞检测（采样后检测）"""
        sampled_points = data.sample(num_points=50)
        for i in range(len(sampled_points) - 1):
            p1 = sampled_points[i]
            p2 = sampled_points[i + 1]
            dist = self._pointToSegmentDistance(x, y, p1[0], p1[1], p2[0], p2[1])
            if dist < threshold:
                return True
        return False
        
    def _hitTestArc(self, data: ArcData, x: float, y: float, threshold: float) -> bool:
        """圆弧碰撞检测（采样后检测）"""
        sampled_points = data.sample(num_points=50)
        for i in range(len(sampled_points) - 1):
            p1 = sampled_points[i]
            p2 = sampled_points[i + 1]
            dist = self._pointToSegmentDistance(x, y, p1[0], p1[1], p2[0], p2[1])
            if dist < threshold:
                return True
        return False
        
    def _hitTestCircle(self, data: CircleData, x: float, y: float, threshold: float) -> bool:
        """圆形碰撞检测"""
        cx, cy = data.center
        rx, ry = data.radius
        
        # 椭圆方程判断
        if data.style.filled:
            # 填充模式：点在椭圆内
            normalized_dist = ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2
            return normalized_dist <= 1.0
        else:
            # 非填充模式：点在椭圆边缘附近
            normalized_dist = ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2
            edge_dist = abs(np.sqrt(normalized_dist) - 1.0) * min(rx, ry)
            return edge_dist < threshold
            
    def _hitTestRectangle(self, data: RectangleData, x: float, y: float) -> bool:
        """矩形碰撞检测"""
        return data.contains_point((x, y))
        
    def _hitTestPolygon(self, data: PolygonData, x: float, y: float) -> bool:
        """多边形碰撞检测"""
        return data.contains_point((x, y))
        
    def _hitTestMarkers(self, data, x: float, y: float, threshold: float) -> bool:
        """标记点碰撞检测"""
        for pos in data.positions:
            dist = np.sqrt((x - pos[0])**2 + (y - pos[1])**2)
            if dist < threshold:
                return True
        return False
        
    @staticmethod
    def _pointToSegmentDistance(px: float, py: float, x1: float, y1: float, 
                                 x2: float, y2: float) -> float:
        """计算点到线段的最短距离
        
        Args:
            px, py: 点坐标
            x1, y1: 线段起点
            x2, y2: 线段终点
            
        Returns:
            最短距离
        """
        dx = x2 - x1
        dy = y2 - y1
        
        if dx == 0 and dy == 0:
            # 线段退化为点
            return np.sqrt((px - x1)**2 + (py - y1)**2)
            
        # 投影参数 t
        t = max(0, min(1, ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)))
        
        # 投影点
        proj_x = x1 + t * dx
        proj_y = y1 + t * dy
        
        # 距离
        return np.sqrt((px - proj_x)**2 + (py - proj_y)**2)
        
    def _createHighlight(self, primitive: Primitive) -> None:
        """创建高亮效果
        
        Args:
            primitive: 图元对象
        """
        # 如果已有高亮，先移除
        self._removeHighlight(primitive.id)
        
        # 根据图元类型创建高亮 Visual
        # 目前简单实现：创建一个包围盒矩形
        # 优化：使用灰色虚线框
        bounds = primitive.data.bounds
        if bounds is None:
            return
            
        x_min, y_min = bounds[0]
        x_max, y_max = bounds[1]
        
        # 增加内边距，确保包围盒比物体稍大，提高可见性
        padding = 1.0
        width = max(x_max - x_min, 1e-4) + padding * 2
        height = max(y_max - y_min, 1e-4) + padding * 2
        center_x = x_min + (x_max - x_min) / 2
        center_y = y_min + (y_max - y_min) / 2
        
        # 创建矩形高亮框 (灰色)
        if VISPY_AVAILABLE and self.parent_view:
            from vispy.scene.visuals import Rectangle
            from vispy.color import Color  # noqa: F401
            
            # 灰色高亮框
            rect = Rectangle(center=(center_x, center_y), width=width, height=height,
                           color=(0.5, 0.5, 0.5, 0.1), border_color=(0.5, 0.5, 0.5, 1.0),
                           border_width=2, parent=self.parent_view.scene)
            rect.order = 1000 # 确保在最上层
            self._highlight_visuals[primitive.id] = rect

    def _removeHighlight(self, primitive_id: str) -> None:
        """移除高亮效果"""
        if primitive_id in self._highlight_visuals:
            visual = self._highlight_visuals[primitive_id]
            visual.parent = None
            del self._highlight_visuals[primitive_id]

    def _boxIntersects(self, bounds: np.ndarray, x1: float, y1: float, x2: float, y2: float) -> bool:
        """检测边界框是否与矩形相交（或包含）"""
        if bounds is None:
            return False
            
        b_x1, b_y1 = bounds[0]
        b_x2, b_y2 = bounds[1]
        
        # 检查是否相交
        # 矩形1: (x1, y1) - (x2, y2)
        # 矩形2: (b_x1, b_y1) - (b_x2, b_y2)
        
        # 如果一个矩形在另一个矩形的左侧、右侧、上方或下方，则不相交
        if x1 > b_x2 or x2 < b_x1 or y1 > b_y2 or y2 < b_y1:
            return False
            
        return True
                
    def updateHighlights(self) -> None:
        """更新所有选中图元的高亮效果"""
        for primitive_id in list(self._selected_ids):
            primitive = self.layer_manager.getPrimitive(primitive_id)
            if primitive:
                self._removeHighlight(primitive_id)
                self._createHighlight(primitive)
                
    def setSelectionThreshold(self, threshold: float) -> None:
        """设置点选阈值
        
        Args:
            threshold: 阈值（像素）
        """
        self._selection_threshold = max(1.0, threshold)
