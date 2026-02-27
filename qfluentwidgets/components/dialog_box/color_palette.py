# coding:utf-8
from typing import Union

from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtGui import QColor, QPainter, QIcon, QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QToolButton, QHBoxLayout, QPushButton

from ...common.icon import FluentIcon as FIF, toQIcon
from ...common.style_sheet import FluentStyleSheet, isDarkTheme
from ...components.widgets.button import TransparentToolButton
from ...components.widgets.flyout import Flyout, FlyoutViewBase, FlyoutAnimationType
from .color_dialog import ColorDialog
from .circle_color_picker import CircleColorPicker
from .screen_color_picker import ScreenColorPicker


class ColorSwatch(QToolButton):
    """ Color swatch """

    colorChanged = Signal(QColor)

    def __init__(self, color: QColor, parent=None):
        super().__init__(parent)
        self.setFixedSize(20, 20)
        self.color = QColor(color)
        self.setCursor(Qt.PointingHandCursor)
        self.setObjectName("colorSwatch")

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        
        # Draw background
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.color)
        
        rect = self.rect().adjusted(1, 1, -1, -1)
        painter.drawRoundedRect(rect, 2, 2)

        # Draw border
        if self.isDown():
            painter.setBrush(Qt.NoBrush)
            painter.setPen(QColor(0, 0, 0, 30))
            painter.drawRoundedRect(rect, 2, 2)
        elif self.underMouse():
            painter.setBrush(Qt.NoBrush)
            painter.setPen(QColor(0, 0, 0, 20) if not isDarkTheme() else QColor(255, 255, 255, 50))
            painter.drawRoundedRect(rect, 2, 2)
        else:
            # Draw subtle border for light colors in light theme
            if not isDarkTheme() and self.color.lightness() > 240:
                painter.setBrush(Qt.NoBrush)
                painter.setPen(QColor(0, 0, 0, 10))
                painter.drawRoundedRect(rect, 2, 2)

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.colorChanged.emit(self.color)


class PickerButton(QPushButton):
    """ Picker button """

    def __init__(self, icon: Union[QIcon, str, FIF], text: str, parent=None):
        super().__init__(parent)
        self.setText(text)
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedHeight(36)
        self.setIconSize(QSize(16, 16))
        self.setObjectName("pickerButton")
        
        if isinstance(icon, FIF):
            self.setIcon(icon.icon())
        else:
            self.setIcon(toQIcon(icon))


