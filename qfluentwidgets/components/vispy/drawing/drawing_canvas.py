# coding:utf-8
"""
交互式绘图Canvas模块

扩展VispyCanvas2D，集成所有管理器，提供完整的交互式绘图功能。
"""
import numpy as np
import math
from typing import Optional, Dict, List, Union
from PySide6.QtCore import QObject, Signal

from ..vispy_canvas import VispyCanvas2D, VISPY_AVAILABLE
from ..vispy_visuals import LineEntry, MarkersEntry, ImageEntry
from .coordinate_system import CoordinateSystem
from .layer_manager import LayerManager, Primitive

try:
    from vispy.scene.cameras import PanZoomCamera
except ImportError:
    PanZoomCamera = None

from .selection_manager import SelectionManager
from .interaction_manager import InteractionManager, InteractionMode
from .drawing_visuals import (
    BezierCurveEntry, ArcEntry, StyledPolygonEntry,
    StyledRectangleEntry, StyledEllipseEntry
)
from .data_models import (
    PrimitiveData, PointData, LineData, BezierData, ArcData, CircleData,
    RectangleData, PolygonData, MarkersData, ImageData, StyleData
)


class InteractiveDrawingCanvas(QObject, VispyCanvas2D):
    """交互式绘图Canvas类
    
    扩展VispyCanvas2D，添加交互式绘图特性：
    - 集成所有管理器
    - 处理鼠标事件
    - 管理预览图元
    - 提供图元CRUD接口
    """
    
    # 信号
    mouseMoved = Signal(object, object)  # 鼠标移动 (screen_pos, world_pos)

    def __init__(self, scale_factor=1.0, origin_offset=(0.0, 0.0), grid_size=100.0, grid_spacing=10.0):
        """初始化交互式绘图Canvas
        
        Args:
            scale_factor: 像素与物理尺寸比例
            origin_offset: 原点世界坐标值
            grid_size: 网格半径大小
            grid_spacing: 网格间距
        """
        # QObject.__init__(self) # implicit in super() if QObject is first
        # But VispyCanvas2D needs init too.
        # super() with multiple inheritance calls MRO.
        # QObject init is safe. VispyCanvasBase init is safe.
        super().__init__()
        # VispyCanvas2D.__init__(self) # Handled by MRO if VispyCanvas2D calls super?
        # VispyCanvasBase does NOT call super().__init__().
        # So super().__init__() calls QObject.__init__.
        # I need to explicitly call VispyCanvas2D.__init__(self).
        VispyCanvas2D.__init__(self, grid_size=grid_size, grid_spacing=grid_spacing)
        
        if not VISPY_AVAILABLE:
            return
            
        # 创建管理器
        self.coordinate_system = CoordinateSystem(
            self.view, 
            self.canvas,
            scale_factor=scale_factor,
            origin_offset=origin_offset
        )
        self.layer_manager = LayerManager()
        self.selection_manager = SelectionManager(
            self.layer_manager,
            self.coordinate_system,
            self.view
        )
        self.interaction_manager = InteractionManager(
            self.coordinate_system,
            self.selection_manager
        )
        
        # 连接交互信号
        self.interaction_manager.primitiveCreated.connect(self._onPrimitiveCreated)
        self.interaction_manager.primitiveMoved.connect(self._onPrimitiveMoved)
        
        # 启用鼠标追踪，确保移动事件在未按键时也能触发（用于预览）
        if self.native_widget:
            self.native_widget.setMouseTracking(True)
            
        # 绑定Vispy事件预览图元
        self._preview_visual: Optional[object] = None
        self._preview_aux_visual: Optional[object] = None
        self._preview_type: Optional[str] = None
        
        # 绑定鼠标事件
        # 优先绑定到 view 的事件
        if self.view:
            self.view.events.mouse_press.connect(self._onMousePress)
            self.view.events.mouse_move.connect(self._onMouseMove)
            self.view.events.mouse_release.connect(self._onMouseRelease)
            self.view.events.mouse_wheel.connect(self._onMouseWheel)
            
        if self.canvas:
            # 双击事件保留在 canvas 上（view 可能不支持）
            self.canvas.events.mouse_double_click.connect(self._onMouseDoubleClick)
            # 绑定 Canvas 级别的鼠标移动事件，用于实时坐标显示（解决仅在按键时更新的问题）
            self.canvas.events.mouse_move.connect(self._onCanvasMouseMove)
            
            # 确保 ESC 键处理不冲突
            # 不连接Vispy键盘事件，避免与Qt键盘事件冲突
            # ESC键处理由Qt层面的drawing_widget.py负责
            
            # 连接 Resize 事件以初始化视图
            self.canvas.events.resize.connect(self._onResize)
            
    def _onResize(self, event):
        """处理Canvas大小改变"""
        if self.coordinate_system:
            self.coordinate_system.initialize_view()
            
    # ==================== 图元CRUD接口 ====================
    
    def addPrimitive(self, data: PrimitiveData, layer_id: str = None) -> str:
        """添加图元
        
        Args:
            data: 图元数据
            layer_id: 图层ID，如果为None则添加到默认图层
            
        Returns:
            图元ID
        """
        # 创建visual
        visual = self._createVisual(data)
        if visual is None:
            raise ValueError(f"无法创建visual: {data.type_name}")
            
        # 创建Primitive对象
        primitive = Primitive(
            id=data.id,
            data=data,
            visual=visual,
            type_name=data.type_name
        )
        
        # 添加到图层
        self.layer_manager.addPrimitive(primitive, layer_id)
        
        # 如果需要创建控制端点
        if data.with_handles:
            self._createHandles(data, layer_id)
        
        # 更新Canvas
        if self.canvas:
            self.canvas.update()
            
        return data.id

    def _createHandles(self, data: PrimitiveData, layer_id: str = None):
        """为图元创建控制端点"""
        points = []
        if isinstance(data, LineData):
            points = data.points
        elif isinstance(data, RectangleData):
            x, y = data.pos
            w, h = data.size
            points = [(x, y), (x+w, y), (x+w, y+h), (x, y+h)]
        elif isinstance(data, CircleData):
            cx, cy = data.center
            # 圆心和右侧边缘点
            points = [(cx, cy), (cx + data.radius, cy)]
        elif isinstance(data, BezierData):
            points = data.control_points
        elif isinstance(data, PolygonData):
            points = data.vertices
            
        # 创建端点图元
        # 使用默认样式，但颜色不同以示区分
        handle_style = data.style.copy()
        handle_style.lineColor = (1.0, 0.5, 0.0, 1.0)  # 橙色端点
        handle_style.fillColor = (1.0, 1.0, 1.0, 1.0)
        
        for pt in points:
            # 确保点是(x, y)格式
            x, y = float(pt[0]), float(pt[1])
            
            point_data = PointData(
                x=x, y=y,
                radius=4.0,
                style=handle_style,
                with_handles=False  # 端点本身不再有端点
            )
            self.addPrimitive(point_data, layer_id)

        
    def removePrimitive(self, primitive_id: str) -> bool:
        """移除图元
        
        Args:
            primitive_id: 图元ID
            
        Returns:
            是否成功移除
        """
        # 清除选中状态（防止高亮残留）
        if hasattr(self, 'selection_manager'):
            self.selection_manager.deselectPrimitive(primitive_id)

        primitive = self.layer_manager.removePrimitive(primitive_id)
        if primitive is None:
            return False
            
        # 销毁visual
        if primitive.visual:
            primitive.visual.destroy()
            
        # 更新Canvas
        if self.canvas:
            self.canvas.update()
            
        return True
        
    def updatePrimitive(self, primitive_id: str, **kwargs) -> bool:
        """更新图元数据
        
        Args:
            primitive_id: 图元ID
            **kwargs: 更新参数
            
        Returns:
            是否成功更新
        """
        primitive = self.layer_manager.getPrimitive(primitive_id)
        if primitive is None:
            return False
            
        # 更新data
        for key, value in kwargs.items():
            if hasattr(primitive.data, key):
                setattr(primitive.data, key, value)
                
        # 更新visual
        if primitive.visual:
            primitive.visual.update_data(**kwargs)
            
        # 更新Canvas
        if self.canvas:
            self.canvas.update()
            
        return True
        
    def getPrimitive(self, primitive_id: str) -> Optional[Primitive]:
        """获取图元
        
        Args:
            primitive_id: 图元ID
            
        Returns:
            Primitive对象，如果不存在返回None
        """
        return self.layer_manager.getPrimitive(primitive_id)
        
    def getAllPrimitives(self) -> List[Primitive]:
        """获取所有图元
        
        Returns:
            Primitive列表
        """
        return self.layer_manager.getAllPrimitives()
        
    def clearAll(self) -> None:
        """清空所有图元"""
        # 销毁所有visual
        for primitive in self.layer_manager.getAllPrimitives():
            if primitive.visual:
                primitive.visual.destroy()
                
        # 清空图层管理器
        self.layer_manager.clear()
        
        # 清空选择
        self.selection_manager.clearSelection()
        
        # 更新Canvas
        if self.canvas:
            self.canvas.update()
            
    # ==================== Visual创建 ====================
    
    def _createVisual(self, data: PrimitiveData):
        """根据数据创建Visual对象
        
        Args:
            data: 图元数据
            
        Returns:
            Visual对象
        """
        if not VISPY_AVAILABLE or not self.view:
            return None
            
        style = data.style
        visual_id = self._generate_visual_id()
        
        try:
            if isinstance(data, PointData):
                return MarkersEntry(
                    self.view, visual_id,
                    pos=np.array([[data.x, data.y]], dtype=np.float32),
                    colors=style.fillColor,  # 使用填充颜色作为点的主颜色
                    sizes=[data.radius * 2],  # MarkersEntry使用直径
                    symbol='disc',
                    edge_color=style.borderColor if style.showBorder else None,
                    edge_width=style.borderWidth if style.showBorder else 0.0
                )
                
            elif isinstance(data, LineData):
                return LineEntry(
                    self.view, visual_id,
                    pos=data.points,
                    color=style.lineColor,
                    width=style.lineWidth
                )
                
            elif isinstance(data, BezierData):
                return BezierCurveEntry(
                    self.view, visual_id,
                    control_points=data.control_points,
                    degree=data.degree,
                    color=style.lineColor,
                    width=style.lineWidth
                )
                
            elif isinstance(data, ArcData):
                return ArcEntry(
                    self.view, visual_id,
                    center=data.center,
                    radius=data.radius,
                    start_angle=data.start_angle,
                    end_angle=data.end_angle,
                    color=style.lineColor,
                    width=style.lineWidth
                )
                
            elif isinstance(data, CircleData):
                return StyledEllipseEntry(
                    self.view, visual_id,
                    center=data.center,
                    radius=data.radius,
                    fill_color=style.fillColor,
                    border_color=style.borderColor,
                    border_width=style.borderWidth,
                    filled=style.filled,
                    show_border=style.showBorder
                )
                
            elif isinstance(data, RectangleData):
                return StyledRectangleEntry(
                    self.view, visual_id,
                    pos=data.pos,
                    size=data.size,
                    fill_color=style.fillColor,
                    border_color=style.borderColor,
                    border_width=style.borderWidth,
                    filled=style.filled,
                    show_border=style.showBorder
                )
                
            elif isinstance(data, PolygonData):
                return StyledPolygonEntry(
                    self.view, visual_id,
                    vertices=data.vertices,
                    fill_color=style.fillColor,
                    border_color=style.borderColor,
                    border_width=style.borderWidth,
                    filled=style.filled,
                    show_border=style.showBorder
                )
                
            elif isinstance(data, MarkersData):
                return MarkersEntry(
                    self.view, visual_id,
                    pos=data.positions,
                    colors=style.fillColor,
                    sizes=data.sizes,
                    symbol=data.symbol,
                    edge_color=style.borderColor if style.showBorder else None,
                    edge_width=style.borderWidth if style.showBorder else 0.0
                )
                
            elif isinstance(data, ImageData):
                if data.data is not None:
                    return ImageEntry(
                        self.view, visual_id,
                        data=data.data,
                        pos=data.pos,
                        interpolation=data.interpolation
                    )
                    
        except Exception as e:
            print(f"创建Visual失败: {e}")
            
        return None
        
    # ==================== 鼠标事件处理 ====================
    
    def _onMousePress(self, event):
        """鼠标按下事件"""
        if not self.canvas:
            return
            
        # 检查event.pos是否有效
        if event.pos is None:
            return
            
        # 获取按钮类型
        button_map = {1: 'left', 2: 'right', 3: 'middle'}
        button = button_map.get(event.button, 'left')
        
        # 获取修饰键
        modifiers = set()
        event_modifiers = getattr(event, 'modifiers', None)
        if event_modifiers:
            if hasattr(event_modifiers, '__iter__'):
                for mod in event_modifiers:
                    if hasattr(mod, 'name'):
                        modifiers.add(mod.name.lower())
                        
        # 处理事件
        result = self.interaction_manager.handleMousePress(
            event.pos[0], event.pos[1],
            button=button,
            modifiers=modifiers
        )
        
        # 更新预览
        self._updatePreview()
        
        # 更新Canvas
        if result.get('handled'):
            event.handled = True
            if self.canvas:
                self.canvas.update()
                
    def _onCanvasMouseMove(self, event):
        """处理Canvas级别的鼠标移动，仅用于坐标更新"""
        if event.pos is None:
            return
            
        # 发送坐标更新信号
        if self.coordinate_system:
            world_pos = self.coordinate_system.screenToWorld(event.pos[0], event.pos[1])
            self.mouseMoved.emit(event.pos, world_pos)

    def _onMouseMove(self, event):
        """鼠标移动事件"""
        if not self.canvas:
            return
            
        # 检查event.pos是否有效
        if event.pos is None:
            return
            
        # 处理事件
        result = self.interaction_manager.handleMouseMove(
            event.pos[0], event.pos[1]
        )
        
        # 更新预览
        self._updatePreview()
        
        # 更新Canvas（如果有变化）
        if result.get('handled') or result.get('moving') or result.get('dragging'):
            event.handled = True
            if self.canvas:
                self.canvas.update()
                
    def _onMouseRelease(self, event):
        """鼠标释放事件"""
        if not self.canvas:
            return
            
        # 检查event.pos是否有效
        if event.pos is None:
            return
            
        button_map = {1: 'left', 2: 'right', 3: 'middle'}
        button = button_map.get(event.button, 'left')
        
        # 处理事件
        result = self.interaction_manager.handleMouseRelease(
            event.pos[0], event.pos[1],
            button=button
        )
        
        # 更新预览
        self._updatePreview()
        
        # 更新Canvas
        if result.get('handled') or result.get('moved') or result.get('created'):
            event.handled = True
            if self.canvas:
                self.canvas.update()
                
    def _onMouseWheel(self, event):
        """鼠标滚轮事件"""
        if not self.canvas or not self.view:
            return
            
        # 检查event.pos是否有效
        if event.pos is None:
            return
            
        # 如果相机交互被禁用（非默认模式），手动处理缩放
        if not self.view.camera.interactive:
            # 获取缩放因子
            # delta通常是(0, 1)或(0, -1)
            delta = event.delta[1]
            scale_factor = 1.1
            
            if delta > 0:
                # 滚轮向上，放大 (Zoom In)，缩小可视区域
                scale = 1.0 / scale_factor
            else:
                # 滚轮向下，缩小 (Zoom Out)，扩大可视区域
                scale = scale_factor
                
            # 获取鼠标位置作为中心点
            # 注意：camera.zoom 需要世界坐标作为中心点，而 event.pos 是屏幕坐标
            center = event.pos
            if self.coordinate_system:
                center = self.coordinate_system.screenToWorld(event.pos[0], event.pos[1])
            
            # 应用缩放
            self.view.camera.zoom(scale, center)
            event.handled = True
            if self.canvas:
                self.canvas.update()
                
    def _onMouseDoubleClick(self, event):
        """鼠标双击事件"""
        if not self.canvas:
            return
            
        # 处理事件
        result = self.interaction_manager.handleDoubleClick(
            event.pos[0], event.pos[1]
        )
        
        # 清除预览
        self._clearPreview()
        
        # 更新Canvas
        if result.get('handled'):
            if self.canvas:
                self.canvas.update()
                
    # ==================== 预览管理 ====================
    
    def _updatePreview(self) -> None:
        """更新预览图元"""
        if not VISPY_AVAILABLE:
            return
            
        # 获取预览数据
        preview_data = self.interaction_manager.getCurrentPreview()
        if preview_data is None:
            self._clearPreview()
            return
            
        try:
            preview_type = preview_data.get('type')
            from vispy.scene import visuals
            
            # 检查是否需要重建visual
            if self._preview_type != preview_type:
                self._clearPreview()
                self._preview_type = preview_type
                
                # 创建新的visual
                if preview_type == 'line':
                    self._preview_visual = visuals.Line(
                        pos=np.zeros((0, 2), dtype=np.float32),
                        color=(0.5, 0.5, 0.5, 0.6),
                        width=1.0,
                        parent=self.view.scene
                    )
                elif preview_type == 'rectangle':
                    # 使用Line绘制矩形边框作为预览
                    self._preview_visual = visuals.Line(
                        pos=np.zeros((0, 2), dtype=np.float32),
                        color=(0.5, 0.5, 0.5, 0.6),
                        width=1.0,
                        parent=self.view.scene
                    )
                elif preview_type == 'circle':
                    self._preview_visual = visuals.Ellipse(
                        center=(0, 0), radius=1,
                        color=(0.5, 0.5, 0.5, 0.3),
                        border_color=(0.5, 0.5, 0.5, 0.6),
                        parent=self.view.scene
                    )
                elif preview_type == 'ellipse':
                    self._preview_visual = visuals.Ellipse(
                        center=(0, 0), radius=(1, 1),
                        color=(0.5, 0.5, 0.5, 0.3),
                        border_color=(0.5, 0.5, 0.5, 0.6),
                        parent=self.view.scene
                    )
                elif preview_type == 'box_select':
                    self._preview_visual = visuals.Line(
                        pos=np.zeros((0, 2), dtype=np.float32),
                        color=(0.3, 0.7, 1.0, 0.8),
                        width=1.0,
                        parent=self.view.scene
                    )
                elif preview_type == 'bezier':
                    # 主visual显示曲线
                    self._preview_visual = visuals.Line(
                        pos=np.zeros((0, 2), dtype=np.float32),
                        color=(0.5, 0.5, 0.5, 0.8),
                        width=1.0,
                        parent=self.view.scene
                    )
                    # 辅助visual显示控制多边形
                    self._preview_aux_visual = visuals.Line(
                        pos=np.zeros((0, 2), dtype=np.float32),
                        color=(0.5, 0.5, 0.5, 0.4),
                        width=1.0,
                        parent=self.view.scene
                    )
                elif preview_type == 'polygon':
                    self._preview_visual = visuals.Line(
                        pos=np.zeros((0, 2), dtype=np.float32),
                        color=(0.5, 0.5, 0.5, 0.6),
                        width=1.0,
                        connect='strip',
                        parent=self.view.scene
                    )

            # 更新数据
            if preview_type == 'line':
                points = np.array(preview_data['points'], dtype=np.float32)
                self._preview_visual.set_data(pos=points)
                
            elif preview_type == 'rectangle':
                x, y = preview_data['x1'], preview_data['y1']
                w, h = preview_data['width'], preview_data['height']
                vertices = np.array([
                    [x, y], [x + w, y], [x + w, y + h], [x, y + h], [x, y]
                ], dtype=np.float32)
                self._preview_visual.set_data(pos=vertices)
                
            elif preview_type == 'circle':
                center = preview_data['center']
                radius = preview_data['radius']
                self._preview_visual.center = center
                self._preview_visual.radius = radius[0] # Vispy Ellipse radius can be float or tuple, but CircleData uses tuple now for consistency

            elif preview_type == 'ellipse':
                center = preview_data['center']
                radius = preview_data['radius']
                self._preview_visual.center = center
                self._preview_visual.radius = radius
                
            elif preview_type == 'box_select':
                x1, y1 = preview_data['x1'], preview_data['y1']
                x2, y2 = preview_data['x2'], preview_data['y2']
                vertices = np.array([
                    [x1, y1], [x2, y1], [x2, y2], [x1, y2], [x1, y1]
                ], dtype=np.float32)
                self._preview_visual.set_data(pos=vertices)
                
            elif preview_type == 'bezier':
                points = np.array(preview_data['points'], dtype=np.float32)
                
                # 更新控制多边形
                if self._preview_aux_visual:
                    self._preview_aux_visual.set_data(pos=points)
                
                # 计算并更新曲线
                n = len(points) - 1
                if n < 1:
                    curve_points = points
                else:
                    num_samples = 50
                    t_values = np.linspace(0, 1, num_samples)
                    curve_points = np.zeros((num_samples, 2))
                    combinations = [math.comb(n, i) for i in range(n + 1)]
                    for i in range(n + 1):
                        basis = combinations[i] * ((1 - t_values) ** (n - i)) * (t_values ** i)
                        curve_points += np.outer(basis, points[i])
                    curve_points = curve_points.astype(np.float32)
                
                self._preview_visual.set_data(pos=curve_points)

            elif preview_type == 'polygon':
                points = np.array(preview_data['points'], dtype=np.float32)
                self._preview_visual.set_data(pos=points)
            
            # 确保创建后立即更新Canvas
            if self.canvas:
                self.canvas.update()
                
        except Exception as e:
            print(f"更新预览失败: {e}")
            import traceback
            traceback.print_exc()
            
    def _clearPreview(self) -> None:
        """清除预览图元"""
        try:
            # 清除主预览
            if self._preview_visual:
                if hasattr(self._preview_visual, 'parent'):
                    self._preview_visual.parent = None
                self._preview_visual = None
                
            # 清除辅助预览
            if self._preview_aux_visual:
                if hasattr(self._preview_aux_visual, 'parent'):
                    self._preview_aux_visual.parent = None
                self._preview_aux_visual = None
            
            self._preview_type = None
            
            # 立即更新scene以确保移除生效
            if hasattr(self, 'canvas') and self.canvas:
                self.canvas.update()
                
        except Exception as e:
            print(f"清除预览图元失败: {e}")
            self._preview_visual = None
            self._preview_aux_visual = None
            self._preview_type = None
            
    # ==================== 信号处理 ====================
    
    def _onPrimitiveCreated(self, data: PrimitiveData):
        """处理图元创建信号"""
        try:
            self.addPrimitive(data)
        except Exception as e:
            print(f"添加图元失败: {e}")
            
    def _onPrimitiveMoved(self, primitive_ids: List[str], dx: float, dy: float):
        """处理图元移动信号"""
        for primitive_id in primitive_ids:
            primitive = self.layer_manager.getPrimitive(primitive_id)
            if primitive is None or primitive.data.locked:
                continue
                
            # 更新数据
            data = primitive.data
            if isinstance(data, (LineData, BezierData, PolygonData, MarkersData)):
                # 有顶点/位置的图元
                if hasattr(data, 'points'):
                    data.points = data.points + np.array([dx, dy])
                elif hasattr(data, 'control_points'):
                    data.control_points = data.control_points + np.array([dx, dy])
                elif hasattr(data, 'vertices'):
                    data.vertices = data.vertices + np.array([dx, dy])
                elif hasattr(data, 'positions'):
                    data.positions = data.positions + np.array([dx, dy])
                    
            elif isinstance(data, (CircleData, ArcData)):
                # 有中心点的图元
                cx, cy = data.center
                data.center = (cx + dx, cy + dy)
                
            elif isinstance(data, RectangleData):
                # 矩形
                x, y = data.pos
                data.pos = (x + dx, y + dy)
                
            elif isinstance(data, ImageData):
                # 图像
                x, y = data.pos
                data.pos = (x + dx, y + dy)
                
            elif isinstance(data, PointData):
                # 点
                data.x += dx
                data.y += dy
                
            # 更新visual
            if primitive.visual:
                try:
                    if isinstance(data, (LineData, BezierData, PolygonData, MarkersData)):
                        if hasattr(data, 'points'):
                            primitive.visual.update_data(pos=data.points)
                        elif hasattr(data, 'control_points'):
                            primitive.visual.update_data(control_points=data.control_points)
                        elif hasattr(data, 'vertices'):
                            primitive.visual.update_data(vertices=data.vertices)
                        elif hasattr(data, 'positions'):
                            primitive.visual.update_data(pos=data.positions)
                    elif isinstance(data, (CircleData, ArcData)):
                        primitive.visual.update_data(center=data.center)
                    elif isinstance(data, RectangleData):
                        primitive.visual.update_data(pos=data.pos)
                    elif isinstance(data, ImageData):
                        primitive.visual.update_data(pos=data.pos)
                except Exception as e:
                    print(f"更新visual失败: {e}")
                    
        # 更新高亮
        self.selection_manager.updateHighlights()
        
        # 更新Canvas
        if self.canvas:
            self.canvas.update()
            
    # ==================== 交互模式 ====================
    
    def setInteractionMode(self, mode: Union[InteractionMode, str]) -> None:
        """设置交互模式
        
        Args:
            mode: 交互模式
        """
        # 切换模式前强制清除预览
        self._clearPreview()

        # 0. 统一转换为枚举，增强健壮性
        target_mode = mode
        if isinstance(mode, str):
            try:
                # 尝试通过名字查找枚举 (支持 'DEFAULT', 'default' 等)
                mode_upper = mode.upper()
                if hasattr(InteractionMode, mode_upper):
                    target_mode = InteractionMode[mode_upper]
                else:
                    # 备用映射
                    mode_map = {
                        'default': InteractionMode.DEFAULT,
                        'move': InteractionMode.MOVE,
                        'draw_line': InteractionMode.DRAW_LINE,
                        'draw_rectangle': InteractionMode.DRAW_RECTANGLE,
                        'draw_circle': InteractionMode.DRAW_CIRCLE,
                        'draw_ellipse': InteractionMode.DRAW_ELLIPSE,
                        'draw_bezier': InteractionMode.DRAW_BEZIER,
                        'draw_polygon': InteractionMode.DRAW_POLYGON,
                        'draw_point': InteractionMode.DRAW_POINT,
                        'edit_bezier': InteractionMode.EDIT_BEZIER,
                    }
                    target_mode = mode_map.get(mode.lower(), InteractionMode.DEFAULT)
            except Exception:
                target_mode = InteractionMode.DEFAULT

        # 1. 确保取消当前正在进行的操作（如绘制过程中的状态）
        if self.interaction_manager:
            self.interaction_manager.cancelCurrentOperation()
        
        # 2. 清除预览图元
        self._clearPreview()
        
        # 3. 设置新模式
        if self.interaction_manager:
            self.interaction_manager.setMode(target_mode)
        
        # 4. 根据模式启用/禁用相机交互
        # 当非默认模式时，禁用相机交互，防止移动画布
        if self.view and self.view.camera:
            # 只有在默认模式下才允许相机交互（平移/缩放）
            self.view.camera.interactive = (target_mode == InteractionMode.DEFAULT)
            
        # 5. 强制更新Canvas和Native Widget
        # 解决ESC切换模式后可能导致的画布内容不可见问题
        if self.canvas:
            self.canvas.update()
            
        if self.native_widget:
            # 仅在不可见时显示，避免不必要的窗口重置
            if not self.native_widget.isVisible():
                self.native_widget.show()
            
            self.native_widget.update()
            self.native_widget.setMouseTracking(True) # 确保鼠标追踪开启
            self.native_widget.setFocus() # 确保获取焦点，否则滚轮缩放等可能失效
            
            # 如果切换到绘制模式，自动获取焦点以便接收键盘事件（如ESC）
            # 在默认模式下不强制抢占，以免影响工具栏操作
            if target_mode != InteractionMode.DEFAULT:
                self.native_widget.setFocus()
        
    def getInteractionMode(self) -> InteractionMode:
        """获取当前交互模式
        
        Returns:
            交互模式
        """
        return self.interaction_manager.getMode()
        
    def setDefaultStyle(self, style: StyleData) -> None:
        """设置默认样式
        
        Args:
            style: 样式数据
        """
        self.interaction_manager.setDefaultStyle(style)
        
    def getDefaultStyle(self) -> StyleData:
        """获取默认样式
        
        Returns:
            样式数据
        """
        return self.interaction_manager.getDefaultStyle()
