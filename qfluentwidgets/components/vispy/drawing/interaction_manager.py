# coding:utf-8
"""
交互管理器模块

实现模式化的鼠标交互管理：
- InteractionMode: 交互模式枚举
- InteractionManager: 交互管理器类
"""
from enum import Enum, auto
from typing import Optional, Tuple, List
import numpy as np
import time
from PySide6.QtCore import QObject, Signal

from .coordinate_system import CoordinateSystem
from .selection_manager import SelectionManager
from .data_models import (
    PrimitiveData, PointData, LineData, BezierData, ArcData, CircleData,
    RectangleData, PolygonData, MarkersData, StyleData
)


class InteractionMode(Enum):
    """交互模式枚举"""
    # 基础模式
    DEFAULT = auto()            # 默认模式（光标模式：拖动平移，滚轮缩放）
    MOVE = auto()               # 移动模式（选择和移动图元）
    
    # 绘制模式
    DRAW_LINE = auto()          # 绘制多段线
    DRAW_RECTANGLE = auto()     # 绘制矩形
    DRAW_CIRCLE = auto()        # 绘制圆形
    DRAW_ELLIPSE = auto()       # 绘制椭圆
    DRAW_BEZIER = auto()        # 绘制贝塞尔曲线
    DRAW_POLYGON = auto()       # 绘制多边形
    DRAW_POINT = auto()         # 绘制点
    
    # 高级模式
    EDIT_BEZIER = auto()        # 编辑贝塞尔曲线控制点（保留，暂作为特定编辑模式）


