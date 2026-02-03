# coding:utf-8
"""
详细调试鼠标事件获取的脚本
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import QTimer

from qfluentwidgets.components.vispy import InteractiveDrawingWidget, InteractionMode


class MouseEventDebugDemo(QMainWindow):
    """鼠标事件调试演示窗口"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("鼠标事件详细调试")
        self.resize(800, 600)
        
        # 创建中心控件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建布局
        layout = QVBoxLayout(central_widget)
        
        # 创建标签显示信息
        self.info_label = QLabel("初始化中...")
        layout.addWidget(self.info_label)
        
        # 创建绘图控件
        self.drawingWidget = InteractiveDrawingWidget()
        layout.addWidget(self.drawingWidget)
        
        # 延迟设置调试
        QTimer.singleShot(1000, self.setupMouseDebug)
    
    def setupMouseDebug(self):
        """设置鼠标事件调试"""
        if not self.drawingWidget.canvas:
            self.info_label.setText("Canvas 未初始化")
            return
            
        canvas = self.drawingWidget.canvas
        
        # 检查canvas事件系统
        info_lines = []
        info_lines.append(f"Canvas: {canvas}")
        info_lines.append(f"Canvas has canvas: {hasattr(canvas, 'canvas')}")
        
        if hasattr(canvas, 'canvas') and canvas.canvas:
            inner_canvas = canvas.canvas
            info_lines.append(f"Inner canvas: {inner_canvas}")
            info_lines.append(f"Inner canvas has events: {hasattr(inner_canvas, 'events')}")
            
            if hasattr(inner_canvas, 'events'):
                events = inner_canvas.events
                info_lines.append(f"Events type: {type(events)}")
                info_lines.append(f"Events attributes: {[attr for attr in dir(events) if not attr.startswith('_')]}")
        
        # 手动连接鼠标事件处理函数
        if hasattr(canvas, 'canvas') and canvas.canvas and hasattr(canvas.canvas, 'events'):
            events = canvas.canvas.events
            if hasattr(events, 'mouse_press'):
                events.mouse_press.connect(self.onMousePress)
                events.mouse_move.connect(self.onMouseMove) 
                events.mouse_release.connect(self.onMouseRelease)
                info_lines.append("成功连接鼠标事件")
            else:
                info_lines.append("events对象没有鼠标事件")
        else:
            info_lines.append("无法连接鼠标事件")
        
        # 设置绘制模式
        self.drawingWidget.setInteractionMode(InteractionMode.DRAW_RECTANGLE)
        info_lines.append("设置绘制模式: DRAW_RECTANGLE")
        
        self.info_label.setText("\n".join(info_lines))
        print("\n".join(info_lines))
    
    def onMousePress(self, event):
        """鼠标按下事件"""
        print(f"鼠标按下: {event}")
        print(f"  - 位置: {event.pos}")
        print(f"  - 按钮: {event.button}")
        print(f"  - 修饰键: {event.modifiers}")
        
        if event.pos is not None:
            screen_x, screen_y = event.pos[0], event.pos[1]
            coord_system = self.drawingWidget.canvas.coordinate_system
            world_x, world_y = coord_system.screenToWorld(screen_x, screen_y)
            print(f"  - 屏幕坐标: ({screen_x:.1f}, {screen_y:.1f})")
            print(f"  - 世界坐标: ({world_x:.2f}, {world_y:.2f})")
    
    def onMouseMove(self, event):
        """鼠标移动事件"""
        if event.pos is not None:
            screen_x, screen_y = event.pos[0], event.pos[1]
            coord_system = self.drawingWidget.canvas.coordinate_system
            world_x, world_y = coord_system.screenToWorld(screen_x, screen_y)
            print(f"鼠标移动: 屏幕({screen_x:.1f}, {screen_y:.1f}) -> 世界({world_x:.2f}, {world_y:.2f})")
    
    def onMouseRelease(self, event):
        """鼠标释放事件"""
        print(f"鼠标释放: {event}")
        if event.pos is not None:
            screen_x, screen_y = event.pos[0], event.pos[1]
            coord_system = self.drawingWidget.canvas.coordinate_system
            world_x, world_y = coord_system.screenToWorld(screen_x, screen_y)
            print(f"  - 屏幕坐标: ({screen_x:.1f}, {screen_y:.1f})")
            print(f"  - 世界坐标: ({world_x:.2f}, {world_y:.2f})")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MouseEventDebugDemo()
    window.show()
    sys.exit(app.exec())
