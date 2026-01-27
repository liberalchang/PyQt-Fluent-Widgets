# coding:utf-8
from typing import Union
import sys

from PySide6.QtCore import Qt, QSize, QRect, QRectF, QTimer
from PySide6.QtGui import QIcon, QPainter, QColor
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QApplication, QGraphicsOpacityEffect

from ..common.config import qconfig, WindowEffect
from ..common.icon import FluentIconBase, toQIcon, drawIcon
from ..common.router import qrouter
from ..common.style_sheet import FluentStyleSheet, isDarkTheme, setTheme, Theme
from ..common.animation import BackgroundAnimationWidget
from ..components.widgets.frameless_window import FramelessWindow
from ..components.widgets.label import CaptionLabel
from ..components.navigation import (NavigationInterface, NavigationBar, NavigationItemPosition,
                                     NavigationBarPushButton, NavigationTreeWidget, NavigationDisplayMode)
from .stacked_widget import StackedWidget

from qframelesswindow import TitleBar, TitleBarBase, TitleBarButton


class FluentWidget(BackgroundAnimationWidget, FramelessWindow):
    """ Fluent widget """

    def __init__(self, parent=None):
        self._isMicaEnabled = False
        self._isAcrylicEnabled = False
        self._acrylicOpacity = 0.5
        self._lightBackgroundColor = QColor(240, 244, 249)
        self._darkBackgroundColor = QColor(32, 32, 32)
        super().__init__(parent=parent)

        # enable window effect based on config
        self.setWindowEffect(qconfig.get(qconfig.windowEffect))

        # show system title bar buttons on macOS
        if sys.platform == "darwin":
            self.setSystemTitleBarButtonVisible(True)

        # set up title bar
        self.setTitleBar(FluentWidgetTitleBar(self))

        qconfig.themeChangedFinished.connect(self._onThemeChangedFinished)

    def setCustomBackgroundColor(self, light, dark):
        """ set custom background color

        Parameters
        ----------
        light, dark: QColor | Qt.GlobalColor | str
            background color in light/dark theme mode
        """
        self._lightBackgroundColor = QColor(light)
        self._darkBackgroundColor = QColor(dark)
        self.setBackgroundColor(self._normalBackgroundColor())

    def setWindowEffect(self, effect: WindowEffect):
        """ set window effect """
        if effect == WindowEffect.MICA:
            self.setMicaEffectEnabled(True)
        elif effect == WindowEffect.ACRYLIC:
            self.setAcrylicEffectEnabled(True)
        else:
            self.setMicaEffectEnabled(False)
            self.setAcrylicEffectEnabled(False)

    def _normalBackgroundColor(self):
        if not self.isMicaEffectEnabled():
            return self._darkBackgroundColor if isDarkTheme() else self._lightBackgroundColor

        return QColor(0, 0, 0, 0)

    def _onThemeChangedFinished(self):
        if self.isMicaEffectEnabled():
            self.windowEffect.setMicaEffect(self.winId(), isDarkTheme())
        elif self.isAcrylicEffectEnabled():
            self.setAcrylicEffectEnabled(True)

    def paintEvent(self, e):
        super().paintEvent(e)
        
        if self.isAcrylicEffectEnabled() or self.isMicaEffectEnabled():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(Qt.NoPen)
            painter.setBrush(Qt.transparent)
            painter.setCompositionMode(QPainter.CompositionMode_Clear)
            painter.fillRect(self.rect(), Qt.transparent)
            painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
        else:
            painter = QPainter(self)
            painter.setPen(Qt.NoPen)
            painter.setBrush(self.backgroundColor)
            painter.drawRect(self.rect())

    def showEvent(self, e):
        super().showEvent(e)
        # reapply mica/acrylic effect after window is fully initialized
        if self.isMicaEffectEnabled():
            self.windowEffect.setMicaEffect(self.winId(), isDarkTheme())
        elif self.isAcrylicEffectEnabled():
            self.setAcrylicEffectEnabled(True)

    def setMicaEffectEnabled(self, isEnabled: bool):
        """ set whether the mica effect is enabled, only available on Win11 """
        if sys.platform != 'win32' or sys.getwindowsversion().build < 22000:
            return

        self._isMicaEnabled = isEnabled

        if isEnabled:
            self._isAcrylicEnabled = False
            self.windowEffect.removeBackgroundEffect(self.winId())
            self.windowEffect.setMicaEffect(self.winId(), isDarkTheme())
            self.setAttribute(Qt.WA_TranslucentBackground)
        else:
            self.windowEffect.removeBackgroundEffect(self.winId())

        self.setBackgroundColor(self._normalBackgroundColor())

    def setAcrylicEffectEnabled(self, isEnabled: bool):
        """ set whether the acrylic effect is enabled, only available on Win11 """
        if sys.platform != 'win32' or sys.getwindowsversion().build < 22000:
            return

        self._isAcrylicEnabled = isEnabled

        if isEnabled:
            self._isMicaEnabled = False
            self.windowEffect.removeBackgroundEffect(self.winId())
            self.setAttribute(Qt.WA_TranslucentBackground)
            
            opacity_hex = hex(int(self._acrylicOpacity * 255))[2:].upper().zfill(2)
            color = f"101010{opacity_hex}" if isDarkTheme() else f"F2F2F2{opacity_hex}"
            self.windowEffect.setAcrylicEffect(self.winId(), gradientColor=color)
            
            self.setBackgroundColor(Qt.transparent)
        else:
            self.windowEffect.removeBackgroundEffect(self.winId())
            self.setAttribute(Qt.WA_TranslucentBackground, False)
            self.setBackgroundColor(self._normalBackgroundColor())

    def setAcrylicOpacity(self, opacity: float):
        """ set the opacity of acrylic effect
        
        Parameters
        ----------
        opacity: float
            opacity value, range from 0 to 1
        """
        if not 0 <= opacity <= 1:
            return
            
        self._acrylicOpacity = opacity
        if self.isAcrylicEffectEnabled():
            self.setAcrylicEffectEnabled(True)

    def isMicaEffectEnabled(self):
        return self._isMicaEnabled

    def isAcrylicEffectEnabled(self):
        return self._isAcrylicEnabled

    def setWindowTitleBarColor(self, color: Union[QColor, str]):
        """ set title label background color """
        c = QColor(color)
        self.titleBar.titleLabel.setStyleSheet(f"background-color: {c.name(QColor.HexArgb)}; padding: 0 4px; border-radius: 4px;")

    # def setTitleBarBackgroundColor(self, color: Union[QColor, str]):
    #     """ set title bar background color """
    #     c = QColor(color)
    #     self.titleBar.setStyleSheet(f"background-color: {c.name(QColor.HexArgb)}")

    def setWindowTitleColor(self, color: Union[QColor, str]):
        """ set title text color """
        c = QColor(color)
        self.titleBar.titleLabel.setStyleSheet(f"color: {c.name(QColor.HexArgb)}")

    def setWindowBorderColor(self, color: Union[QColor, str]):
        """ set window border color """
        if sys.platform != 'win32' or sys.getwindowsversion().build < 22000:
            return

        from ctypes import c_int, byref, sizeof
        import ctypes

        c = QColor(color)
        # DWM expects 0x00BBGGRR
        color_value = (c.blue() << 16) | (c.green() << 8) | c.red()

        DWMWA_BORDER_COLOR = 34
        dwAttribute = DWMWA_BORDER_COLOR
        pvAttribute = c_int(color_value)
        cbAttribute = sizeof(pvAttribute)

        ctypes.windll.dwmapi.DwmSetWindowAttribute(
            int(self.winId()), dwAttribute, byref(pvAttribute), cbAttribute
        )

    def setWidgetOpacity(self, widget: QWidget, opacity: float):
        """ set opacity of any widget """
        effect = QGraphicsOpacityEffect(widget)
        effect.setOpacity(opacity)
        widget.setGraphicsEffect(effect)

    def systemTitleBarRect(self, size: QSize) -> QRect:
        """ Returns the system title bar rect, only works for macOS

        Parameters
        ----------
        size: QSize
            original system title bar rect
        """
        return QRect(0, 0 if self.isFullScreen() else 2, 75, size.height())

    def setTitleBar(self, titleBar):
        super().setTitleBar(titleBar)

        # hide title bar buttons on macOS
        if sys.platform == "darwin" and self.isSystemButtonVisible() and isinstance(titleBar, TitleBarBase):
            titleBar.minBtn.hide()
            titleBar.maxBtn.hide()
            titleBar.closeBtn.hide()


