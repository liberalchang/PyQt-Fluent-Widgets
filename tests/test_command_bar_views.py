# coding:utf-8
"""
CommandBar Views Test - 测试新的视图封装类
演示 VerticalCommandBarView、ResponsiveCommandBarView、MovableCommandBarView 的使用
"""
import sys
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

sys.path.insert(0, str(Path(__file__).parents[1]))

from qfluentwidgets import (
    FluentIcon, setTheme, Theme
)
from qfluentwidgets.components.widgets.command_bar_views import (
    VerticalCommandBarView, ResponsiveCommandBarView, MovableCommandBarView
)


class CommandBarViewsTest(QWidget):
    """CommandBar 视图封装类测试"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CommandBar Views Test")
        # 不设置固定尺寸，允许调整窗口大小来测试响应式布局
        
        setTheme(Theme.LIGHT)
        
        mainLayout = QVBoxLayout(self)
        mainLayout.setSpacing(20)
        mainLayout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        titleLabel = QLabel("<h1>CommandBar Views 封装类测试</h1>")
        mainLayout.addWidget(titleLabel)
        
        # Section 1: VerticalCommandBarView
        self._createVerticalSection(mainLayout)
        
        # Section 2: ResponsiveCommandBarView
        self._createResponsiveSection(mainLayout)
        
        # Section 3: MovableCommandBarView
        self._createMovableSection(mainLayout)

    def _createVerticalSection(self, mainLayout):
        """创建竖直命令栏视图测试"""
        sectionLabel = QLabel("<h2>1. VerticalCommandBarView - 竖直命令栏视图</h2>")
        mainLayout.addWidget(sectionLabel)
        
        infoLabel = QLabel("<b>自动布局的竖直命令栏，使用 QVBoxLayout</b>")
        mainLayout.addWidget(infoLabel)
        
        self.verticalView = VerticalCommandBarView(self)
        self.verticalView.addAction(self._createAction("新建", FluentIcon.ADD))
        self.verticalView.addAction(self._createAction("打开", FluentIcon.FOLDER))
        self.verticalView.addAction(self._createAction("保存", FluentIcon.SAVE))
        self.verticalView.addSeparator()
        self.verticalView.addAction(self._createAction("剪切", FluentIcon.CUT))
        self.verticalView.addAction(self._createAction("复制", FluentIcon.COPY))
        self.verticalView.addAction(self._createAction("粘贴", FluentIcon.PASTE))
        
        self.verticalView.resizeToSuitableHeight()
        mainLayout.addWidget(self.verticalView)

    def _createResponsiveSection(self, mainLayout):
        """创建响应式命令栏视图测试"""
        sectionLabel = QLabel("<h2>2. ResponsiveCommandBarView - 响应式命令栏视图</h2>")
        mainLayout.addWidget(sectionLabel)
        
        infoLabel = QLabel("<b>自动布局的响应式命令栏，可开关响应式模式</b><br>"
                           "<font color='gray'>提示：调整窗口大小可以看到按钮自动隐藏到'更多'菜单</font>")
        mainLayout.addWidget(infoLabel)
        
        self.responsiveView = ResponsiveCommandBarView(self)
        self.responsiveView.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        # 添加多个动作测试响应式
        actions = [
            ("新建文件", FluentIcon.ADD),
            ("打开", FluentIcon.FOLDER),
            ("保存", FluentIcon.SAVE),
            ("另存为", FluentIcon.SAVE_AS),
            ("打印", FluentIcon.PRINT),
            ("导出", FluentIcon.DOWNLOAD),
            ("导入", FluentIcon.UPDATE),
            ("分享", FluentIcon.SHARE),
            ("设置", FluentIcon.SETTING),
            ("帮助", FluentIcon.HELP),
        ]
        
        for text, icon in actions:
            self.responsiveView.addAction(self._createAction(text, icon))
            if text in ["保存", "导出", "分享"]:
                self.responsiveView.addSeparator()
        
        # 不设置固定宽度，让响应式布局生效
        # self.responsiveView.resizeToSuitableWidth()
        mainLayout.addWidget(self.responsiveView)

    def _createMovableSection(self, mainLayout):
        """创建可拖动命令栏视图测试"""
        sectionLabel = QLabel("<h2>3. MovableCommandBarView - 可拖动命令栏视图</h2>")
        mainLayout.addWidget(sectionLabel)
        
        infoLabel = QLabel("<b>自动布局的可拖动命令栏，支持停靠到上下左右</b><br>"
                           "<font color='gray'>提示：调整窗口大小可以测试响应式布局效果</font>")
        mainLayout.addWidget(infoLabel)
        
        self.movableView = MovableCommandBarView(self)
        self.movableView.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        # 添加停靠控制动作
        self.movableView.addAction(self._createAction("顶部", FluentIcon.UP))
        self.movableView.addAction(self._createAction("底部", FluentIcon.DOWN))
        self.movableView.addAction(self._createAction("左侧", FluentIcon.LEFT_ARROW))
        self.movableView.addAction(self._createAction("右侧", FluentIcon.RIGHT_ARROW))
        self.movableView.addSeparator()
        self.movableView.addAction(self._createAction("操作", FluentIcon.ACCEPT))
        
        # 不设置固定宽度，让响应式布局生效
        # self.movableView.resizeToSuitableWidth()
        mainLayout.addWidget(self.movableView)

    def _createAction(self, text: str, icon):
        """创建动作"""
        action = QAction(icon.icon(), text, self)
        action.setToolTip(text)
        return action


def main():
    """运行测试应用"""
    app = QApplication(sys.argv)
    
    window = CommandBarViewsTest()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
