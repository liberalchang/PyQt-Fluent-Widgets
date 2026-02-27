# coding:utf-8
from PySide6.QtCore import Qt, Signal, QRect, QTimer
from PySide6.QtGui import QColor, QPainter, QCursor, QGuiApplication, QPixmap, QPen, QPainterPath
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout

from qfluentwidgets.common.icon import FluentIcon as FIF
from qfluentwidgets.common.style_sheet import FluentStyleSheet
from qfluentwidgets.components.widgets.line_edit import LineEdit
from qfluentwidgets.components.widgets.button import ToolButton

class ScreenColorPickerOverlay(QWidget):
    """ Screen color picker overlay """

    colorSelected = Signal(QColor)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setCursor(Qt.CrossCursor)
        self.setMouseTracking(True)
        
        # Cover all screens
        self.setGeometry(QGuiApplication.primaryScreen().virtualGeometry())
        
        self.currentColor = QColor()
        self.zoomFactor = 4  # Magnification factor
        self.previewSize = 120 # Size of magnifier window
        self.gridSize = 9 # Number of pixels to show (odd number)
        
        # Timer for live update
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(30) # 30ms ~ 33fps

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
        
        # Fill with nearly transparent color to capture mouse events
        painter.fillRect(self.rect(), QColor(0, 0, 0, 1))
        
        global_pos = QCursor.pos()
        local_pos = self.mapFromGlobal(global_pos)
        
        # 1. Capture Live Screen Content
        screen = QGuiApplication.screenAt(global_pos)
        if not screen:
            return

        # Calculate capture area
        # We want to show 'gridSize' pixels (e.g. 9x9)
        # So we capture 9x9 area centered at cursor
        
        # Local coordinates on the specific screen
        screen_geo = screen.geometry()
        local_x = global_pos.x() - screen_geo.x()
        local_y = global_pos.y() - screen_geo.y()
        
        capture_x = local_x - self.gridSize // 2
        capture_y = local_y - self.gridSize // 2
        
        # Grab the content
        pixmap = screen.grabWindow(0, capture_x, capture_y, self.gridSize, self.gridSize)
        
        # Extract center color (current pixel)
        if not pixmap.isNull():
            image = pixmap.toImage()
            # Center of the captured 9x9 grid is at index 4 (if grid=9)
            # But we must be careful if we are at screen edge and captured less
            c_x = min(image.width() // 2, image.width() - 1)
            c_y = min(image.height() // 2, image.height() - 1)
            self.currentColor = image.pixelColor(c_x, c_y)
            
            # Scale up for magnifier
            # Scale to previewSize
            scaled_pixmap = pixmap.scaled(self.previewSize, self.previewSize, Qt.KeepAspectRatio, Qt.FastTransformation)
        else:
            scaled_pixmap = QPixmap(self.previewSize, self.previewSize)
            scaled_pixmap.fill(Qt.black)

        # 2. Draw Magnifier UI
        # Offset magnifier from cursor to avoid occluding the capture area
        offset = 20
        mag_rect = QRect(local_pos.x() + offset, local_pos.y() + offset, self.previewSize, self.previewSize)
        
        # Keep magnifier within screen bounds
        if mag_rect.right() > self.width():
            mag_rect.moveRight(local_pos.x() - offset)
        if mag_rect.bottom() > self.height():
            mag_rect.moveBottom(local_pos.y() - offset)
            
        # Draw Background (Shadow)
        path = QPainterPath()
        path.addRoundedRect(mag_rect, self.previewSize//2, self.previewSize//2)
        
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(0, 0, 0, 40))
        painter.drawPath(path.translated(2, 2))
        
        # Draw Content
        painter.setClipPath(path)
        painter.drawPixmap(mag_rect, scaled_pixmap)
        
        # Draw Grid Lines
        pixel_w = self.previewSize / self.gridSize
        painter.setPen(QPen(QColor(255, 255, 255, 30), 1))
        for i in range(1, self.gridSize):
            x = mag_rect.left() + i * pixel_w
            y = mag_rect.top() + i * pixel_w
            painter.drawLine(x, mag_rect.top(), x, mag_rect.bottom())
            painter.drawLine(mag_rect.left(), y, mag_rect.right(), y)
            
        # Draw Center Highlight (The picked pixel)
        center_rect = QRect(
            mag_rect.left() + (self.gridSize//2) * pixel_w,
            mag_rect.top() + (self.gridSize//2) * pixel_w,
            pixel_w, pixel_w
        )
        painter.setPen(QPen(Qt.red, 2))
        painter.setBrush(Qt.NoBrush)
        painter.drawRect(center_rect)
        
        # Draw Border
        painter.setClipping(False)
        painter.setPen(QPen(QColor(255, 255, 255), 4))
        painter.setBrush(Qt.NoBrush)
        painter.drawRoundedRect(mag_rect, self.previewSize//2, self.previewSize//2)
        
        # Draw Color Text
        text_h = 24
        text_rect = QRect(mag_rect.center().x() - 40, mag_rect.bottom() + 8, 80, text_h)
        
        # Text Background
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(32, 32, 32))
        painter.drawRoundedRect(text_rect, 4, 4)
        
        # Text
        painter.setPen(Qt.white)
        font = painter.font()
        font.setBold(True)
        painter.setFont(font)
        painter.drawText(text_rect, Qt.AlignCenter, self.currentColor.name().upper())

    def wheelEvent(self, e):
        # Zoom in/out
        delta = e.angleDelta().y()
        if delta > 0:
            self.gridSize = max(3, self.gridSize - 2)
        else:
            self.gridSize = min(31, self.gridSize + 2)
        self.update()

    def mouseMoveEvent(self, e):
        self.update()
        
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.colorSelected.emit(self.currentColor)
            self.close()
            
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()



class ColorPreview(QLabel):
    """ Color preview label """

    def __init__(self, color: QColor, parent=None):
        super().__init__(parent)
        self.setFixedSize(24, 24)
        self.setObjectName("previewLabel")
        self.setColor(color)

    def setColor(self, color: QColor):
        self.setStyleSheet(f"background-color: {color.name()};")


class ScreenColorPicker(QWidget):
    """ Screen Color Picker Widget """
    
    colorChanged = Signal(QColor)
    
    def __init__(self, color=Qt.white, parent=None):
        super().__init__(parent)
        self.currentColor = QColor(color)
        
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.setSpacing(10)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        
        # 1. Preview Area
        self.previewLabel = ColorPreview(self.currentColor, self)
        
        # 2. Value Output Box
        self.valueLineEdit = LineEdit(self)
        self.valueLineEdit.setText(self.currentColor.name().upper())
        self.valueLineEdit.setFixedWidth(100)
        self.valueLineEdit.setReadOnly(False)
        self.valueLineEdit.editingFinished.connect(self._onHexEdited)
        
        # 3. Pick Tool Button
        # Using EDIT icon as a placeholder for Dropper/Pipette if not available
        self.pickButton = ToolButton(FIF.EDIT, self) 
        self.pickButton.setToolTip(self.tr("Pick Screen Color"))
        self.pickButton.clicked.connect(self.startPicking)
        
        self.hBoxLayout.addWidget(self.previewLabel)
        self.hBoxLayout.addWidget(self.valueLineEdit)
        self.hBoxLayout.addWidget(self.pickButton)
        self.hBoxLayout.addStretch(1)

        FluentStyleSheet.SCREEN_COLOR_PICKER.apply(self)
        
    def startPicking(self):
        # Create overlay
        self.overlay = ScreenColorPickerOverlay()
        self.overlay.colorSelected.connect(self.setColor)
        self.overlay.show()
        self.overlay.activateWindow()
        
    def setColor(self, color):
        if not color.isValid():
            return
            
        self.currentColor = QColor(color)
        self.previewLabel.setStyleSheet(f"background-color: {self.currentColor.name()};")
        self.valueLineEdit.setText(self.currentColor.name().upper())
        self.colorChanged.emit(self.currentColor)
        
    def _onHexEdited(self):
        text = self.valueLineEdit.text()
        if QColor.isValidColor(text):
            self.setColor(QColor(text))
        else:
            # Revert to current color
            self.valueLineEdit.setText(self.currentColor.name().upper())