class FluentWindowBase(FluentWidget):
    """ Fluent window base class """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.stackedWidget = StackedWidget(self)
        self.navigationInterface = None

        # initialize layout
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)

        FluentStyleSheet.FLUENT_WINDOW.apply(self.stackedWidget)

    def addSubInterface(self, interface: QWidget, icon: Union[FluentIconBase, QIcon, str], text: str,
                        position=NavigationItemPosition.TOP):
        """ add sub interface """
        raise NotImplementedError

    def removeInterface(self, interface: QWidget, isDelete=False):
        """ remove sub interface

        Parameters
        ----------
        interface: QWidget
            sub interface to be removed

        isDelete: bool
            whether to delete the sub interface
        """
        raise NotImplementedError

    def switchTo(self, interface: QWidget):
        self.stackedWidget.setCurrentWidget(interface, popOut=False)

    def _onCurrentInterfaceChanged(self, index: int):
        widget = self.stackedWidget.widget(index)
        self.navigationInterface.setCurrentItem(widget.objectName())
        qrouter.push(self.stackedWidget, widget.objectName())

        self._updateStackedBackground()

    def _updateStackedBackground(self):
        isTransparent = self.stackedWidget.currentWidget().property("isStackedTransparent")
        if bool(self.stackedWidget.property("isTransparent")) == isTransparent:
            return

        self.stackedWidget.setProperty("isTransparent", isTransparent)
        self.stackedWidget.setStyle(QApplication.style())

    def systemTitleBarRect(self, size: QSize) -> QRect:
        """ Returns the system title bar rect, only works for macOS

        Parameters
        ----------
        size: QSize
            original system title bar rect
        """
        return QRect(size.width() - 75, 0 if self.isFullScreen() else 8, 75, size.height())


