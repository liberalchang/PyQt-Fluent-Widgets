# coding:utf-8
import sys
import os

# Add parent directory to sys.path to import qfluentwidgets
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QVBoxLayout, QLabel, QFrame, QWidget, QStackedWidget

from qfluentwidgets import (NavigationItemPosition, TopNavigationBar,
                            FluentIcon as FIF, themeColor, qrouter)


class ContentWidget(QFrame):
    """ Content widget for each navigation item """

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = QLabel(text, self)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.label.setStyleSheet(f"""
            QLabel {{
                font-size: 32px;
                font-weight: bold;
                color: {themeColor().name()};
            }}
        """)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.label, 0, Qt.AlignCenter)
        
        self.setObjectName(text.replace(' ', '-'))
        self.setStyleSheet("ContentWidget { background: transparent; }")


class TestWindow(QWidget):
    """ Test window for TopNavigationBar """

    def __init__(self, showReturnButton=False):
        super().__init__()
        
        # Create layouts
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)
        
        # Create top navigation bar (with optional return button)
        self.navigationBar = TopNavigationBar(self, showReturnButton=showReturnButton)
        
        # Create stacked widget for content switching
        self.stackedWidget = QStackedWidget(self)
        
        # Bind stacked widget to navigation bar for router support
        self.navigationBar.setStackedWidget(self.stackedWidget)
        
        # Create content widgets
        self.homeInterface = ContentWidget('Home Interface', self)
        self.searchInterface = ContentWidget('Search Interface', self)
        self.musicInterface = ContentWidget('Music Interface', self)
        self.videoInterface = ContentWidget('Video Interface', self)
        self.folderInterface = ContentWidget('Folder Interface', self)
        self.settingInterface = ContentWidget('Setting Interface', self)
        
        # Set object names for router (IMPORTANT!)
        self.homeInterface.setObjectName('home')
        self.searchInterface.setObjectName('search')
        self.musicInterface.setObjectName('music')
        self.videoInterface.setObjectName('video')
        self.folderInterface.setObjectName('folder')
        self.settingInterface.setObjectName('settings')
        
        # Add interfaces to stacked widget
        self.stackedWidget.addWidget(self.homeInterface)
        self.stackedWidget.addWidget(self.searchInterface)
        self.stackedWidget.addWidget(self.musicInterface)
        self.stackedWidget.addWidget(self.videoInterface)
        self.stackedWidget.addWidget(self.folderInterface)
        self.stackedWidget.addWidget(self.settingInterface)
        
        # Initialize navigation
        self.initNavigation()
        
        # Add widgets to main layout
        self.vBoxLayout.addWidget(self.navigationBar)
        self.vBoxLayout.addWidget(self.stackedWidget)
        
        # Connect stacked widget signal to update navigation selection
        self.stackedWidget.currentChanged.connect(self._onCurrentInterfaceChanged)
        
        # Set window properties
        self.resize(1000, 600)
        title = 'TopNavigationBar Test'
        if showReturnButton:
            title += ' (With Return Button)'
        else:
            title += ' (No Return Button)'
        self.setWindowTitle(title)
        
        # Add status info to home interface
        returnBtnInfo = '\n   • Return button: ' + ('enabled (try navigating and clicking back button)' if showReturnButton else 'disabled')
        infoLabel = QLabel(self.homeInterface)
        infoLabel.setText('💡 Test Features:\n'
                          '   • Width < 800px: Show icons only\n'
                          '   • Width ≥ 1200px: Show icons and text'
                          + returnBtnInfo)
        infoLabel.setStyleSheet("""
            QLabel {
                background: rgba(0, 120, 215, 20);
                padding: 10px;
                border-radius: 5px;
                color: palette(text);
            }
        """)
        self.homeInterface.layout().insertWidget(0, infoLabel)

    def _onCurrentInterfaceChanged(self, index: int):
        """ Update navigation selection when stacked widget changes """
        widget = self.stackedWidget.widget(index)
        if widget:
            routeKey = widget.objectName()
            # Only update navigation bar if it's different from current
            if routeKey in self.navigationBar.items and routeKey != self.navigationBar._currentRouteKey:
                # Temporarily disconnect to avoid recursion
                self.stackedWidget.currentChanged.disconnect(self._onCurrentInterfaceChanged)
                self.navigationBar.setCurrentItem(routeKey)
                self.stackedWidget.currentChanged.connect(self._onCurrentInterfaceChanged)

    def initNavigation(self):
        """ Initialize navigation items """
        # Set custom selected color (theme color)
        self.navigationBar.setSelectedColor(themeColor(), themeColor())
        
        # Add items to left section
        self.navigationBar.addItem(
            routeKey='home',
            icon=FIF.HOME,
            text='Home',
            onClick=lambda: self.switchTo(self.homeInterface),
            position=NavigationItemPosition.TOP
        )
        
        # Add items to scroll section (main navigation)
        self.navigationBar.addItem(
            routeKey='search',
            icon=FIF.SEARCH,
            text='Search',
            onClick=lambda: self.switchTo(self.searchInterface),
            position=NavigationItemPosition.SCROLL
        )
        
        self.navigationBar.addItem(
            routeKey='music',
            icon=FIF.MUSIC,
            text='Music',
            onClick=lambda: self.switchTo(self.musicInterface),
            position=NavigationItemPosition.SCROLL
        )
        
        self.navigationBar.addItem(
            routeKey='video',
            icon=FIF.VIDEO,
            text='Video',
            onClick=lambda: self.switchTo(self.videoInterface),
            position=NavigationItemPosition.SCROLL
        )
        
        self.navigationBar.addItem(
            routeKey='folder',
            icon=FIF.FOLDER,
            text='Folder',
            onClick=lambda: self.switchTo(self.folderInterface),
            position=NavigationItemPosition.SCROLL
        )
        
        # Add items to right section
        self.navigationBar.addItem(
            routeKey='settings',
            icon=FIF.SETTING,
            text='Settings',
            onClick=lambda: self.switchTo(self.settingInterface),
            position=NavigationItemPosition.BOTTOM
        )
        
        # Set initial selected item and default route
        qrouter.setDefaultRouteKey(self.stackedWidget, 'home')
        self.navigationBar.setCurrentItem('home')
        self.stackedWidget.setCurrentWidget(self.homeInterface)
    
    def switchTo(self, widget):
        """ Switch content area to show different interface """
        self.stackedWidget.setCurrentWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Test 1: Without return button (default)
    w1 = TestWindow(showReturnButton=False)
    w1.move(100, 100)
    w1.show()
    
    # Test 2: With return button
    w2 = TestWindow(showReturnButton=True)
    w2.move(150, 150)
    w2.show()
    
    sys.exit(app.exec())