class ColorPalette(FlyoutViewBase):
    """ Color palette widget """

    colorSelected = Signal(QColor)
    customColorsChanged = Signal(list)

    def __init__(self, customColors=None, parent=None):
        super().__init__(parent)
        self.targetWindow = parent
        self.vBoxLayout = QVBoxLayout(self)
        
        # 0. Screen Color Picker
        self.screenColorPicker = ScreenColorPicker(parent=self)
        self.screenColorPicker.colorChanged.connect(self.colorSelected)
        
        # 1. Automatic Module
        self.autoButton = PickerButton(QIcon(), self.tr("Automatic"), self)
        self.autoButton.clicked.connect(self._onAutoColorClicked)
        
        self.setAutoColor(QColor(0, 0, 0))

        # 2. Theme Colors Module
        self.themeLabel = QLabel(self.tr("Theme Colors"), self)
        self.themeGrid = QGridLayout()
        self.themeGrid.setSpacing(4)
        self.themeGrid.setContentsMargins(0, 0, 0, 0)

        # 3. Standard Colors Module
        self.standardLabel = QLabel(self.tr("Standard Colors"), self)
        self.standardLayout = QHBoxLayout()
        self.standardLayout.setSpacing(4)
        self.standardLayout.setContentsMargins(0, 0, 0, 0)

        # 4. Custom Colors Module
        self.customLabel = QLabel(self.tr("Recent Colors"), self)
        self.circleColorPicker = CircleColorPicker(customColors, self)
        self.circleColorPicker.colorChanged.connect(self.colorSelected)
        self.circleColorPicker.addColorClicked.connect(self._onAddCustomColorClicked)
        self.circleColorPicker.colorsChanged.connect(self.customColorsChanged)

        # 5. More Colors Module
        self.moreButton = PickerButton(FIF.PALETTE, self.tr("More Colors..."), self)
        self.moreButton.clicked.connect(self._onMoreColorsClicked)

        self.__initLayout()
        self.__initColors()
        
        # Style
        self.themeLabel.setObjectName("sectionLabel")
        self.standardLabel.setObjectName("sectionLabel")
        self.customLabel.setObjectName("sectionLabel")
        FluentStyleSheet.COLOR_PALETTE.apply(self)

    def addWidget(self, widget, stretch=0, align=Qt.AlignLeft):
        # Implementation required by FlyoutViewBase, though we don't use it directly
        self.vBoxLayout.addWidget(widget, stretch, align)

    def __initLayout(self):
        self.vBoxLayout.setContentsMargins(4, 4, 4, 4)
        self.vBoxLayout.setSpacing(4)

        # Screen Picker
        screenContainer = QWidget(self)
        screenLayout = QHBoxLayout(screenContainer)
        screenLayout.setContentsMargins(10, 6, 10, 6)
        screenLayout.addWidget(self.screenColorPicker)
        self.vBoxLayout.addWidget(screenContainer)

        # Automatic
        self.vBoxLayout.addWidget(self.autoButton)
        
        # Theme Colors
        self.vBoxLayout.addWidget(self.themeLabel)
        
        themeContainer = QWidget(self)
        themeLayout = QVBoxLayout(themeContainer)
        themeLayout.setContentsMargins(10, 4, 10, 4)
        themeLayout.addLayout(self.themeGrid)
        self.vBoxLayout.addWidget(themeContainer)

        # Standard Colors
        self.vBoxLayout.addWidget(self.standardLabel)
        
        standardContainer = QWidget(self)
        standardLayout = QHBoxLayout(standardContainer)
        standardLayout.setContentsMargins(10, 4, 10, 4)
        standardLayout.addLayout(self.standardLayout)
        self.vBoxLayout.addWidget(standardContainer)
        
        # Custom Colors
        self.vBoxLayout.addWidget(self.customLabel)
        
        customContainer = QWidget(self)
        customLayout = QHBoxLayout(customContainer)
        customLayout.setContentsMargins(10, 4, 10, 4)
        customLayout.addWidget(self.circleColorPicker)
        self.vBoxLayout.addWidget(customContainer)
        
        self.vBoxLayout.addSpacing(4)
        
        # More Colors
        self.vBoxLayout.addWidget(self.moreButton)

    def _onAddCustomColorClicked(self):
        dialog = ColorDialog(self._autoColor, self.tr("Select Color"), self.targetWindow or self.window())
        if dialog.exec():
            try:
                self.circleColorPicker.addColor(dialog.color)
            except RuntimeError:
                # The widget might be deleted when the dialog is closed
                pass

    def __initColors(self):
        # Theme Colors Base
        baseColors = [
            "#FFFFFF", "#000000", "#E7E6E6", "#44546A", "#5B9BD5", 
            "#ED7D31", "#A5A5A5", "#FFC000", "#4472C4", "#70AD47"
        ]
        
        for col, hexColor in enumerate(baseColors):
            base = QColor(hexColor)
            
            def add(row, color):
                swatch = ColorSwatch(color, self)
                swatch.colorChanged.connect(self.colorSelected)
                self.themeGrid.addWidget(swatch, row, col)

            # Row 0: Lighter 80%
            add(0, self._adjustColor(base, 1.8))
            # Row 1: Lighter 60%
            add(1, self._adjustColor(base, 1.6))
            # Row 2: Lighter 40%
            add(2, self._adjustColor(base, 1.4))
            # Row 3: Base
            add(3, base)
            # Row 4: Darker 25%
            add(4, self._adjustColor(base, 0.75))
            # Row 5: Darker 50%
            add(5, self._adjustColor(base, 0.5))

        # Standard Colors
        standardColors = [
            "#C00000", "#FF0000", "#FFC000", "#FFFF00", "#92D050", 
            "#00B050", "#00B0F0", "#0070C0", "#002060", "#7030A0"
        ]
        
        for i, hexColor in enumerate(standardColors):
            swatch = ColorSwatch(QColor(hexColor), self)
            swatch.colorChanged.connect(self.colorSelected)
            self.standardLayout.addWidget(swatch)
            
        self.standardLayout.addStretch(1)

    def _adjustColor(self, color, factor):
        """ Adjust color brightness """
        # Simple implementation using hsv
        # Factor > 1 means lighter, < 1 means darker
        # But Qt's lighter/darker works differently.
        # lighter(150) -> 150% of current factor.
        
        if factor == 1:
            return color
            
        c = QColor(color)
        h, s, v, a = c.getHsv()
        
        if factor > 1:
            return c.lighter(int(factor * 100))
        else:
            return c.darker(int((1/factor) * 100))

    def setAutoColor(self, color: QColor):
        self._autoColor = QColor(color)
        
        pixmap = QPixmap(16, 16)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHints(QPainter.Antialiasing)
        
        painter.setBrush(self._autoColor)
        painter.setPen(QColor(0, 0, 0, 20))
        painter.drawRoundedRect(0, 0, 16, 16, 4, 4)
        painter.end()
        
        self.autoButton.setIcon(QIcon(pixmap))

    def _onAutoColorClicked(self):
        self.colorSelected.emit(self._autoColor)

    def _onMoreColorsClicked(self):
        dialog = ColorDialog(self._autoColor, self.tr("Select Color"), self.targetWindow or self.window())
        dialog.colorChanged.connect(self.colorSelected)
        dialog.exec()