class FluentTitleBarButton(TitleBarButton):
    """ Fluent title bar button """

    def __init__(self, icon: Union[str, QIcon, FluentIconBase], parent=None):
        super().__init__(parent)
        self.setIcon(icon)

    def setIcon(self, icon: Union[str, QIcon, FluentIconBase]):
        self._icon = icon
        self.update()

    def icon(self) -> QIcon:
        return toQIcon(self._icon)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing |
                               QPainter.SmoothPixmapTransform)
        _, bgColor = self._getColors()

        # draw background
        painter.setBrush(bgColor)
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())

        # draw icon
        iw, ih = self.iconSize().width(), self.iconSize().height()
        x = (self.width() - iw) / 2
        y = (self.height() - ih) / 2
        drawIcon(self._icon, painter, QRectF(x, y, iw, ih))



class FluentTitleBar(TitleBar):
    """ Fluent title bar"""

    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedHeight(48)
        self.hBoxLayout.removeWidget(self.minBtn)
        self.hBoxLayout.removeWidget(self.maxBtn)
        self.hBoxLayout.removeWidget(self.closeBtn)

        # add window icon
        self.iconLabel = QLabel(self)
        self.iconLabel.setFixedSize(18, 18)
        self.hBoxLayout.insertWidget(0, self.iconLabel, 0, Qt.AlignLeft | Qt.AlignVCenter)
        self.window().windowIconChanged.connect(self.setIcon)

        # add title label
        self.titleLabel = CaptionLabel(self)
        self.hBoxLayout.insertWidget(1, self.titleLabel, 0, Qt.AlignLeft | Qt.AlignVCenter)
        self.titleLabel.setObjectName('titleLabel')
        self.window().windowTitleChanged.connect(self.setTitle)

        self.vBoxLayout = QVBoxLayout()
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setSpacing(0)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setAlignment(Qt.AlignTop)
        self.buttonLayout.addWidget(self.minBtn)
        self.buttonLayout.addWidget(self.maxBtn)
        self.buttonLayout.addWidget(self.closeBtn)
        self.vBoxLayout.addLayout(self.buttonLayout)
        self.vBoxLayout.addStretch(1)
        self.hBoxLayout.addLayout(self.vBoxLayout, 0)

        FluentStyleSheet.FLUENT_WINDOW.apply(self)

    def setTitle(self, title):
        self.titleLabel.setText(title)
        self.titleLabel.adjustSize()

    def setIcon(self, icon):
        self.iconLabel.setPixmap(QIcon(icon).pixmap(18, 18))


