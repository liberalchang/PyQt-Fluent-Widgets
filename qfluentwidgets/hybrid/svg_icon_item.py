# coding:utf-8
from PySide6.QtCore import Qt, QUrl, Property, QRectF, Signal
from PySide6.QtGui import QColor, QPainter, QImage
from PySide6.QtQuick import QQuickPaintedItem
from PySide6.QtSvg import QSvgRenderer

class SvgIconItem(QQuickPaintedItem):
    """ SVG Icon Item that supports dynamic coloring in Software Rendering mode """
    
    sourceChanged = Signal()
    colorChanged = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._source = ""
        self._color = QColor()
        self._renderer = QSvgRenderer()
        
        # Optimize for software rendering
        self.setRenderTarget(QQuickPaintedItem.Image)

    def getSource(self):
        return self._source

    def setSource(self, source):
        if self._source == source:
            return
        self._source = source
        
        # Handle resource path format
        path = source
        if path.startswith("qrc:"):
            path = path[3:] # Convert qrc:/... to /...
            if not path.startswith(":"):
                path = ":" + path
        elif path.startswith(":/"):
            pass # Already correct for Qt resource
            
        self._renderer.load(path)
        self.update()
        self.sourceChanged.emit()

    source = Property(str, getSource, setSource, notify=sourceChanged)

    def getColor(self):
        return self._color

    def setColor(self, color):
        if self._color == color:
            return
        self._color = QColor(color)
        self.update()
        self.colorChanged.emit()

    color = Property(QColor, getColor, setColor, notify=colorChanged)

    def paint(self, painter):
        if not self._renderer.isValid():
            return
            
        rect = self.boundingRect()
        
        # If color is invalid or fully transparent, draw original
        if not self._color.isValid() or self._color.alpha() == 0:
            self._renderer.render(painter, rect)
            return
            
        # Dynamic coloring logic
        # For better performance, we could cache the image, but for now direct draw
        width = int(rect.width())
        height = int(rect.height())
        
        if width <= 0 or height <= 0:
            return
            
        # Create temporary image for masking
        img = QImage(width, height, QImage.Format_ARGB32_Premultiplied)
        img.fill(Qt.transparent)
        
        p = QPainter(img)
        p.setRenderHint(QPainter.Antialiasing)
        p.setRenderHint(QPainter.SmoothPixmapTransform)
        
        # Draw SVG
        self._renderer.render(p, QRectF(0, 0, width, height))
        
        # Apply Color Overlay
        p.setCompositionMode(QPainter.CompositionMode_SourceIn)
        p.fillRect(img.rect(), self._color)
        p.end()
        
        # Draw result
        painter.drawImage(0, 0, img)
