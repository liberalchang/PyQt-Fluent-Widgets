# coding:utf-8
from typing import List, Dict, Optional

from PySide6.QtCore import Qt, QSize, QRectF, QPoint, QTimer, Signal, QEvent
from PySide6.QtGui import QPainter, QColor, QMouseEvent, QHoverEvent
from PySide6.QtWidgets import QWidget, QButtonGroup, QApplication, QFrame

from ...common.font import setFont
from ...common.icon import FluentIcon, Action
from ...common.style_sheet import isDarkTheme, themeColor
from .menu import RoundMenu, MenuAnimationType, CheckableMenu
from .button import TransparentToggleToolButton
from .tool_tip import ToolTipFilter, ToolTipPosition


class ToolPanelButton(TransparentToggleToolButton):
    """ Tool panel button with sub-options support
    
    Constructors
    ------------
    * ToolPanelButton(`parent`: QWidget = None)
    * ToolPanelButton(`icon`: QIcon | str | FluentIconBase = None, `parent`: QWidget = None)
    """
    
    subOptionChanged = Signal(int, dict)  # (index, option)
    
    def _postInit(self):
        """ Post initialization - called after parent __init__ """
        super()._postInit()
        self._text = ''
        self._toolData = {}
        self._subOptions = []
        self._currentSubIndex = 0
        self._parentPanel = None
        self._longPressTimer = QTimer(self)
        self._longPressTimer.setSingleShot(True)
        self._longPressTimer.timeout.connect(self._onLongPress)
        self._longPressThreshold = 1000  # 1 second
        self._isLongPressing = False
        
        self.setCheckable(True)
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)
        setFont(self, 12)
        
    def setToolData(self, data: Dict):
        """ Set tool data from dictionary
        
        Parameters
        ----------
        data: dict
            Tool data dictionary with keys:
            - icon: FluentIconBase | QIcon - Tool icon
            - name: str - Tool name
            - tooltip: str - Tool tooltip (optional)
            - checked: bool - Whether tool is checked (optional)
            - enabled: bool - Whether tool is enabled (optional)
            - subOptions: List[Dict] - Sub-options list (optional)
            - shortcut: str - Keyboard shortcut (optional)
            - userData: Any - Custom user data (optional)
        """
        self._toolData = data
        
        # Set icon
        if 'icon' in data:
            self.setIcon(data['icon'])
            
        # Set text
        if 'name' in data:
            self._text = data['name']
            # 同时设置父类的文本，确保绘制时能显示
            super().setText(data['name'])
            
        # Set tooltip
        tooltip = data.get('tooltip', data.get('name', ''))
        shortcut = data.get('shortcut', '')
        if shortcut:
            tooltip += f' ({shortcut})'
        self.setToolTip(tooltip)
        
        # Set checked state
        if data.get('checked', False):
            self.setChecked(True)
            
        # Set enabled state
        self.setEnabled(data.get('enabled', True))
        
        # Set sub-options
        if 'subOptions' in data:
            self.setSubOptions(data['subOptions'])
            
        # Install tooltip filter
        self.installEventFilter(ToolTipFilter(
            self, 
            showDelay=300, 
            position=ToolTipPosition.TOP
        ))
        
    def toolData(self) -> Dict:
        """ Get tool data dictionary """
        return self._toolData
        
    def setSubOptions(self, options: List[Dict]):
        """ Set sub-options list
        
        Parameters
        ----------
        options: List[Dict]
            List of sub-option dictionaries with keys:
            - icon: FluentIconBase | QIcon
            - name: str
            - checked: bool (optional)
        """
        self._subOptions = options
        if options:
            # Find checked option or use first as default
            for i, opt in enumerate(options):
                if opt.get('checked', False):
                    self._currentSubIndex = i
                    break
                    
    def subOptions(self) -> List[Dict]:
        """ Get sub-options list """
        return self._subOptions
        
    def currentSubOption(self) -> Optional[Dict]:
        """ Get current selected sub-option """
        if self._subOptions and 0 <= self._currentSubIndex < len(self._subOptions):
            return self._subOptions[self._currentSubIndex]
        return None
        
    def setCurrentSubOption(self, index: int):
        """ Set current sub-option by index """
        if 0 <= index < len(self._subOptions):
            # Update checked state
            for i, opt in enumerate(self._subOptions):
                opt['checked'] = (i == index)
            self._currentSubIndex = index
            
            # Update icon if sub-option has different icon
            current = self._subOptions[index]
            if 'icon' in current:
                self.setIcon(current['icon'])
                
            # Update tooltip
            tooltip = current.get('name', '')
            if 'shortcut' in self._toolData:
                tooltip += f' ({self._toolData["shortcut"]})'
            self.setToolTip(tooltip)
            
            self.subOptionChanged.emit(index, current)
            self.update()
            
    def text(self):
        return self._text
        
    def setText(self, text: str):
        self._text = text
        super().setText(text)  # 同时设置父类的文本
        self.update()
        
    def sizeHint(self) -> QSize:
        if self.isIconOnly():
            return QSize(40, 40)
            
        tw = self.fontMetrics().boundingRect(self.text()).width()
        style = self.toolButtonStyle()
        
        if style == Qt.ToolButtonTextBesideIcon:
            return QSize(tw + 50, 40)
        elif style == Qt.ToolButtonTextOnly:
            return QSize(tw + 32, 40)
            
        return QSize(tw + 32, 56)
        
    def isIconOnly(self):
        if not self.text():
            return True
        return self.toolButtonStyle() in [Qt.ToolButtonIconOnly, Qt.ToolButtonFollowStyle]
        
    def mousePressEvent(self, event: QMouseEvent):
        """ Handle mouse press for sub-options menu and long press """
        if event.button() == Qt.LeftButton:
            # Start long press timer
            if self._subOptions:
                self._isLongPressing = True
                self._longPressTimer.start(self._longPressThreshold)
            super().mousePressEvent(event)
            
        elif event.button() == Qt.RightButton and self._subOptions:
            # Show sub-options menu on right click
            self._showSubOptionsMenu()
            event.accept()
        else:
            super().mousePressEvent(event)
            
    def mouseReleaseEvent(self, event: QMouseEvent):
        """ Handle mouse release - cancel long press """
        self._longPressTimer.stop()
        self._isLongPressing = False
        super().mouseReleaseEvent(event)
        
    def _onLongPress(self):
        """ Handle long press - show sub-options menu """
        if self._isLongPressing and self._subOptions:
            self._showSubOptionsMenu()
            self._isLongPressing = False
            
    def _showSubOptionsMenu(self):
        """ Show sub-options menu """
        if not self._subOptions:
            return
            
        menu = CheckableMenu(parent=self)
        menu.view.setIconSize(QSize(16, 16))
        
        # Add sub-options
        for i, option in enumerate(self._subOptions):
            icon = option.get('icon', FluentIcon.TRANSPARENT)
            action = Action(icon, option.get('name', ''), menu)
            action.setCheckable(True)
            action.setChecked(i == self._currentSubIndex)
            action.triggered.connect(lambda checked, idx=i: self.setCurrentSubOption(idx))
            menu.addAction(action)
            
        # Show menu at button position
        pos = self.mapToGlobal(QPoint(self.width(), 0))
        menu.exec(pos, aniType=MenuAnimationType.DROP_DOWN)
        
    def paintEvent(self, e):
        """ Paint tool button with selection indicator """
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        
        # Draw background and selection state
        if self.isChecked():
            painter.setPen(Qt.NoPen)
            # 使用主题色
            painter.setBrush(themeColor())
            painter.drawRoundedRect(self.rect(), 4, 4)
        elif self.isHover:
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 15) if isDarkTheme() else QColor(0, 0, 0, 15))
            painter.drawRoundedRect(self.rect(), 4, 4)
        
        # Draw icon and text based on button style
        if not self.icon().isNull():
            iw, ih = self.iconSize().width(), self.iconSize().height()
            
            if not self.isEnabled():
                painter.setOpacity(0.43)
            elif self.isPressed:
                painter.setOpacity(0.63)
                
            style = self.toolButtonStyle()
            
            if style == Qt.ToolButtonIconOnly:
                # Icon only - center it
                x = (self.width() - iw) / 2
                y = (self.height() - ih) / 2
                self.icon().paint(painter, QRectF(x, y, iw, ih).toRect())
                
            elif style == Qt.ToolButtonTextBesideIcon:
                # Icon with text beside
                y = (self.height() - ih) / 2
                self.icon().paint(painter, QRectF(8, y, iw, ih).toRect())
                
                # Draw text
                if self.text():
                    if not self.isChecked():
                        painter.setPen(Qt.white if isDarkTheme() else Qt.black)
                    else:
                        painter.setPen(Qt.black if isDarkTheme() else Qt.white)
                        
                    if not self.isEnabled():
                        painter.setOpacity(0.43)
                    elif self.isPressed:
                        painter.setOpacity(0.63)
                    else:
                        painter.setOpacity(1.0)
                        
                    rect = QRectF(iw + 16, 0, self.width() - iw - 16, self.height())
                    painter.drawText(rect, Qt.AlignCenter, self.text())
                    
            elif style == Qt.ToolButtonTextUnderIcon:
                # Icon with text under
                x = (self.width() - iw) / 2
                self.icon().paint(painter, QRectF(x, 8, iw, ih).toRect())
                
                # Draw text
                if self.text():
                    if not self.isChecked():
                        painter.setPen(Qt.white if isDarkTheme() else Qt.black)
                    else:
                        painter.setPen(Qt.black if isDarkTheme() else Qt.white)
                        
                    if not self.isEnabled():
                        painter.setOpacity(0.43)
                    elif self.isPressed:
                        painter.setOpacity(0.63)
                    else:
                        painter.setOpacity(1.0)
                        
                    rect = QRectF(0, ih + 12, self.width(), self.height() - ih - 12)
                    painter.drawText(rect, Qt.AlignHCenter | Qt.AlignTop, self.text())
                    
            elif style == Qt.ToolButtonTextOnly:
                # Text only
                if self.text():
                    if not self.isChecked():
                        painter.setPen(Qt.white if isDarkTheme() else Qt.black)
                    else:
                        painter.setPen(Qt.black if isDarkTheme() else Qt.white)
                        
                    if not self.isEnabled():
                        painter.setOpacity(0.43)
                    elif self.isPressed:
                        painter.setOpacity(0.63)
                    else:
                        painter.setOpacity(1.0)
                        
                    rect = QRectF(0, 0, self.width(), self.height())
                    painter.drawText(rect, Qt.AlignCenter, self.text())
        
        # Draw sub-option indicator (small triangle in bottom-right corner)
        if self._subOptions and len(self._subOptions) > 1:
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(255, 255, 255, 180) if isDarkTheme() else QColor(0, 0, 0, 120))
            
            # Small triangle in bottom-right
            triangle = [
                QPoint(self.width() - 8, self.height() - 3),
                QPoint(self.width() - 3, self.height() - 8),
                QPoint(self.width() - 3, self.height() - 3)
            ]
            painter.drawPolygon(triangle)


