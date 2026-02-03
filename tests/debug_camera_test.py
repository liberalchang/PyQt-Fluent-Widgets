# coding:utf-8
"""
调试相机和坐标系统的详细脚本
"""
import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel

from qfluentwidgets.components.vispy import InteractiveDrawingWidget


class CameraDebugDemo(QMainWindow):
    """相机调试演示窗口"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("相机和坐标系统调试")
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
        
        # 延迟检查相机状态
        from PySide6.QtCore import QTimer
        QTimer.singleShot(1000, self.checkCameraStatus)
    
    def checkCameraStatus(self):
        """检查相机状态"""
        if not self.drawingWidget.canvas:
            self.info_label.setText("Canvas 未初始化")
            return
            
        canvas = self.drawingWidget.canvas
        coord_system = canvas.coordinate_system
        
        info_lines = []
        
        # 检查基本属性
        info_lines.append(f"Canvas: {canvas}")
        info_lines.append(f"View: {canvas.view}")
        info_lines.append(f"Canvas Size: {canvas.canvas.size if canvas.canvas else 'None'}")
        
        if canvas.view:
            info_lines.append(f"Camera: {canvas.view.camera}")
            info_lines.append(f"Camera Type: {type(canvas.view.camera)}")
            
            # 检查相机属性
            camera = canvas.view.camera
            if hasattr(camera, 'center'):
                info_lines.append(f"Camera Center: {camera.center}")
            if hasattr(camera, 'scale_factor'):
                info_lines.append(f"Camera Scale: {camera.scale_factor}")
            if hasattr(camera, 'transform'):
                info_lines.append(f"Transform: {camera.transform}")
                try:
                    # 测试变换矩阵
                    test_point = np.array([0, 0, 0, 1])
                    transformed = camera.transform.imap(test_point)
                    info_lines.append(f"Test Transform (0,0,0,1): {transformed}")
                except Exception as e:
                    info_lines.append(f"Transform Error: {e}")
        
        # 测试坐标转换
        test_points = [(0, 0), (100, 100), (400, 300)]
        info_lines.append("\n坐标转换测试:")
        for screen_x, screen_y in test_points:
            world_x, world_y = coord_system.screenToWorld(screen_x, screen_y)
            info_lines.append(f"  屏幕({screen_x}, {screen_y}) -> 世界({world_x:.2f}, {world_y:.2f})")
        
        # 显示信息
        self.info_label.setText("\n".join(info_lines))
        print("\n".join(info_lines))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CameraDebugDemo()
    window.show()
    sys.exit(app.exec())