class InteractionManager(QObject):
    """交互管理器类
    
    管理鼠标交互模式和状态，分发事件到对应的处理逻辑。
    """
    
    # 信号
    primitiveCreated = Signal(PrimitiveData)        # 图元创建完成
    primitiveMoved = Signal(list, float, float)     # 图元移动 (ids, dx, dy)
    interactionStateChanged = Signal(dict)          # 交互状态改变
    
    def __init__(self, coordinate_system: CoordinateSystem, 
                 selection_manager: SelectionManager):
        """初始化交互管理器
        
        Args:
            coordinate_system: 坐标系统
            selection_manager: 选择管理器
        """
        super().__init__()
        self.coordinate_system = coordinate_system
        self.selection_manager = selection_manager
        
        self._current_mode = InteractionMode.DEFAULT
        self._default_style = StyleData()           # 默认样式
        self._create_handles = False                # 是否创建控制端点
        
        # 交互状态
        self._resetState()
        
    def _resetState(self):
        """重置交互状态"""
        self._is_dragging = False                   # 是否正在拖拽
        self._is_box_selecting = False              # 是否正在框选
        self._drag_start_pos: Optional[Tuple[float, float]] = None  # 拖拽起始点
        self._last_move_pos: Optional[Tuple[float, float]] = None   # 上一次移动的位置
        self._current_pos: Optional[Tuple[float, float]] = None     # 当前鼠标位置
        self._points: List[Tuple[float, float]] = []       # 多点绘制的点列表
        self._press_time = 0.0                      # 按下时间戳
        
    def setMode(self, mode: InteractionMode) -> None:
        """设置交互模式"""
        # 切换模式前清理状态
        self._resetState()
        self._current_mode = mode
        
    def getMode(self) -> InteractionMode:
        """获取当前交互模式"""
        return self._current_mode
        
    def setDefaultStyle(self, style: StyleData) -> None:
        """设置默认样式"""
        self._default_style = style.copy()
        
    def getDefaultStyle(self) -> StyleData:
        """获取默认样式"""
        return self._default_style.copy()
        
    def setCreateHandles(self, enabled: bool) -> None:
        """设置是否创建控制端点"""
        self._create_handles = enabled
        
    def getCreateHandles(self) -> bool:
        """获取是否创建控制端点"""
        return self._create_handles
        
    def handleMousePress(self, screen_x: float, screen_y: float, 
                        button: str = 'left', modifiers: set = None) -> dict:
        """处理鼠标按下事件"""
        if modifiers is None:
            modifiers = set()
            
        # 转换为世界坐标
        world_x, world_y = self.coordinate_system.screenToWorld(screen_x, screen_y)
        self._current_pos = (world_x, world_y)
        self._press_time = time.time()
        
        if button == 'left':
            if self._current_mode == InteractionMode.DEFAULT:
                # 默认模式：不处理，让Vispy默认交互生效（平移）
                return {'handled': False}
            
            elif self._current_mode == InteractionMode.MOVE:
                return self._handleMovePress(world_x, world_y, modifiers)
            
            elif self._current_mode in [InteractionMode.DRAW_RECTANGLE, InteractionMode.DRAW_CIRCLE, InteractionMode.DRAW_ELLIPSE]:
                # 拖动绘制模式：记录起点，开始拖动
                self._is_dragging = True
                self._drag_start_pos = (world_x, world_y)
                self._points = [(world_x, world_y)] # Store start point
                return {'handled': True, 'action': 'start_draw_drag'}
            
            elif self._current_mode in [InteractionMode.DRAW_LINE, InteractionMode.DRAW_BEZIER]:
                # 点击-移动-点击模式：添加点
                self._points.append((world_x, world_y))
                return {'handled': True, 'action': 'add_point'}
                
            elif self._current_mode == InteractionMode.DRAW_POLYGON:
                return self._handlePolygonPress(world_x, world_y)

            elif self._current_mode == InteractionMode.DRAW_POINT:
                return self._createPoint(world_x, world_y)
            
        return {'handled': False}
        
    def handleMouseMove(self, screen_x: float, screen_y: float) -> dict:
        """处理鼠标移动事件"""
        world_x, world_y = self.coordinate_system.screenToWorld(screen_x, screen_y)
        self._current_pos = (world_x, world_y)
        
        if self._current_mode == InteractionMode.DEFAULT:
            return {'handled': False}
            
        elif self._current_mode == InteractionMode.MOVE:
            if self._is_dragging and self._last_move_pos:
                dx = world_x - self._last_move_pos[0]
                dy = world_y - self._last_move_pos[1]
                
                # 更新上一次移动的位置
                self._last_move_pos = (world_x, world_y)
                
                # 实时发送移动信号
                if abs(dx) > 1e-6 or abs(dy) > 1e-6:
                    selected_ids = self.selection_manager.getSelectedPrimitives()
                    if selected_ids:
                        self.primitiveMoved.emit(selected_ids, dx, dy)

                return {
                    'handled': True, 
                    'moving': True, 
                    'dx': dx, 
                    'dy': dy, 
                    'preview': True
                }
            elif self._is_box_selecting and self._drag_start_pos:
                # 框选预览
                return {'handled': True, 'preview': True}
                
            return {'handled': False} # 仅悬停
            
        elif self._current_mode in [InteractionMode.DRAW_RECTANGLE, InteractionMode.DRAW_CIRCLE, InteractionMode.DRAW_ELLIPSE]:
            if self._is_dragging:
                return {'handled': True, 'preview': True}
                
        elif self._current_mode in [InteractionMode.DRAW_LINE, InteractionMode.DRAW_BEZIER, InteractionMode.DRAW_POLYGON]:
            if self._points:
                return {'handled': True, 'preview': True}
                
        return {'handled': False}
        
    def handleMouseRelease(self, screen_x: float, screen_y: float, 
                          button: str = 'left') -> dict:
        """处理鼠标释放事件"""
        world_x, world_y = self.coordinate_system.screenToWorld(screen_x, screen_y)
        
        if button == 'left':
            if self._current_mode == InteractionMode.MOVE:
                if self._is_dragging and self._drag_start_pos:
                    self._is_dragging = False
                    
                    # 使用上次移动位置计算增量，避免重复移动
                    if self._last_move_pos:
                        dx = world_x - self._last_move_pos[0]
                        dy = world_y - self._last_move_pos[1]
                    else:
                        dx = world_x - self._drag_start_pos[0]
                        dy = world_y - self._drag_start_pos[1]
                    
                    # 只有发生实质移动才发送信号
                    if abs(dx) > 1e-6 or abs(dy) > 1e-6:
                        selected_ids = self.selection_manager.getSelectedPrimitives()
                        if selected_ids:
                            self.primitiveMoved.emit(selected_ids, dx, dy)
                            
                    self._drag_start_pos = None
                    self._last_move_pos = None
                    return {'handled': True, 'moved': True}
                
                elif self._is_box_selecting and self._drag_start_pos:
                    self._is_box_selecting = False
                    
                    # 执行框选
                    x1, y1 = self._drag_start_pos
                    x2, y2 = world_x, world_y
                    
                    # 检查是否是点击（移动距离很小）
                    dist = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                    
                    # 计算世界坐标系下的阈值（对应屏幕5像素）
                    # 获取当前缩放比例下的单位像素对应的世界距离
                    # 这里通过变换两个屏幕点来估算
                    p1 = self.coordinate_system.screenToWorld(0, 0)
                    p2 = self.coordinate_system.screenToWorld(5, 0)
                    threshold = np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
                    
                    if dist < threshold:
                         # 点击空白处，取消选择
                        self.selection_manager.clearSelection()
                        result = {'handled': True, 'cleared': True}
                    else:
                        # 框选
                        selected_ids = self.selection_manager.boxSelect(x1, y1, x2, y2, append=False)
                        result = {'handled': True, 'selected': True, 'count': len(selected_ids)}
                    
                    self._drag_start_pos = None
                    # 状态改变，清除预览
                    self.interactionStateChanged.emit({'box_select_end': True})
                    return result
            
            elif self._current_mode == InteractionMode.DRAW_RECTANGLE:
                if self._is_dragging:
                    self._is_dragging = False
                    return self._finishRectangle()
                    
            elif self._current_mode == InteractionMode.DRAW_CIRCLE:
                if self._is_dragging:
                    self._is_dragging = False
                    return self._finishCircle()

            elif self._current_mode == InteractionMode.DRAW_ELLIPSE:
                if self._is_dragging:
                    self._is_dragging = False
                    return self._finishEllipse()
                    
        return {'handled': False}
        
    def handleDoubleClick(self, screen_x: float, screen_y: float) -> dict:
        """处理鼠标双击事件"""
        world_x, world_y = self.coordinate_system.screenToWorld(screen_x, screen_y)
        
        if self._current_mode == InteractionMode.DRAW_LINE:
            return self._finishLine()
        elif self._current_mode == InteractionMode.DRAW_BEZIER:
            return self._finishBezier()
            
        return {'handled': False}

    def getCurrentPreview(self) -> Optional[dict]:
        """获取当前预览数据"""
        if not self._current_pos:
            return None
            
        if self._current_mode == InteractionMode.MOVE and self._is_box_selecting and self._drag_start_pos:
            return self._generateBoxSelectionPreview()
        elif self._current_mode == InteractionMode.DRAW_LINE and self._points:
            return self._generateLinePreview()
        elif self._current_mode == InteractionMode.DRAW_RECTANGLE and self._is_dragging and self._points:
            return self._generateRectanglePreview()
        elif self._current_mode == InteractionMode.DRAW_CIRCLE and self._is_dragging and self._points:
            return self._generateCirclePreview()
        elif self._current_mode == InteractionMode.DRAW_ELLIPSE and self._is_dragging and self._points:
            return self._generateEllipsePreview()
        elif self._current_mode == InteractionMode.DRAW_BEZIER and self._points:
            return self._generateBezierPreview()
        elif self._current_mode == InteractionMode.DRAW_POLYGON and self._points:
            return self._generatePolygonPreview()
            
        return None

    def cancelCurrentOperation(self) -> None:
        """取消当前操作"""
        self._resetState()
        self.interactionStateChanged.emit({'cancelled': True})

    # ==================== 内部处理方法 ====================

    def _handleMovePress(self, world_x: float, world_y: float, modifiers: set) -> dict:
        """处理移动模式按下"""
        primitive_id = self.selection_manager.pickPrimitive(world_x, world_y)
        
        if primitive_id:
            # 如果点击了图元
            if not self.selection_manager.isSelected(primitive_id):
                # 如果未选中，则选中它（除非按住Ctrl/Shift多选，这里简化为单选或点击即选中）
                self.selection_manager.selectPrimitive(primitive_id, append=False)
            
            # 开始拖动
            self._is_dragging = True
            self._drag_start_pos = (world_x, world_y)
            self._last_move_pos = (world_x, world_y)
            return {'handled': True, 'selected': True, 'drag_start': True}
        
        # 检查是否点击在选中区域的包围盒内（支持拖动选中区域的空白处）
        elif self._isPointInSelectionBounds(world_x, world_y):
            # 开始拖动选中区域
            self._is_dragging = True
            self._drag_start_pos = (world_x, world_y)
            self._last_move_pos = (world_x, world_y)
            return {'handled': True, 'selected': True, 'drag_start': True}
            
        else:
            # 点击空白处，开始框选（而不是立即取消选择，只有点击释放时且位移小才取消选择）
            # 或者：如果Shift未按下，清除选择，然后开始框选
            # 根据常规软件习惯（如PPT/CAD），点击空白处通常立即取消选择，并开始框选。
            if 'Shift' not in modifiers and 'Control' not in modifiers:
                self.selection_manager.clearSelection()
            
            self._is_box_selecting = True
            self._drag_start_pos = (world_x, world_y)
            return {'handled': True, 'box_select_start': True}

    def _isPointInSelectionBounds(self, x: float, y: float) -> bool:
        """判断点是否在当前选中图元的包围盒内"""
        selected_ids = self.selection_manager.getSelectedPrimitives()
        if not selected_ids:
            return False
            
        # 计算所有选中图元的包围盒并集
        min_x, min_y = float('inf'), float('inf')
        max_x, max_y = float('-inf'), float('-inf')
        
        has_bounds = False
        for pid in selected_ids:
            primitive = self.selection_manager.layer_manager.getPrimitive(pid)
            if primitive and hasattr(primitive.data, 'bounds'):
                b = primitive.data.bounds
                # bounds is [[min_x, min_y], [max_x, max_y]]
                min_x = min(min_x, b[0][0])
                min_y = min(min_y, b[0][1])
                max_x = max(max_x, b[1][0])
                max_y = max(max_y, b[1][1])
                has_bounds = True
                
        if not has_bounds:
            return False
            
        # 增加一点容差，使得操作更容易
        tolerance = 0.0 # 可以根据需要调整，目前为0
        return (min_x - tolerance <= x <= max_x + tolerance and 
                min_y - tolerance <= y <= max_y + tolerance)

    def _generateBoxSelectionPreview(self) -> dict:
        """生成框选预览"""
        if not self._drag_start_pos or not self._current_pos:
            return None
            
        x1, y1 = self._drag_start_pos
        x2, y2 = self._current_pos
        
        return {
            'type': 'box_select',
            'x1': x1, 'y1': y1,
            'x2': x2, 'y2': y2,
            # 可以在这里传递颜色配置，但需要DrawingCanvas支持
            # 目前DrawingCanvas的box_select是硬编码颜色的
        }

    def _handlePolygonPress(self, world_x: float, world_y: float) -> dict:
        """处理多边形绘制点击"""
        if not self._points:
            # 第一个点
            self._points.append((world_x, world_y))
            return {'handled': True, 'action': 'start_polygon'}
        
        # 检查是否闭合（点击位置距离起点很近）
        start_point = self._points[0]
        dist = np.sqrt((world_x - start_point[0])**2 + (world_y - start_point[1])**2)
        
        # 容差值，视坐标系比例而定，这里暂定一个较小值，实际应用中可能需要屏幕像素距离判断
        # 由于我们这里只有世界坐标，假设用户点击很准，或者需要CoordinateSystem转换
        # 为了更准确，建议在Screen坐标判断，但这里参数传入了world。
        # 简单处理：如果距离小于一定阈值（比如 5.0 单位），认为是闭合
        # 注意：这取决于zoom level。更好的方式是计算屏幕距离。
        # 这里的 world_x 是 float，假设世界坐标系尺度正常。
        
        if dist < 2.0 and len(self._points) >= 3: # 至少3个点才能闭合
            return self._finishPolygon()
            
        self._points.append((world_x, world_y))
        return {'handled': True, 'action': 'add_vertex'}

    def _createPoint(self, x: float, y: float) -> dict:
        """创建点"""
        # 使用 PointData 表示单个点，或者 MarkersData
        # 这里为了简单统一，如果只创建一个点，使用 PointData 可能更直观，
        # 但 DrawingCanvas 中 MarkersData 处理了批量点。
        # 如果 _createPoint 是为了“点”工具，通常创建一个点。
        # 让我们检查 PointData 是否更好。
        # PointData 有 radius 属性。
        
        # 使用 MarkersData 保持一致性 (因为之前代码是这样)
        data = MarkersData(
            positions=np.array([[x, y]], dtype=np.float32),
            sizes=np.array([self._default_style.pointSize]), # 使用样式中的大小
            style=self._default_style.copy(),
            with_handles=self._create_handles
        )
        self.primitiveCreated.emit(data)
        return {'handled': True, 'created': True}

    # ==================== 完成绘制 ====================

    def _finishLine(self) -> dict:
        if len(self._points) < 2:
            self._resetState()
            return {'handled': False, 'error': 'Not enough points'}
            
        data = LineData(
            points=np.array(self._points, dtype=np.float32),
            style=self._default_style.copy(),
            with_handles=self._create_handles
        )
        self.primitiveCreated.emit(data)
        self._resetState()
        return {'handled': True, 'created': True, 'type': 'line'}

    def _finishRectangle(self) -> dict:
        if not self._points or not self._current_pos:
            self._resetState()
            return {'handled': False}
            
        x1, y1 = self._points[0]
        x2, y2 = self._current_pos
        
        w, h = abs(x2 - x1), abs(y2 - y1)
        if w < 1e-6 or h < 1e-6:
            self._resetState()
            return {'handled': False, 'error': 'Size too small'}
            
        data = RectangleData(
            pos=(min(x1, x2), min(y1, y2)),
            size=(w, h),
            style=self._default_style.copy(),
            with_handles=self._create_handles
        )
        self.primitiveCreated.emit(data)
        self._resetState()
        return {'handled': True, 'created': True, 'type': 'rectangle'}

    def _finishCircle(self) -> dict:
        if not self._points or not self._current_pos:
            self._resetState()
            return {'handled': False}
            
        center = self._points[0]
        dx = self._current_pos[0] - center[0]
        dy = self._current_pos[1] - center[1]
        radius = np.sqrt(dx**2 + dy**2)
        
        if radius < 1e-6:
            self._resetState()
            return {'handled': False, 'error': 'Size too small'}
        
        data = CircleData(
            center=center,
            radius=(radius, radius),
            style=self._default_style.copy(),
            with_handles=self._create_handles
        )
        self.primitiveCreated.emit(data)
        self._resetState()
        return {'handled': True, 'created': True, 'type': 'circle'}

    def _finishEllipse(self) -> dict:
        if not self._points or not self._current_pos:
            self._resetState()
            return {'handled': False}
            
        center = self._points[0]
        rx = abs(self._current_pos[0] - center[0])
        ry = abs(self._current_pos[1] - center[1])
        
        if rx < 1e-6 or ry < 1e-6:
            self._resetState()
            return {'handled': False, 'error': 'Size too small'}
            
        data = CircleData(
            center=center,
            radius=(rx, ry),
            style=self._default_style.copy(),
            with_handles=self._create_handles
        )
        # 显式修改 type_name 为 ellipse 以便区分
        # 注意：CircleData 默认 type_name 为 "circle"，这里覆盖它可能需要在 DataModel 中支持，
        # 或者仅仅作为运行时标识。鉴于 CircleData 支持 (rx, ry)，它本质上就是椭圆。
        # 为了保持一致性，我们不修改 type_name，或者如果上层逻辑依赖 type_name 区分工具，
        # 我们可能需要派生 EllipseData。
        # 但根据 data_models.py，CircleData 已经包含 rx, ry。
        # 如果需要区分，可以在 userData 中标记，或者直接使用 CircleData。
        # 考虑到 InteractionMode 区分了 Circle 和 Ellipse，这里返回 type='ellipse' 给调用者是正确的。
        
        self.primitiveCreated.emit(data)
        self._resetState()
        return {'handled': True, 'created': True, 'type': 'ellipse'}


    def _finishBezier(self) -> dict:
        if len(self._points) < 2:
            self._resetState()
            return {'handled': False}
            
        # 贝塞尔曲线阶数为 点数 - 1
        data = BezierData(
            control_points=np.array(self._points, dtype=np.float32),
            degree=len(self._points) - 1,
            style=self._default_style.copy(),
            with_handles=self._create_handles
        )
        self.primitiveCreated.emit(data)
        self._resetState()
        return {'handled': True, 'created': True, 'type': 'bezier'}

    def _finishPolygon(self) -> dict:
        if len(self._points) < 3:
            self._resetState()
            return {'handled': False}
            
        data = PolygonData(
            vertices=np.array(self._points, dtype=np.float32),
            style=self._default_style.copy(),
            with_handles=self._create_handles
        )
        self.primitiveCreated.emit(data)
        self._resetState()
        return {'handled': True, 'created': True, 'type': 'polygon'}

    # ==================== 预览生成 ====================

    def _generateLinePreview(self) -> dict:
        points = self._points + [self._current_pos]
        return {'type': 'line', 'points': points}

    def _generateRectanglePreview(self) -> dict:
        x1, y1 = self._points[0]
        x2, y2 = self._current_pos
        return {
            'type': 'rectangle',
            'x1': min(x1, x2), 'y1': min(y1, y2),
            'width': abs(x2 - x1), 'height': abs(y2 - y1)
        }

    def _generateCirclePreview(self) -> dict:
        center = self._points[0]
        dx = self._current_pos[0] - center[0]
        dy = self._current_pos[1] - center[1]
        radius = np.sqrt(dx**2 + dy**2)
        return {'type': 'circle', 'center': center, 'radius': (radius, radius)}

    def _generateEllipsePreview(self) -> dict:
        center = self._points[0]
        dx = abs(self._current_pos[0] - center[0])
        dy = abs(self._current_pos[1] - center[1])
        return {'type': 'ellipse', 'center': center, 'radius': (dx, dy)}

    def _generateBezierPreview(self) -> dict:
        points = self._points + [self._current_pos]
        return {'type': 'bezier', 'points': points}

    def _generatePolygonPreview(self) -> dict:
        points = self._points + [self._current_pos]
        return {'type': 'polygon', 'points': points}
