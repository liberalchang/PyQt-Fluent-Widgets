import sys
import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel
from PySide6.QtGui import QColor

# Insert the package path to ensure we use the local version
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from qfluentwidgets import FluentWindow, SubtitleLabel, PrimaryPushButton, Slider, ComboBox, qconfig, WindowEffect, setTheme, Theme

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("TestFluentStyles")

class TestWindow(FluentWindow):
    def __init__(self):
        super().__init__(showReturnButton=False)
        logger.info("TestWindow initializing...")
        self.setWindowTitle("Fluent Style Test")
        self.resize(1200, 600)

        self.mainWidget = QWidget()
        self.mainWidget.setObjectName("test")
        self.addSubInterface(self.mainWidget, "test", "Test")

        self.vBoxLayout = QVBoxLayout(self.mainWidget)
        
        self.label = SubtitleLabel("Window Style Test", self)
        self.vBoxLayout.addWidget(self.label, 0, Qt.AlignCenter)

        # Window Effect Config
        self.effectLabel = QLabel("Window Effect (Restart to apply)", self)
        self.vBoxLayout.addWidget(self.effectLabel, 0, Qt.AlignCenter)

        self.effectComboBox = ComboBox(self)
        self.effectComboBox.addItems([e.value for e in WindowEffect])
        self.effectComboBox.setCurrentText(qconfig.get(qconfig.windowEffect).value)
        self.effectComboBox.currentTextChanged.connect(self.onEffectChanged)
        self.vBoxLayout.addWidget(self.effectComboBox, 0, Qt.AlignCenter)

        # Style Buttons
        self.btnMica = PrimaryPushButton("Enable Mica", self)
        self.btnMica.clicked.connect(self.enableMica)
        self.vBoxLayout.addWidget(self.btnMica, 0, Qt.AlignCenter)

        self.btnAcrylic = PrimaryPushButton("Enable Acrylic", self)
        self.btnAcrylic.clicked.connect(self.enableAcrylic)
        self.vBoxLayout.addWidget(self.btnAcrylic, 0, Qt.AlignCenter)

        self.btnDisable = PrimaryPushButton("Disable Effects", self)
        self.btnDisable.clicked.connect(self.disableEffects)
        self.vBoxLayout.addWidget(self.btnDisable, 0, Qt.AlignCenter)

        # Color Buttons
        self.btnTitleBarColor = PrimaryPushButton("Set Title Label Red", self)
        self.btnTitleBarColor.clicked.connect(lambda: self.setWindowTitleBarColor(QColor(255, 0, 0)))
        self.vBoxLayout.addWidget(self.btnTitleBarColor, 0, Qt.AlignCenter)

        self.btnTitleBarBgColor = PrimaryPushButton("Set Title Bar Bg Cyan", self)
        self.btnTitleBarBgColor.clicked.connect(lambda: self.setTitleBarBackgroundColor(QColor(0, 255, 255)))
        self.vBoxLayout.addWidget(self.btnTitleBarBgColor, 0, Qt.AlignCenter)

        self.btnTitleTextColor = PrimaryPushButton("Set Title Text Blue", self)
        self.btnTitleTextColor.clicked.connect(lambda: self.setWindowTitleColor(QColor(0, 0, 255)))
        self.vBoxLayout.addWidget(self.btnTitleTextColor, 0, Qt.AlignCenter)
        
        self.btnBorderColor = PrimaryPushButton("Set Border Green", self)
        self.btnBorderColor.clicked.connect(lambda: self.setWindowBorderColor(QColor(0, 255, 0)))
        self.vBoxLayout.addWidget(self.btnBorderColor, 0, Qt.AlignCenter)

        # Acrylic Opacity Slider
        self.acrylicOpacityLabel = QLabel("Acrylic Opacity: 0.6", self)
        self.vBoxLayout.addWidget(self.acrylicOpacityLabel, 0, Qt.AlignCenter)
        
        self.acrylicSlider = Slider(Qt.Horizontal, self)
        self.acrylicSlider.setRange(0, 100)
        self.acrylicSlider.setValue(60)
        self.acrylicSlider.setFixedWidth(200)
        self.acrylicSlider.valueChanged.connect(self.updateAcrylicOpacity)
        self.vBoxLayout.addWidget(self.acrylicSlider, 0, Qt.AlignCenter)

        # Opacity Slider
        self.opacityLabel = QLabel("Button Opacity: 1.0", self)
        self.vBoxLayout.addWidget(self.opacityLabel, 0, Qt.AlignCenter)
        
        self.slider = Slider(Qt.Horizontal, self)
        self.slider.setRange(0, 100)
        self.slider.setValue(100)
        self.slider.setFixedWidth(200)
        self.slider.valueChanged.connect(self.updateOpacity)
        self.vBoxLayout.addWidget(self.slider, 0, Qt.AlignCenter)

    def onEffectChanged(self, text):
        effect = WindowEffect(text)
        qconfig.set(qconfig.windowEffect, effect, save=False)
        self.effectLabel.setText("Window Effect (Restart to apply) - Temporary")

    def enableMica(self):
        logger.info("Enabling Mica")
        self.setMicaEffectEnabled(True)

    def enableAcrylic(self):
        logger.info("Enabling Acrylic")
        self.setAcrylicEffectEnabled(True)

    def disableEffects(self):
        logger.info("Disabling Effects")
        self.setMicaEffectEnabled(False)
        self.setAcrylicEffectEnabled(False)

    def updateAcrylicOpacity(self, value):
        opacity = value / 100.0
        self.acrylicOpacityLabel.setText(f"Acrylic Opacity: {opacity:.2f}")
        self.setAcrylicOpacity(opacity)

    def updateOpacity(self, value):
        opacity = value / 100.0
        self.opacityLabel.setText(f"Button Opacity: {opacity:.2f}")
        self.setWidgetOpacity(self.btnMica, opacity)

if __name__ == '__main__':
    # 1. 设置颜色主题 / Set Color Theme (Theme.LIGHT, Theme.DARK, Theme.AUTO)
    setTheme(Theme.LIGHT, save=False)
    # setTheme(Theme.DARK, save=False)

    # 2. 设置窗口特效 / Set Window Effect
    # WindowEffect.MICA    : 云母效果 / Mica Effect (Win11 only)
    # WindowEffect.ACRYLIC : 亚克力效果 / Acrylic Effect (Win10/Win11)
    # WindowEffect.DISABLE : 普通纯色背景 / Normal Solid Background
    # qconfig.set(qconfig.windowEffect, WindowEffect.MICA, save=False)
    qconfig.set(qconfig.windowEffect, WindowEffect.ACRYLIC, save=False)
    # qconfig.set(qconfig.windowEffect, WindowEffect.DISABLE, save=False)
    
    app = QApplication(sys.argv)
    w = TestWindow()
    w.show()
    sys.exit(app.exec())
