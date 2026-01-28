# coding:utf-8
import sys
import os

# Add parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget

from qfluentwidgets import (NavigationItemPosition, TopNavigationBar,
                            FluentIcon as FIF)


class SimpleTestWindow(QWidget):
    """ Simple test window for TopNavigationBar """

    def __init__(self):
        super().__init__()
        
        # Create layouts
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        
        # Create top navigation bar WITH return button
        self.navigationBar = TopNavigationBar(self, showReturnButton=True)
        
        # Create content label
        self.contentLabel = QLabel('Content Area', self)
        self.contentLabel.setAlignment(Qt.AlignCenter)
        self.contentLabel.setStyleSheet('QLabel { font-size: 24px; padding: 50px; }')
        
        # Add widgets
        self.vBoxLayout.addWidget(self.navigationBar)
        self.vBoxLayout.addWidget(self.contentLabel)
        
        # Add navigation items
        self.navigationBar.addItem('home', FIF.HOME, 'Home', 
                                  position=NavigationItemPosition.TOP)
        self.navigationBar.addItem('search', FIF.SEARCH, 'Search',
                                  position=NavigationItemPosition.SCROLL)
        self.navigationBar.addItem('settings', FIF.SETTING, 'Settings',
                                  position=NavigationItemPosition.BOTTOM)
        
        self.navigationBar.setCurrentItem('home')
        
        # Set window properties
        self.resize(1000, 600)
        self.setWindowTitle('TopNavigationBar - Simple Example with Return Button')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SimpleTestWindow()
    w.show()
    sys.exit(app.exec())