class FluentWindow(FluentWindowBase):
    """ Fluent window """

    def __init__(self, parent=None, showReturnButton=True):
        super().__init__(parent)
        self.setTitleBar(FluentTitleBar(self))

        self.navigationInterface = NavigationInterface(self, showReturnButton=showReturnButton)
        self.widgetLayout = QHBoxLayout()

        # initialize layout
        self.hBoxLayout.addWidget(self.navigationInterface)
        self.hBoxLayout.addLayout(self.widgetLayout)
        self.hBoxLayout.setStretchFactor(self.widgetLayout, 1)

        self.widgetLayout.addWidget(self.stackedWidget)
        self.widgetLayout.setContentsMargins(0, 48, 0, 0)

        self.navigationInterface.displayModeChanged.connect(self.titleBar.raise_)
        self.titleBar.raise_()

    def addSubInterface(self, interface: QWidget, icon: Union[FluentIconBase, QIcon, str], text: str,
                        position=NavigationItemPosition.TOP, parent=None, isTransparent=False) -> NavigationTreeWidget:
        """ add sub interface, the object name of `interface` should be set already
        before calling this method

        Parameters
        ----------
        interface: QWidget
            the subinterface to be added

        icon: FluentIconBase | QIcon | str
            the icon of navigation item

        text: str
            the text of navigation item

        position: NavigationItemPosition
            the position of navigation item

        parent: QWidget | str
            * QWidget: the parent of navigation item
            * str: the parent route key of navigation item

        isTransparent: bool
            whether to use transparent background
        """
        if not interface.objectName():
            raise ValueError("The object name of `interface` can't be empty string.")

        parentRouteKey = parent
        if parent and isinstance(parent, QWidget):
            parentRouteKey = parent.objectName()
            if not parentRouteKey:
                raise ValueError("The object name of `parent` can't be empty string.")

        interface.setProperty("isStackedTransparent", isTransparent)
        self.stackedWidget.addWidget(interface)

        # add navigation item
        routeKey = interface.objectName()
        item = self.navigationInterface.addItem(
            routeKey=routeKey,
            icon=icon,
            text=text,
            onClick=lambda: self.switchTo(interface),
            position=position,
            tooltip=text,
            parentRouteKey=parentRouteKey
        )

        # initialize selected item
        if self.stackedWidget.count() == 1:
            self.stackedWidget.currentChanged.connect(self._onCurrentInterfaceChanged)
            self.navigationInterface.setCurrentItem(routeKey)
            qrouter.setDefaultRouteKey(self.stackedWidget, routeKey)

        self._updateStackedBackground()

        return item

    def removeInterface(self, interface, isDelete=False):
        self.navigationInterface.removeWidget(interface.objectName())
        self.stackedWidget.removeWidget(interface)
        interface.hide()

        if isDelete:
            interface.deleteLater()

    def resizeEvent(self, e):
        # 确保初始化已完成，避免在初始化完成前触发展开导致标题栏布局错乱问题
        if not hasattr(self, 'navigationItems'):
            super().resizeEvent(e)
            return
            
        # 如果启用了自动伸缩，则由NavigationPanel内部处理，这里不再重复处理
        if self.navigationInterface.isAutoResizeEnabled():
            super().resizeEvent(e)
            return
            
        # 实现滞后逻辑：
        # 当窗口宽度 >= 1200 且未展开时，强制展开
        # 注意：NavigationPanel 内置逻辑会在 width < minimumExpandWidth (800) 时自动折叠
        if self.width() >= 1200 and self.navigationInterface.panel.displayMode != NavigationDisplayMode.EXPAND:
            self.navigationInterface.expand()
            
        super().resizeEvent(e)


class MSFluentTitleBar(FluentTitleBar):

    def __init__(self, parent):
        super().__init__(parent)
        self.hBoxLayout.insertSpacing(0, 20)
        self.hBoxLayout.insertSpacing(2, 2)


