# coding:utf-8
import sys
import os

# Add parent directory to sys.path to import qfluentwidgets
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QFrame

from qfluentwidgets import (NavigationItemPosition, FluentWindow,
                            FluentIcon as FIF, Theme, setTheme, WindowEffect)


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

        # 启用亚克力特效（Windows 11）
        self.setWindowEffect(WindowEffect.ACRYLIC)

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
        self.setWindowTitle('Navigation Test - 亚克力特效')
    
    def initNavigation(self):
        self.addSubInterface(self.searchInterface, FIF.SEARCH, 'Search')
        self.addSubInterface(self.musicInterface, FIF.MUSIC, 'Music')
        self.addSubInterface(self.videoInterface, FIF.VIDEO, 'Video')
        self.addSubInterface(self.folderInterface, FIF.FOLDER, 'Folder Library', NavigationItemPosition.SCROLL)
        
        self.navigationInterface.addSeparator()

        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)
    
    # def showEvent(self, e):
    #     """重写 showEvent 确保初始显示时窗口特效生效"""
    #     super().showEvent(e)
    #     # 延迟触发窗口特效应用，确保窗口完全显示后再应用
    #     from PySide6.QtCore import QTimer
    #     QTimer.singleShot(100, self._ensureWindowEffect)
    
    # def _ensureWindowEffect(self):
    #     """确保窗口特效生效"""
    #     if self.isMicaEffectEnabled():
    #         self.setMicaEffectEnabled(True)
    #     elif self.isAcrylicEffectEnabled():
    #         self.setAcrylicEffectEnabled(True)


if __name__ == '__main__':
    # 设置主题（可选择 Theme.LIGHT 或 Theme.DARK）
    setTheme(Theme.LIGHT, save=False)  # 使用暗色主题以更好展示亚克力特效
    
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())
