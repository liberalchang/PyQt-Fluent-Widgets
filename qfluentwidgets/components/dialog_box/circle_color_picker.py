# coding:utf-8
from typing import List, Union

from PySide6.QtCore import Qt, Signal, QSize, QRectF
from PySide6.QtGui import QColor, QPainter, QBrush, QPen, QMouseEvent, QAction, QIcon
from PySide6.QtWidgets import QWidget, QHBoxLayout, QAbstractButton, QButtonGroup, QMenu, QToolButton

from ...common.style_sheet import isDarkTheme, FluentStyleSheet
from ...common.icon import FluentIcon as FIF


class CircleColorItem(QAbstractButton):
    """ Circle color item """

    removeRequested = Signal()

    def __init__(self, color: QColor, parent=None):
        super().__init__(parent)
        self.setFixedSize(30, 30)
        self.setCheckable(True)
        self.color = QColor(color)
        self.setCursor(Qt.PointingHandCursor)
        self.setToolTip(self.color.name().upper())

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)

        # Center and radius
        cx, cy = self.width() / 2, self.height() / 2
        
        # Draw checked state
        if self.isChecked():
            # Outer ring
            radius_outer = 13
            pen = QPen(self.color, 2)
            painter.setPen(pen)
            painter.setBrush(Qt.NoBrush)
            painter.drawEllipse(QRectF(cx - radius_outer, cy - radius_outer, radius_outer * 2, radius_outer * 2))
            
            # Inner circle
            radius_inner = 9
            painter.setPen(Qt.NoPen)
            painter.setBrush(self.color)
            painter.drawEllipse(QRectF(cx - radius_inner, cy - radius_inner, radius_inner * 2, radius_inner * 2))
        else:
            # Normal state: larger solid circle
            radius = 11
            
            painter.setPen(Qt.NoPen)
            painter.setBrush(self.color)
            painter.drawEllipse(QRectF(cx - radius, cy - radius, radius * 2, radius * 2))

            if self.isDown():
                painter.setBrush(QColor(0, 0, 0, 20))
                painter.drawEllipse(QRectF(cx - radius, cy - radius, radius * 2, radius * 2))

    def contextMenuEvent(self, e):
        menu = QMenu(self)
        # Create Remove action
        action = QAction(self.tr("Remove"), menu)
        action.triggered.connect(self.removeRequested.emit)
        menu.addAction(action)
        menu.exec(e.globalPos())


class CircleColorPicker(QWidget):
    """ Circle color picker """

    colorChanged = Signal(QColor)
    addColorClicked = Signal()
    colorRemoved = Signal(QColor)
    colorAdded = Signal(QColor)
    colorsChanged = Signal(list)

    def __init__(self, colors: List[Union[QColor, str]] = None, parent=None):
        super().__init__(parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.buttonGroup = QButtonGroup(self)
        self.colors = []
        
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.setSpacing(10)
        self.hBoxLayout.setAlignment(Qt.AlignLeft)

        self.buttonGroup.setExclusive(True)
        self.buttonGroup.buttonClicked.connect(self._onButtonClicked)
        
        # Add Button
        self.addButton = QToolButton(self)
        self.addButton.setFixedSize(30, 30)
        self.addButton.setCursor(Qt.PointingHandCursor)
        self.addButton.setIcon(FIF.ADD.icon())
        self.addButton.clicked.connect(self.addColorClicked)

        FluentStyleSheet.CIRCLE_COLOR_PICKER.apply(self)

        if colors:
            self.setColors(colors)
        else:
            self.hBoxLayout.addWidget(self.addButton)

    def setColors(self, colors: List[Union[QColor, str]]):
        """ set color list """
        # Clear existing buttons
        for btn in self.buttonGroup.buttons():
            self.buttonGroup.removeButton(btn)
            self.hBoxLayout.removeWidget(btn)
            btn.deleteLater()
            
        # Ensure add button is removed from layout to be re-added at the end
        self.hBoxLayout.removeWidget(self.addButton)
        self.addButton.setParent(None) # Detach temporarily or just hide? 
        # Better: remove it, add items, then add it back.
        
        self.colors = []
        for c in colors:
            self.addColor(c, False)
            
        # Add the 'Add' button at the end
        self.hBoxLayout.addWidget(self.addButton)

    def setColor(self, color: QColor):
        """ set current color """
        color = QColor(color)
        for btn in self.buttonGroup.buttons():
            if btn.color == color:
                btn.setChecked(True)
                return

    def color(self):
        """ get current color """
        btn = self.buttonGroup.checkedButton()
        return btn.color if btn else QColor()

    def _onButtonClicked(self, button):
        if isinstance(button, CircleColorItem) and button.color.isValid():
            self.colorChanged.emit(button.color)
            
    def addColor(self, color: QColor, updateLayout=True):
        """ add a new color """
        color = QColor(color)
        if color in self.colors:
            return

        self.colors.append(color)
        item = CircleColorItem(color, self)
        item.removeRequested.connect(lambda: self.removeColor(color))
        
        if updateLayout:
            # Insert before the add button
            index = self.hBoxLayout.indexOf(self.addButton)
            if index >= 0:
                self.hBoxLayout.insertWidget(index, item)
            else:
                self.hBoxLayout.addWidget(item)
                self.hBoxLayout.addWidget(self.addButton)
        else:
            self.hBoxLayout.addWidget(item)
            
        self.buttonGroup.addButton(item)
        self.colorAdded.emit(color)
        self.colorsChanged.emit(self.colors)

    def removeColor(self, color: QColor):
        """ remove a color """
        color = QColor(color)
        if color not in self.colors:
            return
            
        # Find the button
        for btn in self.buttonGroup.buttons():
            if btn.color == color:
                self.buttonGroup.removeButton(btn)
                self.hBoxLayout.removeWidget(btn)
                btn.deleteLater()
                self.colors.remove(color)
                self.colorRemoved.emit(color)
                self.colorsChanged.emit(self.colors)
                break
