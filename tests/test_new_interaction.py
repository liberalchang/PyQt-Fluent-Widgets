# coding:utf-8
"""
测试新的交互逻辑
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox
from PySide6.QtCore import Qt, QTimer

from qfluentwidgets.components.vispy import InteractiveDrawingWidget, InteractionMode


class NewInteractionTest(QMainWindow):
    """新交互逻辑测试"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("新交互逻辑测试")
        self.resize(1000, 700)
        
        # 创建中心控件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建布局
        layout = QVBoxLayout(central_widget)
        
        # 创建说明标签
        info_label = QLabel("新交互逻辑测试\n"
                          "1. 默认模式：保持Vispy原生交互（左键平移，滚轮缩放）\n"
                          "2. 移动模式：左键选择和移动图元\n"
                          "3. 绘制模式：各种绘制工具\n"
                          "4. ESC键：取消当前操作\n"
                          "5. 端点控制：勾选'生成端点'后绘制图元会自动生成控制点")
        layout.addWidget(info_label)
        
        # 创建按钮布局
        button_layout = QVBoxLayout()
        
        # 选项
        self.chk_handles = QCheckBox("生成端点 (Create Handles)")
        self.chk_handles.toggled.connect(self.onHandlesToggled)
        button_layout.addWidget(self.chk_handles)

        # 基础模式按钮
        btn_default = QPushButton("默认模式")
        btn_default.clicked.connect(lambda: self.setMode(InteractionMode.DEFAULT))
        button_layout.addWidget(btn_default)
        
        btn_move = QPushButton("移动模式")
        btn_move.clicked.connect(lambda: self.setMode(InteractionMode.MOVE))
        button_layout.addWidget(btn_move)
        
        # 绘制模式按钮
        btn_line = QPushButton("多段线")
        btn_line.clicked.connect(lambda: self.setMode(InteractionMode.DRAW_LINE))
        button_layout.addWidget(btn_line)
        
        btn_rect = QPushButton("矩形")
        btn_rect.clicked.connect(lambda: self.setMode(InteractionMode.DRAW_RECTANGLE))
        button_layout.addWidget(btn_rect)
        
        btn_circle = QPushButton("圆形")
        btn_circle.clicked.connect(lambda: self.setMode(InteractionMode.DRAW_CIRCLE))
        button_layout.addWidget(btn_circle)
        
        btn_bezier = QPushButton("贝塞尔曲线")
        btn_bezier.clicked.connect(lambda: self.setMode(InteractionMode.DRAW_BEZIER))
        button_layout.addWidget(btn_bezier)
        
        btn_polygon = QPushButton("多边形")
        btn_polygon.clicked.connect(lambda: self.setMode(InteractionMode.DRAW_POLYGON))
        button_layout.addWidget(btn_polygon)
        
        btn_point = QPushButton("点")
        btn_point.clicked.connect(lambda: self.setMode(InteractionMode.DRAW_POINT))
        button_layout.addWidget(btn_point)
        
        btn_edit_bezier = QPushButton("编辑贝塞尔")
        btn_edit_bezier.clicked.connect(lambda: self.setMode(InteractionMode.EDIT_BEZIER))
        button_layout.addWidget(btn_edit_bezier)
        
        # 功能按钮
        btn_clear = QPushButton("清空画布")
        btn_clear.clicked.connect(self.clearCanvas)
        button_layout.addWidget(btn_clear)
        
        btn_test = QPushButton("添加测试图元")
        btn_test.clicked.connect(self.addTestPrimitives)
        button_layout.addWidget(btn_test)
        
        layout.addLayout(button_layout)
        
        # 状态标签
        self.status_label = QLabel("准备就绪")
        layout.addWidget(self.status_label)
        
        # 创建绘图控件
        self.drawingWidget = InteractiveDrawingWidget()
        layout.addWidget(self.drawingWidget)
        
        # 连接信号
        self.drawingWidget.interactionModeChanged.connect(self.onModeChanged)
        self.drawingWidget.primitiveAdded.connect(self.onPrimitiveAdded)
        
        # 延迟初始化
        QTimer.singleShot(1000, self.initialize)
    
    def initialize(self):
        """初始化"""
        self.setMode(InteractionMode.DEFAULT)
        self.addTestPrimitives()
    
    def setMode(self, mode: InteractionMode):
        """设置交互模式"""
        if self.drawingWidget:
            self.drawingWidget.setInteractionMode(mode)
            mode_names = {
                InteractionMode.DEFAULT: "默认模式",
                InteractionMode.MOVE: "移动模式",
                InteractionMode.DRAW_LINE: "多段线",
                InteractionMode.DRAW_RECTANGLE: "矩形",
                InteractionMode.DRAW_CIRCLE: "圆形",
                InteractionMode.DRAW_BEZIER: "贝塞尔曲线",
                InteractionMode.DRAW_POLYGON: "多边形",
                InteractionMode.DRAW_POINT: "点",
                InteractionMode.EDIT_BEZIER: "编辑贝塞尔"
            }
            mode_name = mode_names.get(mode, f"未知模式({mode})")
            self.status_label.setText(f"当前模式: {mode_name}")
    
    def clearCanvas(self):
        """清空画布"""
        if self.drawingWidget:
            self.drawingWidget.clearAll()
            self.status_label.setText("画布已清空")
    
    def addTestPrimitives(self):
        """添加测试图元"""
        if self.drawingWidget:
            import numpy as np
            self.drawingWidget.addRectangle(pos=(50, 50), size=(80, 60))
            self.drawingWidget.addCircle(center=(200, 100), radius=40)
            self.drawingWidget.addLine(np.array([[300, 50], [400, 150]], dtype=np.float32))
            self.drawingWidget.autoRange()
            self.status_label.setText("已添加测试图元")
    
    def onModeChanged(self, mode: InteractionMode):
        """模式改变回调"""
        print(f"交互模式改变为: {mode}")
    
    def onPrimitiveAdded(self, primitive_id: str):
        """图元添加回调"""
        print(f"图元已添加: {primitive_id}")

    def onHandlesToggled(self, checked: bool):
        """端点选项切换回调"""
        if self.drawingWidget:
            self.drawingWidget.setCreateHandles(checked)
            self.status_label.setText(f"端点生成: {'开启' if checked else '关闭'}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NewInteractionTest()
    window.show()
    sys.exit(app.exec())
