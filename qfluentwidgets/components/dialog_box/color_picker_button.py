# coding:utf-8
from typing import Union

from PySide6.QtCore import Qt, Signal, QRect
from PySide6.QtGui import QColor, QPainter, QIcon
from PySide6.QtWidgets import QPushButton, QVBoxLayout

from ...common.icon import FluentIcon as FIF, toQIcon
from ...common.style_sheet import isDarkTheme
from ...components.widgets.flyout import Flyout, FlyoutAnimationType, FlyoutViewBase
from ...components.widgets.scroll_area import SingleDirectionScrollArea
from .color_dialog import ColorDialog, ColorPickerWidget
from .circle_color_picker import CircleColorPicker
from .screen_color_picker import ScreenColorPickerOverlay
from .color_palette import ColorPalette


class ColorPickerFlyoutView(FlyoutViewBase):
    """ Color picker flyout view """

    def __init__(self, color, title, parent=None, enableAlpha=True):
        super().__init__(parent)
        self.scrollArea = SingleDirectionScrollArea(self)
        self.widget = ColorPickerWidget(color, title, self.scrollArea, enableAlpha)

        self.scrollArea.setWidget(self.widget)
        self.scrollArea.setViewportMargins(48, 24, 0, 24)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Match ColorDialog's content area size (699 - 81 = 618)
        self.setFixedSize(488, 618)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.scrollArea)

    @property
    def colorChanged(self):
        return self.widget.colorChanged
        
    def addWidget(self, widget, stretch=0, align=Qt.AlignLeft):
        pass


class SimpleFlyoutView(FlyoutViewBase):
    """ Simple flyout view """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setContentsMargins(12, 12, 12, 12)

    def addWidget(self, widget, stretch=0, align=Qt.AlignLeft):
        self.vBoxLayout.addWidget(widget, stretch, align)


