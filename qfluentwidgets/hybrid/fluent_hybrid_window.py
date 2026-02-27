# coding:utf-8
import re
from PySide6.QtCore import (
    Qt,
    QUrl,
    QFile,
    QTextStream,
    QTimer,
)
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtQml import QQmlPropertyMap, qmlRegisterType, qmlRegisterSingletonInstance

from qfluentwidgets.window.fluent_window import FluentWindowBase
from qfluentwidgets.common.config import qconfig, Theme, isDarkTheme, WindowEffect
from qfluentwidgets.common.style_sheet import setTheme
from qfluentwidgets.common.icon import FluentIcon
from qfluentwidgets.components.navigation.navigation_panel import NavigationItemPosition

from .communication_bridge import CommunicationBridge
from .qml_manager import HybridQml
from .svg_icon_item import SvgIconItem
from .icon_provider import FluentIconImageProvider


class FluentHybridWindow(FluentWindowBase):
    """Fluent Hybrid Window with QML TitleBar and Sidebar"""

    def __init__(self, parent=None):
        # Force Software Rendering for QQuickWidget compatibility
        # QQuickWindow.setGraphicsApi(QSGRendererInterface.Software)

        # Register custom SvgIconItem
        qmlRegisterType(SvgIconItem, "FluentUI", 1, 0, "SvgIcon")

        super().__init__(parent)

        self.navigationItems = []
        self._styles = {"Light": {}, "Dark": {}}
        self.styleMap = QQmlPropertyMap(self)

        # 1. Initialize Communication Bridge
        self.bridge = CommunicationBridge(window=self)

        # 2. Setup QML Title Bar
        self.titleBarContainer = QQuickWidget(self)
        self.titleBarContainer.setResizeMode(QQuickWidget.SizeRootObjectToView)
        self.titleBarContainer.setFixedHeight(48)
        self.titleBarContainer.setAttribute(Qt.WA_AlwaysStackOnTop)
        self.titleBarContainer.setClearColor(Qt.transparent)

        # Replace default title bar
        self.setTitleBar(self.titleBarContainer)

        # Workaround for FramelessWindow nativeEvent accessing maxBtn
        class DummyButton:
            def setState(self, state):
                pass

        self.titleBarContainer.maxBtn = DummyButton()

        # 3. Setup QML Sidebar
        self.sidebarContainer = QQuickWidget(self)
        self.sidebarContainer.setResizeMode(QQuickWidget.SizeRootObjectToView)
        self.sidebarContainer.setFixedWidth(200)  # Default width, adjustable
        self.sidebarContainer.setClearColor(Qt.transparent)

        # 4. Layout (hBoxLayout inherited from FluentWindowBase)
        # FluentWindowBase creates self.hBoxLayout = QHBoxLayout(self)
        # We add sidebar and stackedWidget
        self.hBoxLayout.setContentsMargins(0, 48, 0, 0)  # Top margin for title bar
        self.hBoxLayout.addWidget(self.sidebarContainer)
        self.hBoxLayout.addWidget(self.stackedWidget)

        # 5. Load Style and QML
        self._loadStyle()
        self._initQml()

    def _loadStyle(self):
        """Load and parse QSS from resource"""
        # Load theme styles
        for path in [":/qss/qss/light/theme.qss", ":/qss/qss/dark/theme.qss"]:
            file = QFile(path)
            if file.open(QFile.ReadOnly | QFile.Text):
                stream = QTextStream(file)
                qss = stream.readAll()
                file.close()
                self._parseQss(qss)

    def _parseQss(self, qss):
        # Find blocks: QObject[theme="Name"] { ... }
        pattern = re.compile(r'QObject\[theme="(\w+)"\]\s*\{([^}]+)\}')
        matches = pattern.findall(qss)

        for theme, content in matches:
            # Parse properties: qproperty-name: value;
            # Value might contain rgba(...) so match until semicolon
            prop_pattern = re.compile(r"qproperty-([\w]+):\s*([^;]+);")
            props = prop_pattern.findall(content)
            for key, value in props:
                self._styles[theme][key] = value.strip()

    def _updateStyleMap(self):
        """Update the style map based on current theme."""
        theme = "Dark" if isDarkTheme() else "Light"
        props = self._styles.get(theme, {})

        print(f"DEBUG: Updating StyleMap for theme {theme}. Props count: {len(props)}")

        # Update Bridge Style
        if self.bridge:
            self.bridge.setStyle(props)

        # Update PropertyMap
        # for key, value in props.items():
        #     self.styleMap[key] = value

    def _initQml(self):
        # Ensure engines are created
        if not self.titleBarContainer.engine():
            print("ERROR: titleBarContainer engine is None")
        if not self.sidebarContainer.engine():
            print("ERROR: sidebarContainer engine is None")

        # Register Image Provider
        self.titleBarContainer.engine().addImageProvider(
            "FluentIcons", FluentIconImageProvider()
        )
        self.sidebarContainer.engine().addImageProvider(
            "FluentIcons", FluentIconImageProvider()
        )

        # Context Properties - MUST set on QQuickWidget.rootContext()
        titleCtx = self.titleBarContainer.rootContext()
        sideCtx = self.sidebarContainer.rootContext()

        print(
            f"DEBUG: Setting context properties. Bridge: {self.bridge}, StyleMap: {self.styleMap}"
        )

        titleCtx.setContextProperty("bridge", self.bridge)
        sideCtx.setContextProperty("bridge", self.bridge)
        sideCtx.setContextProperty("navItems", self.navigationItems)

        # Expose Style Map
        self._updateStyleMap()

        # Register Bridge as Singleton
        qmlRegisterSingletonInstance(
            CommunicationBridge, "FluentUI", 1, 0, "Bridge", self.bridge
        )

        # self.titleBarContainer.rootContext().setContextProperty("ThemeMap", self.styleMap)
        # self.sidebarContainer.rootContext().setContextProperty("ThemeMap", self.styleMap)

        # Verify properties
        # print(f"DEBUG: Title Context Bridge: {titleCtx.contextProperty('bridge')}")

        # Load QML
        print(
            f"DEBUG: Loading QML from {HybridQml.TITLE_BAR.path} and {HybridQml.SIDE_NAV.path}"
        )
        self.titleBarContainer.setSource(QUrl(HybridQml.TITLE_BAR.path))
        self.sidebarContainer.setSource(QUrl(HybridQml.SIDE_NAV.path))

        # Check errors
        for error in self.titleBarContainer.errors():
            print(f"TitleBar Error: {error.toString()}")
        for error in self.sidebarContainer.errors():
            print(f"SideBar Error: {error.toString()}")

        # 6. Connect Signals
        self._connectSignals()

        # 7. Initial State
        self.resize(1000, 650)

        # Fix transparent background issues
        self.titleBarContainer.setAttribute(Qt.WA_TranslucentBackground)
        self.sidebarContainer.setAttribute(Qt.WA_TranslucentBackground)

        # Initial Theme
        self._onThemeChanged()
        self._onWindowEffectChanged()

        qconfig.appRestartSig.connect(self._onWindowEffectChanged)

    def addSubInterface(self, interface, icon, text, position=None):
        """Add sub interface"""
        self.stackedWidget.addWidget(interface)
        interface.setObjectName(text)

        # Add to navItems
        # icon can be FluentIcon enum or string
        iconName = icon.value if hasattr(icon, "value") else icon
        itemPosition = self._normalizePosition(position)

        item = {
            "routeKey": text,
            "text": text,
            "icon": iconName,
            "position": itemPosition,
        }
        self.navigationItems.append(item)
        self.sidebarContainer.rootContext().setContextProperty(
            "navItems", self.navigationItems
        )
        if self.stackedWidget.count() == 1:
            self.stackedWidget.setCurrentWidget(interface)
            if self.bridge:
                self.bridge.functionWindowChanged.emit(text)
                self.bridge.setCurrentRoute(text)

    def _normalizePosition(self, position):
        if isinstance(position, NavigationItemPosition):
            if position == NavigationItemPosition.TOP:
                return "top"
            if position == NavigationItemPosition.BOTTOM:
                return "bottom"
            return "scroll"
        if isinstance(position, str):
            value = position.lower()
            if value in ("top", "scroll", "bottom"):
                return value
        return "scroll"

    def _isHoverMaxBtn(self):
        # Fix AttributeError in FramelessWindow
        return False

    def _connectSignals(self):
        # Window Controls
        self.bridge.windowMinimize.connect(self.showMinimized)
        self.bridge.windowMaximize.connect(self._toggleMaximized)
        self.bridge.windowClose.connect(self.close)

        # Theme Sync
        qconfig.themeChanged.connect(self._onThemeChanged)
        self.bridge.themeToggle.connect(self._toggleTheme)

        # Navigation
        self.bridge.menuClicked.connect(self._onMenuClicked)

        self.bridge.setTransitionDurationMs(600)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        # Notify QML about maximize state change (e.g. via snap layout or double click)
        if self.bridge:
            self.bridge.setIsMaximized(self.isMaximized())

    def _toggleMaximized(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
        # State update is handled in resizeEvent, but good to be explicit
        self.bridge.maximizedChanged.emit(self.isMaximized())

    def _toggleTheme(self):
        if qconfig.theme == Theme.DARK:
            setTheme(Theme.LIGHT, save=False)
        else:
            setTheme(Theme.DARK, save=False)

    def _onThemeChanged(self):
        # Notify QML via Bridge
        isDark = isDarkTheme()
        themeName = "Dark" if isDark else "Light"
        # Update bridge theme property (triggers QML bindings)
        self.bridge.setTheme(themeName)

        # Update Style Map
        self._updateStyleMap()

        # Update widget background
        color = QColor(32, 32, 32) if isDark else QColor(243, 243, 243)
        self.setBackgroundColor(color)
        QTimer.singleShot(0, self._refreshQmlSurfaces)

    def _refreshQmlSurfaces(self):
        try:
            self.titleBarContainer.update()
            self.sidebarContainer.update()
        except Exception:
            try:
                self.titleBarContainer.repaint()
                self.sidebarContainer.repaint()
            except Exception:
                pass

    def _onWindowEffectChanged(self):
        try:
            effect = qconfig.get(qconfig.windowEffect)
            self.setWindowEffect(effect)
            # 同步给 QML：透明处理由 QML 根据此状态决定是否显示背景色
            if effect == WindowEffect.MICA:
                self.bridge.setWindowEffect("Mica")
            elif effect == WindowEffect.ACRYLIC:
                self.bridge.setWindowEffect("Acrylic")
            else:
                self.bridge.setWindowEffect("None")
        except Exception:
            pass

    def _onMenuClicked(self, routeKey):
        if routeKey == "toggle_sidebar":
            self.toggleSidebar()
            return

        # Switch Stacked Widget
        # Find widget by objectName (which we set to routeKey)
        for i in range(self.stackedWidget.count()):
            w = self.stackedWidget.widget(i)
            if w.objectName() == routeKey:
                self.stackedWidget.setCurrentWidget(w)
                if self.bridge:
                    self.bridge.functionWindowChanged.emit(routeKey)
                    self.bridge.setCurrentRoute(routeKey)
                break

    def toggleSidebar(self):
        current_width = self.sidebarContainer.width()
        new_width = 48 if current_width > 100 else 200
        self.sidebarContainer.setFixedWidth(new_width)
        self.bridge.sidebarExpandChanged.emit(new_width > 100)


class Widget(QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent=parent)
        layout = QVBoxLayout(self)
        label = QLabel(text, self)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setStyleSheet("QLabel { font-size: 24px; color: #555; }")


if __name__ == "__main__":
    import sys
    from qfluentwidgets import Theme, qconfig

    # Enable high DPI scaling
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )

    # Set QML Style to Basic to allow customization
    from PySide6.QtQuickControls2 import QQuickStyle

    QQuickStyle.setStyle("Basic")

    app = QApplication(sys.argv)
    w = FluentHybridWindow()

    # Add sub interfaces with FluentIcon
    w.addSubInterface(Widget("Home Interface"), FluentIcon.HOME, "Home")
    w.addSubInterface(Widget("Music Interface"), FluentIcon.MUSIC, "Music")
    w.addSubInterface(Widget("Video Interface"), FluentIcon.VIDEO, "Video")
    w.addSubInterface(Widget("Folder Interface"), FluentIcon.FOLDER, "Files")
    w.addSubInterface(Widget("Settings Interface"), FluentIcon.SETTING, "Settings")

    w.setWindowTitle("Fluent Hybrid Window Demo")
    w.resize(1000, 700)
    w.show()

    sys.exit(app.exec())
