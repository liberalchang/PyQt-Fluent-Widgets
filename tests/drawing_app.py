# coding: utf-8
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from typing import Optional, Tuple
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QStackedWidget, QFrame, QSizePolicy,
                               QCheckBox)
from PySide6.QtCore import Qt, Signal, QSize, QEvent
from PySide6.QtGui import QColor, QIcon, QPainter

from qfluentwidgets import (CaptionLabel, DoubleSpinBox, SpinBox, ColorDialog, 
                            FluentIcon, PushButton, ToolButton, Theme, isDarkTheme,
                            CheckBox, DrawIcon)
from qfluentwidgets.components.widgets.tool_tip import ToolTipFilter

from qfluentwidgets.components.vispy import (
    InteractiveDrawingWidget,
    InteractionMode,
    StyleData
)
from qfluentwidgets.components.widgets import VerticalToolPanel

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
        
        # 标题（如果需要）
        # self.titleLabel = CaptionLabel(title, self)
        # self.layout.addWidget(self.titleLabel)
        
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
        iconBtn = ToolButton(FluentIcon.BRUSH, widget) # 用BRUSH代替点图标
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
        self.pointSize.valueChanged.connect(self._onStyleChanged) # 注意：点大小通常在PrimitiveData中，这里我们假设StyleData不直接存点大小，或者我们需要特殊处理。但StyleData确实没有点大小。StyleData有lineWidth。
        # 等等，StyleData没有点大小(radius)。DrawingCanvas使用的是PointData.radius。
        # 默认PointData.radius是3.0。
        # 交互管理器创建点时，使用默认的点大小吗？
        # 目前InteractionManager创建点时：data = PointData(x=x, y=y, style=self._default_style.copy())
        # PointData默认radius=3.0。
        # 如果要在UI上控制默认点大小，我们需要扩展InteractionManager或StyleData。
        # 鉴于StyleData是通用的，我们可以暂且忽略点大小的即时控制，或者将其存入StyleData的userData?
        # 或者，我们只能控制StyleData里的属性。
        # 用户明确要求"点大小标签，点大小"。
        # 我需要一种方式将这个值传递给InteractionManager。
        # 我可以在DrawingApp中处理。
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
        # print(f"DEBUG: ConfigPanel._onStyleChanged idx={idx}")
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

class DrawingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("交互式绘图应用")
        self.resize(1200, 800)
        
        # 主布局
        central = QWidget()
        self.setCentralWidget(central)
        vlayout = QVBoxLayout(central)
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
        # scale_factor=0.05: 1像素 = 0.05米
        # grid_size=5000: 半径5000米（范围-5000到5000），总宽10000米
        # grid_spacing=1.0: 间隔1米
        self.drawingWidget = InteractiveDrawingWidget(
            scale_factor=0.05,
            grid_size=5000.0,
            grid_spacing=1.0
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

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            # 切换回光标模式
            if self.toolPanel.toolButtons:
                self.toolPanel.toolButtons[0].click()
        else:
            super().keyPressEvent(e)

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
                icon = sub.get('icon') # Sub option icon
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
            
        # 更新端点选项状态
        self.drawingWidget.setCreateHandles(self.configPanel.getHandlesState())
        
        # 强制更新样式，确保第一次切换时样式正确应用
        # 这解决了从绘制点切换到矩形时，第一个矩形可能沿用点样式的问题
        self.configPanel.forceUpdateStyle(self.configPanel.stack.currentIndex())
            
    def _onModeChanged(self, mode):
        # 画布模式改变 -> 更新顶部面板
        index = 0
        if mode == InteractionMode.DEFAULT:
            index = 0
        elif mode == InteractionMode.MOVE:
            index = 1
        elif mode == InteractionMode.DRAW_POINT:
            index = 2
        elif mode in [InteractionMode.DRAW_LINE, InteractionMode.DRAW_BEZIER]:
            index = 3
        else: # Shapes
            index = 4
            
        self.configPanel.stack.setCurrentIndex(index)
        # 强制更新样式，确保工具切换时应用正确的样式
        self.configPanel.forceUpdateStyle(index)
            
    def _onStyleChanged(self, style):
        # 配置面板修改 -> 更新画布默认样式
        self.drawingWidget.setDefaultStyle(style)
        
        # 特殊处理点大小 (通过userData传递? 或者修改DrawingWidget接口)
        # 简单起见，目前仅支持StyleData里的属性。
        # 如果需要支持点大小，我们需要修改InteractiveDrawingWidget来接受createOptions

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DrawingApp()
    window.show()
    
    # # --- Simulation Start ---
    # import time
    # from PySide6.QtCore import QPoint
    
    # print("\n=== STARTING SIMULATION ===")
    
    # # 1. Switch to Point Tool
    # print("1. Switching to Point Tool...")
    # window.toolPanel.toolButtons[2].click()
    # QApplication.processEvents()
    
    # # 2. Set Point Style (Red, Opaque)
    # print("2. Setting Point Style (Red, Opaque)...")
    # window.configPanel.pointFillColor.setColor((1.0, 0.0, 0.0, 1.0))
    # window.configPanel.pointSize.setValue(10)
    # QApplication.processEvents() # Allow signals to propagate
    
    # # Verify InteractionManager has Point Style
    # im_style = window.drawingWidget.canvas.interaction_manager.getDefaultStyle()
    # print(f"   IM Default Style (Point): {im_style.fillColor}")
    
    # # 3. Draw a Point
    # print("3. Drawing a Point...")
    # im = window.drawingWidget.canvas.interaction_manager
    # im.handleMousePress(100, 100, 'left')
    # im.handleMouseRelease(100, 100, 'left')
    # QApplication.processEvents()
    
    # # 4. Switch to Rectangle Tool
    # print("4. Switching to Rectangle Tool...")
    # window.toolPanel.toolButtons[4].click()
    # QApplication.processEvents()
    
    # # Verify InteractionManager has Shape Style
    # # Shape default is usually (0, 0.6, 1.0, 0.3)
    # im_style = window.drawingWidget.canvas.interaction_manager.getDefaultStyle()
    # print(f"   IM Default Style (Rect): {im_style.fillColor}")
    
    # shape_fill = window.configPanel.shapeFillColor.getColor()
    # print(f"   ConfigPanel Shape Fill: {shape_fill}")
    
    # if im_style.fillColor == shape_fill:
    #     print("   [PASS] Style updated correctly.")
    # else:
    #     print("   [FAIL] Style mismatch! InteractionManager has wrong style.")
        
    # # 5. Draw a Rectangle
    # print("5. Drawing a Rectangle...")
    # im.handleMousePress(200, 200, 'left')
    # im.handleMouseMove(300, 300)
    # im.handleMouseRelease(300, 300, 'left')
    # QApplication.processEvents()
    
    # # 6. Verify Created Rectangle Style
    # primitives = window.drawingWidget.canvas.layer_manager.getAllPrimitives()
    # rect_prim = primitives[-1] # Last one
    # print(f"   Created Primitive Type: {rect_prim.type_name}")
    # print(f"   Created Primitive Fill: {rect_prim.data.style.fillColor}")
    
    # # Inspect Scene Children Count
    # scene = window.drawingWidget.canvas.view.scene
    # print(f"   Scene Children Count: {len(scene.children)}")
    # # Print children types
    # for child in scene.children:
    #     print(f"     - Child: {type(child).__name__}, Parent: {child.parent}")

    # if rect_prim.data.style.fillColor == shape_fill:
    #     print("   [PASS] Rectangle created with correct style.")
    # else:
    #     print("   [FAIL] Rectangle created with WRONG style.")

    # # 7. Delete the Rectangle
    # print("7. Deleting the Rectangle...")
    # window.drawingWidget.canvas.removePrimitive(rect_prim.id)
    # QApplication.processEvents()
    
    # # 8. Check Previous Primitive (Point)
    # primitives = window.drawingWidget.canvas.layer_manager.getAllPrimitives()
    # if len(primitives) > 0:
    #     point_prim = primitives[0]
    #     print(f"   Remaining Primitive Type: {point_prim.type_name}")
    #     print(f"   Remaining Primitive Fill: {point_prim.data.style.fillColor}")
    #     # Check if Point turned Blue
    #     if point_prim.data.style.fillColor == shape_fill:
    #          print("   [FAIL] Color Transferred! Point is now Blue.")
    #     else:
    #          print("   [PASS] Point color remains unchanged.")
    # else:
    #     print("   [FAIL] No primitives left?")
        
    # print("=== SIMULATION END ===\n")
    # --- Simulation End ---
    
    sys.exit(app.exec())
