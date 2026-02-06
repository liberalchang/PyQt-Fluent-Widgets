from typing import Union
from PySide6.QtCore import Qt, QUrl, QTimer, QObject, Property, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtQml import qmlRegisterType
from PySide6.QtGui import QIcon, QColor

from ..common.icon import FluentIconBase, FluentIcon, AntDesignIcon
from ..common.config import isDarkTheme, Theme, qconfig
from .svg_icon_item import SvgIconItem
from .qml_manager import HybridQml


class SplashBridge(QObject):
    isDarkChanged = Signal()
    titleTextChanged = Signal()
    descriptionTextChanged = Signal()
    iconPathChanged = Signal()
    iconColorChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._isDark = isDarkTheme()
        self._titleText = "应用启动中"
        self._descriptionText = "正在加载，请稍候……"
        self._iconPath = ""
        self._iconColor = ""

    def getIsDark(self): return self._isDark
    def setIsDark(self, v: bool):
        if self._isDark != v:
            self._isDark = v
            self.isDarkChanged.emit()
    isDark = Property(bool, getIsDark, setIsDark, notify=isDarkChanged)

    def getTitleText(self): return self._titleText
    def setTitleText(self, t: str):
        if self._titleText != t:
            self._titleText = t
            self.titleTextChanged.emit()
    titleText = Property(str, getTitleText, setTitleText, notify=titleTextChanged)

    def getDescriptionText(self): return self._descriptionText
    def setDescriptionText(self, t: str):
        if self._descriptionText != t:
            self._descriptionText = t
            self.descriptionTextChanged.emit()
    descriptionText = Property(str, getDescriptionText, setDescriptionText, notify=descriptionTextChanged)

    def getIconPath(self): return self._iconPath
    def setIconPath(self, p: str):
        if self._iconPath != p:
            self._iconPath = p
            self.iconPathChanged.emit()
    iconPath = Property(str, getIconPath, setIconPath, notify=iconPathChanged)

    def getIconColor(self): return self._iconColor
    def setIconColor(self, c: str):
        if self._iconColor != c:
            self._iconColor = c
            self.iconColorChanged.emit()
    iconColor = Property(str, getIconColor, setIconColor, notify=iconColorChanged)


class HybridSplashScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        qmlRegisterType(SvgIconItem, "FluentUI", 1, 0, "SvgIcon")

        self._container = QQuickWidget(self)
        self._container.setResizeMode(QQuickWidget.SizeRootObjectToView)
        self._container.setClearColor(Qt.transparent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self._container)

        self.bridge = SplashBridge(self)
        self._container.rootContext().setContextProperty("bridge", self.bridge)

        self._container.setSource(QUrl(HybridQml.SPLASH.path))
        self.resize(640, 420)
        self._iconRaw = None
        qconfig.themeChangedFinished.connect(self._syncTheme)
        self._syncTheme()

    def _resolve_icon_path(self, icon: Union[FluentIconBase, str, QIcon]) -> str:
        try:
            if isinstance(icon, FluentIconBase):
                return icon.path(Theme.DARK if isDarkTheme() else Theme.LIGHT)
            if isinstance(icon, QIcon):
                return ""
            if isinstance(icon, str) and icon:
                if hasattr(FluentIcon, icon):
                    return getattr(FluentIcon, icon).path(Theme.DARK if isDarkTheme() else Theme.LIGHT)
                if hasattr(AntDesignIcon, icon):
                    return getattr(AntDesignIcon, icon).path(Theme.DARK if isDarkTheme() else Theme.LIGHT)
                return icon
        except Exception:
            pass
        return ""

    def setIcon(self, icon: Union[FluentIconBase, str, QIcon]):
        self._iconRaw = icon
        self.bridge.setIconPath(self._resolve_icon_path(icon))

    def setTitle(self, title: str):
        self.bridge.setTitleText(title or "")

    def setDescription(self, description: str):
        self.bridge.setDescriptionText(description or "")

    def setIconColor(self, color: Union[QColor, str]):
        if isinstance(color, QColor):
            self.bridge.setIconColor(color.name())
        elif isinstance(color, str):
            self.bridge.setIconColor(color)
        else:
            self.bridge.setIconColor("")

    def setDark(self, is_dark: bool):
        self.bridge.setIsDark(bool(is_dark))

    def showFor(self, ms: int, onFinished=None):
        self.show()
        QTimer.singleShot(int(ms), lambda: self._closeAndCall(onFinished))

    def _closeAndCall(self, cb):
        try:
            self.close()
        finally:
            if callable(cb):
                cb()

    def _syncTheme(self):
        self.bridge.setIsDark(isDarkTheme())
        if self._iconRaw is not None:
            self.bridge.setIconPath(self._resolve_icon_path(self._iconRaw))
