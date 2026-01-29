# coding:utf-8
from typing import Iterable, List, Tuple, Union
from enum import Enum

from PySide6.QtCore import Qt, QSize, QRectF, QRect, QPoint, QEvent
from PySide6.QtGui import QAction, QPainter, QColor, QFont, QHoverEvent, QPainterPath, QMouseEvent, QPen
from PySide6.QtWidgets import QLayoutItem, QWidget, QFrame, QHBoxLayout, QApplication

from ...common.font import setFont
from ...common.icon import FluentIcon, Icon, Action
from ...common.style_sheet import isDarkTheme, updateDynamicStyle
from .menu import RoundMenu, MenuAnimationType
from .button import TransparentToggleToolButton
from .tool_tip import ToolTipFilter
from .flyout import FlyoutViewBase, Flyout


class CommandButton(TransparentToggleToolButton):
    """ Command button

    Constructors
    ------------
    * CommandButton(`parent`: QWidget = None)
    * CommandButton(`icon`: QIcon | str | FluentIconBase = None, `parent`: QWidget = None)
    """

    def _postInit(self):
        super()._postInit()
        self.setCheckable(False)
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)
        setFont(self, 12)

        self._text = ''
        self._action = None
        self._isTight = False

    def setTight(self, isTight: bool):
        self._isTight = isTight
        self.update()

    def isTight(self):
        return self._isTight

    def sizeHint(self) -> QSize:
        if self.isIconOnly():
            return QSize(36, 34) if self.isTight() else QSize(48, 34)

        # get the width of text
        tw = self.fontMetrics().boundingRect(self.text()).width()

        style = self.toolButtonStyle()
        if style == Qt.ToolButtonTextBesideIcon:
            return QSize(tw + 47, 34)
        if style == Qt.ToolButtonTextOnly:
            return QSize(tw + 32, 34)

        return QSize(tw + 32, 50)

    def isIconOnly(self):
        if not self.text():
            return True

        return self.toolButtonStyle() in [Qt.ToolButtonIconOnly, Qt.ToolButtonFollowStyle]

    def _drawIcon(self, icon, painter, rect):
        pass

    def text(self):
        return self._text

    def setText(self, text: str):
        self._text = text
        self.update()

    def setAction(self, action: QAction):
        self._action = action
        self._onActionChanged()

        self.clicked.connect(action.trigger)
        action.toggled.connect(self.setChecked)
        action.changed.connect(self._onActionChanged)

        self.installEventFilter(CommandToolTipFilter(self, 700))

    def _onActionChanged(self):
        action = self.action()
        self.setIcon(action.icon())
        self.setText(action.text())
        self.setToolTip(action.toolTip())
        self.setEnabled(action.isEnabled())
        self.setCheckable(action.isCheckable())
        self.setChecked(action.isChecked())

    def action(self):
        return self._action

    def paintEvent(self, e):
        super().paintEvent(e)

        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing |
                               QPainter.SmoothPixmapTransform)

        if not self.isChecked():
            painter.setPen(Qt.white if isDarkTheme() else Qt.black)
        else:
            painter.setPen(Qt.black if isDarkTheme() else Qt.white)

        if not self.isEnabled():
            painter.setOpacity(0.43)
        elif self.isPressed:
            painter.setOpacity(0.63)

        # draw icon and text
        style = self.toolButtonStyle()
        iw, ih = self.iconSize().width(), self.iconSize().height()

        if self.isIconOnly():
            y = (self.height() - ih) / 2
            x = (self.width() - iw) / 2
            super()._drawIcon(self._icon, painter, QRectF(x, y, iw, ih))
        elif style == Qt.ToolButtonTextOnly:
            painter.drawText(self.rect(), Qt.AlignCenter, self.text())
        elif style == Qt.ToolButtonTextBesideIcon:
            y = (self.height() - ih) / 2
            super()._drawIcon(self._icon, painter, QRectF(11, y, iw, ih))

            rect = QRectF(26, 0, self.width() - 26, self.height())
            painter.drawText(rect, Qt.AlignCenter, self.text())
        elif style == Qt.ToolButtonTextUnderIcon:
            x = (self.width() - iw) / 2
            super()._drawIcon(self._icon, painter, QRectF(x, 9, iw, ih))

            rect = QRectF(0, ih + 13, self.width(), self.height() - ih - 13)
            painter.drawText(rect, Qt.AlignHCenter | Qt.AlignTop, self.text())


