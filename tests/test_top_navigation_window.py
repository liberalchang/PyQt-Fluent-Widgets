# coding:utf-8
import sys
import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QIcon

# Add parent directory to sys.path to import qfluentwidgets
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from qfluentwidgets import (TopNavigationFluentWindow, FluentIcon as FIF, 
                             setTheme, Theme, NavigationItemPosition)


class ContentWidget(QWidget):
    """ Content widget """

    def __init__(self, title: str, parent=None):
        super().__init__(parent)
        self.titleLabel = QLabel(title, self)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.setContentsMargins(30, 30, 30, 30)
        
        # Set stylesheet
        self.titleLabel.setStyleSheet("""
            QLabel {
                font-size: 32px;
                font-weight: bold;
                color: #333;
            }
        """)
        
        self.setStyleSheet("ContentWidget { background-color: white; }")


class TopNavigationWindow(TopNavigationFluentWindow):
    """ Top navigation window """

    def __init__(self, showReturnButton=True):
        super().__init__(showReturnButton=showReturnButton)
        
        # Create sub interfaces
        self.homeInterface = ContentWidget('Home Interface', self)
        self.musicInterface = ContentWidget('Music Interface', self)
        self.videoInterface = ContentWidget('Video Interface', self)
        self.folderInterface = ContentWidget('Folder Interface', self)
        self.settingInterface = ContentWidget('Setting Interface', self)
        
        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        # Set object names (must match route keys)
        self.homeInterface.setObjectName('home')
        self.musicInterface.setObjectName('music')
        self.videoInterface.setObjectName('video')
        self.folderInterface.setObjectName('folder')
        self.settingInterface.setObjectName('settings')

        # Add sub interfaces to navigation
        self.addSubInterface(
            self.homeInterface, 
            FIF.HOME, 
            'Home',
            position=NavigationItemPosition.SCROLL
        )
        
        self.addSubInterface(
            self.musicInterface,
            FIF.MUSIC,
            'Music',
            position=NavigationItemPosition.SCROLL
        )
        
        self.addSubInterface(
            self.videoInterface,
            FIF.VIDEO,
            'Video',
            position=NavigationItemPosition.SCROLL
        )
        
        self.addSubInterface(
            self.folderInterface,
            FIF.FOLDER,
            'Folder',
            position=NavigationItemPosition.SCROLL
        )
        
        self.addSubInterface(
            self.settingInterface,
            FIF.SETTING,
            'Settings',
            position=NavigationItemPosition.BOTTOM
        )

    def initWindow(self):
        self.resize(1000, 700)
        self.setWindowTitle('TopNavigationFluentWindow Demo')
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        
        # Center window on screen
        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)


class SimpleTopNavigationWindow(TopNavigationFluentWindow):
    """ Simple top navigation window without return button """

    def __init__(self):
        super().__init__(showReturnButton=False)
        
        # Create sub interfaces
        self.homeInterface = ContentWidget('Home', self)
        self.appInterface = ContentWidget('Apps', self)
        self.gameInterface = ContentWidget('Games', self)
        
        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        # Set object names
        self.homeInterface.setObjectName('home')
        self.appInterface.setObjectName('apps')
        self.gameInterface.setObjectName('games')

        # Add sub interfaces
        self.addSubInterface(self.homeInterface, FIF.HOME, 'Home')
        self.addSubInterface(self.appInterface, FIF.APPLICATION, 'Apps')
        self.addSubInterface(self.gameInterface, FIF.GAME, 'Games')
        
        # Set responsive width for better UX
        self.setResponsiveWidth(800, 1200)

    def initWindow(self):
        self.resize(900, 650)
        self.setWindowTitle('Simple TopNavigationFluentWindow')
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        
        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)


if __name__ == '__main__':
    # Enable DPI scaling (AA_EnableHighDpiScaling and AA_UseHighDpiPixmaps are deprecated in PySide6)
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    
    # Set theme
    setTheme(Theme.LIGHT)
    
    # Show window with return button
    w1 = TopNavigationWindow(showReturnButton=True)
    w1.show()
    
    # Show simple window without return button
    # w2 = SimpleTopNavigationWindow()
    # w2.show()

    sys.exit(app.exec())
