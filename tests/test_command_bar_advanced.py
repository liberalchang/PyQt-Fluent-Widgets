# coding:utf-8
"""
Advanced CommandBar test - comprehensive feature demonstration
Tests all CommandBar variants and features including orientation, responsive, and movable
"""
import sys
from pathlib import Path

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea

sys.path.insert(0, str(Path(__file__).parents[1]))

from qfluentwidgets import (
    CommandBar, VerticalCommandBar, ResponsiveCommandBar, MovableCommandBar,
    DockPosition, FluentIcon, setTheme, Theme, PrimaryPushButton
)


class AdvancedCommandBarTest(QWidget):
    """Advanced test for all CommandBar features"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced CommandBar Feature Test")
        self.setGeometry(100, 100, 1200, 600)
        self.setStyleSheet("background-color: white;")
        
        setTheme(Theme.LIGHT)
        
        # 创建滚动区域
        scrollArea = QScrollArea(self)
        scrollArea.setWidgetResizable(True)
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
        # 创建内容容器
        contentWidget = QWidget()
        mainLayout = QVBoxLayout(contentWidget)
        mainLayout.setSpacing(30)
        mainLayout.setContentsMargins(30, 30, 30, 30)
        
        # 设置滚动区域的内容
        scrollArea.setWidget(contentWidget)
        
        # 主布局
        rootLayout = QVBoxLayout(self)
        rootLayout.setContentsMargins(0, 0, 0, 0)
        rootLayout.addWidget(scrollArea)
        
        # Title
        titleLabel = QLabel("<h1>CommandBar Advanced Features Test</h1>")
        mainLayout.addWidget(titleLabel)
        
        # Section 1: Orientation Control
        self._createOrientationSection(mainLayout)
        
        # Section 2: Responsive Behavior
        self._createResponsiveSection(mainLayout)
        
        # Section 3: Movable and Docking
        self._createMovableSection(mainLayout)
        
        mainLayout.addStretch(1)

    def _createOrientationSection(self, mainLayout):
        """Create orientation control test section"""
        sectionLabel = QLabel("<h2>1. Orientation Control</h2>")
        mainLayout.addWidget(sectionLabel)
        
        # Horizontal bar
        horizLabel = QLabel("<b>Horizontal CommandBar:</b>")
        mainLayout.addWidget(horizLabel)
        
        self.horizontalBar = CommandBar(self)
        self.horizontalBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self._populateBar(self.horizontalBar)
        self.horizontalBar.resizeToSuitableWidth()
        mainLayout.addWidget(self.horizontalBar)
        
        # Vertical bar in horizontal layout
        testLayout = QHBoxLayout()
        
        vertLabel = QLabel("<b>Vertical CommandBar:</b>")
        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(vertLabel)
        
        self.verticalBar = VerticalCommandBar(self)
        self.verticalBar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self._populateBar(self.verticalBar)
        self.verticalBar.resizeToSuitableHeight()
        verticalLayout.addWidget(self.verticalBar)
        verticalLayout.addStretch(1)
        
        testLayout.addLayout(verticalLayout)
        
        # Dynamic orientation bar
        dynamicLayout = QVBoxLayout()
        dynLabel = QLabel("<b>Dynamic Orientation (click button to switch):</b>")
        dynamicLayout.addWidget(dynLabel)
        
        self.dynamicBar = CommandBar(self)
        self.dynamicBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self._populateBar(self.dynamicBar)
        self.dynamicBar.resizeToSuitableWidth()
        dynamicLayout.addWidget(self.dynamicBar)
        
        switchBtn = PrimaryPushButton("Switch Orientation", self)
        switchBtn.clicked.connect(self._onSwitchOrientation)
        dynamicLayout.addWidget(switchBtn)
        dynamicLayout.addStretch(1)
        
        testLayout.addLayout(dynamicLayout)
        testLayout.addStretch(1)
        
        mainLayout.addLayout(testLayout)

    def _createResponsiveSection(self, mainLayout):
        """Create responsive behavior test section"""
        sectionLabel = QLabel("<h2>2. Responsive Behavior</h2>")
        mainLayout.addWidget(sectionLabel)
        
        infoLabel = QLabel(
            "<b>Resize the window to see buttons hide automatically and appear in 'More' menu</b><br>"
            "This CommandBar has many actions to test responsive behavior."
        )
        mainLayout.addWidget(infoLabel)
        
        self.responsiveBar = ResponsiveCommandBar(self)
        self.responsiveBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # 强制设置为响应式模式
        self.responsiveBar.setResponsive(True)
        
        # Add many actions
        actions = [
            ("New File", FluentIcon.ADD),
            ("Open", FluentIcon.FOLDER),
            ("Save", FluentIcon.SAVE),
            ("Save As", FluentIcon.SAVE_AS),
            ("Print", FluentIcon.PRINT),
            ("Export", FluentIcon.DOWNLOAD),
            ("Import", FluentIcon.UPDATE),
            ("Share", FluentIcon.SHARE),
            ("Settings", FluentIcon.SETTING),
            ("Help", FluentIcon.HELP),
            ("About", FluentIcon.INFO),
        ]
        
        for i, (text, icon) in enumerate(actions):
            self.responsiveBar.addAction(self._createAction(text, icon))
            if i in [2, 5, 8]:  # Add separators
                self.responsiveBar.addSeparator()
        
        # Add hidden actions
        self.responsiveBar.addHiddenAction(self._createAction("Hidden Action 1", FluentIcon.CALENDAR))
        self.responsiveBar.addHiddenAction(self._createAction("Hidden Action 2", FluentIcon.CHECKBOX))
        
        # 不设置固定宽度，让响应式布局生效
        # self.responsiveBar.resizeToSuitableWidth()
        mainLayout.addWidget(self.responsiveBar)
        
        # 显示当前响应式状态
        statusLabel = QLabel(f"<b>Responsive Mode: {self.responsiveBar.isResponsive()}</b>")
        mainLayout.addWidget(statusLabel)

    def _createMovableSection(self, mainLayout):
        """Create movable and docking test section"""
        sectionLabel = QLabel("<h2>3. Movable and Docking</h2>")
        mainLayout.addWidget(sectionLabel)
        
        infoLabel = QLabel(
            "<b>拖动左侧（水平）或上方（竖直）的拖动区域来移动和停靠CommandBar</b><br>"
            "• <b>拖动区域</b>：水平时在左侧，竖直时在上方，有明显的拖动点标识<br>"
            "• <b>智能停靠</b>：先切换方向再停靠，避免按钮折叠问题<br>"
            "• <b>自由浮动</b>：可以停靠到上下左右，也可以自由放置在任意位置<br>"
            "• <b>停靠预览</b>：拖动时接近边缘会显示蓝色预览区域"
        )
        mainLayout.addWidget(infoLabel)
        
        # Create container for movable bar
        containerWidget = QWidget(self)
        containerWidget.setStyleSheet("background-color: #f0f0f0; border: 2px solid #ccc;")
        containerWidget.setFixedSize(600, 400)  # 设置固定尺寸，确保有足够空间
        
        self.movableBar = MovableCommandBar(containerWidget)
        self.movableBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        # Add dock control actions
        self.movableBar.addAction(self._createAction("Top", FluentIcon.UP, 
                                   lambda: self.movableBar.setDockPosition(DockPosition.TOP)))
        self.movableBar.addAction(self._createAction("Bottom", FluentIcon.DOWN,
                                   lambda: self.movableBar.setDockPosition(DockPosition.BOTTOM)))
        self.movableBar.addAction(self._createAction("Left", FluentIcon.LEFT_ARROW,
                                   lambda: self.movableBar.setDockPosition(DockPosition.LEFT)))
        self.movableBar.addAction(self._createAction("Right", FluentIcon.RIGHT_ARROW,
                                   lambda: self.movableBar.setDockPosition(DockPosition.RIGHT)))
        self.movableBar.addSeparator()
        self.movableBar.addAction(self._createAction("Action", FluentIcon.ACCEPT))
        
        # 设置初始尺寸和位置，确保有足够空间显示
        self.movableBar.resizeToSuitableWidth()
        self.movableBar.move(10, 10)
        
        # 强制更新布局以确保拖动区域正确显示
        self.movableBar.updateGeometry()
        
        mainLayout.addWidget(containerWidget)

    def _populateBar(self, bar: CommandBar):
        """Populate a CommandBar with standard actions"""
        bar.addAction(self._createAction("New", FluentIcon.ADD))
        bar.addAction(self._createAction("Open", FluentIcon.FOLDER))
        bar.addAction(self._createAction("Save", FluentIcon.SAVE))
        bar.addSeparator()
        bar.addAction(self._createAction("Cut", FluentIcon.CUT))
        bar.addAction(self._createAction("Copy", FluentIcon.COPY))
        bar.addAction(self._createAction("Paste", FluentIcon.PASTE))

    def _createAction(self, text: str, icon: FluentIcon, callback=None):
        """Create QAction with icon and text"""
        action = QAction(icon.icon(), text, self)
        action.setToolTip(text)
        if callback:
            action.triggered.connect(callback)
        return action

    def _onSwitchOrientation(self):
        """Switch orientation of dynamic bar"""
        bar = self.dynamicBar
        if bar.orientation() == Qt.Horizontal:
            bar.setOrientation(Qt.Vertical)
            bar.resizeToSuitableHeight()
        else:
            bar.setOrientation(Qt.Horizontal)
            bar.resizeToSuitableWidth()


def main():
    """Run the advanced test application"""
    app = QApplication(sys.argv)
    
    window = AdvancedCommandBarTest()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