class CommandToolTipFilter(ToolTipFilter):
    """ Command tool tip filter """

    def _canShowToolTip(self) -> bool:
        return super()._canShowToolTip() and self.parent().isIconOnly()


class MoreActionsButton(CommandButton):
    """ More action button """

    def _postInit(self):
        super()._postInit()
        self.setIcon(FluentIcon.MORE)

    def sizeHint(self):
        return QSize(40, 34)

    def clearState(self):
        self.setAttribute(Qt.WA_UnderMouse, False)
        e = QHoverEvent(QEvent.HoverLeave, QPoint(-1, -1), QPoint())
        QApplication.sendEvent(self, e)


class CommandSeparator(QWidget):
    """ Command separator """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._orientation = Qt.Horizontal
        self._updateSize()

    def setOrientation(self, orientation: Qt.Orientation):
        """ Set separator orientation """
        if self._orientation == orientation:
            return
        
        self._orientation = orientation
        self._updateSize()
        self.update()

    def orientation(self):
        """ Get separator orientation """
        return self._orientation

    def _updateSize(self):
        """ Update size based on orientation """
        if self._orientation == Qt.Horizontal:
            self.setFixedSize(9, 34)
        else:
            self.setFixedSize(34, 9)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QColor(255, 255, 255, 21)
                       if isDarkTheme() else QColor(0, 0, 0, 15))
        
        if self._orientation == Qt.Horizontal:
            painter.drawLine(5, 2, 5, self.height() - 2)
        else:
            painter.drawLine(2, 5, self.width() - 2, 5)


class CommandMenu(RoundMenu):
    """ Command menu """

    def __init__(self, parent=None):
        super().__init__("", parent)
        self.setItemHeight(32)
        self.view.setIconSize(QSize(16, 16))

    def exec(self, pos, ani=True, aniType=MenuAnimationType.DROP_DOWN):
        return super().exec(pos, ani, aniType)


