# coding: utf-8
import sys
import os

# Ensure the package is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from qfluentwidgets import FluentWindow, NavigationItemPosition
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets.components.vispy import DrawingView

class Window(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drawing View Test")
        self.resize(1200, 800)
        
        self.drawingInterface = DrawingView(self)
        self.drawingInterface.setObjectName('drawingInterface')
        self.addSubInterface(self.drawingInterface, FIF.EDIT, 'Drawing', NavigationItemPosition.TOP)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
