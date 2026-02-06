# coding:utf-8
from PySide6.QtCore import QObject, Signal, Slot, QPoint, Property
from qfluentwidgets.common.icon import FluentIcon, AntDesignIcon, getIconColor
from qfluentwidgets.common.config import qconfig, Theme

class CommunicationBridge(QObject):
    """ Bridge for communication between QML and Widget """
    
    # Signals from QML to Widget
    menuClicked = Signal(str)
    themeToggle = Signal()
    windowMinimize = Signal()
    windowMaximize = Signal()
    windowClose = Signal()
    windowRestore = Signal()
    
    # Signals from Widget to QML
    functionWindowChanged = Signal(str)
    sidebarExpandChanged = Signal(bool)
    themeChanged = Signal(str) # "Dark" or "Light"
    maximizedChanged = Signal(bool) # True if maximized
    styleChanged = Signal()
    currentRouteChanged = Signal(str)
    windowEffectChanged = Signal(str)  # "Mica" | "Acrylic" | "None"

    # Pre-build icon map for O(1) lookup
    _ICON_MAP = {i.value: i for i in AntDesignIcon}
    _ICON_MAP.update({i.value: i for i in FluentIcon})

    def __init__(self, window=None, parent=None):
        super().__init__(parent=parent)
        self._window = window
        self._theme = "Light"
        self._style = {}
        self._isMaximized = False
        self._currentRoute = ""
        self._windowEffect = "None"

    def getIsMaximized(self):
        return self._isMaximized

    def setIsMaximized(self, value):
        if self._isMaximized == value:
            return
        self._isMaximized = value
        self.maximizedChanged.emit(value)

    isMaximized = Property(bool, getIsMaximized, setIsMaximized, notify=maximizedChanged)

    def getTheme(self):
        return self._theme

    def setTheme(self, theme):
        if self._theme == theme:
            return
        self._theme = theme
        self.themeChanged.emit(theme)

    theme = Property(str, getTheme, setTheme, notify=themeChanged)

    def getStyle(self):
        return self._style

    def setStyle(self, style):
        # Always emit signal to force QML update, even if dict content looks same
        self._style = style
        self.styleChanged.emit()

    style = Property(dict, getStyle, setStyle, notify=styleChanged)

    def getCurrentRoute(self):
        return self._currentRoute

    def setCurrentRoute(self, routeKey):
        if self._currentRoute == routeKey:
            return
        self._currentRoute = routeKey
        self.currentRouteChanged.emit(routeKey)

    currentRoute = Property(str, getCurrentRoute, setCurrentRoute, notify=currentRouteChanged)

    def getWindowEffect(self):
        return self._windowEffect

    def setWindowEffect(self, effect):
        if self._windowEffect == effect:
            return
        self._windowEffect = effect
        self.windowEffectChanged.emit(effect)

    windowEffect = Property(str, getWindowEffect, setWindowEffect, notify=windowEffectChanged)

    @Slot()
    def requestMenuToggle(self):
        self.menuClicked.emit("toggle_sidebar")

    @Slot(str)
    def requestMenuClicked(self, routeKey):
        self.menuClicked.emit(routeKey)

    @Slot()
    def requestThemeToggle(self):
        self.themeToggle.emit()

    @Slot()
    def requestWindowMinimize(self):
        self.windowMinimize.emit()

    @Slot()
    def requestWindowMaximize(self):
        self.windowMaximize.emit()

    @Slot()
    def requestWindowClose(self):
        self.windowClose.emit()

    @Slot(int, int)
    def moveWindow(self, dx, dy):
        """ Move the window by delta (dx, dy) """
        if self._window:
            new_pos = self._window.pos() + QPoint(dx, dy)
            self._window.move(new_pos)

    @Slot(str, str, result=str)
    def getIconPath(self, iconName, themeTrigger=""):
        """ Get icon path by name (e.g. 'Home') """
        if iconName not in self._ICON_MAP:
            return ""

        item = self._ICON_MAP[iconName]
        path = item.path(qconfig.theme)
        
        # QML requires explicit scheme for resource paths in some contexts
        if path.startswith(":"):
            return f"qrc{path}"
            
        return path
