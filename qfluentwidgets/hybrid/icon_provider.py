# coding:utf-8
from PySide6.QtQuick import QQuickImageProvider
from PySide6.QtGui import QImage, QPainter, QColor
from PySide6.QtCore import Qt
from PySide6.QtSvg import QSvgRenderer

from ..common.icon import FluentIcon, AntDesignIcon

class FluentIconImageProvider(QQuickImageProvider):
    """ Provides SVG icons as QImage for QML, supporting dynamic coloring """
    
    def __init__(self):
        super().__init__(QQuickImageProvider.Image)
        # Pre-build lookup map for O(1) access
        self._ICON_MAP = {i.value: i for i in AntDesignIcon}
        self._ICON_MAP.update({i.value: i for i in FluentIcon})

    def requestImage(self, id, size, requestedSize):
        """
        id format: "IconName/ThemeName/ColorHex" 
        Example: "Home/Light/#FF0000" or "Home/Light/transparent"
        If ColorHex is omitted or "transparent", no tinting is applied.
        """
        parts = id.split('/')
        name = parts[0]
        
        # Defaults
        theme_name = "Light"
        color_str = "transparent"
        
        if len(parts) > 1:
            theme_name = parts[1]
        if len(parts) > 2:
            color_str = parts[2]
            
        if name not in self._ICON_MAP:
            if size is not None:
                size.setWidth(0)
                size.setHeight(0)
            return QImage()
            
        icon_enum = self._ICON_MAP[name]
        
        # Get path for theme (FluentIcon.path(theme))
        # Theme enum in config is lowercase usually, but FluentIcon might handle string?
        # FluentIcon.path() takes 'theme' argument which is Theme.LIGHT or Theme.DARK enum, or string?
        # Let's check icon.py. usually it expects Theme enum.
        # But we can try to map string to enum if needed. 
        # Actually FluentIcon.path() uses qconfig.theme if not provided.
        # But here we want explicit theme.
        
        from ..common.config import Theme
        theme_enum = Theme.DARK if theme_name == "Dark" else Theme.LIGHT
        
        path = icon_enum.path(theme_enum)
        
        # Remove "qrc" prefix if present (QSvgRenderer handles :/ but not qrc:/)
        if path.startswith("qrc"):
            path = path[3:]
            
        renderer = QSvgRenderer(path)
        if not renderer.isValid():
            if size is not None:
                size.setWidth(0)
                size.setHeight(0)
            return QImage()
             
        # Determine output size
        width = requestedSize.width() if requestedSize.width() > 0 else 24
        height = requestedSize.height() if requestedSize.height() > 0 else 24
        
        img = QImage(width, height, QImage.Format_ARGB32_Premultiplied)
        img.fill(Qt.transparent)
        
        painter = QPainter(img)
        renderer.render(painter)
        
        # Apply color tint if specified
        if color_str != "transparent" and color_str:
            c = QColor(color_str)
            if c.isValid() and c.alpha() > 0:
                painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
                painter.fillRect(img.rect(), c)
                
        painter.end()
        
        if size is not None:
            size.setWidth(img.width())
            size.setHeight(img.height())
        return img
