#!/usr/bin/env python3
# coding: utf-8
"""
DrawIcon使用示例
展示如何在应用中使用绘图图标枚举
"""

from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QAction
from qfluentwidgets.common import DrawIcon

class DrawingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("绘图应用示例")
        self.setGeometry(200, 200, 800, 600)
        
        # 创建工具栏
        toolbar = QToolBar("绘图工具")
        self.addToolBar(toolbar)
        
        # 添加绘图工具按钮
        self.create_drawing_actions(toolbar)
        
    def create_drawing_actions(self, toolbar):
        """创建绘图工具动作"""
        
        # 选择工具
        select_action = QAction(DrawIcon.CURSOR.icon(), "选择工具", self)
        select_action.triggered.connect(lambda: self.on_tool_selected("选择"))
        toolbar.addAction(select_action)
        
        toolbar.addSeparator()
        
        # 基础绘图工具
        line_action = QAction(DrawIcon.LINE.icon(), "直线", self)
        line_action.triggered.connect(lambda: self.on_tool_selected("直线"))
        toolbar.addAction(line_action)
        
        circle_action = QAction(DrawIcon.CIRCLE.icon(), "圆形", self)
        circle_action.triggered.connect(lambda: self.on_tool_selected("圆形"))
        toolbar.addAction(circle_action)
        
        ellipse_action = QAction(DrawIcon.ELLIPSE.icon(), "椭圆", self)
        ellipse_action.triggered.connect(lambda: self.on_tool_selected("椭圆"))
        toolbar.addAction(ellipse_action)
        
        rectangle_action = QAction(DrawIcon.RECTANGLE.icon(), "矩形", self)
        rectangle_action.triggered.connect(lambda: self.on_tool_selected("矩形"))
        toolbar.addAction(rectangle_action)
        
        polygon_action = QAction(DrawIcon.POLYGON.icon(), "多边形", self)
        polygon_action.triggered.connect(lambda: self.on_tool_selected("多边形"))
        toolbar.addAction(polygon_action)
        
        curve_action = QAction(DrawIcon.CURVE.icon(), "曲线", self)
        curve_action.triggered.connect(lambda: self.on_tool_selected("曲线"))
        toolbar.addAction(curve_action)
        
        point_action = QAction(DrawIcon.POINT.icon(), "点", self)
        point_action.triggered.connect(lambda: self.on_tool_selected("点"))
        toolbar.addAction(point_action)
        
        toolbar.addSeparator()
        
        # 移动工具
        move_action = QAction(DrawIcon.MOVE.icon(), "移动", self)
        move_action.triggered.connect(lambda: self.on_tool_selected("移动"))
        toolbar.addAction(move_action)
        
    def on_tool_selected(self, tool_name):
        """工具选择回调"""
        self.setWindowTitle(f"绘图应用示例 - 当前工具: {tool_name}")
        print(f"选择了工具: {tool_name}")

def main():
    app = QApplication(sys.argv)
    window = DrawingApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    import sys
    main()
