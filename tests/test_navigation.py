# coding:utf-8
import sys
import os

# Add parent directory to sys.path to import qfluentwidgets
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QFrame

from qfluentwidgets import (NavigationItemPosition, FluentWindow,
                            FluentIcon as FIF, Theme, setTheme)


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
        self.setWindowTitle('Navigation Test')

    def initNavigation(self):
        self.addSubInterface(self.searchInterface, FIF.SEARCH, 'Search')
        self.addSubInterface(self.musicInterface, FIF.MUSIC, 'Music')
        self.addSubInterface(self.videoInterface, FIF.VIDEO, 'Video')
        self.addSubInterface(self.folderInterface, FIF.FOLDER, 'Folder Library', NavigationItemPosition.SCROLL)
        
        self.navigationInterface.addSeparator()

        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)
    
    # def resizeEvent(self, e):
    #     """重写 resizeEvent 以确保窗口特效在最大化后仍然有效"""
    #     super().resizeEvent(e)
    #     # 注意：由于 FluentWidget 现在已经内置了 OpenGL 修复和延迟初始化，
    #     # 这个方法主要是为了向后兼容和额外保险


if __name__ == '__main__':
    # 设置主题（可选择 Theme.LIGHT 或 Theme.DARK）
    setTheme(Theme.LIGHT, save=False)  # 使用亮色主题以更好展示云母特效
    
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())