class DropDownColorPalette(TransparentToolButton):
    """ Drop down color palette """

    colorSelected = Signal(QColor)

    def __init__(self, icon: Union[str, QIcon, FIF], parent=None):
        super().__init__(parent)
        self.setIcon(icon)
        self.clicked.connect(self.showFlyout)
        self.currentColor = QColor(Qt.black)
        self.customColors = []

    def showFlyout(self):
        palette = ColorPalette(self.customColors, self.window())
        palette.setAutoColor(self.currentColor)
        
        palette.colorSelected.connect(self._onColorSelected)
        palette.customColorsChanged.connect(self._onCustomColorsChanged)
        palette.colorSelected.connect(lambda: w.close())
        
        # Take over dialog handling to persist data if Flyout closes
        palette.circleColorPicker.addColorClicked.disconnect(palette._onAddCustomColorClicked)
        palette.circleColorPicker.addColorClicked.connect(self._openCustomColorDialog)
        
        palette.moreButton.clicked.disconnect(palette._onMoreColorsClicked)
        palette.moreButton.clicked.connect(self._openMoreColorsDialog)
        
        w = Flyout.make(palette, self, self.window(), FlyoutAnimationType.PULL_UP, True)

    def _openCustomColorDialog(self):
        dialog = ColorDialog(self.currentColor, self.tr("Select Color"), self.window())
        dialog.colorChanged.connect(self._onCustomColorAdded)
        dialog.exec()

    def _onCustomColorAdded(self, color):
        if color not in self.customColors:
            self.customColors.append(color)
            self._onCustomColorsChanged(self.customColors)

    def _openMoreColorsDialog(self):
        dialog = ColorDialog(self.currentColor, self.tr("Select Color"), self.window())
        dialog.colorChanged.connect(self._onColorSelected)
        dialog.exec()

    def _onColorSelected(self, color):
        self.currentColor = color
        self.colorSelected.emit(color)
        self.update()

    def _onCustomColorsChanged(self, colors):
        self.customColors = colors[:]

    def paintEvent(self, e):
        super().paintEvent(e)
        # Draw the color bar at the bottom of the icon
        if not self.icon().isNull():
            painter = QPainter(self)
            painter.setRenderHints(QPainter.Antialiasing)
            
            # Calculate position
            # Center of the button
            w = self.width()
            h = self.height()
            iconSize = self.iconSize()
            
            # Draw color strip
            painter.setPen(Qt.NoPen)
            painter.setBrush(self.currentColor)
            
            # Position: bottom of the icon
            rectWidth = iconSize.width() - 4
            rectHeight = 4
            x = (w - rectWidth) / 2
            y = (h + iconSize.height()) / 2 - 2
            
            painter.drawRoundedRect(x, y, rectWidth, rectHeight, 2, 2)
