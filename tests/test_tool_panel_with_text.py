# coding:utf-8
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea
from PySide6.QtGui import QColor

from qfluentwidgets import (ToolPanel, VerticalToolPanel, FluentIcon, setTheme, Theme,
                             setThemeColor, isDarkTheme)
from qfluentwidgets.common.style_sheet import FluentStyleSheet


class TextToolPanelDemo(QWidget):
    """ Tool panel demo with text display testing """
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ToolPanel Text Display Demo')
        self.resize(1000, 700)
        
        # Set theme
        setTheme(Theme.AUTO)
        setThemeColor(QColor(0, 159, 170))
        
        # Create main layout
        mainLayout = QVBoxLayout(self)
        mainLayout.setContentsMargins(20, 20, 20, 20)
        mainLayout.setSpacing(20)
        
        # Create different tool panel configurations
        self._createIconOnlyPanel(mainLayout)
        self._createTextBesideIconPanel(mainLayout)
        self._createTextUnderIconPanel(mainLayout)
        self._createTextOnlyPanel(mainLayout)
        self._createMixedStylePanel(mainLayout)
        
        # Create info area
        self.infoLabel = QLabel('Select a tool to see detailed info here')
        self.infoLabel.setAlignment(Qt.AlignCenter)
        self.infoLabel.setMinimumSize(400, 100)
        self.infoLabel.setStyleSheet(
            f'background-color: {"#2b2b2b" if isDarkTheme() else "#f5f5f5"}; '
            f'color: {"white" if isDarkTheme() else "black"}; '
            'border-radius: 8px; font-size: 14px; padding: 20px;'
        )
        mainLayout.addWidget(self.infoLabel)
        
    def _createIconOnlyPanel(self, parentLayout):
        """ Create icon-only tool panel """
        container = QWidget()
        layout = QVBoxLayout(container)
        
        title = QLabel('Icon Only Panel (Qt.ToolButtonIconOnly)')
        title.setStyleSheet('font-size: 16px; font-weight: bold; margin: 10px 0;')
        layout.addWidget(title)
        
        panel = ToolPanel(container)
        panel.setOrientation(Qt.Horizontal)
        panel.setToolButtonStyle(Qt.ToolButtonIconOnly)
        
        tools = [
            {'icon': FluentIcon.SAVE, 'name': 'Save', 'tooltip': 'Save File (Ctrl+S)'},
            {'icon': FluentIcon.FOLDER, 'name': 'Open', 'tooltip': 'Open File (Ctrl+O)'},
            {'icon': FluentIcon.CUT, 'name': 'Cut', 'tooltip': 'Cut (Ctrl+X)'},
            {'icon': FluentIcon.COPY, 'name': 'Copy', 'tooltip': 'Copy (Ctrl+C)'},
            {'icon': FluentIcon.PASTE, 'name': 'Paste', 'tooltip': 'Paste (Ctrl+V)'},
        ]
        
        panel.addTools(tools)
        panel.resizeToSuitableWidth()
        panel.toolClicked.connect(lambda btn: self._onToolClicked(btn, "Icon Only"))
        
        layout.addWidget(panel)
        parentLayout.addWidget(container)
        
    def _createTextBesideIconPanel(self, parentLayout):
        """ Create text beside icon tool panel """
        container = QWidget()
        layout = QVBoxLayout(container)
        
        title = QLabel('Text Beside Icon Panel (Qt.ToolButtonTextBesideIcon)')
        title.setStyleSheet('font-size: 16px; font-weight: bold; margin: 10px 0;')
        layout.addWidget(title)
        
        panel = ToolPanel(container)
        panel.setOrientation(Qt.Horizontal)
        panel.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        tools = [
            {'icon': FluentIcon.SAVE, 'name': 'Save', 'tooltip': 'Save File (Ctrl+S)'},
            {'icon': FluentIcon.FOLDER, 'name': 'Open', 'tooltip': 'Open File (Ctrl+O)'},
            {'icon': FluentIcon.CUT, 'name': 'Cut', 'tooltip': 'Cut (Ctrl+X)'},
            {'icon': FluentIcon.COPY, 'name': 'Copy', 'tooltip': 'Copy (Ctrl+C)'},
            {'icon': FluentIcon.PASTE, 'name': 'Paste', 'tooltip': 'Paste (Ctrl+V)'},
        ]
        
        panel.addTools(tools)
        panel.resizeToSuitableWidth()
        panel.toolClicked.connect(lambda btn: self._onToolClicked(btn, "Text Beside Icon"))
        
        layout.addWidget(panel)
        parentLayout.addWidget(container)
        
    def _createTextUnderIconPanel(self, parentLayout):
        """ Create text under icon tool panel """
        container = QWidget()
        layout = QVBoxLayout(container)
        
        title = QLabel('Text Under Icon Panel (Qt.ToolButtonTextUnderIcon)')
        title.setStyleSheet('font-size: 16px; font-weight: bold; margin: 10px 0;')
        layout.addWidget(title)
        
        panel = ToolPanel(container)
        panel.setOrientation(Qt.Horizontal)
        panel.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        
        tools = [
            {'icon': FluentIcon.SAVE, 'name': 'Save', 'tooltip': 'Save File (Ctrl+S)'},
            {'icon': FluentIcon.FOLDER, 'name': 'Open', 'tooltip': 'Open File (Ctrl+O)'},
            {'icon': FluentIcon.CUT, 'name': 'Cut', 'tooltip': 'Cut (Ctrl+X)'},
            {'icon': FluentIcon.COPY, 'name': 'Copy', 'tooltip': 'Copy (Ctrl+C)'},
            {'icon': FluentIcon.PASTE, 'name': 'Paste', 'tooltip': 'Paste (Ctrl+V)'},
        ]
        
        panel.addTools(tools)
        panel.resizeToSuitableWidth()
        panel.toolClicked.connect(lambda btn: self._onToolClicked(btn, "Text Under Icon"))
        
        layout.addWidget(panel)
        parentLayout.addWidget(container)
        
    def _createTextOnlyPanel(self, parentLayout):
        """ Create text only tool panel """
        container = QWidget()
        layout = QVBoxLayout(container)
        
        title = QLabel('Text Only Panel (Qt.ToolButtonTextOnly)')
        title.setStyleSheet('font-size: 16px; font-weight: bold; margin: 10px 0;')
        layout.addWidget(title)
        
        panel = ToolPanel(container)
        panel.setOrientation(Qt.Horizontal)
        panel.setToolButtonStyle(Qt.ToolButtonTextOnly)
        
        tools = [
            {'icon': FluentIcon.SAVE, 'name': 'Save', 'tooltip': 'Save File (Ctrl+S)'},
            {'icon': FluentIcon.FOLDER, 'name': 'Open', 'tooltip': 'Open File (Ctrl+O)'},
            {'icon': FluentIcon.CUT, 'name': 'Cut', 'tooltip': 'Cut (Ctrl+X)'},
            {'icon': FluentIcon.COPY, 'name': 'Copy', 'tooltip': 'Copy (Ctrl+C)'},
            {'icon': FluentIcon.PASTE, 'name': 'Paste', 'tooltip': 'Paste (Ctrl+V)'},
        ]
        
        panel.addTools(tools)
        panel.resizeToSuitableWidth()
        panel.toolClicked.connect(lambda btn: self._onToolClicked(btn, "Text Only"))
        
        layout.addWidget(panel)
        parentLayout.addWidget(container)
        
    def _createMixedStylePanel(self, parentLayout):
        """ Create mixed style tool panel """
        container = QWidget()
        layout = QVBoxLayout(container)
        
        title = QLabel('Mixed Style Panel (Icon Only + Text Beside Icon)')
        title.setStyleSheet('font-size: 16px; font-weight: bold; margin: 10px 0;')
        layout.addWidget(title)
        
        panel = ToolPanel(container)
        panel.setOrientation(Qt.Horizontal)
        
        # Add icon-only tools first
        icon_tools = [
            {'icon': FluentIcon.SAVE, 'name': 'Save', 'tooltip': 'Save File (Ctrl+S)'},
            {'icon': FluentIcon.FOLDER, 'name': 'Open', 'tooltip': 'Open File (Ctrl+O)'},
        ]
        panel.addTools(icon_tools)
        panel.addSeparator()
        
        # Then add text beside icon tools
        panel.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        text_tools = [
            {'icon': FluentIcon.CUT, 'name': 'Cut', 'tooltip': 'Cut (Ctrl+X)'},
            {'icon': FluentIcon.COPY, 'name': 'Copy', 'tooltip': 'Copy (Ctrl+C)'},
            {'icon': FluentIcon.PASTE, 'name': 'Paste', 'tooltip': 'Paste (Ctrl+V)'},
        ]
        panel.addTools(text_tools)
        
        panel.resizeToSuitableWidth()
        panel.toolClicked.connect(lambda btn: self._onToolClicked(btn, "Mixed Style"))
        
        layout.addWidget(panel)
        parentLayout.addWidget(container)
        
    def _onToolClicked(self, button, panelType):
        """ Handle tool click with detailed info """
        data = button.toolData()
        
        info = f"<h3>{panelType} Panel</h3>"
        info += f"<p><b>Tool Name:</b> {data.get('name', 'Unknown')}</p>"
        info += f"<p><b>Tooltip:</b> {data.get('tooltip', 'No tooltip')}</p>"
        info += f"<p><b>Shortcut:</b> {data.get('shortcut', 'None')}</p>"
        info += f"<p><b>Button Style:</b> {button.toolButtonStyle()}</p>"
        info += f"<p><b>Is Icon Only:</b> {button.isIconOnly()}</p>"
        info += f"<p><b>Button Size:</b> {button.size().width()} x {button.size().height()}</p>"
        info += f"<p><b>Size Hint:</b> {button.sizeHint().width()} x {button.sizeHint().height()}</p>"
        
        # Show sub-option info if available
        if button.subOptions():
            info += f"<p><b>Sub-Options:</b> {len(button.subOptions())} available</p>"
            current = button.currentSubOption()
            if current:
                info += f"<p><b>Current Sub-Option:</b> {current.get('name', 'Unknown')}</p>"
                
        self.infoLabel.setText(info)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = TextToolPanelDemo()
    demo.show()
    sys.exit(app.exec())
