# coding:utf-8
import sys
import os

# Add parent directory to sys.path to import qfluentwidgets
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QFrame, QPushButton, QVBoxLayout

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


class TestWindow(FluentWindow):

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
        self.setWindowTitle('Navigation Layout Test')

    def initNavigation(self):
        self.addSubInterface(self.searchInterface, FIF.SEARCH, 'Search')
        self.addSubInterface(self.musicInterface, FIF.MUSIC, 'Music')
        self.addSubInterface(self.videoInterface, FIF.VIDEO, 'Video')
        self.addSubInterface(self.folderInterface, FIF.FOLDER, 'Folder Library', NavigationItemPosition.SCROLL)
        
        self.navigationInterface.addSeparator()

        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)


class TestControlWindow(QFrame):
    """测试控制窗口"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Navigation Layout Test Control")
        self.resize(300, 200)
        
        layout = QVBoxLayout(self)
        
        # 说明标签
        infoLabel = QLabel("测试导航布局修复效果：\n1. ReturnButton和MenuButton不再重叠\n2. MenuButton位置固定在标题下方")
        infoLabel.setWordWrap(True)
        layout.addWidget(infoLabel)
        
        # 测试按钮
        self.testWithReturnBtn = QPushButton("测试显示ReturnButton")
        self.testWithoutReturnBtn = QPushButton("测试隐藏ReturnButton")
        
        self.testWithReturnBtn.clicked.connect(self.testWithReturn)
        self.testWithoutReturnBtn.clicked.connect(self.testWithoutReturn)
        
        layout.addWidget(self.testWithReturnBtn)
        layout.addWidget(self.testWithoutReturnBtn)
        
        self.windows = []
    
    def testWithReturn(self):
        """测试显示ReturnButton的情况"""
        window = TestWindow(showReturnButton=True)
        window.show()
        self.windows.append(window)
    
    def testWithoutReturn(self):
        """测试隐藏ReturnButton的情况"""
        window = TestWindow(showReturnButton=False)
        window.show()
        self.windows.append(window)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 创建测试控制窗口
    control = TestControlWindow()
    control.show()
    
    # 创建默认测试窗口
    w = TestWindow(showReturnButton=False)  # 默认隐藏ReturnButton
    w.show()
    
    sys.exit(app.exec())