class ColorButton(QPushButton):
    """ Color picker button """

    colorChanged = Signal(QColor)

    def __init__(self, color: Union[QColor, str, Qt.GlobalColor], title: str, parent=None,
                 icon: Union[str, QIcon, FIF] = None, showPreview=True, customColors=None):
        super().__init__(parent)
        self.setText(title)
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedSize(160 if title else 96, 40)
        
        self.customColors = customColors if customColors else []
        self._color = QColor(color)
        self._showPreview = showPreview
        self._icon = icon
        
        if icon:
            if isinstance(icon, FIF):
                self._icon = icon.icon()
            else:
                self._icon = toQIcon(icon)
        
        self.clicked.connect(self.showFlyout)
        self.setObjectName("colorButton")

    def color(self):
        return self._color
        
    def setColor(self, color):
        self._color = QColor(color)
        self.colorChanged.emit(self._color)
        self.update()
        
    def setIcon(self, icon: Union[str, QIcon, FIF]):
        if isinstance(icon, FIF):
            self._icon = icon.icon()
        else:
            self._icon = toQIcon(icon)
        self.update()

    def showFlyout(self):
        palette = ColorPalette(self.customColors, self.window())
        palette.setAutoColor(self._color)
        
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
        dialog = ColorDialog(self._color, self.tr("Select Color"), self.window())
        if dialog.exec():
            try:
                self._onCustomColorAdded(dialog.color)
            except RuntimeError:
                pass

    def _onCustomColorAdded(self, color):
        if color not in self.customColors:
            self.customColors.append(color)
            self._onCustomColorsChanged(self.customColors)

    def _openMoreColorsDialog(self):
        dialog = ColorDialog(self._color, self.tr("Select Color"), self.window())
        if dialog.exec():
            self._onColorSelected(dialog.color)

    def _onColorSelected(self, color):
        self.setColor(color)

    def _onCustomColorsChanged(self, colors):
        self.customColors = colors[:]

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        
        # Draw background
        painter.setPen(Qt.NoPen)
        if self.isDown():
            painter.setBrush(QColor(0, 0, 0, 10))
        elif self.underMouse():
            painter.setBrush(QColor(0, 0, 0, 6))
        else:
            painter.setBrush(QColor(255, 255, 255, 255) if not isDarkTheme() else QColor(255, 255, 255, 13))
            
        painter.drawRoundedRect(self.rect(), 4, 4)
        
        # Draw border
        painter.setBrush(Qt.NoBrush)
        if isDarkTheme():
            painter.setPen(QColor(255, 255, 255, 25))
        else:
            painter.setPen(QColor(0, 0, 0, 15))
        painter.drawRoundedRect(self.rect().adjusted(0, 0, -1, -1), 4, 4)
        
        # Content Layout
        rect = self.rect()
        x = 10
        y = (rect.height() - 20) / 2
        
        # 1. Color Preview (Rounded Square)
        if self._showPreview:
            painter.setPen(Qt.NoPen)
            painter.setBrush(self._color)
            painter.drawRoundedRect(x, y + 2, 16, 16, 4, 4)
            x += 24
            
        # 2. Icon (if present)
        if self._icon:
            # If we just showed a preview, icon goes next to it
            # Or if no preview, icon is first
            
            pixmap = self._icon.pixmap(16, 16)
            painter.drawPixmap(x, y + 2, pixmap)
            
            # Draw color strip if preview is hidden
            if not self._showPreview:
                painter.setBrush(self._color)
                painter.setPen(Qt.NoPen)
                # Draw at bottom of icon
                painter.drawRoundedRect(x + 2, y + 16, 12, 3, 1.5, 1.5)
            
            x += 24
            
        # 3. Text
        chevronX = rect.width() - 20
        if self.text():
            painter.setPen(QColor(0, 0, 0, 255) if not isDarkTheme() else QColor(255, 255, 255, 255))
            painter.setFont(self.font())
            textRect = QRect(int(x), 0, int(chevronX - x - 5), int(rect.height()))
            painter.drawText(textRect, Qt.AlignLeft | Qt.AlignVCenter, self.text())

        # 4. Chevron (Arrow)
        # Draw chevron
        painter.setPen(QColor(0, 0, 0, 150) if not isDarkTheme() else QColor(255, 255, 255, 150))
        painter.setBrush(Qt.NoBrush)
        FIF.ARROW_DOWN.render(painter, QRect(int(chevronX), int(y + 2), 12, 12))
        
        painter.end()


class ColorDialogButton(ColorButton):
    """ Color dialog button """

    def showFlyout(self):
        view = ColorPickerFlyoutView(self._color, self.tr("Select Color"), self.window(), enableAlpha=True)
        view.colorChanged.connect(self._onColorSelected)
        
        # ColorPickerWidget is large, ensure it fits or is scrollable if needed.
        # But Flyout doesn't enforce scroll.
        # Assuming screen is large enough for now.
        
        w = Flyout.make(view, self, self.window(), FlyoutAnimationType.PULL_UP, True)  # noqa: F841


class CircleColorButton(ColorButton):
    """ Circle color picker button """

    def showFlyout(self):
        view = SimpleFlyoutView(self.window())
        
        picker = CircleColorPicker(self.customColors, view)
        picker.colorChanged.connect(self._onColorSelected)
        picker.colorsChanged.connect(self._onCustomColorsChanged)
        picker.addColorClicked.connect(self._openCustomColorDialog)
        
        view.addWidget(picker)
        
        # Close flyout on color selection
        picker.colorChanged.connect(lambda: w.close())
        
        w = Flyout.make(view, self, self.window(), FlyoutAnimationType.PULL_UP, True)


class ScreenColorButton(ColorButton):
    """ Screen color picker button """

    def showFlyout(self):
        # Directly trigger screen color picker overlay
        self.overlay = ScreenColorPickerOverlay()
        self.overlay.colorSelected.connect(self._onColorSelected)
        self.overlay.show()
        self.overlay.activateWindow()
