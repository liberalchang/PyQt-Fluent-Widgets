# coding:utf-8
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtGui import QColor

from qfluentwidgets import (ToolPanel, VerticalToolPanel, FluentIcon, setTheme, Theme,
                             setThemeColor, isDarkTheme)
from qfluentwidgets.common.style_sheet import FluentStyleSheet


class ToolPanelDemo(QWidget):
    """ Tool panel demo window """
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ToolPanel Demo - Photoshop Style Toolbox')
        self.resize(900, 700)
        
        # Set theme
        setTheme(Theme.AUTO)
        setThemeColor(QColor(0, 159, 170))
        
        # Create main layout
        mainLayout = QHBoxLayout(self)
        mainLayout.setContentsMargins(20, 20, 20, 20)
        mainLayout.setSpacing(20)
        
        # Create left vertical tool panel
        self.leftPanel = self._createLeftPanel()
        mainLayout.addWidget(self.leftPanel, 0, Qt.AlignLeft | Qt.AlignTop)
        
        # Create center area
        centerLayout = QVBoxLayout()
        
        # Create top horizontal tool panel
        self.topPanel = self._createTopPanel()
        centerLayout.addWidget(self.topPanel, 0, Qt.AlignTop)
        
        # Create info label
        self.infoLabel = QLabel('Select a tool to see info here')
        self.infoLabel.setAlignment(Qt.AlignCenter)
        self.infoLabel.setMinimumSize(400, 300)
        self.infoLabel.setStyleSheet(
            f'background-color: {"#2b2b2b" if isDarkTheme() else "#f5f5f5"}; '
            f'color: {"white" if isDarkTheme() else "black"}; '
            'border-radius: 8px; font-size: 14px; padding: 20px;'
        )
        centerLayout.addWidget(self.infoLabel, 1)
        
        mainLayout.addLayout(centerLayout, 1)
        
        # Apply styles
        FluentStyleSheet.TOOL_PANEL.apply(self.leftPanel)
        FluentStyleSheet.TOOL_PANEL.apply(self.topPanel)
        
    def _createLeftPanel(self):
        """ Create left vertical tool panel (like Photoshop tools) """
        panel = VerticalToolPanel(self)
        
        # Define tools data
        tools = [
            {
                'icon': FluentIcon.MOVE,
                'name': 'Move Tool',
                'tooltip': 'Move Tool',
                'checked': True,
                'shortcut': 'V',
                'subOptions': [
                    {'icon': FluentIcon.MOVE, 'name': 'Move Tool', 'checked': True},
                    {'icon': FluentIcon.ALIGNMENT, 'name': 'Artboard Tool', 'checked': False},
                ]
            },
            {
                'icon': FluentIcon.ZOOM,
                'name': 'Zoom Tool',
                'tooltip': 'Zoom Tool',
                'shortcut': 'Z',
            },
            {
                'icon': FluentIcon.BRUSH,
                'name': 'Brush Tool',
                'tooltip': 'Brush Tool',
                'shortcut': 'B',
                'subOptions': [
                    {'icon': FluentIcon.BRUSH, 'name': 'Brush Tool', 'checked': True},
                    {'icon': FluentIcon.PENCIL_INK, 'name': 'Pencil Tool', 'checked': False},
                    {'icon': FluentIcon.MIX_VOLUMES, 'name': 'Color Replacement Tool', 'checked': False},
                ]
            },
            {
                'icon': FluentIcon.EDIT,
                'name': 'Eraser Tool',
                'tooltip': 'Eraser Tool',
                'shortcut': 'E',
                'subOptions': [
                    {'icon': FluentIcon.EDIT, 'name': 'Eraser Tool', 'checked': True},
                    {'icon': FluentIcon.BASKETBALL, 'name': 'Background Eraser', 'checked': False},
                    {'icon': FluentIcon.CANCEL_MEDIUM, 'name': 'Magic Eraser', 'checked': False},
                ]
            },
        ]
        
        panel.addTools(tools)
        panel.addSeparator()
        
        # Add more tools
        more_tools = [
            {
                'icon': FluentIcon.PALETTE,
                'name': 'Gradient Tool',
                'tooltip': 'Gradient Tool',
                'shortcut': 'G',
            },
            {
                'icon': FluentIcon.TRANSPARENT,
                'name': 'Paint Bucket',
                'tooltip': 'Paint Bucket Tool',
                'shortcut': 'K',
            },
            {
                'icon': FluentIcon.EMOJI_TAB_SYMBOLS,
                'name': 'Shape Tool',
                'tooltip': 'Shape Tool',
                'shortcut': 'U',
            },
        ]
        
        panel.addTools(more_tools)
        
        # Connect signals
        panel.toolChanged.connect(self._onToolChanged)
        
        # Resize to suitable height
        panel.resizeToSuitableHeight()
        
        return panel
        
    def _createTopPanel(self):
        """ Create top horizontal tool panel """
        panel = ToolPanel(self)
        panel.setOrientation(Qt.Horizontal)
        
        # Define tools
        tools = [
            {
                'icon': FluentIcon.SAVE,
                'name': 'Save',
                'tooltip': 'Save File',
                'shortcut': 'Ctrl+S',
            },
            {
                'icon': FluentIcon.FOLDER,
                'name': 'Open',
                'tooltip': 'Open File',
                'shortcut': 'Ctrl+O',
            },
            {
                'icon': FluentIcon.CUT,
                'name': 'Cut',
                'tooltip': 'Cut',
                'shortcut': 'Ctrl+X',
            },
            {
                'icon': FluentIcon.COPY,
                'name': 'Copy',
                'tooltip': 'Copy',
                'shortcut': 'Ctrl+C',
            },
            {
                'icon': FluentIcon.PASTE,
                'name': 'Paste',
                'tooltip': 'Paste',
                'shortcut': 'Ctrl+V',
            },
        ]
        
        panel.addTools(tools)
        panel.addSeparator()
        
        # Add more tools with text
        # panel.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        more_tools = [
            {
                'icon': FluentIcon.CANCEL,
                'name': 'Undo',
                'tooltip': 'Undo',
                'shortcut': 'Ctrl+Z',
            },
            {
                'icon': FluentIcon.RETURN,
                'name': 'Redo',
                'tooltip': 'Redo',
                'shortcut': 'Ctrl+Y',
            },
        ]
        
        panel.addTools(more_tools)
        
        # Connect signals
        panel.toolClicked.connect(self._onTopToolClicked)
        
        # Resize to suitable width
        panel.resizeToSuitableWidth()
        
        return panel
        
    def _onToolChanged(self, button):
        """ Handle tool changed """
        data = button.toolData()
        name = data.get('name', 'Unknown')
        shortcut = data.get('shortcut', 'None')
        
        info = f"<h3>{name}</h3>"
        info += f"<p><b>Shortcut:</b> {shortcut}</p>"
        
        # Show sub-option info
        if button.subOptions():
            current = button.currentSubOption()
            if current:
                info += f"<p><b>Current Sub-Option:</b> {current.get('name', 'Unknown')}</p>"
                info += f"<p><b>Sub-Options Count:</b> {len(button.subOptions())}</p>"
                info += "<ul>"
                for opt in button.subOptions():
                    marker = "✓" if opt.get('checked') else "○"
                    info += f"<li>{marker} {opt.get('name', 'Unknown')}</li>"
                info += "</ul>"
                
        info += "<p><i>Right-click or long-press to see sub-options</i></p>"
        
        self.infoLabel.setText(info)
        
    def _onTopToolClicked(self, button):
        """ Handle top tool clicked """
        data = button.toolData()
        name = data.get('name', 'Unknown')
        self.infoLabel.setText(f"<h3>Action: {name}</h3><p>Tool clicked!</p>")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ToolPanelDemo()
    demo.show()
    sys.exit(app.exec())
