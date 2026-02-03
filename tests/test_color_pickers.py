# coding:utf-8
import sys
import os

# Add parent directory to sys.path to import qfluentwidgets
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

from qfluentwidgets import (ColorDialog, DropDownColorPalette, CircleColorPicker, 
                           ScreenColorPicker, FluentIcon as FIF, setTheme, Theme, 
                           setThemeColor, PrimaryPushButton, ToggleButton, ColorButton,
                           ColorDialogButton, CircleColorButton, ScreenColorButton,
                           SingleDirectionScrollArea)

class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setWindowTitle('Color Pickers Test')
        
        # Main layout containing the scroll area
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        
        # Scroll Area
        self.scrollArea = SingleDirectionScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet("QScrollArea{border: none; background: transparent}")
        self.mainLayout.addWidget(self.scrollArea)
        
        # Scroll Widget (content container)
        self.scrollWidget = QWidget()
        self.scrollArea.setWidget(self.scrollWidget)
        
        self.vBoxLayout = QVBoxLayout(self.scrollWidget)
        self.vBoxLayout.setContentsMargins(20, 20, 20, 20)
        self.vBoxLayout.setSpacing(20)

        # 1. Screen Color Picker
        self.addSection("Screen Color Picker")
        self.screenPicker = ScreenColorPicker(parent=self.scrollWidget)
        self.vBoxLayout.addWidget(self.screenPicker)
        
        # 2. Circle Color Picker
        self.addSection("Circle Color Picker")
        self.circlePicker = CircleColorPicker(
            [QColor("#009FAA"), QColor("#FF0000"), QColor("#00FF00"), QColor("#0000FF")],
            self.scrollWidget
        )
        self.vBoxLayout.addWidget(self.circlePicker)
        
        # 3. Drop Down Color Palette (Standard Icon)
        self.addSection("DropDown Color Palette (Standard)")
        self.paletteBtn = DropDownColorPalette(FIF.PALETTE, self.scrollWidget)
        self.vBoxLayout.addWidget(self.paletteBtn)
        
        # 4. Drop Down Color Palette (Custom Icon)
        self.addSection("DropDown Color Palette (Custom Icon)")
        # Create a custom icon (just using another standard one for demo)
        self.customPaletteBtn = DropDownColorPalette(FIF.BRUSH, self.scrollWidget) 
        self.vBoxLayout.addWidget(self.customPaletteBtn)

        # 5. Color Dialog
        self.addSection("Color Dialog")
        self.dialogBtn = PrimaryPushButton("Open Color Dialog", self.scrollWidget)
        self.dialogBtn.clicked.connect(self.showColorDialog)
        self.vBoxLayout.addWidget(self.dialogBtn)

        # 6. Universal Color Button (Integrates All)
        self.addSection("Universal Color Button (Integrates All)")

        description = QLabel(
            "This component integrates:\n"
            "1. Screen Color Picker (Top)\n"
            "2. Theme & Standard Colors\n"
            "3. Custom Colors (CircleColorPicker)\n"
            "4. More Colors (ColorDialog)", 
            self.scrollWidget
        )
        description.setStyleSheet("color: gray; font-size: 12px; margin-bottom: 5px;")
        self.vBoxLayout.addWidget(description)
        
        # Format 1: Color Preview + Icon
        self.btn1 = ColorButton(QColor("#009FAA"), "Color + Icon", self.scrollWidget, icon=FIF.EDIT)
        self.vBoxLayout.addWidget(self.btn1)
        
        # Format 2: Color Preview + Chevron (Icon=None)
        self.btn2 = ColorButton(QColor("#FF0000"), "Color + Chevron", self.scrollWidget)
        self.vBoxLayout.addWidget(self.btn2)
        
        # Format 3: Icon + Chevron + Color Strip (Implicit via paintEvent?)
        # Currently our implementation draws Icon if present, Preview if requested.
        # To get Icon + Chevron (no preview square), we set showPreview=False
        self.btn3 = ColorButton(QColor("#00FF00"), "Icon + Chevron", self.scrollWidget, icon=FIF.BRUSH, showPreview=False)
        self.vBoxLayout.addWidget(self.btn3)

        # 7. Dropdown Component Variants
        self.addSection("Dropdown Component Variants")

        # ColorDialog Dropdown
        self.btnDialog = ColorDialogButton(QColor("#FF00FF"), "Color Dialog Dropdown", self.scrollWidget)
        self.vBoxLayout.addWidget(self.btnDialog)

        # CircleColorPicker Dropdown
        self.btnCircle = CircleColorButton(
            QColor("#00FFFF"), 
            "Circle Picker Dropdown", 
            self.scrollWidget,
            customColors=[QColor("#009FAA"), QColor("#FF0000"), QColor("#00FF00"), QColor("#0000FF")]
        )
        self.vBoxLayout.addWidget(self.btnCircle)

        # ScreenColorPicker Dropdown
        self.btnScreen = ScreenColorButton(QColor("#FFFF00"), "Screen Picker Dropdown", self.scrollWidget)
        self.vBoxLayout.addWidget(self.btnScreen)

        # Theme Toggle
        self.addSection("Theme Control")
        self.themeBtn = ToggleButton("Toggle Theme", self.scrollWidget)
        self.themeBtn.clicked.connect(self.toggleTheme)
        self.vBoxLayout.addWidget(self.themeBtn)

        self.vBoxLayout.addStretch(1)
        
        # Connect signals
        self.screenPicker.colorChanged.connect(lambda c: print(f"Screen Picker: {c.name()}"))
        self.circlePicker.colorChanged.connect(lambda c: print(f"Circle Picker: {c.name()}"))
        self.paletteBtn.colorSelected.connect(lambda c: print(f"Palette Selected: {c.name()}"))
        self.customPaletteBtn.colorSelected.connect(lambda c: print(f"Custom Palette Selected: {c.name()}"))
        self.btnDialog.colorChanged.connect(lambda c: print(f"Dialog Dropdown Selected: {c.name()}"))
        self.btnCircle.colorChanged.connect(lambda c: print(f"Circle Dropdown Selected: {c.name()}"))
        self.btnScreen.colorChanged.connect(lambda c: print(f"Screen Dropdown Selected: {c.name()}"))

    def addSection(self, title):
        label = QLabel(title, self.scrollWidget)
        label.setStyleSheet("font-size: 16px; font-weight: bold; margin-top: 10px;")
        self.vBoxLayout.addWidget(label)

    def showColorDialog(self):
        w = ColorDialog(QColor("#009FAA"), "Select Color", self)
        w.colorChanged.connect(lambda c: print(f"Dialog Selected: {c.name()}"))
        w.exec()

    def toggleTheme(self):
        if self.themeBtn.isChecked():
            setTheme(Theme.DARK)
        else:
            setTheme(Theme.LIGHT)

if __name__ == '__main__':
    # Enable high DPI scaling
    # QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    # QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    # QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    sys.exit(app.exec())
