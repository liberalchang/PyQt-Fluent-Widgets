# coding:utf-8
from typing import Dict, Union

from PySide6.QtCore import Qt, QRect, QPropertyAnimation, QEasingCurve, Property, QRectF, QPoint, QEvent
from PySide6.QtGui import QFont, QPainter, QColor, QIcon
from PySide6.QtWidgets import QWidget, QHBoxLayout

from ...common.config import isDarkTheme
from ...common.font import setFont
from ...common.style_sheet import themeColor
from ...common.color import autoFallbackThemeColor
from ...common.icon import drawIcon, FluentIconBase, toQIcon
from ...common.icon import FluentIcon as FIF
from ...common.router import qrouter
from ...common.style_sheet import FluentStyleSheet
from ..widgets.scroll_area import ScrollArea
from ..widgets.tool_tip import ToolTipFilter
from .navigation_widget import NavigationPushButton, NavigationWidget, NavigationIndicator, NavigationToolButton
from .navigation_panel import RouteKeyError, NavigationItemPosition


class TopNavigationBarPushButton(NavigationPushButton):
    """ Top navigation bar push button (horizontal layout) """

    def __init__(self, icon: Union[str, QIcon, FIF], text: str, isSelectable: bool, selectedIcon=None, parent=None):
        super().__init__(icon, text, isSelectable, parent)
        self._selectedIcon = selectedIcon
        self._isTextVisible = True
        self.lightSelectedColor = QColor()
        self.darkSelectedColor = QColor()

        self._updateSize()
        setFont(self, 12)

    def setSelectedColor(self, light, dark):
        self.lightSelectedColor = QColor(light)
        self.darkSelectedColor = QColor(dark)
        self.update()

    def selectedIcon(self):
        if self._selectedIcon:
            return toQIcon(self._selectedIcon)

        return QIcon()

    def setSelectedIcon(self, icon: Union[str, QIcon, FIF]):
        self._selectedIcon = icon
        self.update()

    def setTextVisible(self, isVisible: bool):
        """ Set whether text is visible """
        if self._isTextVisible == isVisible:
            return

        self._isTextVisible = isVisible
        self._updateSize()
        self.update()

    def isTextVisible(self):
        return self._isTextVisible

    def _updateSize(self):
        """ Update button size based on text visibility """
        if self._isTextVisible:
            # Calculate width based on text length
            textWidth = self.fontMetrics().boundingRect(self.text()).width()
            width = max(80, min(150, 48 + textWidth + 20))
            self.setFixedSize(width, 48)
        else:
            # Icon only mode
            self.setFixedSize(60, 48)

    def indicatorRect(self):
        """ Get the indicator geometry (bottom center) """
        width = int(self.width() * 0.6)
        x = (self.width() - width) / 2
        return QRectF(x, self.height() - 3, width, 3)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing |
                               QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)
        painter.setPen(Qt.NoPen)

        self._drawBackground(painter)
        self._drawIcon(painter)
        self._drawText(painter)

    def _drawBackground(self, painter: QPainter):
        if self.isSelected or self.isAboutSelected:
            painter.setBrush(QColor(255, 255, 255, 42) if isDarkTheme() else Qt.white)
            painter.drawRoundedRect(self.rect(), 5, 5)

            # Draw indicator at bottom
            if not self.isAboutSelected:
                painter.setBrush(autoFallbackThemeColor(self.lightSelectedColor, self.darkSelectedColor))
                if not self.isPressed:
                    painter.drawRoundedRect(self.indicatorRect(), 1.5, 1.5)
                else:
                    rect = self.indicatorRect()
                    painter.drawRoundedRect(rect.adjusted(0, 2, 0, 0), 1.5, 1.5)
        elif self.isPressed or self.isEnter:
            c = 255 if isDarkTheme() else 0
            alpha = 9 if self.isEnter else 6
            painter.setBrush(QColor(c, c, c, alpha))
            painter.drawRoundedRect(self.rect(), 5, 5)

    def _drawIcon(self, painter: QPainter):
        if (self.isPressed or not self.isEnter) and not (self.isSelected or self.isAboutSelected):
            painter.setOpacity(0.6)
        if not self.isEnabled():
            painter.setOpacity(0.4)

        # Icon position: left side, vertically centered
        if self._isTextVisible:
            iconX = 16
        else:
            iconX = (self.width() - 20) / 2

        iconY = (self.height() - 20) / 2
        rect = QRectF(iconX, iconY, 20, 20)

        selectedIcon = self._selectedIcon or self._icon

        if isinstance(selectedIcon, FluentIconBase) and (self.isSelected or self.isAboutSelected):
            color = autoFallbackThemeColor(self.lightSelectedColor, self.darkSelectedColor)
            selectedIcon.render(painter, rect, fill=color.name())
        elif self.isSelected or self.isAboutSelected:
            drawIcon(selectedIcon, painter, rect)
        else:
            drawIcon(self._icon, painter, rect)

    def _drawText(self, painter: QPainter):
        if not self._isTextVisible:
            return

        if self.isSelected or self.isAboutSelected:
            painter.setPen(autoFallbackThemeColor(self.lightSelectedColor, self.darkSelectedColor))
        else:
            painter.setPen(Qt.white if isDarkTheme() else Qt.black)

        painter.setFont(self.font())
        # Text position: right of icon
        textX = 44
        rect = QRect(textX, 0, self.width() - textX, self.height())
        painter.drawText(rect, Qt.AlignLeft | Qt.AlignVCenter, self.text())

    def setText(self, text: str):
        super().setText(text)
        if self._isTextVisible:
            self._updateSize()


