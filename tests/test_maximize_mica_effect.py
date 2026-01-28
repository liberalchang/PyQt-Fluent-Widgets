# coding:utf-8
import sys
import os

# Add parent directory to sys.path to import qfluentwidgets
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtCore import Qt, QEvent
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QFrame, QVBoxLayout, QPushButton

from qfluentwidgets import (NavigationItemPosition, FluentWindow,
                            FluentIcon as FIF)


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = QLabel(text, self)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))


class TestMaximizeWindow(FluentWindow):
    """测试最大化后云母效果的窗口"""

    def __init__(self, showReturnButton=True):
        super().__init__(showReturnButton=showReturnButton)

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
        self.setWindowTitle('Maximize Mica Effect Test')
        
        # 启用云母效果
        self.setMicaEffectEnabled(True)
        print(f"初始状态 - 云母效果启用: {self.isMicaEffectEnabled()}")
        print(f"初始状态 - 窗口状态: {self.windowState()}")

    def initNavigation(self):
        self.addSubInterface(self.searchInterface, FIF.SEARCH, 'Search')
        self.addSubInterface(self.musicInterface, FIF.MUSIC, 'Music')
        self.addSubInterface(self.videoInterface, FIF.VIDEO, 'Video')
        self.addSubInterface(self.folderInterface, FIF.FOLDER, 'Folder Library', NavigationItemPosition.SCROLL)
        
        self.navigationInterface.addSeparator()

        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)

    def changeEvent(self, event):
        """重写changeEvent来检测窗口状态变化"""
        super().changeEvent(event)
        
        if event.type() == QEvent.WindowStateChange:
            print(f"窗口状态变化 - 新状态: {self.windowState()}")
            print(f"云母效果启用状态: {self.isMicaEffectEnabled()}")
            
            # 检查是否是最大化状态
            if self.isMaximized():
                print("窗口已最大化，重新应用云母效果...")
                # 重新应用云母效果
                if self.isMicaEffectEnabled():
                    self.windowEffect.setMicaEffect(self.winId(), True)
                    print("已重新应用云母效果")
            else:
                print("窗口非最大化状态")
    
    def showEvent(self, event):
        """重写showEvent"""
        super().showEvent(event)
        print(f"显示事件 - 云母效果启用: {self.isMicaEffectEnabled()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 创建测试窗口
    w = TestMaximizeWindow(showReturnButton=True)
    w.show()
    
    print("测试窗口已创建，请尝试最大化窗口来观察云母效果的变化")
    
    sys.exit(app.exec())
