# coding:utf-8
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea
from PySide6.QtGui import QColor

from qfluentwidgets import (FluentIcon, setTheme, Theme, setThemeColor, isDarkTheme)
from qfluentwidgets.components.widgets.tool_panel_views import (
    VerticalToolPanelView, HorizontalToolPanelView, 
    ScrollableToolPanelView, ResponsiveToolPanelView
)


class ToolPanelViewsDemo(QWidget):
    """ Tool panel views demo - 工具面板视图封装演示 """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('ToolPanel Views Demo - 工具面板视图封装演示')
        self.resize(1200, 1000)
        
        # Set theme
        setTheme(Theme.AUTO)
        setThemeColor(QColor(0, 159, 170))
        
        # Create main layout
        mainLayout = QVBoxLayout(self)
        mainLayout.setContentsMargins(20, 20, 20, 20)
        mainLayout.setSpacing(20)
        
        # Create different panel views
        self._createVerticalPanelView(mainLayout)
        self._createHorizontalPanelView(mainLayout)
        self._createScrollablePanelView(mainLayout)
        self._createResponsivePanelView(mainLayout)
        
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
        
    def _createVerticalPanelView(self, parentLayout):
        """ Create vertical tool panel view """
        container = QWidget()
        layout = QVBoxLayout(container)
        
        title = QLabel('Vertical Tool Panel View (竖直工具面板视图)')
        title.setStyleSheet('font-size: 16px; font-weight: bold; margin: 10px 0;')
        layout.addWidget(title)
        
        panelView = VerticalToolPanelView(container)
        
        tools = [
            {
                'icon': FluentIcon.MOVE,
                'name': 'Move Tool',
                'tooltip': 'Move Tool (V)',
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
                'tooltip': 'Zoom Tool (Z)',
                'shortcut': 'Z',
            },
            {
                'icon': FluentIcon.BRUSH,
                'name': 'Brush Tool',
                'tooltip': 'Brush Tool (B)',
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
                'tooltip': 'Eraser Tool (E)',
                'shortcut': 'E',
            },
        ]
        
        panelView.addTools(tools)
        panelView.addSeparator()
        
        more_tools = [
            {
                'icon': FluentIcon.PALETTE,
                'name': 'Gradient Tool',
                'tooltip': 'Gradient Tool (G)',
                'shortcut': 'G',
            },
            {
                'icon': FluentIcon.TRANSPARENT,
                'name': 'Paint Bucket',
                'tooltip': 'Paint Bucket Tool (K)',
                'shortcut': 'K',
            },
            {
                'icon': FluentIcon.EMOJI_TAB_SYMBOLS,
                'name': 'Shape Tool',
                'tooltip': 'Shape Tool (U)',
                'shortcut': 'U',
            },
        ]
        
        panelView.addTools(more_tools)
        panelView.resizeToSuitableHeight()
        panelView.toolChanged.connect(lambda btn: self._onToolClicked(btn, "Vertical Panel View"))
        
        layout.addWidget(panelView)
        parentLayout.addWidget(container)
        
    def _createHorizontalPanelView(self, parentLayout):
        """ Create horizontal tool panel view """
        container = QWidget()
        layout = QVBoxLayout(container)
        
        title = QLabel('Horizontal Tool Panel View (水平工具面板视图)')
        title.setStyleSheet('font-size: 16px; font-weight: bold; margin: 10px 0;')
        layout.addWidget(title)
        
        panelView = HorizontalToolPanelView(container)
        
        # Icon only tools
        icon_tools = [
            {'icon': FluentIcon.SAVE, 'name': 'Save', 'tooltip': 'Save File (Ctrl+S)'},
            {'icon': FluentIcon.FOLDER, 'name': 'Open', 'tooltip': 'Open File (Ctrl+O)'},
            {'icon': FluentIcon.CUT, 'name': 'Cut', 'tooltip': 'Cut (Ctrl+X)'},
            {'icon': FluentIcon.COPY, 'name': 'Copy', 'tooltip': 'Copy (Ctrl+C)'},
            {'icon': FluentIcon.PASTE, 'name': 'Paste', 'tooltip': 'Paste (Ctrl+V)'},
        ]
        
        panelView.addTools(icon_tools)
        panelView.addSeparator()
        
        # Text beside icon tools
        panelView.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        text_tools = [
            {'icon': FluentIcon.CANCEL, 'name': 'Undo', 'tooltip': 'Undo (Ctrl+Z)'},
            {'icon': FluentIcon.RETURN, 'name': 'Redo', 'tooltip': 'Redo (Ctrl+Y)'},
        ]
        
        panelView.addTools(text_tools)
        panelView.resizeToSuitableWidth()
        panelView.toolClicked.connect(lambda btn: self._onToolClicked(btn, "Horizontal Panel View"))
        
        layout.addWidget(panelView)
        parentLayout.addWidget(container)
        
    def _createScrollablePanelView(self, parentLayout):
        """ Create scrollable tool panel view """
        container = QWidget()
        layout = QVBoxLayout(container)
        
        title = QLabel('Scrollable Tool Panel View (可滚动工具面板视图)')
        title.setStyleSheet('font-size: 16px; font-weight: bold; margin: 10px 0;')
        layout.addWidget(title)
        
        # Create vertical scrollable panel
        panelView = ScrollableToolPanelView(Qt.Vertical, container)
        
        # Add many tools to test scrolling
        tools = []
        for i in range(30):
            tools.append({
                'icon': FluentIcon.SAVE,
                'name': f'Tool {i+1}',
                'tooltip': f'Tool {i+1} description',
                'shortcut': f'Ctrl+{i+1}',
            })
            
        panelView.addTools(tools)
        panelView.setButtonTight(False)
        
        # 强制更新滚动尺寸
        panelView.resizeToSuitableSize()
        
        # 直接强制更新面板和滚动区域
        panelView.panel.resizeToSuitableHeight()
        panelView.scrollArea.widget().resize(panelView.panel.sizeHint())
        
        # 设置滚动区域的固定尺寸（可选）
        panelView.scrollArea.setFixedHeight(500)  # 设置滚动区域高度为200px
        panelView.scrollArea.setFixedWidth(100)  # 设置滚动区域宽度为100px
        
        panelView.toolClicked.connect(lambda btn: self._onToolClicked(btn, "Scrollable Panel View"))
        
        layout.addWidget(panelView)
        parentLayout.addWidget(container)
        
    def _createResponsivePanelView(self, parentLayout):
        """ Create responsive tool panel view """
        container = QWidget()
        layout = QVBoxLayout(container)
        
        title = QLabel('Responsive Tool Panel View (响应式工具面板视图)')
        title.setStyleSheet('font-size: 16px; font-weight: bold; margin: 10px 0;')
        layout.addWidget(title)
        
        # Create horizontal responsive panel
        panelView = ResponsiveToolPanelView(Qt.Horizontal, container)
        
        tools = [
            {'icon': FluentIcon.SAVE, 'name': 'Save', 'tooltip': 'Save File (Ctrl+S)'},
            {'icon': FluentIcon.FOLDER, 'name': 'Open', 'tooltip': 'Open File (Ctrl+O)'},
            {'icon': FluentIcon.CUT, 'name': 'Cut', 'tooltip': 'Cut (Ctrl+X)'},
            {'icon': FluentIcon.COPY, 'name': 'Copy', 'tooltip': 'Copy (Ctrl+C)'},
            {'icon': FluentIcon.PASTE, 'name': 'Paste', 'tooltip': 'Paste (Ctrl+V)'},
            {'icon': FluentIcon.CANCEL, 'name': 'Undo', 'tooltip': 'Undo (Ctrl+Z)'},
            {'icon': FluentIcon.RETURN, 'name': 'Redo', 'tooltip': 'Redo (Ctrl+Y)'},
            {'icon': FluentIcon.SETTING, 'name': 'Settings', 'tooltip': 'Settings'},
            {'icon': FluentIcon.DOWNLOAD, 'name': 'Download', 'tooltip': 'Download'},
            {'icon': FluentIcon.CLOUD, 'name': 'Upload', 'tooltip': 'Upload'},
            {'icon': FluentIcon.ZOOM, 'name': 'Zoom', 'tooltip': 'Zoom'},
            {'icon': FluentIcon.BRUSH, 'name': 'Brush', 'tooltip': 'Brush'},
            {'icon': FluentIcon.EDIT, 'name': 'Edit', 'tooltip': 'Edit'},
            {'icon': FluentIcon.PALETTE, 'name': 'Palette', 'tooltip': 'Palette'},
            {'icon': FluentIcon.TRANSPARENT, 'name': 'Fill', 'tooltip': 'Fill'},
        ]
        
        panelView.addTools(tools)
        panelView.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        panelView.setButtonTight(False)
        panelView.toolClicked.connect(lambda btn: self._onToolClicked(btn, "Responsive Panel View"))
        
        layout.addWidget(panelView)
        parentLayout.addWidget(container)
        
    def _onToolClicked(self, button, panelType):
        """ Handle tool click with detailed info """
        data = button.toolData()
        
        info = f"<h3>{panelType}</h3>"
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
    demo = ToolPanelViewsDemo()
    demo.show()
    sys.exit(app.exec())
