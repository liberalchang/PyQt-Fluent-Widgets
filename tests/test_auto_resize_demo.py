# coding:utf-8
import sys
import os

# Add parent directory to sys.path to import qfluentwidgets
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QFrame
from qfluentwidgets import (NavigationItemPosition, FluentWindow, FluentIcon as FIF)


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

        # create sub interfaces
        self.searchInterface = Widget('Search Interface', self)
        self.musicInterface = Widget('Music Interface', self)
        self.videoInterface = Widget('Video Interface', self)
        self.folderInterface = Widget('Folder Interface', self)
        self.settingInterface = Widget('Setting Interface', self)
        
        # add items to navigation interface
        self.initNavigation()
        
        # 启用自动伸缩功能，使用默认范围 800-1200px
        self.navigationInterface.setAutoResizeEnabled(True)
        print(f"自动伸缩已启用，范围: {self.navigationInterface.getAutoResizeRange()}")
        
        # 添加状态标签用于显示当前状态
        self.statusLabel = QLabel("窗口宽度: 900px, 导航状态: 正常", self)
        self.statusLabel.setStyleSheet("background: rgba(0, 0, 0, 100); color: white; padding: 5px; border-radius: 3px;")
        self.statusLabel.move(10, 50)
        
        self.resize(900, 700)
        self.setWindowTitle('PySide6-Fluent-Widgets Navigation Test (自动伸缩测试)')
        
    def initNavigation(self):
        self.addSubInterface(self.searchInterface, FIF.SEARCH, 'Search')
        self.addSubInterface(self.musicInterface, FIF.MUSIC, 'Music')
        self.addSubInterface(self.videoInterface, FIF.VIDEO, 'Video')
        self.addSubInterface(self.folderInterface, FIF.FOLDER, 'Folder Library', NavigationItemPosition.SCROLL)
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)
    
    def resizeEvent(self, e):
        super().resizeEvent(e)
        
        # 更新状态标签
        if hasattr(self, 'statusLabel'):
            width = self.width()
            display_mode = self.navigationInterface.panel.display_mode if hasattr(self.navigationInterface.panel, 'display_mode') else self.navigationInterface.panel.displayMode
            mode_text = {
                'NavigationDisplayMode.COMPACT': '折叠',
                'NavigationDisplayMode.EXPAND': '展开', 
                'NavigationDisplayMode.MINIMAL': '最小',
                'NavigationDisplayMode.MENU': '菜单'
            }.get(str(display_mode), str(display_mode))
            
            self.statusLabel.setText(f"窗口宽度: {width}px, 导航状态: {mode_text}")
            
            # 根据窗口宽度改变状态标签颜色
            if width < 800:
                self.statusLabel.setStyleSheet("background: rgba(255, 0, 0, 100); color: white; padding: 5px; border-radius: 3px;")
            elif width >= 1200:
                self.statusLabel.setStyleSheet("background: rgba(0, 255, 0, 100); color: white; padding: 5px; border-radius: 3px;")
            else:
                self.statusLabel.setStyleSheet("background: rgba(255, 165, 0, 100); color: white; padding: 5px; border-radius: 3px;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    
    print("=" * 50)
    print("自动伸缩测试说明:")
    print("1. 窗口宽度 < 800px: 导航栏自动折叠（红色背景）")
    print("2. 窗口宽度 >= 1200px: 导航栏自动展开（绿色背景）")
    print("3. 800px <= 窗口宽度 < 1200px: 保持当前状态（橙色背景）")
    print("4. 调整窗口大小来测试自动伸缩功能")
    print("=" * 50)
    
    sys.exit(app.exec())