class FluentWidgetTitleBar(FluentTitleBar):

    def __init__(self, parent):
        super().__init__(parent)

        if sys.platform == "darwin":
            self.iconLabel.hide()
            self.titleLabel.hide()
            self.setFixedHeight(28)
        else:
            self.hBoxLayout.setContentsMargins(16, 0, 0, 0)
            self.setFixedHeight(self.buttonLayout.sizeHint().height())

        for button in self.findChildren(TitleBarButton):
            FluentStyleSheet.FLUENT_WINDOW.apply(button)



class MSFluentWindow(FluentWindowBase):
    """ Fluent window in Microsoft Store style """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitleBar(MSFluentTitleBar(self))

        self.navigationInterface = NavigationBar(self)

        # initialize layout
        self.hBoxLayout.setContentsMargins(0, 48, 0, 0)
        self.hBoxLayout.addWidget(self.navigationInterface)
        self.hBoxLayout.addWidget(self.stackedWidget, 1)

        self.titleBar.raise_()
        self.titleBar.setAttribute(Qt.WA_StyledBackground)

    def addSubInterface(self, interface: QWidget, icon: Union[FluentIconBase, QIcon, str], text: str,
                        selectedIcon=None, position=NavigationItemPosition.TOP, isTransparent=False) -> NavigationBarPushButton:
        """ add sub interface, the object name of `interface` should be set already
        before calling this method

        Parameters
        ----------
        interface: QWidget
            the subinterface to be added

        icon: FluentIconBase | QIcon | str
            the icon of navigation item

        text: str
            the text of navigation item

        selectedIcon: str | QIcon | FluentIconBase
            the icon of navigation item in selected state

        position: NavigationItemPosition
            the position of navigation item
        """
        if not interface.objectName():
            raise ValueError("The object name of `interface` can't be empty string.")

        interface.setProperty("isStackedTransparent", isTransparent)
        self.stackedWidget.addWidget(interface)

        # add navigation item
        routeKey = interface.objectName()
        item = self.navigationInterface.addItem(
            routeKey=routeKey,
            icon=icon,
            text=text,
            onClick=lambda: self.switchTo(interface),
            selectedIcon=selectedIcon,
            position=position
        )

        if self.stackedWidget.count() == 1:
            self.stackedWidget.currentChanged.connect(self._onCurrentInterfaceChanged)
            self.navigationInterface.setCurrentItem(routeKey)
            qrouter.setDefaultRouteKey(self.stackedWidget, routeKey)

        self._updateStackedBackground()

        return item

    def removeInterface(self, interface, isDelete=False):
        self.navigationInterface.removeWidget(interface.objectName())
        self.stackedWidget.removeWidget(interface)
        interface.hide()

        if isDelete:
            interface.deleteLater()


class SplitTitleBar(TitleBar):

    def __init__(self, parent):
        super().__init__(parent)
        # add window icon
        self.iconLabel = QLabel(self)
        self.iconLabel.setFixedSize(18, 18)
        self.hBoxLayout.insertSpacing(0, 12)
        self.hBoxLayout.insertWidget(1, self.iconLabel, 0, Qt.AlignLeft | Qt.AlignBottom)
        self.window().windowIconChanged.connect(self.setIcon)

        # add title label
        self.titleLabel = QLabel(self)
        self.hBoxLayout.insertWidget(2, self.titleLabel, 0, Qt.AlignLeft | Qt.AlignBottom)
        self.titleLabel.setObjectName('titleLabel')
        self.window().windowTitleChanged.connect(self.setTitle)

        FluentStyleSheet.FLUENT_WINDOW.apply(self)

    def setTitle(self, title):
        self.titleLabel.setText(title)
        self.titleLabel.adjustSize()

    def setIcon(self, icon):
        self.iconLabel.setPixmap(QIcon(icon).pixmap(18, 18))


class SplitFluentWindow(FluentWindow):
    """ Fluent window with split style """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitleBar(SplitTitleBar(self))

        if sys.platform == "darwin":
            self.titleBar.setFixedHeight(48)

        self.widgetLayout.setContentsMargins(0, 0, 0, 0)

        self.titleBar.raise_()
        self.navigationInterface.displayModeChanged.connect(self.titleBar.raise_)


class FluentBackgroundTheme:
    """ Fluent background theme """
    DEFAULT = (QColor(243, 243, 243), QColor(32, 32, 32))   # light, dark
    DEFAULT_BLUE = (QColor(240, 244, 249), QColor(25, 33, 42))