class ToolPanelSeparator(QWidget):
    """ Tool panel separator """
    
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
            self.setFixedSize(9, 40)
        else:
            self.setFixedSize(40, 9)
            
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QColor(255, 255, 255, 21) if isDarkTheme() else QColor(0, 0, 0, 15))
        
        if self._orientation == Qt.Horizontal:
            painter.drawLine(5, 4, 5, self.height() - 4)
        else:
            painter.drawLine(4, 5, self.width() - 4, 5)


class MoreToolsButton(ToolPanelButton):
    """ More tools button """
    
    def _postInit(self):
        super()._postInit()
        self.setIcon(FluentIcon.MORE)
        self.setCheckable(False)
        self.setToolTip('More Tools')
        
    def sizeHint(self):
        return QSize(40, 40)
        
    def clearState(self):
        self.setAttribute(Qt.WA_UnderMouse, False)
        e = QHoverEvent(QEvent.HoverLeave, QPoint(-1, -1), QPoint())
        QApplication.sendEvent(self, e)


class ToolPanel(QFrame):
    """ Tool panel container
    
    A Photoshop-style tool panel with exclusive tool selection,
    sub-options, responsive layout, and keyboard shortcuts.
    """
    
    toolClicked = Signal(ToolPanelButton)
    toolChanged = Signal(ToolPanelButton)
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._orientation = Qt.Horizontal
        self._widgets = []  # type: List[QWidget]
        self._hiddenWidgets = []  # type: List[QWidget]
        self._spacing = 4
        self._toolButtonStyle = Qt.ToolButtonIconOnly
        self._iconSize = QSize(16, 16)
        
        # Button group for exclusive selection
        self._buttonGroup = QButtonGroup(self)
        self._buttonGroup.setExclusive(True)
        self._buttonGroup.buttonClicked.connect(self._onToolClicked)
        
        # More button for hidden tools
        self.moreButton = MoreToolsButton(self)
        self.moreButton.clicked.connect(self._showMoreToolsMenu)
        self.moreButton.hide()
        
        setFont(self, 12)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
    def setOrientation(self, orientation: Qt.Orientation):
        """ Set tool panel orientation """
        if self._orientation == orientation:
            return
            
        self._orientation = orientation
        
        # Update separators orientation
        for widget in self._widgets:
            if isinstance(widget, ToolPanelSeparator):
                widget.setOrientation(orientation)
                
        # Update fixed size based on orientation
        if self._widgets:
            if orientation == Qt.Horizontal:
                height = max(w.sizeHint().height() for w in self._widgets if not isinstance(w, ToolPanelSeparator))
                self.setFixedHeight(height)
                self.setMaximumWidth(16777215)
            else:
                width = max(w.sizeHint().width() for w in self._widgets if not isinstance(w, ToolPanelSeparator))
                self.setFixedWidth(width)
                self.setMaximumHeight(16777215)
                
        self.updateGeometry()
        
    def orientation(self):
        """ Get tool panel orientation """
        return self._orientation
        
    def setSpacing(self, spacing: int):
        """ Set spacing between tools """
        if spacing == self._spacing:
            return
        self._spacing = spacing
        self.updateGeometry()
        
    def spacing(self):
        """ Get spacing between tools """
        return self._spacing
        
    def setToolButtonStyle(self, style: Qt.ToolButtonStyle):
        """ Set the style of tool buttons """
        if self._toolButtonStyle == style:
            return
            
        self._toolButtonStyle = style
        for w in self.toolButtons:
            w.setToolButtonStyle(style)
        self.updateGeometry()
        
    def toolButtonStyle(self):
        """ Get tool button style """
        return self._toolButtonStyle
        
    def setIconSize(self, size: QSize):
        """ Set icon size """
        if size == self._iconSize:
            return
            
        self._iconSize = size
        for w in self.toolButtons:
            w.setIconSize(size)
            
    def iconSize(self):
        """ Get icon size """
        return self._iconSize
        
    def addTool(self, data: Dict) -> ToolPanelButton:
        """ Add tool from data dictionary
        
        Parameters
        ----------
        data: dict
            Tool data dictionary (see ToolPanelButton.setToolData for keys)
            
        Returns
        -------
        button: ToolPanelButton
            The created tool button
        """
        button = ToolPanelButton(self)
        button.setToolData(data)
        button.setToolButtonStyle(self._toolButtonStyle)
        button.setIconSize(self._iconSize)
        button.setFont(self.font())
        button._parentPanel = self
        
        self._buttonGroup.addButton(button)
        self._insertWidgetToLayout(-1, button)
        
        return button
        
    def addTools(self, tools: List[Dict]):
        """ Add multiple tools from data list """
        for tool in tools:
            self.addTool(tool)
            
    def setTools(self, tools: List[Dict]):
        """ Set tools from data list (clears existing tools) """
        self.clearTools()
        self.addTools(tools)
        
    def addSeparator(self):
        """ Add separator """
        self.insertSeparator(-1)
        
    def insertSeparator(self, index: int):
        """ Insert separator at index """
        separator = ToolPanelSeparator(self)
        separator.setOrientation(self._orientation)
        self._insertWidgetToLayout(index, separator)
        
    def addWidget(self, widget: QWidget):
        """ Add custom widget """
        self._insertWidgetToLayout(-1, widget)
        
    def removeWidget(self, widget: QWidget):
        """ Remove widget """
        if widget not in self._widgets:
            return
            
        if isinstance(widget, ToolPanelButton):
            self._buttonGroup.removeButton(widget)
            
        self._widgets.remove(widget)
        widget.hide()
        widget.deleteLater()
        self.updateGeometry()
        
    def clearTools(self):
        """ Clear all tools """
        for widget in self._widgets[:]:
            self.removeWidget(widget)
            
    def currentTool(self) -> Optional[ToolPanelButton]:
        """ Get currently selected tool """
        return self._buttonGroup.checkedButton()
        
    def setCurrentTool(self, button: ToolPanelButton):
        """ Set currently selected tool """
        if button in self._buttonGroup.buttons():
            button.setChecked(True)
            
    def getToolData(self) -> List[Dict]:
        """ Export tool data """
        data = []
        for widget in self._widgets:
            if isinstance(widget, ToolPanelButton):
                tool_data = widget.toolData().copy()
                tool_data['checked'] = widget.isChecked()
                if widget.subOptions():
                    tool_data['subOptions'] = widget.subOptions()
                    tool_data['currentSubOption'] = widget._currentSubIndex
                data.append(tool_data)
        return data
        
    @property
    def toolButtons(self) -> List[ToolPanelButton]:
        """ Get all tool buttons """
        return [w for w in self._widgets if isinstance(w, ToolPanelButton)]
        
    def _insertWidgetToLayout(self, index: int, widget: QWidget):
        """ Insert widget to layout """
        widget.setParent(self)
        # 不在这里显示widget，让updateGeometry统一管理显示状态
        
        if index < 0:
            self._widgets.append(widget)
        else:
            self._widgets.insert(index, widget)
            
        # Update fixed size
        if self._orientation == Qt.Horizontal:
            heights = [w.sizeHint().height() for w in self._widgets if not isinstance(w, ToolPanelSeparator)]
            if heights:
                self.setFixedHeight(max(heights))
        else:
            widths = [w.sizeHint().width() for w in self._widgets if not isinstance(w, ToolPanelSeparator)]
            if widths:
                self.setFixedWidth(max(widths))
                
        self.updateGeometry()
        
    def updateGeometry(self):
        """ Update layout geometry """
        self._hiddenWidgets.clear()
        self.moreButton.hide()
        
        visibles = self._visibleWidgets()
        
        # 首先隐藏所有widgets，然后只显示可见的
        for widget in self._widgets:
            widget.hide()
        
        if self._orientation == Qt.Horizontal:
            # Horizontal layout
            x = self.contentsMargins().left()
            h = self.height()
            
            for widget in visibles:
                widget.show()
                # 使用sizeHint()来获取正确的尺寸
                widgetHeight = widget.sizeHint().height()
                widgetWidth = widget.sizeHint().width()
                
                widget.resize(widgetWidth, widgetHeight)
                widget.move(x, (h - widgetHeight) // 2)
                x += (widgetWidth + self.spacing())
                
            # Show more button if needed
            if len(visibles) < len(self._widgets):
                self.moreButton.show()
                self.moreButton.move(x, (h - self.moreButton.height()) // 2)
        else:
            # Vertical layout
            y = self.contentsMargins().top()
            w = self.width()
            
            for i, widget in enumerate(visibles):
                widget.show()
                # 使用sizeHint()来获取正确的尺寸
                widgetHeight = widget.sizeHint().height()
                widgetWidth = widget.sizeHint().width()
                widget.resize(widgetWidth, widgetHeight)  # 确保widget有正确的尺寸
                
                # 检查是否会超出面板边界
                if y + widgetHeight > self.height():
                    break
                    
                widget.move((w - widgetWidth) // 2, y)
                y += (widgetHeight + self.spacing())
                
            # Show more button if needed
            if len(visibles) < len(self._widgets):
                self.moreButton.show()
                self.moreButton.move((w - self.moreButton.width()) // 2, y)
                
        # Hide overflow widgets
        for widget in self._widgets[len(visibles):]:
            self._hiddenWidgets.append(widget)
            
    def _visibleWidgets(self) -> List[QWidget]:
        """ Calculate visible widgets """
        if self._orientation == Qt.Horizontal:
            if self.suitableWidth() <= self.width():
                # 确保返回唯一的widgets列表，避免重复
                seen = set()
                unique_widgets = []
                for widget in self._widgets:
                    if widget not in seen:
                        seen.add(widget)
                        unique_widgets.append(widget)
                return unique_widgets
                
            w = self.moreButton.width()
            for index, widget in enumerate(self._widgets):
                w += widget.sizeHint().width()
                if index > 0:
                    w += self.spacing()
                if w > self.width():
                    break
            return self._widgets[:index]
        else:
            if self.suitableHeight() <= self.height():
                return self._widgets
                
            margins = self.contentsMargins()
            availableHeight = self.height() - margins.top() - margins.bottom()
            h = 0
            for index, widget in enumerate(self._widgets):
                widgetHeight = widget.sizeHint().height()
                if h + widgetHeight > availableHeight:
                    break
                h += widgetHeight
                if index > 0:
                    h += self.spacing()
            return self._widgets[:index]
            
    def suitableWidth(self):
        """ Calculate suitable width """
        widths = [w.sizeHint().width() for w in self._widgets]
        contentWidth = sum(widths) + self.spacing() * max(len(widths) - 1, 0)
        # 加上边距
        margins = self.contentsMargins()
        return contentWidth + margins.left() + margins.right()
        
    def suitableHeight(self):
        """ Calculate suitable height """
        heights = [w.sizeHint().height() for w in self._widgets]
        contentHeight = sum(heights) + self.spacing() * max(len(heights) - 1, 0)
        # 加上边距
        margins = self.contentsMargins()
        return contentHeight + margins.top() + margins.bottom()
        
    def resizeToSuitableWidth(self):
        """ Resize to suitable width """
        self.setFixedWidth(self.suitableWidth())
        
    def resizeToSuitableHeight(self):
        """ Resize to suitable height """
        self.setFixedHeight(self.suitableHeight())
        
    def resizeEvent(self, e):
        """ Handle resize event """
        self.updateGeometry()
        
    def _onToolClicked(self, button: ToolPanelButton):
        """ Handle tool clicked """
        self.toolClicked.emit(button)
        self.toolChanged.emit(button)
        
    def _showMoreToolsMenu(self):
        """ Show more tools menu """
        self.moreButton.clearState()
        
        menu = RoundMenu(parent=self)
        menu.view.setIconSize(QSize(16, 16))
        
        # Add hidden tools
        for widget in self._hiddenWidgets:
            if isinstance(widget, ToolPanelButton):
                data = widget.toolData()
                icon = data.get('icon', FluentIcon.TRANSPARENT)
                action = Action(icon, data.get('name', ''), menu)
                action.triggered.connect(lambda checked, btn=widget: btn.click())
                menu.addAction(action)
                
        # Show menu
        if self._orientation == Qt.Horizontal:
            pos = self.moreButton.mapToGlobal(QPoint(0, self.moreButton.height()))
        else:
            pos = self.moreButton.mapToGlobal(QPoint(self.moreButton.width(), 0))
            
        menu.exec(pos, aniType=MenuAnimationType.DROP_DOWN)


class VerticalToolPanel(ToolPanel):
    """ Vertical tool panel """
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setOrientation(Qt.Vertical)
