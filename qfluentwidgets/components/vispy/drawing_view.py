# coding: utf-8
from typing import Optional, Tuple
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, 
                               QFrame, QCheckBox, QToolButton)
from PySide6.QtCore import Qt, Signal, QEvent, QSize
from PySide6.QtGui import QColor, QPainter

from ...common.icon import FluentIcon, DrawIcon
from ...common.config import isDarkTheme, Theme
from ...components.widgets.label import CaptionLabel
from ...components.widgets.spin_box import DoubleSpinBox
from ...components.widgets.button import PushButton, ToolButton
from ...components.widgets.check_box import CheckBox
from ...components.dialog_box.color_dialog import ColorDialog
from ...components.widgets.tool_tip import ToolTipFilter

from .drawing import InteractiveDrawingWidget, InteractionMode, StyleData
from ...components.widgets import VerticalToolPanel

class ColorPickerButton(PushButton):
    """颜色选择按钮"""
    colorChanged = Signal(object)
    
    def __init__(self, color: tuple = (255, 255, 255, 255), parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(60, 24)
        self._color = QColor(*[int(c*255) if isinstance(c, float) else c for c in color])
        self.clicked.connect(self._showColorDialog)
        
    def setColor(self, color):
        if isinstance(color, tuple):
            # 转换为 0-255 范围
            self._color = QColor(*[int(c*255) if isinstance(c, float) and c <= 1.0 else int(c) for c in color])
        else:
            self._color = QColor(color)
        self.update()
        
    def getColor(self) -> Tuple[float, float, float, float]:
        return (self._color.redF(), self._color.greenF(), self._color.blueF(), self._color.alphaF())
        
    def _showColorDialog(self):
        dlg = ColorDialog(self._color, "选择颜色", self.window())
        if dlg.exec():
            self._color = dlg.color
            self.colorChanged.emit(self.getColor())
            self.update()
            
    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # 绘制颜色块
        rect = self.rect().adjusted(6, 6, -6, -6)
        painter.setBrush(self._color)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(rect, 4, 4)

class PropertyGroup(QWidget):
    """属性组控件"""
    def __init__(self, title: str, parent=None):
        super().__init__(parent)
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(10, 0, 10, 0)
        self.layout.setSpacing(12)
        
    def addWidget(self, widget):
        self.layout.addWidget(widget)
        
    def addLabel(self, text: str):
        label = CaptionLabel(text, self)
        self.layout.addWidget(label)
        return label
        
    def addSeparator(self):
        line = QFrame(self)
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setFixedHeight(16)
        line.setStyleSheet("QFrame{border: 1px solid rgba(0,0,0,0.1);}")
        self.layout.addWidget(line)

class ConfigPanel(QWidget):
    """顶部配置面板"""
    styleChanged = Signal(StyleData)
    handlesChanged = Signal(bool)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(50)
        self.setStyleSheet("ConfigPanel{background-color: rgba(255, 255, 255, 0.9); border-bottom: 1px solid rgba(0,0,0,0.1);}")
        
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(16, 0, 16, 0)
        
        self.stack = QStackedWidget(self)
        self.layout.addWidget(self.stack)
        
        # 当前样式数据
        self._currentStyle = StyleData()
        
        # 初始化页面
        self._initPages()
        
    def _initPages(self):
        # 1. 光标/移动模式页面
        self.defaultPage = self._createInfoPage("光标模式", DrawIcon.CURSOR)
        self.movePage = self._createInfoPage("移动模式", DrawIcon.MOVE)
        
        # 2. 点页面
        self.pointPage = self._createPointPage()
        
        # 3. 线条页面
        self.linePage = self._createLinePage()
        
        # 4. 形状页面 (矩形/圆/多边形)
        self.shapePage = self._createShapePage()
        
        self.stack.addWidget(self.defaultPage) # 0
        self.stack.addWidget(self.movePage)    # 1
        self.stack.addWidget(self.pointPage)   # 2
        self.stack.addWidget(self.linePage)    # 3
        self.stack.addWidget(self.shapePage)   # 4
        
    def _createInfoPage(self, text, icon):
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setAlignment(Qt.AlignLeft)
        
        btn = ToolButton(icon, widget)
        btn.setFixedSize(32, 32)
        
        label = CaptionLabel(text, widget)
        
        layout.addWidget(btn)
        layout.addWidget(label)
        return widget
        
    def _createPointPage(self):
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setAlignment(Qt.AlignLeft)
        layout.setSpacing(16)
        
        # 图标
        iconBtn = ToolButton(FluentIcon.BRUSH, widget)
        layout.addWidget(iconBtn)
        
        # 描边属性
        layout.addWidget(CaptionLabel("描边:", widget))
        self.pointStrokeColor = ColorPickerButton((255, 255, 255), widget)
        self.pointStrokeWidth = DoubleSpinBox(widget)
        self.pointStrokeWidth.setRange(0, 20)
        self.pointStrokeWidth.setValue(0)
        layout.addWidget(self.pointStrokeColor)
        layout.addWidget(self.pointStrokeWidth)
        
        # 分隔
        self._addSep(layout)
        
        # 大小属性
        layout.addWidget(CaptionLabel("点大小:", widget))
        self.pointSize = DoubleSpinBox(widget)
        self.pointSize.setRange(1, 100)
        self.pointSize.setValue(5)
        layout.addWidget(self.pointSize)
        
        # 分隔
        self._addSep(layout)
        
        # 填充属性
        layout.addWidget(CaptionLabel("点颜色:", widget))
        self.pointFillColor = ColorPickerButton((255, 0, 0), widget)
        layout.addWidget(self.pointFillColor)
        
        # 连接信号
        self.pointStrokeColor.colorChanged.connect(self._onStyleChanged)
        self.pointStrokeWidth.valueChanged.connect(self._onStyleChanged)
        self.pointSize.valueChanged.connect(self._onStyleChanged)
        self.pointFillColor.colorChanged.connect(self._onStyleChanged)
        
        return widget

    def _createLinePage(self):
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setAlignment(Qt.AlignLeft)
        layout.setSpacing(16)
        
        iconBtn = ToolButton(FluentIcon.EDIT, widget)
        layout.addWidget(iconBtn)
        
        # 线条属性
        layout.addWidget(CaptionLabel("线条:", widget))
        self.lineColor = ColorPickerButton((255, 255, 255), widget)
        self.lineWidth = DoubleSpinBox(widget)
        self.lineWidth.setRange(1, 20)
        self.lineWidth.setValue(2)
        layout.addWidget(self.lineColor)
        layout.addWidget(self.lineWidth)

        self._addSep(layout)

        # 端点选项
        self.lineHandles = CheckBox("添加端点", widget)
        layout.addWidget(self.lineHandles)
        
        self.lineColor.colorChanged.connect(self._onStyleChanged)
        self.lineWidth.valueChanged.connect(self._onStyleChanged)
        self.lineHandles.stateChanged.connect(self._onHandlesChanged)
        
        return widget
        
    def _createShapePage(self):
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setAlignment(Qt.AlignLeft)
        layout.setSpacing(16)
        
        iconBtn = ToolButton(FluentIcon.TILES, widget)
        layout.addWidget(iconBtn)
        
        # 描边
        layout.addWidget(CaptionLabel("描边:", widget))
        self.shapeStrokeColor = ColorPickerButton((255, 255, 255), widget)
        self.shapeStrokeWidth = DoubleSpinBox(widget)
        self.shapeStrokeWidth.setRange(0, 20)
        self.shapeStrokeWidth.setValue(1)
        layout.addWidget(self.shapeStrokeColor)
        layout.addWidget(self.shapeStrokeWidth)
        
        self._addSep(layout)
        
        # 填充
        layout.addWidget(CaptionLabel("填充:", widget))
        self.shapeFillColor = ColorPickerButton((100, 100, 100, 100), widget)
        layout.addWidget(self.shapeFillColor)

        self._addSep(layout)

        # 端点选项
        self.shapeHandles = CheckBox("添加端点", widget)
        layout.addWidget(self.shapeHandles)
        
        self.shapeStrokeColor.colorChanged.connect(self._onStyleChanged)
        self.shapeStrokeWidth.valueChanged.connect(self._onStyleChanged)
        self.shapeFillColor.colorChanged.connect(self._onStyleChanged)
        self.shapeHandles.stateChanged.connect(self._onHandlesChanged)
        
        return widget
        
    def _addSep(self, layout):
        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setFixedHeight(16)
        line.setStyleSheet("QFrame{border: 1px solid rgba(0,0,0,0.1);}")
        layout.addWidget(line)
        
    def setStyleData(self, style: StyleData):
        self._currentStyle = style
        # 更新UI不触发信号
        self.blockSignals(True)
        
        # Point
        self.pointStrokeColor.setColor(style.borderColor)
        self.pointStrokeWidth.setValue(style.borderWidth)
        self.pointFillColor.setColor(style.fillColor) # Point Face -> Fill
        self.pointSize.setValue(style.pointSize)
        
        # Line
        self.lineColor.setColor(style.lineColor)
        self.lineWidth.setValue(style.lineWidth)
        
        # Shape
        self.shapeStrokeColor.setColor(style.borderColor)
        self.shapeStrokeWidth.setValue(style.borderWidth)
        self.shapeFillColor.setColor(style.fillColor)
        
        self.blockSignals(False)
        
    def updatePageIcon(self, index, icon):
        """更新指定页面的图标"""
        target_page = None
        if index == 0:
            target_page = self.defaultPage
        elif index == 1:
            target_page = self.movePage
        elif index == 2:
            target_page = self.pointPage
        elif index == 3:
            target_page = self.linePage
        elif index == 4:
            target_page = self.shapePage
            
        if target_page:
            layout = target_page.layout()
            # 假设第一个控件总是图标按钮
            item = layout.itemAt(0)
            if item and item.widget():
                item.widget().setIcon(icon)
        
    def _getStyleForIndex(self, idx):
        """根据页面索引获取样式数据"""
        style = StyleData()
        
        if idx == 2: # Point
            style.borderColor = self.pointStrokeColor.getColor()
            style.borderWidth = self.pointStrokeWidth.value()
            style.fillColor = self.pointFillColor.getColor()
            style.showBorder = style.borderWidth > 0
            style.pointSize = self.pointSize.value()
            
        elif idx == 3: # Line
            style.lineColor = self.lineColor.getColor()
            style.lineWidth = self.lineWidth.value()
            
        elif idx == 4: # Shape
            style.borderColor = self.shapeStrokeColor.getColor()
            style.borderWidth = self.shapeStrokeWidth.value()
            style.fillColor = self.shapeFillColor.getColor()
            style.showBorder = style.borderWidth > 0
            
        return style

    def _onStyleChanged(self):
        # 从当前显示的页面收集数据
        # 使用新的StyleData实例，避免不同工具间的样式污染
        idx = self.stack.currentIndex()
        style = self._getStyleForIndex(idx)
        self._currentStyle = style
        self.styleChanged.emit(style)

    def forceUpdateStyle(self, idx):
        """强制更新指定页面的样式"""
        style = self._getStyleForIndex(idx)
        self._currentStyle = style
        self.styleChanged.emit(style)

    def _onHandlesChanged(self, state):
        self.handlesChanged.emit(state == Qt.Checked)
        
    def getHandlesState(self):
        idx = self.stack.currentIndex()
        if idx == 3: # Line
            return self.lineHandles.isChecked()
        elif idx == 4: # Shape
            return self.shapeHandles.isChecked()
        return False


class DrawingView(QWidget):
    """交互式绘图视图
    
    集成了：
    1. 顶部配置面板 (ConfigPanel)
    2. 左侧工具栏 (VerticalToolPanel)
    3. 中央绘图画布 (InteractiveDrawingWidget)
    """
    
    def __init__(self, parent=None, scale_factor=0.05, grid_size=5000.0, grid_spacing=1.0):
        """
        Args:
            parent: 父组件
            scale_factor: 缩放比例
            grid_size: 网格大小
            grid_spacing: 网格间距
        """
        super().__init__(parent)
        self.setObjectName('drawingView')
        
        # 主布局
        vlayout = QVBoxLayout(self)
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.setSpacing(0)
        
        # 1. 顶部配置面板
        self.configPanel = ConfigPanel(self)
        vlayout.addWidget(self.configPanel)
        
        # 2. 下部区域 (工具栏 + 画布)
        hlayout = QHBoxLayout()
        hlayout.setSpacing(0)
        vlayout.addLayout(hlayout)
        
        # 工具栏
        self.toolPanel = VerticalToolPanel()
        self.toolPanel.setFixedWidth(60)
        hlayout.addWidget(self.toolPanel)
        
        # 创建绘图控件
        self.drawingWidget = InteractiveDrawingWidget(
            scale_factor=scale_factor,
            grid_size=grid_size,
            grid_spacing=grid_spacing
        )
        hlayout.addWidget(self.drawingWidget)
        
        # 捕获ESC键
        self.drawingWidget.installEventFilter(self)
        if self.drawingWidget.canvas and self.drawingWidget.canvas.native_widget:
            self.drawingWidget.canvas.native_widget.installEventFilter(self)
        
        # 初始化
        self._initTools()
        self._connectSignals()
        self._initStyle()
        
        # 默认选中第一个工具
        if self.toolPanel.toolButtons:
            self.toolPanel.toolButtons[0].click()
            
    def eventFilter(self, obj, e):
        is_target = (obj is self.drawingWidget)
        if not is_target and self.drawingWidget.canvas and self.drawingWidget.canvas.native_widget:
            if obj is self.drawingWidget.canvas.native_widget:
                is_target = True

        if is_target and e.type() == QEvent.KeyPress:
            if e.key() == Qt.Key_Escape:
                # 显式取消当前操作，确保状态正确重置
                if hasattr(self.drawingWidget.canvas, 'interaction_manager'):
                    self.drawingWidget.canvas.interaction_manager.cancelCurrentOperation()
                
                # 切换回光标模式
                if self.toolPanel.toolButtons:
                    self.toolPanel.toolButtons[0].click()
                return True
        return super().eventFilter(obj, e)

    def _initTools(self):
        # 清空现有工具
        self.toolPanel.clearTools()
        
        # 1. 光标 (View)
        self.toolPanel.addTool({
            'name': 'cursor',
            'icon': DrawIcon.CURSOR,
            'tooltip': '光标模式',
            'mode': InteractionMode.DEFAULT
        })
        
        # 2. 移动 (Move)
        self.toolPanel.addTool({
            'name': 'move',
            'icon': DrawIcon.MOVE,
            'tooltip': '移动模式',
            'mode': InteractionMode.MOVE
        })
        
        # 3. 点 (Point)
        self.toolPanel.addTool({
            'name': 'point',
            'icon': DrawIcon.POINT,
            'tooltip': '点',
            'mode': InteractionMode.DRAW_POINT
        })
        
        # 4. 线条 (Line/Bezier)
        lineBtn = self.toolPanel.addTool({
            'name': 'line_group',
            'icon': DrawIcon.LINE,
            'tooltip': '线条工具',
            'subOptions': [
                {'name': '多段线', 'icon': DrawIcon.LINE, 'mode': InteractionMode.DRAW_LINE, 'checked': True},
                {'name': '贝塞尔曲线', 'icon': DrawIcon.CURVE, 'mode': InteractionMode.DRAW_BEZIER}
            ]
        })
        lineBtn.subOptionChanged.connect(self._onSubOptionChanged)
        
        # 5. 形状 (Rect/Circle/Polygon)
        shapeBtn = self.toolPanel.addTool({
            'name': 'shape_group',
            'icon': DrawIcon.RECTANGLE,
            'tooltip': '形状工具',
            'subOptions': [
                {'name': '矩形', 'icon': DrawIcon.RECTANGLE, 'mode': InteractionMode.DRAW_RECTANGLE, 'checked': True},
                {'name': '椭圆', 'icon': DrawIcon.ELLIPSE, 'mode': InteractionMode.DRAW_ELLIPSE},
                {'name': '圆形', 'icon': DrawIcon.CIRCLE, 'mode': InteractionMode.DRAW_CIRCLE},
                {'name': '多边形', 'icon': DrawIcon.POLYGON, 'mode': InteractionMode.DRAW_POLYGON}
            ]
        })
        shapeBtn.subOptionChanged.connect(self._onSubOptionChanged)
        
    def _onSubOptionChanged(self, index, option):
        sender = self.sender()
        if sender.isChecked():
            mode = option.get('mode')
            if mode:
                self.drawingWidget.setInteractionMode(mode)
                
            # 更新配置面板图标
            icon = option.get('icon')
            name = sender.toolData().get('name')
            if name == 'line_group':
                self.configPanel.updatePageIcon(3, icon)
            elif name == 'shape_group':
                self.configPanel.updatePageIcon(4, icon)
                
            # 强制更新样式以确保切换工具时应用正确的样式
            # 找到对应的 ConfigPanel 索引
            panel_idx = 0
            if name == 'line_group':
                panel_idx = 3
            elif name == 'shape_group':
                panel_idx = 4
            self.configPanel.forceUpdateStyle(panel_idx)

    def _connectSignals(self):
        self.toolPanel.toolChanged.connect(self._onToolChanged)
        self.drawingWidget.interactionModeChanged.connect(self._onModeChanged)
        self.configPanel.styleChanged.connect(self._onStyleChanged)
        self.configPanel.handlesChanged.connect(self.drawingWidget.setCreateHandles)
        
    def _initStyle(self):
        style = StyleData(
            lineWidth=2.0,
            lineColor=(0, 0.6, 1.0, 1.0),
            fillColor=(0, 0.6, 1.0, 0.3),
            borderColor=(0, 0.6, 1.0, 1.0),
            borderWidth=2.0
        )
        self.drawingWidget.setDefaultStyle(style)
        self.configPanel.setStyleData(style)
        
    def _onToolChanged(self, button):
        # 工具栏点击 -> 设置画布模式
        data = button.toolData()
        name = data.get('name')
        
        mode = InteractionMode.DEFAULT
        icon = data.get('icon') # Default icon
        
        if name == 'line_group' or name == 'shape_group':
            sub = button.currentSubOption()
            if sub:
                mode = sub.get('mode', InteractionMode.DEFAULT)
                icon = sub.get('icon')
        else:
            mode = data.get('mode', InteractionMode.DEFAULT)
            
        self.drawingWidget.setInteractionMode(mode)
        
        # 切换配置面板页面
        if name == 'cursor':
            self.configPanel.stack.setCurrentIndex(0)
            self.configPanel.updatePageIcon(0, icon)
        elif name == 'move':
            self.configPanel.stack.setCurrentIndex(1)
            self.configPanel.updatePageIcon(1, icon)
        elif name == 'point':
            self.configPanel.stack.setCurrentIndex(2)
            self.configPanel.updatePageIcon(2, icon)
        elif name == 'line_group':
            self.configPanel.stack.setCurrentIndex(3)
            self.configPanel.updatePageIcon(3, icon)
        elif name == 'shape_group':
            self.configPanel.stack.setCurrentIndex(4)
            self.configPanel.updatePageIcon(4, icon)
            
        # 强制更新样式
        self.configPanel.forceUpdateStyle(self.configPanel.stack.currentIndex())

    def _onModeChanged(self, mode):
        # 模式改变 -> 更新配置面板
        index = 0
        if mode == InteractionMode.DEFAULT:
            index = 0
        elif mode == InteractionMode.MOVE:
            index = 1
        elif mode in [InteractionMode.DRAW_POINT]:
            index = 2
        elif mode in [InteractionMode.DRAW_LINE, InteractionMode.DRAW_BEZIER]:
            index = 3
        elif mode in [InteractionMode.DRAW_RECTANGLE, InteractionMode.DRAW_CIRCLE, 
                     InteractionMode.DRAW_ELLIPSE, InteractionMode.DRAW_POLYGON]:
            index = 4
            
        if self.configPanel.stack.currentIndex() != index:
            self.configPanel.stack.setCurrentIndex(index)
            
        # 强制更新样式
        self.configPanel.forceUpdateStyle(index)

    def _onStyleChanged(self, style):
        self.drawingWidget.setDefaultStyle(style)