class CommandBar(QFrame):
    """ Command bar """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._orientation = Qt.Horizontal
        self._widgets = []  # type: List[QWidget]
        self._hiddenWidgets = []  # type: List[QWidget]
        self._hiddenActions = []  # type: List[QAction]

        self._menuAnimation = MenuAnimationType.DROP_DOWN
        self._toolButtonStyle = Qt.ToolButtonIconOnly
        self._iconSize = QSize(16, 16)
        self._isButtonTight = False
        self._spacing = 4

        self.moreButton = MoreActionsButton(self)
        self.moreButton.clicked.connect(self._showMoreActionsMenu)
        self.moreButton.hide()

        setFont(self, 12)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def setOrientation(self, orientation: Qt.Orientation):
        """ Set command bar orientation """
        if self._orientation == orientation:
            return
        
        self._orientation = orientation
        
        # Update separators orientation
        for widget in self._widgets:
            if isinstance(widget, CommandSeparator):
                widget.setOrientation(orientation)
        
        # Update fixed size based on orientation - 考虑拖动区域
        if self._widgets:
            if orientation == Qt.Horizontal:
                # 竖直拖动区域高度转为水平时不需要考虑
                height = max(w.height() for w in self._widgets)
                # 如果有拖动区域，确保高度足够容纳拖动区域
                if hasattr(self, '_dragHandleRect') and self._dragHandleRect.height() > 8:
                    height = max(height, self._dragHandleRect.height())
                self.setFixedHeight(height)
                self.setMaximumWidth(16777215)  # Reset width constraint
            else:
                # 水平拖动区域宽度转为竖直时不需要考虑  
                width = max(w.width() for w in self._widgets)
                # 如果有拖动区域，确保宽度足够容纳拖动区域
                if hasattr(self, '_dragHandleRect') and self._dragHandleRect.width() > 8:
                    width = max(width, self._dragHandleRect.width())
                self.setFixedWidth(width)
                self.setMaximumHeight(16777215)  # Reset height constraint
        
        self.updateGeometry()

    def orientation(self):
        """ Get command bar orientation """
        return self._orientation

    def setSpaing(self, spacing: int):
        if spacing == self._spacing:
            return

        self._spacing = spacing
        self.updateGeometry()

    def spacing(self):
        return self._spacing

    def addAction(self, action: QAction):
        """ add action

        Parameters
        ----------
        action: QAction
            the action to add
        """
        if action in self.actions():
            return

        button = self._createButton(action)
        self._insertWidgetToLayout(-1, button)
        super().addAction(action)
        return button

    def addActions(self, actions: Iterable[QAction]):
        for action in actions:
            self.addAction(action)

    def addHiddenAction(self, action: QAction):
        """ add hidden action """
        if action in self.actions():
            return

        self._hiddenActions.append(action)
        self.updateGeometry()
        super().addAction(action)

    def addHiddenActions(self, actions: List[QAction]):
        """ add hidden action """
        for action in actions:
            self.addHiddenAction(action)

    def insertAction(self, before: QAction, action: QAction):
        if before not in self.actions():
            return

        index = self.actions().index(before)
        button = self._createButton(action)
        self._insertWidgetToLayout(index, button)
        super().insertAction(before, action)
        return button

    def addSeparator(self):
        self.insertSeparator(-1)

    def insertSeparator(self, index: int):
        separator = CommandSeparator(self)
        separator.setOrientation(self._orientation)
        self._insertWidgetToLayout(index, separator)

    def addWidget(self, widget: QWidget):
        """ add widget to command bar """
        self._insertWidgetToLayout(-1, widget)

    def removeAction(self, action: QAction):
        if action not in self.actions():
            return

        for w in self.commandButtons:
            if w.action() is action:
                self._widgets.remove(w)
                w.hide()
                w.deleteLater()
                break

        self.updateGeometry()

    def removeWidget(self, widget: QWidget):
        if widget not in self._widgets:
            return

        self._widgets.remove(widget)
        self.updateGeometry()

    def removeHiddenAction(self, action: QAction):
        if action in self._hiddenActions:
            self._hiddenActions.remove(action)

    def setToolButtonStyle(self, style: Qt.ToolButtonStyle):
        """ set the style of tool button """
        if self.toolButtonStyle() == style:
            return

        self._toolButtonStyle = style
        for w in self.commandButtons:
            w.setToolButtonStyle(style)

    def toolButtonStyle(self):
        return self._toolButtonStyle

    def setButtonTight(self, isTight: bool):
        if self.isButtonTight() == isTight:
            return

        self._isButtonTight = isTight

        for w in self.commandButtons:
            w.setTight(isTight)

        self.updateGeometry()

    def isButtonTight(self):
        return self._isButtonTight

    def setIconSize(self, size: QSize):
        if size == self._iconSize:
            return

        self._iconSize = size
        for w in self.commandButtons:
            w.setIconSize(size)

    def iconSize(self):
        return self._iconSize

    def resizeEvent(self, e):
        self.updateGeometry()

    def _createButton(self, action: QAction):
        """ create command button """
        button = CommandButton(self)
        button.setAction(action)
        button.setToolButtonStyle(self.toolButtonStyle())
        button.setTight(self.isButtonTight())
        button.setIconSize(self.iconSize())
        button.setFont(self.font())
        return button

    def _insertWidgetToLayout(self, index: int, widget: QWidget):
        """ add widget to layout """
        widget.setParent(self)
        widget.show()

        if index < 0:
            self._widgets.append(widget)
        else:
            self._widgets.insert(index, widget)

        # Set fixed size based on orientation
        if self._orientation == Qt.Horizontal:
            self.setFixedHeight(max(w.height() for w in self._widgets))
        else:
            self.setFixedWidth(max(w.width() for w in self._widgets))
        
        self.updateGeometry()

    def minimumSizeHint(self) -> QSize:
        return self.moreButton.size()

    def updateGeometry(self):
        self._hiddenWidgets.clear()
        self.moreButton.hide()

        visibles = self._visibleWidgets()
        
        if self._orientation == Qt.Horizontal:
            # Horizontal layout - 考虑拖动区域偏移
            x = self.contentsMargins().left()
            # 如果是 MovableCommandBar 且有拖动区域，增加偏移
            if hasattr(self, '_dragHandleRect') and self._dragHandleRect.width() > 8:
                x += self._dragHandleRect.width()
            
            h = self.height()

            for widget in visibles:
                widget.show()
                widget.move(x, (h - widget.height()) // 2)
                x += (widget.width() + self.spacing())

            # show more actions button
            if self._hiddenActions or len(visibles) < len(self._widgets):
                self.moreButton.show()
                self.moreButton.move(x, (h - self.moreButton.height()) // 2)
        else:
            # Vertical layout - 考虑拖动区域偏移
            y = self.contentsMargins().top()
            # 如果是 MovableCommandBar 且有拖动区域，增加偏移
            if hasattr(self, '_dragHandleRect') and self._dragHandleRect.height() > 8:
                y += self._dragHandleRect.height()
            
            w = self.width()

            for widget in visibles:
                widget.show()
                widget.move((w - widget.width()) // 2, y)
                y += (widget.height() + self.spacing())

            # show more actions button
            if self._hiddenActions or len(visibles) < len(self._widgets):
                self.moreButton.show()
                self.moreButton.move((w - self.moreButton.width()) // 2, y)

        for widget in self._widgets[len(visibles):]:
            widget.hide()
            self._hiddenWidgets.append(widget)

    def _visibleWidgets(self) -> List[QWidget]:
        """ return the visible widgets in layout """
        # have enough spacing to show all widgets
        if self._orientation == Qt.Horizontal:
            if self.suitableWidth() <= self.width():
                return self._widgets

            w = self.moreButton.width()
            # 如果是 MovableCommandBar 且有拖动区域，增加拖动区域宽度
            if hasattr(self, '_dragHandleRect') and self._dragHandleRect.width() > 8:
                w += self._dragHandleRect.width()
            
            for index, widget in enumerate(self._widgets):
                w += widget.width()
                if index > 0:
                    w += self.spacing()

                if w > self.width():
                    break

            return self._widgets[:index]
        else:
            # Vertical orientation
            if self.suitableHeight() <= self.height():
                return self._widgets

            h = self.moreButton.height()
            # 如果是 MovableCommandBar 且有拖动区域，增加拖动区域高度
            if hasattr(self, '_dragHandleRect') and self._dragHandleRect.height() > 8:
                h += self._dragHandleRect.height()
            
            for index, widget in enumerate(self._widgets):
                h += widget.height()
                if index > 0:
                    h += self.spacing()

                if h > self.height():
                    break

            return self._widgets[:index]

    def suitableWidth(self):
        widths = [w.width() for w in self._widgets]
        if self._hiddenActions:
            widths.append(self.moreButton.width())
        
        # 如果是 MovableCommandBar 且有拖动区域，增加拖动区域宽度
        dragHandleWidth = 0
        if hasattr(self, '_dragHandleRect') and self._dragHandleRect.width() > 8:
            dragHandleWidth = self._dragHandleRect.width()

        return dragHandleWidth + sum(widths) + self.spacing() * max(len(widths) - 1, 0)

    def suitableHeight(self):
        """ Calculate suitable height for vertical orientation """
        heights = [w.height() for w in self._widgets]
        if self._hiddenActions:
            heights.append(self.moreButton.height())
        
        # 如果是 MovableCommandBar 且有拖动区域，增加拖动区域高度
        dragHandleHeight = 0
        if hasattr(self, '_dragHandleRect') and self._dragHandleRect.height() > 8:
            dragHandleHeight = self._dragHandleRect.height()

        return dragHandleHeight + sum(heights) + self.spacing() * max(len(heights) - 1, 0)

    def resizeToSuitableWidth(self):
        self.setFixedWidth(self.suitableWidth())

    def resizeToSuitableHeight(self):
        """ Resize to suitable height for vertical orientation """
        self.setFixedHeight(self.suitableHeight())

    def setFont(self, font: QFont):
        super().setFont(font)
        for button in self.commandButtons:
            button.setFont(font)

    @property
    def commandButtons(self):
        return [w for w in self._widgets if isinstance(w, CommandButton)]

    def setMenuDropDown(self, down: bool):
        """ set the animation direction of more actions menu """
        if down:
            self._menuAnimation = MenuAnimationType.DROP_DOWN
        else:
            self._menuAnimation = MenuAnimationType.PULL_UP

    def isMenuDropDown(self):
        return self._menuAnimation == MenuAnimationType.DROP_DOWN

    def _showMoreActionsMenu(self):
        """ show more actions menu """
        self.moreButton.clearState()

        actions = self._hiddenActions.copy()

        for w in reversed(self._hiddenWidgets):
            if isinstance(w, CommandButton):
                actions.insert(0, w.action())

        menu = CommandMenu(self)
        menu.addActions(actions)

        if self._orientation == Qt.Horizontal:
            x = -menu.width() + menu.layout().contentsMargins().right() + \
                self.moreButton.width() + 18
            if self._menuAnimation == MenuAnimationType.DROP_DOWN:
                y = self.moreButton.height()
            else:
                y = -5
        else:
            # Vertical orientation - show menu to the right
            x = self.moreButton.width()
            y = -menu.height() + menu.layout().contentsMargins().bottom() + \
                self.moreButton.height() + 18

        pos = self.moreButton.mapToGlobal(QPoint(x, y))
        menu.exec(pos, aniType=self._menuAnimation)


class CommandViewMenu(CommandMenu):
    """ Command view menu """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.view.setObjectName('commandListWidget')

    def setDropDown(self, down: bool, long=False):
        self.view.setProperty('dropDown', down)
        self.view.setProperty('long', long)
        updateDynamicStyle(self.view)

    def exec(self, pos, ani=True, aniType=MenuAnimationType.DROP_DOWN):
        return super().exec(pos, ani, aniType)


class CommandViewBar(CommandBar):
    """ Command view bar """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMenuDropDown(True)

    def setMenuDropDown(self, down: bool):
        """ set the animation direction of more actions menu """
        if down:
            self._menuAnimation = MenuAnimationType.FADE_IN_DROP_DOWN
        else:
            self._menuAnimation = MenuAnimationType.FADE_IN_PULL_UP

    def isMenuDropDown(self):
        return self._menuAnimation == MenuAnimationType.FADE_IN_DROP_DOWN

    def _showMoreActionsMenu(self):
        self.moreButton.clearState()

        actions = self._hiddenActions.copy()

        for w in reversed(self._hiddenWidgets):
            if isinstance(w, CommandButton):
                actions.insert(0, w.action())

        menu = CommandViewMenu(self)
        menu.addActions(actions)

        # adjust the shape of view
        view = self.parent()  # type: CommandBarView
        view.setMenuVisible(True)

        # adjust the shape of menu
        menu.closedSignal.connect(lambda: view.setMenuVisible(False))
        menu.setDropDown(self.isMenuDropDown(), menu.view.width() > view.width()+5)

        # adjust menu size
        if menu.view.width() < view.width():
            menu.view.setFixedWidth(view.width())
            menu.adjustSize()

        x = -menu.width() + menu.layout().contentsMargins().right() + \
            self.moreButton.width() + 18
        if self.isMenuDropDown():
            y = self.moreButton.height()
        else:
            y = -13
            menu.setShadowEffect(0, (0, 0), QColor(0, 0, 0, 0))
            menu.layout().setContentsMargins(12, 20, 12, 8)

        pos = self.moreButton.mapToGlobal(QPoint(x, y))
        menu.exec(pos, aniType=self._menuAnimation)


class CommandBarView(FlyoutViewBase):
    """ Command bar view """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.bar = CommandViewBar(self)
        self.hBoxLayout = QHBoxLayout(self)

        self.hBoxLayout.setContentsMargins(6, 6, 6, 6)
        self.hBoxLayout.addWidget(self.bar)
        self.hBoxLayout.setSizeConstraint(QHBoxLayout.SetMinAndMaxSize)

        self.setButtonTight(True)
        self.setIconSize(QSize(14, 14))

        self._isMenuVisible = False

    def setMenuVisible(self, isVisible):
        self._isMenuVisible = isVisible
        self.update()

    def addWidget(self, widget: QWidget):
        self.bar.addWidget(widget)

    def setSpaing(self, spacing: int):
        self.bar.setSpaing(spacing)

    def spacing(self):
        return self.bar.spacing()

    def addAction(self, action: QAction):
        return self.bar.addAction(action)

    def addActions(self, actions: Iterable[QAction]):
        self.bar.addActions(actions)

    def addHiddenAction(self, action: QAction):
        self.bar.addHiddenAction(action)

    def addHiddenActions(self, actions: List[QAction]):
        self.bar.addHiddenActions(actions)

    def insertAction(self, before: QAction, action: QAction):
        return self.bar.insertAction(before, action)

    def addSeparator(self):
        self.bar.addSeparator()

    def insertSeparator(self, index: int):
        self.bar.insertSeparator(index)

    def removeAction(self, action: QAction):
        self.bar.removeAction(action)

    def removeWidget(self, widget: QWidget):
        self.bar.removeWidget(widget)

    def removeHiddenAction(self, action: QAction):
        self.bar.removeAction(action)

    def setToolButtonStyle(self, style: Qt.ToolButtonStyle):
        self.bar.setToolButtonStyle(style)

    def toolButtonStyle(self):
        return self.bar.toolButtonStyle()

    def setButtonTight(self, isTight: bool):
        self.bar.setButtonTight(isTight)

    def isButtonTight(self):
        return self.bar.isButtonTight()

    def setIconSize(self, size: QSize):
        self.bar.setIconSize(size)

    def iconSize(self):
        return self.bar.iconSize()

    def setFont(self, font: QFont):
        self.bar.setFont(font)

    def setMenuDropDown(self, down: bool):
        self.bar.setMenuDropDown(down)

    def suitableWidth(self):
        m = self.contentsMargins()
        return m.left() + m.right() + self.bar.suitableWidth()

    def resizeToSuitableWidth(self):
        self.bar.resizeToSuitableWidth()
        self.setFixedWidth(self.suitableWidth())

    def actions(self):
        return self.bar.actions()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)

        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)
        path.addRoundedRect(QRectF(self.rect().adjusted(1, 1, -1, -1)), 8, 8)

        if self._isMenuVisible:
            y = self.height() - 10 if self.bar.isMenuDropDown() else 1
            path.addRect(1, y, self.width() - 2, 9)

        painter.setBrush(
            QColor(40, 40, 40) if isDarkTheme() else QColor(248, 248, 248))
        painter.setPen(
            QColor(56, 56, 56) if isDarkTheme() else QColor(233, 233, 233))
        painter.drawPath(path.simplified())


class DockPosition(Enum):
    """ Dock position enumeration """
    TOP = Qt.TopDockWidgetArea
    BOTTOM = Qt.BottomDockWidgetArea
    LEFT = Qt.LeftDockWidgetArea
    RIGHT = Qt.RightDockWidgetArea


class VerticalCommandBar(CommandBar):
    """ Vertical command bar """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setOrientation(Qt.Vertical)


class ResponsiveCommandBar(CommandBar):
    """ Responsive command bar """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._isResponsive = True

    def setResponsive(self, enabled: bool):
        """ Set responsive mode """
        self._isResponsive = enabled
        self.updateGeometry()

    def isResponsive(self):
        """ Get responsive mode """
        return self._isResponsive

    def _visibleWidgets(self) -> List[QWidget]:
        """ return the visible widgets in layout """
        if not self._isResponsive:
            return self._widgets
        
        return super()._visibleWidgets()


class MovableCommandBar(CommandBar):
    """ Movable command bar with drag and dock functionality """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._dockPosition = DockPosition.TOP
        self._dragStartPos = QPoint()
        self._isDragging = False
        self._dragHandleRect = QRect()
        self._isResponsive = True
        self._isFloating = False  # 新增：是否为自由浮动状态
        self._pendingOrientation = None  # 新增：待切换的方向
        
        self.setMouseTracking(True)
        self._updateDragHandle()
        
        # 确保初始时有正确的最小尺寸
        self.setMinimumSize(100, 40)

    def setResponsive(self, enabled: bool):
        """ Set responsive mode """
        self._isResponsive = enabled
        self.updateGeometry()

    def isResponsive(self):
        """ Get responsive mode """
        return self._isResponsive

    def _visibleWidgets(self) -> List[QWidget]:
        """ return the visible widgets in layout """
        if not self._isResponsive:
            return self._widgets
        
        return super()._visibleWidgets()

    def setDockPosition(self, position: DockPosition, force=False):
        """ Set dock position """
        if self._dockPosition == position and not force:
            return
        
        oldOrientation = self.orientation()
        
        # 先切换方向，再设置停靠位置
        if position in [DockPosition.LEFT, DockPosition.RIGHT]:
            self._pendingOrientation = Qt.Vertical
        else:
            self._pendingOrientation = Qt.Horizontal
        
        # 应用方向切换
        if self._pendingOrientation != oldOrientation:
            self.setOrientation(self._pendingOrientation)
            # 强制更新几何布局
            self.updateGeometry()
        
        self._dockPosition = position
        self._isFloating = False
        self._updateDragHandle()
        
        # 根据停靠位置调整尺寸
        if position in [DockPosition.LEFT, DockPosition.RIGHT]:
            # 竖直停靠时，调整高度
            self.resizeToSuitableHeight()
            # 重置宽度约束
            self.setMaximumWidth(16777215)
        else:
            # 水平停靠时，调整宽度
            self.resizeToSuitableWidth()
            # 重置高度约束
            self.setMaximumHeight(16777215)

    def dockPosition(self):
        """ Get dock position """
        return self._dockPosition

    def _updateDragHandle(self):
        """ Update drag handle rectangle - 增加拖动区域 """
        if self.orientation() == Qt.Horizontal:
            # 水平时，在左侧增加拖动区域
            self._dragHandleRect = QRect(0, 0, 20, self.height())
        else:
            # 竖直时，在上方增加拖动区域
            self._dragHandleRect = QRect(0, 0, self.width(), 20)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self._updateDragHandle()

    def mousePressEvent(self, event: QMouseEvent):
        """ Handle mouse press for dragging """
        if event.button() == Qt.LeftButton and self._dragHandleRect.contains(event.pos()):
            self._isDragging = True
            self._dragStartPos = event.globalPos() - self.pos()
            event.accept()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        """ Handle mouse move for dragging """
        if self._isDragging:
            # Update cursor
            self.setCursor(Qt.ClosedHandCursor)
            
            # Move the command bar
            newPos = event.globalPos() - self._dragStartPos
            self.move(newPos)
            
            # Detect dock position based on position relative to parent
            if self.parent():
                parentRect = self.parent().rect()
                localPos = self.parent().mapFromGlobal(event.globalPos())
                
                # 增加停靠阈值，更容易触发停靠
                dockThreshold = 80
                
                # Determine which edge is closest
                distances = {
                    DockPosition.TOP: localPos.y(),
                    DockPosition.BOTTOM: parentRect.height() - localPos.y(),
                    DockPosition.LEFT: localPos.x(),
                    DockPosition.RIGHT: parentRect.width() - localPos.x()
                }
                
                # Find closest edge
                closest = min(distances.items(), key=lambda x: x[1])
                if closest[1] < dockThreshold:
                    # 预览停靠位置，但不立即切换
                    self._pendingDockPosition = closest[0]
                else:
                    # 远离边缘时设为浮动状态
                    self._pendingDockPosition = None
            
            event.accept()
        elif self._dragHandleRect.contains(event.pos()):
            self.setCursor(Qt.OpenHandCursor)
        else:
            self.setCursor(Qt.ArrowCursor)
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        """ Handle mouse release after dragging """
        if event.button() == Qt.LeftButton and self._isDragging:
            self._isDragging = False
            self.setCursor(Qt.ArrowCursor)
            
            # 检查是否需要停靠
            if hasattr(self, '_pendingDockPosition') and self._pendingDockPosition:
                # 执行停靠
                self.setDockPosition(self._pendingDockPosition)
                
                # Snap to final position based on dock position
                if self.parent():
                    parentRect = self.parent().rect()
                    
                    if self._dockPosition == DockPosition.TOP:
                        self.move(0, 0)
                    elif self._dockPosition == DockPosition.BOTTOM:
                        self.move(0, parentRect.height() - self.height())
                    elif self._dockPosition == DockPosition.LEFT:
                        self.move(0, 0)
                    elif self._dockPosition == DockPosition.RIGHT:
                        self.move(parentRect.width() - self.width(), 0)
                
                # 停靠后再次强制更新布局
                self.updateGeometry()
            else:
                # 自由浮动状态
                self._isFloating = True
            
            event.accept()
        else:
            super().mouseReleaseEvent(event)

    def paintEvent(self, e):
        """ Paint with drag handle indicator - Fluent 2 设计风格 """
        super().paintEvent(e)
        
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        
        # Fluent 2 设计风格的拖动区域
        if self.orientation() == Qt.Horizontal:
            # 水平布局 - 左侧拖动区域
            handleWidth = 20
            handleRect = QRect(2, 4, handleWidth - 4, self.height() - 8)
            
            # 背景渐变
            isDark = isDarkTheme()
            if isDark:
                # 暗色主题：微妙的半透明背景
                bgColor = QColor(255, 255, 255, 8)
                borderColor = QColor(255, 255, 255, 20)
                dotColor = QColor(255, 255, 255, 120)
            else:
                # 亮色主题：微妙的半透明背景
                bgColor = QColor(0, 0, 0, 6)
                borderColor = QColor(0, 0, 0, 15)
                dotColor = QColor(0, 0, 0, 100)
            
            # 绘制背景
            painter.fillRect(handleRect, bgColor)
            
            # 绘制边框（仅在悬停或拖动时）
            if self._isDragging or self._dragHandleRect.contains(self.mapFromGlobal(self.cursor().pos())):
                painter.setPen(QPen(borderColor, 1))
                painter.setBrush(Qt.NoBrush)
                painter.drawRoundedRect(handleRect, 3, 3)
            
            # 绘制 Fluent 2 风格的拖动点（更现代的点状设计）
            painter.setPen(QPen(dotColor, 2, Qt.SolidLine, Qt.RoundCap))
            
            # 三行点，每行2个点，更紧凑的布局
            dotSpacing = 6
            dotY = self.height() // 2 - 6
            
            for row in range(3):
                y = dotY + row * dotSpacing
                # 左边的点
                painter.drawPoint(8, y)
                # 右边的点
                painter.drawPoint(14, y)
                
        else:
            # 竖直布局 - 上方拖动区域
            handleHeight = 20
            handleRect = QRect(4, 2, self.width() - 8, handleHeight - 4)
            
            # 背景渐变
            isDark = isDarkTheme()
            if isDark:
                bgColor = QColor(255, 255, 255, 8)
                borderColor = QColor(255, 255, 255, 20)
                dotColor = QColor(255, 255, 255, 120)
            else:
                bgColor = QColor(0, 0, 0, 6)
                borderColor = QColor(0, 0, 0, 15)
                dotColor = QColor(0, 0, 0, 100)
            
            # 绘制背景
            painter.fillRect(handleRect, bgColor)
            
            # 绘制边框（仅在悬停或拖动时）
            if self._isDragging or self._dragHandleRect.contains(self.mapFromGlobal(self.cursor().pos())):
                painter.setPen(QPen(borderColor, 1))
                painter.setBrush(Qt.NoBrush)
                painter.drawRoundedRect(handleRect, 3, 3)
            
            # 绘制 Fluent 2 风格的拖动点（三列点，每列2个点）
            painter.setPen(QPen(dotColor, 2, Qt.SolidLine, Qt.RoundCap))
            
            dotSpacing = 6
            dotX = self.width() // 2 - 6
            
            for col in range(3):
                x = dotX + col * dotSpacing
                # 上边的点
                painter.drawPoint(x, 8)
                # 下边的点
                painter.drawPoint(x, 14)
        
        # 如果正在拖动且接近停靠边缘，显示预览
        if self._isDragging and hasattr(self, '_pendingDockPosition') and self._pendingDockPosition:
            # 注释掉在父容器绘制预览的功能，避免绘制警告
            # 这种预览应该通过其他方式实现，比如父容件的paintEvent
            pass