class TopNavigationBar(QWidget):
    """ Top navigation bar with horizontal layout """

    def __init__(self, parent=None, showReturnButton=False):
        """
        Parameters
        ----------
        parent: QWidget
            parent widget
        
        showReturnButton: bool
            whether to show return button
        """
        super().__init__(parent=parent)
        self.indicator = NavigationIndicator(self)
        self._isIndicatorAnimationEnabled = True
        self._textHideWidth = 800
        self._textShowWidth = 1200
        self._isTextVisible = True
        self._isReturnButtonVisible = showReturnButton

        self.lightSelectedColor = QColor()
        self.darkSelectedColor = QColor()

        self.scrollArea = ScrollArea(self)
        self.scrollWidget = QWidget()
        self.returnButton = NavigationToolButton(FIF.RETURN, self)

        self.hBoxLayout = QHBoxLayout(self)
        self.leftLayout = QHBoxLayout()
        self.rightLayout = QHBoxLayout()
        self.scrollLayout = QHBoxLayout(self.scrollWidget)

        self.items = {}   # type: Dict[str, NavigationWidget]
        self.history = qrouter
        self._currentRouteKey = None
        self._stackedWidget = None  # Reference to external stacked widget

        self.__initWidget()

    def __initWidget(self):
        self.setFixedHeight(56)
        self.setAttribute(Qt.WA_StyledBackground)
        self.window().installEventFilter(self)

        # Initialize return button
        self.returnButton.setDisabled(True)
        self.returnButton.setVisible(self._isReturnButtonVisible)
        self.returnButton.clicked.connect(self.history.pop)
        self.history.emptyChanged.connect(self.returnButton.setDisabled)
        
        # Add tooltip
        self.returnButton.installEventFilter(ToolTipFilter(self.returnButton, 1000))
        self.returnButton.setToolTip(self.tr('Back'))

        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.verticalScrollBar().setEnabled(False)
        self.scrollArea.setWidget(self.scrollWidget)
        self.scrollArea.setWidgetResizable(True)

        self.scrollWidget.setObjectName('scrollWidget')
        FluentStyleSheet.NAVIGATION_INTERFACE.apply(self)
        FluentStyleSheet.NAVIGATION_INTERFACE.apply(self.scrollWidget)
        self.__initLayout()

        self.indicator.aniFinished.connect(self._onIndicatorAniFinished)

    def __initLayout(self):
        self.hBoxLayout.setContentsMargins(5, 0, 5, 0)
        self.leftLayout.setContentsMargins(0, 4, 0, 4)
        self.rightLayout.setContentsMargins(0, 4, 0, 4)
        self.scrollLayout.setContentsMargins(0, 4, 0, 4)
        self.hBoxLayout.setSpacing(4)
        self.leftLayout.setSpacing(4)
        self.rightLayout.setSpacing(4)
        self.scrollLayout.setSpacing(4)

        # Add return button to left layout if visible
        if self._isReturnButtonVisible:
            self.leftLayout.addWidget(self.returnButton, 0, Qt.AlignLeft | Qt.AlignVCenter)

        self.hBoxLayout.addLayout(self.leftLayout, 0)
        self.hBoxLayout.addWidget(self.scrollArea, 1)
        self.hBoxLayout.addLayout(self.rightLayout, 0)

        self.leftLayout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.scrollLayout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.rightLayout.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

    def widget(self, routeKey: str):
        if routeKey not in self.items:
            raise RouteKeyError(f"`{routeKey}` is illegal.")

        return self.items[routeKey]

    def addItem(self, routeKey: str, icon: Union[str, QIcon, FluentIconBase], text: str, onClick=None,
                selectable=True, selectedIcon=None, position=NavigationItemPosition.SCROLL):
        """ Add navigation item

        Parameters
        ----------
        routeKey: str
            the unique name of item

        icon: str | QIcon | FluentIconBase
            the icon of navigation item

        text: str
            the text of navigation item

        onClick: callable
            the slot connected to item clicked signal

        selectable: bool
            whether the item is selectable

        selectedIcon: str | QIcon | FluentIconBase
            the icon of navigation item in selected state

        position: NavigationItemPosition
            where the button is added (TOP->LEFT, SCROLL->SCROLL, BOTTOM->RIGHT)
        """
        return self.insertItem(-1, routeKey, icon, text, onClick, selectable, selectedIcon, position)

    def addWidget(self, routeKey: str, widget: NavigationWidget, onClick=None, position=NavigationItemPosition.SCROLL):
        """ Add custom widget

        Parameters
        ----------
        routeKey: str
            the unique name of item

        widget: NavigationWidget
            the custom widget to be added

        onClick: callable
            the slot connected to item clicked signal

        position: NavigationItemPosition
            where the button is added
        """
        self.insertWidget(-1, routeKey, widget, onClick, position)

    def insertItem(self, index: int, routeKey: str, icon: Union[str, QIcon, FluentIconBase], text: str, onClick=None,
                   selectable=True, selectedIcon=None, position=NavigationItemPosition.SCROLL):
        """ Insert navigation item

        Parameters
        ----------
        index: int
            the insert position of parent widget

        routeKey: str
            the unique name of item

        icon: str | QIcon | FluentIconBase
            the icon of navigation item

        text: str
            the text of navigation item

        onClick: callable
            the slot connected to item clicked signal

        selectable: bool
            whether the item is selectable

        selectedIcon: str | QIcon | FluentIconBase
            the icon of navigation item in selected state

        position: NavigationItemPosition
            where the button is added
        """
        if routeKey in self.items:
            return

        w = TopNavigationBarPushButton(icon, text, selectable, selectedIcon, self)
        w.setSelectedColor(self.lightSelectedColor, self.darkSelectedColor)
        w.setTextVisible(self._isTextVisible)
        self.insertWidget(index, routeKey, w, onClick, position)
        return w

    def insertWidget(self, index: int, routeKey: str, widget: NavigationWidget, onClick=None,
                     position=NavigationItemPosition.SCROLL):
        """ Insert custom widget

        Parameters
        ----------
        index: int
            insert position

        routeKey: str
            the unique name of item

        widget: NavigationWidget
            the custom widget to be added

        onClick: callable
            the slot connected to item clicked signal

        position: NavigationItemPosition
            where the button is added
        """
        if routeKey in self.items:
            return

        self._registerWidget(routeKey, widget, onClick)
        self._insertWidgetToLayout(index, widget, position)

    def _registerWidget(self, routeKey: str, widget: NavigationWidget, onClick):
        """ Register widget """
        widget.clicked.connect(self._onWidgetClicked)

        if onClick is not None:
            widget.clicked.connect(onClick)

        widget.setProperty('routeKey', routeKey)
        self.items[routeKey] = widget

    def _insertWidgetToLayout(self, index: int, widget: NavigationWidget, position: NavigationItemPosition):
        """ Insert widget to layout """
        # Map vertical positions to horizontal: TOP->LEFT, SCROLL->SCROLL, BOTTOM->RIGHT
        if position == NavigationItemPosition.TOP:
            widget.setParent(self)
            self.leftLayout.insertWidget(index, widget, 0, Qt.AlignLeft | Qt.AlignVCenter)
        elif position == NavigationItemPosition.SCROLL:
            widget.setParent(self.scrollWidget)
            self.scrollLayout.insertWidget(index, widget, 0, Qt.AlignLeft | Qt.AlignVCenter)
        else:  # BOTTOM -> RIGHT
            widget.setParent(self)
            self.rightLayout.insertWidget(index, widget, 0, Qt.AlignRight | Qt.AlignVCenter)

        widget.show()

    def removeWidget(self, routeKey: str):
        """ Remove widget

        Parameters
        ----------
        routeKey: str
            the unique name of item
        """
        if routeKey not in self.items:
            return

        widget = self.items.pop(routeKey)
        widget.deleteLater()
        self.history.remove(routeKey)

    def currentItem(self):
        return self.widget(self._currentRouteKey) if self._currentRouteKey else None

    def setCurrentItem(self, routeKey: str):
        """ Set current selected item

        Parameters
        ----------
        routeKey: str
            the unique name of item
        """
        if routeKey not in self.items or routeKey == self._currentRouteKey:
            return

        self._stopIndicatorAnimation()

        prevItem = self.currentItem()
        self._currentRouteKey = routeKey
        
        # Push to router if stacked widget is bound
        if self._stackedWidget:
            self.history.push(self._stackedWidget, routeKey)

        # Early return if indicator is not enabled or previous selected item is None
        if not self.isIndicatorAnimationEnabled() or prevItem is None:
            for k, widget in self.items.items():
                widget.setSelected(k == routeKey)

            return

        # Calculate the start and final geometry for animation
        newItem = self.currentItem()
        preIndicatorRect = self._getIndicatorRect(prevItem)
        newIndicatorRect = self._getIndicatorRect(newItem)

        # Start animation
        prevItem.setSelected(False)
        newItem.setAboutSelected(True)
        self.indicator.raise_()
        self.indicator.setIndicatorColor(newItem.lightIndicatorColor, newItem.darkIndicatorColor)
        self.indicator.startAnimation(preIndicatorRect, newIndicatorRect)

    def setFont(self, font: QFont):
        """ Set the font of navigation item """
        super().setFont(font)

        for widget in self.buttons():
            widget.setFont(font)

    def setTextVisible(self, isVisible: bool):
        """ Set whether text is visible on all buttons """
        if isVisible == self._isTextVisible:
            return

        self._isTextVisible = isVisible
        for widget in self.buttons():
            widget.setTextVisible(isVisible)

    def isTextVisible(self):
        return self._isTextVisible

    def setSelectedColor(self, light, dark):
        """ Set the selected color of all items """
        self.lightSelectedColor = QColor(light)
        self.darkSelectedColor = QColor(dark)
        for button in self.buttons():
            button.setSelectedColor(self.lightSelectedColor, self.darkSelectedColor)

    def setResponsiveWidth(self, hideWidth: int, showWidth: int):
        """ Set responsive width thresholds

        Parameters
        ----------
        hideWidth: int
            window width threshold to hide text (show icon only)

        showWidth: int
            window width threshold to show text
        """
        self._textHideWidth = hideWidth
        self._textShowWidth = showWidth

    def setReturnButtonVisible(self, isVisible: bool):
        """ Set whether the return button is visible
        
        Parameters
        ----------
        isVisible: bool
            whether to show return button
        """
        if self._isReturnButtonVisible == isVisible:
            return
        
        self._isReturnButtonVisible = isVisible
        self.returnButton.setVisible(isVisible)
        
        # Rebuild layout to add/remove return button
        if isVisible and self.returnButton not in [self.leftLayout.itemAt(i).widget() for i in range(self.leftLayout.count())]:
            self.leftLayout.insertWidget(0, self.returnButton, 0, Qt.AlignLeft | Qt.AlignVCenter)

    def isReturnButtonVisible(self):
        """ Check if return button is visible """
        return self._isReturnButtonVisible

    def setStackedWidget(self, stackedWidget):
        """ Bind a QStackedWidget for router management
        
        Parameters
        ----------
        stackedWidget: QStackedWidget
            The stacked widget to bind for navigation routing
        """
        from PySide6.QtWidgets import QStackedWidget
        # Accept both QStackedWidget and custom StackedWidget
        if not (isinstance(stackedWidget, QStackedWidget) or hasattr(stackedWidget, 'currentChanged')):
            raise TypeError("stackedWidget must be a QStackedWidget or have similar interface")
        
        self._stackedWidget = stackedWidget

    def buttons(self):
        return [i for i in self.items.values() if isinstance(i, TopNavigationBarPushButton)]

    def isIndicatorAnimationEnabled(self):
        return self._isIndicatorAnimationEnabled

    def setIndicatorAnimationEnabled(self, isEnabled: bool):
        self._isIndicatorAnimationEnabled = isEnabled

    def _onWidgetClicked(self):
        widget = self.sender()  # type: NavigationWidget
        if widget.isSelectable:
            self.setCurrentItem(widget.property('routeKey'))

    def _getIndicatorRect(self, item: NavigationWidget):
        if not item:
            return QRect()

        pos = item.mapTo(self, QPoint(0, 0))
        rect = item.indicatorRect()
        return rect.translated(pos)

    def _stopIndicatorAnimation(self):
        if not self.isIndicatorAnimationEnabled():
            return

        self.indicator.stopAnimation()
        self._onIndicatorAniFinished()

    def _onIndicatorAniFinished(self):
        item = self.currentItem()
        if not item:
            return

        item.setAboutSelected(False)
        item.setSelected(True)
        self.indicator.hide()

    def eventFilter(self, obj, e: QEvent):
        """ Event filter to handle window resize """
        if e.type() == QEvent.Resize and obj == self.window():
            width = self.window().width()

            # Responsive text display based on window width
            if width < self._textHideWidth and self._isTextVisible:
                self.setTextVisible(False)
            elif width >= self._textShowWidth and not self._isTextVisible:
                self.setTextVisible(True)

        return super().eventFilter(obj, e)
