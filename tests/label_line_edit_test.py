# coding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout



import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from qfluentwidgets import LabelLineEdit, setTheme, Theme

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(50, 50, 50, 50)
        self.setWindowTitle("LabelLineEdit Demo")

        self.lineEdit1 = LabelLineEdit(self)
        self.lineEdit1.setLabel("Label")
        self.lineEdit1.setText("Content")
        self.layout().addWidget(self.lineEdit1)

        self.lineEdit2 = LabelLineEdit(self)
        self.lineEdit2.setPrefix("Prefix")
        self.lineEdit2.setText("Content with prefix")
        self.layout().addWidget(self.lineEdit2)

        self.lineEdit3 = LabelLineEdit(self)
        self.lineEdit3.setSuffix("Suffix")
        self.lineEdit3.setText("Content with suffix")
        self.layout().addWidget(self.lineEdit3)
        
        self.lineEdit4 = LabelLineEdit(self)
        self.lineEdit4.setPrefix("KG")
        self.lineEdit4.setSuffix("Unit")
        self.lineEdit4.setText("Weight")
        self.layout().addWidget(self.lineEdit4)

if __name__ == '__main__':
    # Enable high DPI scaling
    # QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    # QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    setTheme(Theme.LIGHT)
    
    w = Demo()
    w.show()
    
    sys.exit(app.exec())
