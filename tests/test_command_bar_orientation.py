# coding:utf-8
"""
CommandBar orientation and movable feature test
Tests for horizontal/vertical CommandBar, ResponsiveCommandBar, and MovableCommandBar
"""
import sys
from pathlib import Path

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel

# Add project root to path
sys.path.insert(0, str(Path(__file__).parents[1]))

from qfluentwidgets import (
    CommandBar, VerticalCommandBar, ResponsiveCommandBar, MovableCommandBar,
    DockPosition, FluentIcon, setTheme, Theme
)


class CommandBarTestWindow(QWidget):
    """Test window for CommandBar orientation features"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CommandBar Orientation Test")
        self.setGeometry(100, 100, 1000, 700)
        
        # Set theme
        setTheme(Theme.LIGHT)
        
        # Create main layout
        mainLayout = QVBoxLayout(self)
        mainLayout.setSpacing(20)
        mainLayout.setContentsMargins(20, 20, 20, 20)
        
        # Test 1: Horizontal CommandBar (default)
        mainLayout.addWidget(QLabel("<b>1. Horizontal CommandBar (Default)</b>"))
        self.horizontalBar = self._createHorizontalCommandBar()
        mainLayout.addWidget(self.horizontalBar)
        
        # Test 2: Vertical CommandBar
        horizontalSection = QHBoxLayout()
        
        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(QLabel("<b>2. Vertical CommandBar</b>"))
        self.verticalBar = self._createVerticalCommandBar()
        verticalLayout.addWidget(self.verticalBar)
        
        horizontalSection.addLayout(verticalLayout)
        
        # Test 3: Dynamic orientation switch
        dynamicLayout = QVBoxLayout()
        dynamicLayout.addWidget(QLabel("<b>3. Dynamic Orientation Switch</b>"))
        self.dynamicBar = self._createDynamicCommandBar()
        dynamicLayout.addWidget(self.dynamicBar)
        horizontalSection.addLayout(dynamicLayout)
        
        mainLayout.addLayout(horizontalSection)
        
        # Test 4: Responsive CommandBar
        mainLayout.addWidget(QLabel("<b>4. Responsive CommandBar (resize window to test)</b>"))
        self.responsiveBar = self._createResponsiveCommandBar()
        mainLayout.addWidget(self.responsiveBar)
        
        # Test 5: Movable CommandBar
        mainLayout.addWidget(QLabel("<b>5. Movable CommandBar (drag to move and dock)</b>"))
        self.movableBar = self._createMovableCommandBar()
        mainLayout.addWidget(self.movableBar)
        
        mainLayout.addStretch(1)

    def _createHorizontalCommandBar(self):
        """Create horizontal CommandBar"""
        bar = CommandBar(self)
        bar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        # Add actions
        bar.addAction(self._createAction("New", FluentIcon.ADD))
        bar.addAction(self._createAction("Open", FluentIcon.FOLDER))
        bar.addAction(self._createAction("Save", FluentIcon.SAVE))
        bar.addSeparator()
        bar.addAction(self._createAction("Cut", FluentIcon.CUT))
        bar.addAction(self._createAction("Copy", FluentIcon.COPY))
        bar.addAction(self._createAction("Paste", FluentIcon.PASTE))
        bar.addSeparator()
        bar.addAction(self._createAction("Undo", FluentIcon.CANCEL))
        bar.addAction(self._createAction("Redo", FluentIcon.RETURN))
        
        bar.resizeToSuitableWidth()
        return bar

    def _createVerticalCommandBar(self):
        """Create vertical CommandBar"""
        bar = VerticalCommandBar(self)
        bar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        
        # Add actions
        bar.addAction(self._createAction("Home", FluentIcon.HOME))
        bar.addAction(self._createAction("Search", FluentIcon.SEARCH))
        bar.addAction(self._createAction("Mail", FluentIcon.MAIL))
        bar.addSeparator()
        bar.addAction(self._createAction("Settings", FluentIcon.SETTING))
        bar.addAction(self._createAction("Info", FluentIcon.INFO))
        
        bar.resizeToSuitableHeight()
        return bar

    def _createDynamicCommandBar(self):
        """Create CommandBar with dynamic orientation switch"""
        bar = CommandBar(self)
        bar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        # Add actions
        bar.addAction(self._createAction("Edit", FluentIcon.EDIT))
        bar.addAction(self._createAction("Delete", FluentIcon.DELETE))
        bar.addSeparator()
        
        # Add orientation switch action
        switchAction = QAction(FluentIcon.ROTATE.icon(), "Switch Orientation", self)
        switchAction.triggered.connect(lambda: self._switchOrientation(bar))
        bar.addAction(switchAction)
        
        bar.resizeToSuitableWidth()
        return bar

    def _switchOrientation(self, bar: CommandBar):
        """Switch CommandBar orientation"""
        if bar.orientation() == Qt.Horizontal:
            bar.setOrientation(Qt.Vertical)
            bar.resizeToSuitableHeight()
        else:
            bar.setOrientation(Qt.Horizontal)
            bar.resizeToSuitableWidth()

    def _createResponsiveCommandBar(self):
        """Create responsive CommandBar"""
        bar = ResponsiveCommandBar(self)
        bar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        # Add many actions to test responsive behavior
        bar.addAction(self._createAction("File", FluentIcon.FOLDER))
        bar.addAction(self._createAction("Edit", FluentIcon.EDIT))
        bar.addAction(self._createAction("View", FluentIcon.VIEW))
        bar.addAction(self._createAction("Format", FluentIcon.PALETTE))
        bar.addSeparator()
        bar.addAction(self._createAction("Insert", FluentIcon.ADD))
        bar.addAction(self._createAction("Tools", FluentIcon.SETTING))
        bar.addAction(self._createAction("Help", FluentIcon.HELP))
        bar.addSeparator()
        bar.addAction(self._createAction("Share", FluentIcon.SHARE))
        bar.addAction(self._createAction("Print", FluentIcon.PRINT))
        bar.addAction(self._createAction("Export", FluentIcon.DOWNLOAD))
        
        # Add some hidden actions
        bar.addHiddenAction(self._createAction("Hidden 1", FluentIcon.CALENDAR))
        bar.addHiddenAction(self._createAction("Hidden 2", FluentIcon.CHECKBOX))
        
        bar.resizeToSuitableWidth()
        return bar

    def _createMovableCommandBar(self):
        """Create movable CommandBar"""
        bar = MovableCommandBar(self)
        bar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        # Add actions
        bar.addAction(self._createAction("Top", FluentIcon.UP))
        bar.addAction(self._createAction("Bottom", FluentIcon.DOWN))
        bar.addAction(self._createAction("Left", FluentIcon.LEFT_ARROW))
        bar.addAction(self._createAction("Right", FluentIcon.RIGHT_ARROW))
        bar.addSeparator()
        
        # Add dock position actions
        topAction = QAction(FluentIcon.UP.icon(), "Dock Top", self)
        topAction.triggered.connect(lambda: bar.setDockPosition(DockPosition.TOP))
        bar.addAction(topAction)
        
        leftAction = QAction(FluentIcon.LEFT_ARROW.icon(), "Dock Left", self)
        leftAction.triggered.connect(lambda: bar.setDockPosition(DockPosition.LEFT))
        bar.addAction(leftAction)
        
        bar.resizeToSuitableWidth()
        return bar

    def _createAction(self, text: str, icon: FluentIcon):
        """Create QAction with icon and text"""
        action = QAction(icon.icon(), text, self)
        action.setToolTip(text)
        return action


def main():
    """Run the test application"""
    app = QApplication(sys.argv)
    
    # Create and show test window
    window = CommandBarTestWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
