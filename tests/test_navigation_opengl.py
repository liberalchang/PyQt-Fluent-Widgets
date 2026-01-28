# coding:utf-8
import sys
import os

# Add parent directory to sys.path to import qfluentwidgets
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtCore import Qt, QTimer, QEvent
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QFrame

from qfluentwidgets import (NavigationItemPosition, FluentWindow,
                            FluentIcon as FIF, Theme, setTheme)

# 尝试导入 OpenGL 相关模块
try:
    from PySide6.QtOpenGLWidgets import QOpenGLWidget
    from PySide6.QtGui import QSurfaceFormat
    OPENGL_AVAILABLE = True
    print("OpenGL available")
except ImportError:
    OPENGL_AVAILABLE = False
    print("OpenGL not available")


class OpenGLWidget(QOpenGLWidget if OPENGL_AVAILABLE else QFrame):
    """简单的 OpenGL Widget，用于测试 OpenGL 上下文对云母特效的影响"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        if OPENGL_AVAILABLE:
            # 设置 OpenGL 格式
            fmt = QSurfaceFormat()
            fmt.setDepthBufferSize(24)
            fmt.setStencilBufferSize(8)
            fmt.setSamples(4)  # 抗锯齿
            QSurfaceFormat.setDefaultFormat(fmt)
            print("OpenGL widget created with format")
        else:
            print("Fallback widget created")


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = QLabel(text, self)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))


class Window(FluentWindow):

    def __init__(self):
        super().__init__(showReturnButton=True)

        # 启用云母特效（Windows 11）
        self.setMicaEffectEnabled(True)
        
        # 添加 OpenGL Widget 来测试
        if OPENGL_AVAILABLE:
            self.openglWidget = OpenGLWidget(self)
            print("OpenGL widget added to window")

        # create sub interfaces
        self.searchInterface = Widget('Search Interface', self)
        self.musicInterface = Widget('Music Interface', self)
        self.videoInterface = Widget('Video Interface', self)
        self.folderInterface = Widget('Folder Interface', self)
        self.settingInterface = Widget('Setting Interface', self)

        # add items to navigation interface
        self.initNavigation()
        self.navigationInterface.setAutoResizeEnabled(True)

        self.resize(900, 700)
        self.setWindowTitle('Navigation Test - OpenGL Experiment')
    
    def initNavigation(self):
        self.addSubInterface(self.searchInterface, FIF.SEARCH, 'Search')
        self.addSubInterface(self.musicInterface, FIF.MUSIC, 'Music')
        self.addSubInterface(self.videoInterface, FIF.VIDEO, 'Video')
        self.addSubInterface(self.folderInterface, FIF.FOLDER, 'Folder Library', NavigationItemPosition.SCROLL)
        
        self.navigationInterface.addSeparator()

        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)
    
    def changeEvent(self, e):
        """监听窗口状态变化"""
        super().changeEvent(e)
        
        # 检查窗口状态变化
        if e.type() == QEvent.WindowStateChange:
            print("Window state changed")
            print(f"Is maximized: {self.isMaximized()}")
            print(f"OpenGL available: {OPENGL_AVAILABLE}")
            
            # 如果窗口被最大化，延迟重新应用云母特效
            if self.isMaximized():
                print("Window maximized, re-applying Mica effect...")
                # 直接操作 windowEffect，绕过主题检查
                QTimer.singleShot(300, self._forceMicaEffect)
                QTimer.singleShot(600, self._forceMicaEffect)
    
    def _forceMicaEffect(self):
        """强制重新应用云母特效"""
        try:
            from qfluentwidgets.common.config import isDarkTheme
            # 直接调用 windowEffect.setMicaEffect
            self.windowEffect.removeBackgroundEffect(self.winId())
            self.windowEffect.setMicaEffect(self.winId(), isDarkTheme())
            self.setAttribute(Qt.WA_TranslucentBackground)
            print("Force applied Mica effect")
        except Exception as ex:
            print(f"Error applying Mica effect: {ex}")


if __name__ == '__main__':
    # 设置主题（可选择 Theme.LIGHT 或 Theme.DARK）
    setTheme(Theme.LIGHT, save=False)  # 使用亮色主题以更好展示云母特效
    
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())
