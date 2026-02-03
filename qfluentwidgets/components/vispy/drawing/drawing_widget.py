# coding:utf-8
"""
交互式绘图Widget模块

提供InteractiveDrawingWidget控件，封装InteractiveDrawingCanvas，
提供高层API接口和信号，便于用户使用。
"""
from typing import Union, Tuple, Optional, List
import numpy as np
from PySide6.QtCore import Qt, Signal, QEvent
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFileDialog
from PySide6.QtGui import QKeyEvent
from qfluentwidgets.common import DrawIcon

try:
    from vispy import app as vispy_app
    VISPY_AVAILABLE = True
except ImportError:
    VISPY_AVAILABLE = False

from .drawing_canvas import InteractiveDrawingCanvas
from .interaction_manager import InteractionMode
from .data_models import (
    PrimitiveData, LineData, BezierData, ArcData, CircleData,
    RectangleData, PolygonData, MarkersData, ImageData, StyleData
)
from qfluentwidgets.common import isDarkTheme


class InteractiveDrawingWidget(QWidget):
    """交互式绘图Widget
    
    提供完整的2D交互式绘图功能，支持：
    - 多种图元绘制
    - 图层管理
    - 选择和移动
    - 样式控制
    - 与ToolPanel集成
    """
    
    # 信号
    primitiveAdded = Signal(str)                    # 图元添加 (primitive_id)
    primitiveRemoved = Signal(str)                  # 图元移除 (primitive_id)
    selectionChanged = Signal(list)                 # 选择改变 (selected_ids)
    interactionModeChanged = Signal(InteractionMode)  # 交互模式改变
    primitiveMoved = Signal(list, float, float)     # 图元移动 (ids, dx, dy)
    
    def __init__(self, parent=None, scale_factor=1.0, origin_offset=(0.0, 0.0), grid_size=100.0, grid_spacing=10.0):
        """初始化交互式绘图Widget
        
        Args:
            parent: 父控件
            scale_factor: 像素与物理尺寸比例
            origin_offset: 原点世界坐标值
            grid_size: 网格大小
            grid_spacing: 网格间距
        """
        super().__init__(parent)
        
        if not VISPY_AVAILABLE:
            self._init_fallback_ui()
            return
            
        # 创建布局
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        
        # 创建Canvas
        self.canvas = InteractiveDrawingCanvas(
            scale_factor=scale_factor, 
            origin_offset=origin_offset,
            grid_size=grid_size,
            grid_spacing=grid_spacing
        )
        
        if self.canvas.native_widget:
            self.vBoxLayout.addWidget(self.canvas.native_widget)
            # 安装事件过滤器以捕获按键事件（因为点击画布时native_widget会获得焦点）
            self.canvas.native_widget.installEventFilter(self)
            
        # 坐标显示标签
        self.coordLabel = QLabel(self)
        self.coordLabel.setStyleSheet(
            "QLabel { background-color: rgba(0, 0, 0, 150); color: white; "
            "padding: 4px; border-radius: 4px; font-family: Consolas, monospace; }"
        )
        self.coordLabel.hide()
        
        # 连接信号
        self.canvas.selection_manager.selectionChanged.connect(self._onSelectionChanged)
        self.canvas.interaction_manager.primitiveCreated.connect(self._onPrimitiveCreated)
        self.canvas.interaction_manager.primitiveMoved.connect(self._onPrimitiveMoved)
        self.canvas.mouseMoved.connect(self._onMouseMoved)
        
        # 初始化主题
        self.set_theme(isDarkTheme())
        
        # 启用键盘事件
        self.setFocusPolicy(Qt.StrongFocus)
        
    def eventFilter(self, obj, event):
        """事件过滤器"""
        if self.canvas and obj is self.canvas.native_widget:
            if event.type() == QEvent.KeyPress:
                # 处理删除键
                if event.key() == Qt.Key_Delete:
                    if self.canvas.interaction_manager.getMode() == InteractionMode.MOVE:
                        selected_ids = self.canvas.selection_manager.getSelectedPrimitives()
                        if selected_ids:
                            for pid in selected_ids:
                                self.canvas.removePrimitive(pid)
                            self.canvas.selection_manager.clearSelection()
                            return True
        
        return super().eventFilter(obj, event)

    def _init_fallback_ui(self):
        """Vispy 不可用时的降级 UI"""
        self.vBoxLayout = QVBoxLayout(self)
        label = QLabel("Vispy 未安装，无法使用交互式绘图\n请使用: pip install vispy", self)
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
            
    def _onMouseMoved(self, screen_pos, world_pos):
        """鼠标移动处理"""
        if not hasattr(self, 'coordLabel'):
            return
            
        # 格式化显示: 【(base_x, base_y):(world_x, world_y)】
        try:
            bx, by = int(screen_pos[0]), int(screen_pos[1])
            wx, wy = world_pos[0], world_pos[1]
            text = f"【({bx},{by}):({wx:.2f},{wy:.2f})】"
            self.coordLabel.setText(text)
            self.coordLabel.adjustSize()
            self._updateLabelPosition()
            if self.coordLabel.isHidden():
                self.coordLabel.show()
        except Exception as e:
            pass
            
    def resizeEvent(self, event):
        """重设大小时更新标签位置"""
        super().resizeEvent(event)
        self._updateLabelPosition()
        
    def _updateLabelPosition(self):
        """更新标签位置到右下角"""
        if hasattr(self, 'coordLabel') and self.coordLabel.isVisible():
            m = 10  # 边距
            x = self.width() - self.coordLabel.width() - m
            y = self.height() - self.coordLabel.height() - m
            self.coordLabel.move(x, y)
            
    # ==================== 图元绘制接口 ====================
    
    def addLine(self, points: np.ndarray, style: StyleData = None) -> str:
        """添加直线/折线
        
        Args:
            points: 点坐标数组，形状 (N, 2)
            style: 样式数据，如果为None则使用默认样式
            
        Returns:
            图元ID
        """
        if not self.canvas:
            return ""
            
        data = LineData(
            points=points,
            style=style if style else self.canvas.getDefaultStyle()
        )
        primitive_id = self.canvas.addPrimitive(data)
        self.primitiveAdded.emit(primitive_id)
        return primitive_id
        
    def addBezierCurve(self, control_points: np.ndarray, degree: int = 2, 
                       style: StyleData = None) -> str:
        """添加贝塞尔曲线
        
        Args:
            control_points: 控制点，形状 (3, 2) 或 (4, 2)
            degree: 阶数，2=二阶，3=三阶
            style: 样式数据
            
        Returns:
            图元ID
        """
        if not self.canvas:
            return ""
            
        data = BezierData(
            control_points=control_points,
            degree=degree,
            style=style if style else self.canvas.getDefaultStyle()
        )
        primitive_id = self.canvas.addPrimitive(data)
        self.primitiveAdded.emit(primitive_id)
        return primitive_id
        
    def addArc(self, center: Tuple[float, float], radius: float,
               start_angle: float, end_angle: float, style: StyleData = None) -> str:
        """添加圆弧
        
        Args:
            center: 中心点 (x, y)
            radius: 半径
            start_angle: 起始角度（度数）
            end_angle: 结束角度（度数）
            style: 样式数据
            
        Returns:
            图元ID
        """
        if not self.canvas:
            return ""
            
        data = ArcData(
            center=center,
            radius=radius,
            start_angle=start_angle,
            end_angle=end_angle,
            style=style if style else self.canvas.getDefaultStyle()
        )
        primitive_id = self.canvas.addPrimitive(data)
        self.primitiveAdded.emit(primitive_id)
        return primitive_id
        
    def addCircle(self, center: Tuple[float, float], radius: Union[float, Tuple[float, float]],
                  style: StyleData = None) -> str:
        """添加圆形/椭圆
        
        Args:
            center: 中心点 (x, y)
            radius: 半径（圆）或 (rx, ry)（椭圆）
            style: 样式数据
            
        Returns:
            图元ID
        """
        if not self.canvas:
            return ""
            
        data = CircleData(
            center=center,
            radius=radius if isinstance(radius, tuple) else (radius, radius),
            style=style if style else self.canvas.getDefaultStyle()
        )
        primitive_id = self.canvas.addPrimitive(data)
        self.primitiveAdded.emit(primitive_id)
        return primitive_id
        
    def addRectangle(self, pos: Tuple[float, float], size: Tuple[float, float],
                     style: StyleData = None) -> str:
        """添加矩形
        
        Args:
            pos: 左上角位置 (x, y)
            size: 尺寸 (width, height)
            style: 样式数据
            
        Returns:
            图元ID
        """
        if not self.canvas:
            return ""
            
        data = RectangleData(
            pos=pos,
            size=size,
            style=style if style else self.canvas.getDefaultStyle()
        )
        primitive_id = self.canvas.addPrimitive(data)
        self.primitiveAdded.emit(primitive_id)
        return primitive_id
        
    def addPolygon(self, vertices: np.ndarray, style: StyleData = None) -> str:
        """添加多边形
        
        Args:
            vertices: 顶点坐标数组，形状 (N, 2)
            style: 样式数据
            
        Returns:
            图元ID
        """
        if not self.canvas:
            return ""
            
        data = PolygonData(
            vertices=vertices,
            style=style if style else self.canvas.getDefaultStyle()
        )
        primitive_id = self.canvas.addPrimitive(data)
        self.primitiveAdded.emit(primitive_id)
        return primitive_id
        
    def addMarkers(self, positions: np.ndarray, sizes: np.ndarray = None, 
                   symbol: str = 'o', style: StyleData = None) -> str:
        """添加标记点
        
        Args:
            positions: 点位置数组，形状 (N, 2)
            sizes: 点大小数组，形状 (N,)
            symbol: 符号类型
            style: 样式数据
            
        Returns:
            图元ID
        """
        if not self.canvas:
            return ""
            
        if sizes is None:
            sizes = np.array([5.0] * len(positions))
            
        data = MarkersData(
            positions=positions,
            sizes=sizes,
            symbol=symbol,
            style=style if style else self.canvas.getDefaultStyle()
        )
        primitive_id = self.canvas.addPrimitive(data)
        self.primitiveAdded.emit(primitive_id)
        return primitive_id
        
    def addImage(self, data: np.ndarray, pos: Tuple[float, float] = (0, 0),
                 interpolation: str = 'nearest', image_path: str = None,
                 style: StyleData = None) -> str:
        """添加图像
        
        Args:
            data: 图像数据，形状 (H, W) 或 (H, W, 3/4)
            pos: 左下角位置 (x, y)
            interpolation: 插值方式
            image_path: 图像文件路径（可选，用于记录来源）
            style: 样式数据
            
        Returns:
            图元ID
        """
        if not self.canvas:
            return ""
            
        image_data = ImageData(
            data=data,
            pos=pos,
            interpolation=interpolation,
            image_path=image_path,
            style=style if style else self.canvas.getDefaultStyle()
        )
        primitive_id = self.canvas.addPrimitive(image_data)
        self.primitiveAdded.emit(primitive_id)
        return primitive_id
        
    def addImageFromFile(self, file_path: str = None, pos: Tuple[float, float] = None) -> str:
        """从文件添加图像
        
        Args:
            file_path: 图像文件路径，如果为None则打开文件对话框
            pos: 位置，如果为None则放置在中心
            
        Returns:
            图元ID
        """
        if not self.canvas:
            return ""
            
        # 如果没有提供路径，打开文件对话框
        if file_path is None:
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "选择图像文件",
                "",
                "图像文件 (*.png *.jpg *.jpeg *.bmp *.gif);;所有文件 (*.*)"
            )
            if not file_path:
                return ""
                
        # 加载图像
        try:
            from PIL import Image
            img = Image.open(file_path)
            img_array = np.array(img)
            
            # 计算位置（如果未指定则放置在中心）
            if pos is None:
                bounds = self.canvas.coordinate_system.getViewBounds()
                if bounds:
                    center_x = (bounds[0] + bounds[2]) / 2
                    center_y = (bounds[1] + bounds[3]) / 2
                    h, w = img_array.shape[:2]
                    pos = (center_x - w/2, center_y - h/2)
                else:
                    pos = (0, 0)
                    
            return self.addImage(img_array, pos=pos, image_path=file_path)
            
        except Exception as e:
            print(f"加载图像失败: {e}")
            return ""
            
    # ==================== 图元管理接口 ====================
    
    def removePrimitive(self, primitive_id: str) -> bool:
        """移除图元
        
        Args:
            primitive_id: 图元ID
            
        Returns:
            是否成功移除
        """
        if not self.canvas:
            return False
            
        result = self.canvas.removePrimitive(primitive_id)
        if result:
            self.primitiveRemoved.emit(primitive_id)
        return result
        
    def updatePrimitive(self, primitive_id: str, **kwargs) -> bool:
        """更新图元
        
        Args:
            primitive_id: 图元ID
            **kwargs: 更新参数
            
        Returns:
            是否成功更新
        """
        if not self.canvas:
            return False
            
        return self.canvas.updatePrimitive(primitive_id, **kwargs)
        
    def getPrimitiveData(self, primitive_id: str) -> Optional[PrimitiveData]:
        """获取图元数据
        
        Args:
            primitive_id: 图元ID
            
        Returns:
            图元数据，如果不存在返回None
        """
        if not self.canvas:
            return None
            
        primitive = self.canvas.getPrimitive(primitive_id)
        return primitive.data if primitive else None
        
    def clearAll(self) -> None:
        """清空所有图元"""
        if self.canvas:
            self.canvas.clearAll()
            
    # ==================== 交互模式 ====================
    
    def setInteractionMode(self, mode: InteractionMode) -> None:
        """设置交互模式
        
        Args:
            mode: 交互模式
        """
        if self.canvas:
            self.canvas.setInteractionMode(mode)
            # 切换模式时强制清除预览，防止跨工具的视觉残留
            if hasattr(self.canvas, '_clearPreview'):
                self.canvas._clearPreview()
            self.interactionModeChanged.emit(mode)
            
    def getInteractionMode(self) -> InteractionMode:
        """获取当前交互模式
        
        Returns:
            交互模式
        """
        if self.canvas:
            return self.canvas.getInteractionMode()
        return InteractionMode.DEFAULT

    def setCreateHandles(self, enabled: bool) -> None:
        """设置是否创建控制端点
        
        Args:
            enabled: 是否创建
        """
        if self.canvas and hasattr(self.canvas, 'interaction_manager'):
            self.canvas.interaction_manager.setCreateHandles(enabled)
            
    def getCreateHandles(self) -> bool:
        """获取是否创建控制端点
        
        Returns:
            是否创建
        """
        if self.canvas and hasattr(self.canvas, 'interaction_manager'):
            return self.canvas.interaction_manager.getCreateHandles()
        return False
        
    # ==================== 选择管理 ====================
    
    def getSelectedPrimitives(self) -> List[str]:
        """获取当前选中的图元ID列表
        
        Returns:
            图元ID列表
        """
        if not self.canvas:
            return []
            
        return self.canvas.selection_manager.getSelectedPrimitives()
        
    def selectPrimitive(self, primitive_id: str, append: bool = False) -> bool:
        """选中图元
        
        Args:
            primitive_id: 图元ID
            append: 是否追加到当前选择
            
        Returns:
            是否成功选中
        """
        if not self.canvas:
            return False
            
        return self.canvas.selection_manager.selectPrimitive(primitive_id, append)
        
    def clearSelection(self) -> None:
        """清除所有选择"""
        if self.canvas:
            self.canvas.selection_manager.clearSelection()
            
    # ==================== 样式设置 ====================
    
    def setDefaultStyle(self, style: StyleData) -> None:
        """设置默认样式
        
        Args:
            style: 样式数据
        """
        if self.canvas:
            self.canvas.setDefaultStyle(style)
            
    def getDefaultStyle(self) -> StyleData:
        """获取默认样式
        
        Returns:
            样式数据
        """
        if self.canvas:
            return self.canvas.getDefaultStyle()
        return StyleData()
        
    # ==================== 图层管理 ====================
    
    def addLayer(self, name: str = "", zorder: int = None):
        """添加新图层
        
        Args:
            name: 图层名称
            zorder: 图层顺序
            
        Returns:
            Layer对象
        """
        if not self.canvas:
            return None
            
        return self.canvas.layer_manager.addLayer(name, zorder)
        
    def removeLayer(self, layer_id: str):
        """移除图层
        
        Args:
            layer_id: 图层ID
            
        Returns:
            被移除的Layer对象
        """
        if not self.canvas:
            return None
            
        return self.canvas.layer_manager.removeLayer(layer_id)
        
    def getAllLayers(self):
        """获取所有图层
        
        Returns:
            图层列表
        """
        if not self.canvas:
            return []
            
        return self.canvas.layer_manager.getAllLayers()
        
    # ==================== 数据导出 ====================
    
    def exportLayerData(self) -> dict:
        """导出所有图层数据
        
        Returns:
            包含所有数据的字典
        """
        if not self.canvas:
            return {'layers': []}
            
        return self.canvas.layer_manager.exportData()
        
    # ==================== 视图控制 ====================
    
    def autoRange(self) -> None:
        """自动调整视图范围"""
        if self.canvas:
            self.canvas.auto_range()
            
    # ==================== 信号处理 ====================
    
    def _onSelectionChanged(self, selected_ids: List[str]):
        """处理选择改变信号"""
        self.selectionChanged.emit(selected_ids)
        
    def _onPrimitiveCreated(self, data: PrimitiveData):
        """处理图元创建信号"""
        # 信号已经在addPrimitive中发送
        pass
        
    def _onPrimitiveMoved(self, primitive_ids: List[str], dx: float, dy: float):
        """处理图元移动信号"""
        self.primitiveMoved.emit(primitive_ids, dx, dy)
        
    # ==================== 与ToolPanel集成的便捷方法 ====================
    
    def createDrawingToolsData(self) -> List[dict]:
        """创建绘图工具数据，用于ToolPanel
        
        Returns:
            工具数据列表
        """
        tools = [
            {
                'icon': DrawIcon.CURSOR,
                'name': '默认',
                'tooltip': '默认模式（Vispy原生交互）',
                'userData': {'mode': InteractionMode.DEFAULT}
            },
            {
                'icon': DrawIcon.MOVE,
                'name': '移动',
                'tooltip': '移动模式（选择和移动图元）',
                'userData': {'mode': InteractionMode.MOVE}
            },
            {
                'icon': DrawIcon.LINE,
                'name': '多段线',
                'tooltip': '绘制多段线',
                'userData': {'mode': InteractionMode.DRAW_LINE}
            },
            {
                'icon': DrawIcon.RECTANGLE,
                'name': '矩形',
                'tooltip': '绘制矩形',
                'userData': {'mode': InteractionMode.DRAW_RECTANGLE}
            },
            {
                'icon': DrawIcon.CIRCLE,
                'name': '圆形',
                'tooltip': '绘制圆形',
                'userData': {'mode': InteractionMode.DRAW_CIRCLE}
            },
            {
                'icon': DrawIcon.CURVE,
                'name': '贝塞尔曲线',
                'tooltip': '绘制贝塞尔曲线',
                'userData': {'mode': InteractionMode.DRAW_BEZIER}
            },
            {
                'icon': DrawIcon.POLYGON,
                'name': '多边形',
                'tooltip': '绘制多边形',
                'userData': {'mode': InteractionMode.DRAW_POLYGON}
            },
            {
                'icon': DrawIcon.POINT,
                'name': '点',
                'tooltip': '绘制点',
                'userData': {'mode': InteractionMode.DRAW_POINT}
            },
            {
                'icon': DrawIcon.CURSOR,
                'name': '编辑贝塞尔',
                'tooltip': '编辑贝塞尔曲线控制点',
                'userData': {'mode': InteractionMode.EDIT_BEZIER}
            },
        ]
        
        return tools
        
    def onToolPanelChanged(self, tool_button):
        """处理ToolPanel工具改变事件
        
        Args:
            tool_button: ToolPanelButton对象
        """
        # 获取工具的用户数据
        tool_data = tool_button.toolData()
        user_data = tool_data.get('userData', {})
        
        # 获取交互模式
        mode = user_data.get('mode')
        if mode:
            self.setInteractionMode(mode)

    def keyPressEvent(self, event: QKeyEvent):
        """键盘事件处理
        
        Args:
            event: 键盘事件
        """
        key = event.key()
        
        # ESC键：取消当前操作
        if key == Qt.Key_Escape:
            if self.canvas and hasattr(self.canvas, 'interaction_manager'):
                # 取消当前操作
                self.canvas.interaction_manager.cancelCurrentOperation()
                
                # 清除预览
                if hasattr(self.canvas, '_clearPreview'):
                    self.canvas._clearPreview()
                
                # 强制更新画布，确保不会消失
                if self.canvas.canvas:
                    self.canvas.canvas.update()
                    # 确保画布可见
                    self.canvas.canvas.show()
                
                # 确保native_widget可见
                if hasattr(self.canvas, 'native_widget') and self.canvas.native_widget:
                    self.canvas.native_widget.show()
        
        # 调用父类方法
        super().keyPressEvent(event)
