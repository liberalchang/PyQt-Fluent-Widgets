# coding:utf-8
"""
测试DragOnlySplitter组件
"""
import sys
from pathlib import Path

# 添加项目路径到最前面，确保使用本地开发版本
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QVBoxLayout, QTextEdit, QWidget

from qfluentwidgets import (
    FluentSplitter, DragOnlySplitter, setTheme, Theme, 
    PushButton, BodyLabel, FluentWindow, FluentIcon
)


class TestInterface(QWidget):
    """测试界面"""
    
    def __init__(self):
        super().__init__()
        self.setObjectName("testInterface")
        self.setupUI()
    
    def setupUI(self):
        """设置UI"""
        layout = QVBoxLayout(self)
        
        # 测试FluentSplitter（支持折叠）
        layout.addWidget(BodyLabel("FluentSplitter（支持折叠）:"))
        fluent_splitter = FluentSplitter(Qt.Horizontal)
        fluent_splitter.addWidget(QTextEdit("左侧面板 - FluentSplitter（支持折叠功能）"))
        fluent_splitter.addWidget(QTextEdit("右侧面板 - FluentSplitter"))
        fluent_splitter.setSizes([400, 400])
        layout.addWidget(fluent_splitter)
        
        # 测试DragOnlySplitter（只可拖动）
        layout.addWidget(BodyLabel("DragOnlySplitter（只可拖动）:"))
        drag_only_splitter = DragOnlySplitter(Qt.Horizontal)
        drag_only_splitter.addWidget(QTextEdit("左侧面板 - DragOnlySplitter（只有拖动功能）"))
        drag_only_splitter.addWidget(QTextEdit("右侧面板 - DragOnlySplitter"))
        drag_only_splitter.setSizes([400, 400])
        layout.addWidget(drag_only_splitter)
        
        # 测试垂直方向的DragOnlySplitter
        layout.addWidget(BodyLabel("DragOnlySplitter（垂直方向）:"))
        vertical_splitter = DragOnlySplitter(Qt.Vertical)
        vertical_splitter.addWidget(QTextEdit("上面板 - 垂直DragOnlySplitter"))
        vertical_splitter.addWidget(QTextEdit("下面板 - 垂直DragOnlySplitter"))
        vertical_splitter.setSizes([300, 300])
        layout.addWidget(vertical_splitter)


class TestSplitterWindow(FluentWindow):
    """分割器测试窗口"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("DragOnlySplitter 测试")
        self.resize(1000, 800)
        
        # 创建测试界面
        self.test_interface = TestInterface()
        
        # 添加主题切换按钮到标题栏
        self.theme_button = PushButton("切换主题")
        self.theme_button.clicked.connect(self._toggle_theme)
        self.titleBar.hBoxLayout.addWidget(self.theme_button)
        
        # 将测试界面添加到窗口
        self.addSubInterface(
            self.test_interface, 
            FluentIcon.MENU, 
            "分割器测试"
        )
        
        self._is_dark = False
    
    def _toggle_theme(self):
        """切换主题"""
        self._is_dark = not self._is_dark
        theme = Theme.DARK if self._is_dark else Theme.LIGHT
        setTheme(theme, self)
        self.setWindowTitle(f"DragOnlySplitter 测试 - {'深色' if self._is_dark else '浅色'}主题")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestSplitterWindow()
    window.show()
    sys.exit(app.exec())
