# coding:utf-8
"""
调试坐标转换的测试脚本
"""
import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

from qfluentwidgets.components.vispy import InteractiveDrawingWidget, InteractionMode


class CoordinateDebugDemo(QMainWindow):
    """坐标调试演示窗口"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("坐标转换调试")
        self.resize(800, 600)
        
        # 创建中心控件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建布局
        layout = QVBoxLayout(central_widget)
        
        # 创建标签显示坐标信息
        self.coord_label = QLabel("鼠标坐标: 未检测")
        layout.addWidget(self.coord_label)
        
        # 创建绘图控件
        self.drawingWidget = InteractiveDrawingWidget()
        layout.addWidget(self.drawingWidget)
        
        # 创建测试按钮
        test_btn = QPushButton("测试坐标转换")
        test_btn.clicked.connect(self.testCoordinateConversion)
        layout.addWidget(test_btn)
        
        # 连接鼠标事件
        if hasattr(self.drawingWidget, 'canvas') and self.drawingWidget.canvas:
            if hasattr(self.drawingWidget.canvas, 'events'):
                self.drawingWidget.canvas.events.mouse_move.connect(self.onMouseMove)
        
        # 测试一些固定点
        self.testFixedPoints()
    
    def onMouseMove(self, event):
        """鼠标移动事件"""
        if event.pos is None:
            return
            
        screen_x, screen_y = event.pos[0], event.pos[1]
        
        # 获取坐标系统
        coord_system = self.drawingWidget.canvas.coordinate_system
        
        # 转换为世界坐标
        world_x, world_y = coord_system.screenToWorld(screen_x, screen_y)
        
        # 显示信息
        info = f"屏幕坐标: ({screen_x:.1f}, {screen_y:.1f}) -> 世界坐标: ({world_x:.2f}, {world_y:.2f})"
        self.coord_label.setText(info)
    
    def testCoordinateConversion(self):
        """测试坐标转换"""
        coord_system = self.drawingWidget.canvas.coordinate_system
        
        # 测试几个关键点
        test_points = [
            (0, 0),           # 左上角
            (100, 100),      # 中心附近
            (400, 300),      # 右下
        ]
        
        print("=== 坐标转换测试 ===")
        for screen_x, screen_y in test_points:
            world_x, world_y = coord_system.screenToWorld(screen_x, screen_y)
            print(f"屏幕({screen_x}, {screen_y}) -> 世界({world_x:.2f}, {world_y:.2f})")
    
    def testFixedPoints(self):
        """测试固定点绘制"""
        # 在固定位置添加一些测试图形
        self.drawingWidget.addRectangle(pos=(50, 50), size=(30, 20))
        self.drawingWidget.addCircle(center=(150, 100), radius=25)
        self.drawingWidget.addLine(np.array([[200, 50], [250, 150]], dtype=np.float32))
        
        # 自动缩放
        self.drawingWidget.autoRange()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CoordinateDebugDemo()
    window.show()
    sys.exit(app.exec())
