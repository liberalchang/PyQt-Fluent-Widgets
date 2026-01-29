# coding:utf-8
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QScrollArea
from .tool_panel import ToolPanel, VerticalToolPanel
from .flyout import FlyoutViewBase


class VerticalToolPanelView(FlyoutViewBase):
    """ Vertical tool panel view - 竖直工具面板视图封装 """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.panel = VerticalToolPanel(self)
        self.vBoxLayout = QVBoxLayout(self)

        self.vBoxLayout.setContentsMargins(6, 6, 6, 6)
        self.vBoxLayout.addWidget(self.panel)
        self.vBoxLayout.setSizeConstraint(QVBoxLayout.SetMinAndMaxSize)

        # 设置默认样式
        self.setButtonTight(True)
        self.setIconSize(QSize(16, 16))

    # 委托所有方法到内部的 panel
    def addTool(self, data):
        """ Add tool from data dictionary """
        return self.panel.addTool(data)
        
    def addTools(self, tools):
        """ Add multiple tools from data list """
        return self.panel.addTools(tools)
        
    def setTools(self, tools):
        """ Set tools from data list (clears existing tools) """
        return self.panel.setTools(tools)
        
    def addSeparator(self):
        """ Add separator """
        return self.panel.addSeparator()
        
    def insertSeparator(self, index: int):
        """ Insert separator at index """
        return self.panel.insertSeparator(index)
        
    def addWidget(self, widget):
        """ Add custom widget """
        return self.panel.addWidget(widget)
        
    def removeWidget(self, widget):
        """ Remove widget """
        return self.panel.removeWidget(widget)
        
    def clearTools(self):
        """ Clear all tools """
        return self.panel.clearTools()
        
    def currentTool(self):
        """ Get currently selected tool """
        return self.panel.currentTool()
        
    def setCurrentTool(self, button):
        """ Set currently selected tool """
        return self.panel.setCurrentTool(button)
        
    def setSpacing(self, spacing: int):
        """ Set spacing between tools """
        return self.panel.setSpacing(spacing)
        
    def spacing(self):
        """ Get spacing between tools """
        return self.panel.spacing()
        
    def setToolButtonStyle(self, style):
        """ Set the style of tool buttons """
        return self.panel.setToolButtonStyle(style)
        
    def toolButtonStyle(self):
        """ Get tool button style """
        return self.panel.toolButtonStyle()
        
    def setIconSize(self, size: QSize):
        """ Set icon size """
        return self.panel.setIconSize(size)
        
    def iconSize(self):
        """ Get icon size """
        return self.panel.iconSize()
        
    def setButtonTight(self, tight: bool):
        """ Set button tight mode """
        if tight:
            self.setSpacing(0)
            self.setIconSize(QSize(16, 16))
        else:
            self.setSpacing(4)
            self.setIconSize(QSize(20, 20))
            
    def resizeToSuitableHeight(self):
        """ Resize to suitable height """
        return self.panel.resizeToSuitableHeight()
        
    def getToolData(self):
        """ Export tool data """
        return self.panel.getToolData()
        
    def toolButtons(self):
        """ Get all tool buttons """
        return self.panel.toolButtons()
        
    # 信号委托
    @property
    def toolClicked(self):
        """ Tool clicked signal """
        return self.panel.toolClicked
        
    @property
    def toolChanged(self):
        """ Tool changed signal """
        return self.panel.toolChanged


class HorizontalToolPanelView(FlyoutViewBase):
    """ Horizontal tool panel view - 水平工具面板视图封装 """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.panel = ToolPanel(self)
        self.panel.setOrientation(Qt.Horizontal)
        self.hBoxLayout = QHBoxLayout(self)

        self.hBoxLayout.setContentsMargins(6, 6, 6, 6)
        self.hBoxLayout.addWidget(self.panel)
        self.hBoxLayout.setSizeConstraint(QHBoxLayout.SetMinAndMaxSize)

        # 设置默认样式
        self.setButtonTight(True)
        self.setIconSize(QSize(16, 16))

    # 委托所有方法到内部的 panel
    def addTool(self, data):
        """ Add tool from data dictionary """
        return self.panel.addTool(data)
        
    def addTools(self, tools):
        """ Add multiple tools from data list """
        return self.panel.addTools(tools)
        
    def setTools(self, tools):
        """ Set tools from data list (clears existing tools) """
        return self.panel.setTools(tools)
        
    def addSeparator(self):
        """ Add separator """
        return self.panel.addSeparator()
        
    def insertSeparator(self, index: int):
        """ Insert separator at index """
        return self.panel.insertSeparator(index)
        
    def addWidget(self, widget):
        """ Add custom widget """
        return self.panel.addWidget(widget)
        
    def removeWidget(self, widget):
        """ Remove widget """
        return self.panel.removeWidget(widget)
        
    def clearTools(self):
        """ Clear all tools """
        return self.panel.clearTools()
        
    def currentTool(self):
        """ Get currently selected tool """
        return self.panel.currentTool()
        
    def setCurrentTool(self, button):
        """ Set currently selected tool """
        return self.panel.setCurrentTool(button)
        
    def setSpacing(self, spacing: int):
        """ Set spacing between tools """
        return self.panel.setSpacing(spacing)
        
    def spacing(self):
        """ Get spacing between tools """
        return self.panel.spacing()
        
    def setToolButtonStyle(self, style):
        """ Set the style of tool buttons """
        return self.panel.setToolButtonStyle(style)
        
    def toolButtonStyle(self):
        """ Get tool button style """
        return self.panel.toolButtonStyle()
        
    def setIconSize(self, size: QSize):
        """ Set icon size """
        return self.panel.setIconSize(size)
        
    def iconSize(self):
        """ Get icon size """
        return self.panel.iconSize()
        
    def setButtonTight(self, tight: bool):
        """ Set button tight mode """
        if tight:
            self.setSpacing(0)
            self.setIconSize(QSize(16, 16))
        else:
            self.setSpacing(4)
            self.setIconSize(QSize(20, 20))
            
    def resizeToSuitableWidth(self):
        """ Resize to suitable width """
        return self.panel.resizeToSuitableWidth()
        
    def getToolData(self):
        """ Export tool data """
        return self.panel.getToolData()
        
    def toolButtons(self):
        """ Get all tool buttons """
        return self.panel.toolButtons()
        
    # 信号委托
    @property
    def toolClicked(self):
        """ Tool clicked signal """
        return self.panel.toolClicked
        
    @property
    def toolChanged(self):
        """ Tool changed signal """
        return self.panel.toolChanged


class ScrollableToolPanelView(QWidget):
    """ Scrollable tool panel view - 可滚动工具面板视图封装 """

    def __init__(self, orientation=Qt.Vertical, parent=None):
        super().__init__(parent)
        
        # 创建滚动区域
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
        # 设置滚动区域背景透明
        self.scrollArea.setStyleSheet("QScrollArea { background: transparent; }")
        self.scrollArea.viewport().setStyleSheet("background: transparent;")
        
        # 创建内部的面板
        if orientation == Qt.Vertical:
            self.panel = VerticalToolPanel()
            self.mainLayout = QVBoxLayout(self)
        else:
            self.panel = ToolPanel()
            self.panel.setOrientation(Qt.Horizontal)
            self.mainLayout = QHBoxLayout(self)
            
        # 设置面板背景透明
        self.panel.setStyleSheet("background: transparent;")
            
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.addWidget(self.scrollArea)
        
        # 设置滚动区域的内容
        self.scrollArea.setWidget(self.panel)
        
        # 设置面板的最小尺寸，确保滚动区域知道内容大小
        if orientation == Qt.Vertical:
            self.panel.setMinimumWidth(50)  # 设置最小宽度
        else:
            self.panel.setMinimumHeight(50)  # 设置最小高度
        
        # 设置默认样式
        self.setButtonTight(True)
        self.setIconSize(QSize(16, 16))

    def setOrientation(self, orientation):
        """ Set panel orientation """
        if orientation == Qt.Vertical:
            if not isinstance(self.panel, VerticalToolPanel):
                # 重新创建垂直面板
                tools = self.panel.getToolData()
                self.panel = VerticalToolPanel()
                self.panel.setTools(tools)
        else:
            if isinstance(self.panel, VerticalToolPanel):
                # 重新创建水平面板
                tools = self.panel.getToolData()
                self.panel = ToolPanel()
                self.panel.setOrientation(Qt.Horizontal)
                self.panel.setTools(tools)
                
        self.scrollArea.setWidget(self.panel)

    # 委托所有方法到内部的 panel
    def addTool(self, data):
        """ Add tool from data dictionary """
        return self.panel.addTool(data)
        
    def addTools(self, tools):
        """ Add multiple tools from data list """
        return self.panel.addTools(tools)
        
    def setTools(self, tools):
        """ Set tools from data list (clears existing tools) """
        return self.panel.setTools(tools)
        
    def addSeparator(self):
        """ Add separator """
        return self.panel.addSeparator()
        
    def insertSeparator(self, index: int):
        """ Insert separator at index """
        return self.panel.insertSeparator(index)
        
    def addWidget(self, widget):
        """ Add custom widget """
        return self.panel.addWidget(widget)
        
    def removeWidget(self, widget):
        """ Remove widget """
        return self.panel.removeWidget(widget)
        
    def clearTools(self):
        """ Clear all tools """
        return self.panel.clearTools()
        
    def currentTool(self):
        """ Get currently selected tool """
        return self.panel.currentTool()
        
    def setCurrentTool(self, button):
        """ Set currently selected tool """
        return self.panel.setCurrentTool(button)
        
    def setSpacing(self, spacing: int):
        """ Set spacing between tools """
        return self.panel.setSpacing(spacing)
        
    def spacing(self):
        """ Get spacing between tools """
        return self.panel.spacing()
        
    def setToolButtonStyle(self, style):
        """ Set the style of tool buttons """
        return self.panel.setToolButtonStyle(style)
        
    def toolButtonStyle(self):
        """ Get tool button style """
        return self.panel.toolButtonStyle()
        
    def setIconSize(self, size: QSize):
        """ Set icon size """
        return self.panel.setIconSize(size)
        
    def iconSize(self):
        """ Get icon size """
        return self.panel.iconSize()
        
    def setButtonTight(self, tight: bool):
        """ Set button tight mode """
        if tight:
            self.setSpacing(0)
            self.setIconSize(QSize(16, 16))
        else:
            self.setSpacing(4)
            self.setIconSize(QSize(20, 20))
            
    def resizeToSuitableSize(self):
        """ Resize to suitable size """
        if isinstance(self.panel, VerticalToolPanel):
            self.panel.resizeToSuitableHeight()
        else:
            self.panel.resizeToSuitableWidth()
            
    def getToolData(self):
        """ Export tool data """
        return self.panel.getToolData()
        
    def toolButtons(self):
        """ Get all tool buttons """
        return self.panel.toolButtons()
        
    # 信号委托
    @property
    def toolClicked(self):
        """ Tool clicked signal """
        return self.panel.toolClicked
        
    @property
    def toolChanged(self):
        """ Tool changed signal """
        return self.panel.toolChanged


class ResponsiveToolPanelView(QWidget):
    """ Responsive tool panel view - 响应式工具面板视图封装 """

    def __init__(self, orientation=Qt.Vertical, parent=None):
        super().__init__(parent)
        self.orientation = orientation
        
        # 创建主布局
        if orientation == Qt.Vertical:
            self.mainLayout = QVBoxLayout(self)
        else:
            self.mainLayout = QHBoxLayout(self)
            
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        
        # 创建面板
        if orientation == Qt.Vertical:
            self.panel = VerticalToolPanel(self)
        else:
            self.panel = ToolPanel(self)
            self.panel.setOrientation(Qt.Horizontal)
            
        # 设置面板背景透明
        self.panel.setStyleSheet("background: transparent;")
            
        self.mainLayout.addWidget(self.panel)
        
        # 设置默认样式
        self.setButtonTight(True)
        self.setIconSize(QSize(16, 16))

    def resizeEvent(self, event):
        """ Handle resize event for responsive behavior """
        super().resizeEvent(event)
        
        # 根据可用空间调整面板
        if self.orientation == Qt.Vertical:
            available_height = self.height() - self.mainLayout.contentsMargins().top() - self.mainLayout.contentsMargins().bottom()
            if available_height < self.panel.suitableHeight():
                # 空间不足，启用滚动
                if not hasattr(self, '_scrollArea'):
                    self._enableScrolling()
        else:
            available_width = self.width() - self.mainLayout.contentsMargins().left() - self.mainLayout.contentsMargins().right()
            if available_width < self.panel.suitableWidth():
                # 空间不足，启用滚动
                if not hasattr(self, '_scrollArea'):
                    self._enableScrolling()
                    
    def _enableScrolling(self):
        """ Enable scrolling when space is insufficient """
        # 移除面板
        self.mainLayout.removeWidget(self.panel)
        
        # 创建滚动区域
        if not hasattr(self, '_scrollArea'):
            self._scrollArea = QScrollArea(self)
            self._scrollArea.setWidgetResizable(True)
            self._scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            self._scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            
            # 设置滚动区域背景透明
            self._scrollArea.setStyleSheet("QScrollArea { background: transparent; }")
            self._scrollArea.viewport().setStyleSheet("background: transparent;")
            
            self.mainLayout.addWidget(self._scrollArea)
            
        # 设置面板为滚动区域的内容
        self._scrollArea.setWidget(self.panel)

    # 委托所有方法到内部的 panel
    def addTool(self, data):
        """ Add tool from data dictionary """
        return self.panel.addTool(data)
        
    def addTools(self, tools):
        """ Add multiple tools from data list """
        return self.panel.addTools(tools)
        
    def setTools(self, tools):
        """ Set tools from data list (clears existing tools) """
        return self.panel.setTools(tools)
        
    def addSeparator(self):
        """ Add separator """
        return self.panel.addSeparator()
        
    def insertSeparator(self, index: int):
        """ Insert separator at index """
        return self.panel.insertSeparator(index)
        
    def addWidget(self, widget):
        """ Add custom widget """
        return self.panel.addWidget(widget)
        
    def removeWidget(self, widget):
        """ Remove widget """
        return self.panel.removeWidget(widget)
        
    def clearTools(self):
        """ Clear all tools """
        return self.panel.clearTools()
        
    def currentTool(self):
        """ Get currently selected tool """
        return self.panel.currentTool()
        
    def setCurrentTool(self, button):
        """ Set currently selected tool """
        return self.panel.setCurrentTool(button)
        
    def setSpacing(self, spacing: int):
        """ Set spacing between tools """
        return self.panel.setSpacing(spacing)
        
    def spacing(self):
        """ Get spacing between tools """
        return self.panel.spacing()
        
    def setToolButtonStyle(self, style):
        """ Set the style of tool buttons """
        return self.panel.setToolButtonStyle(style)
        
    def toolButtonStyle(self):
        """ Get tool button style """
        return self.panel.toolButtonStyle()
        
    def setIconSize(self, size: QSize):
        """ Set icon size """
        return self.panel.setIconSize(size)
        
    def iconSize(self):
        """ Get icon size """
        return self.panel.iconSize()
        
    def setButtonTight(self, tight: bool):
        """ Set button tight mode """
        if tight:
            self.setSpacing(0)
            self.setIconSize(QSize(16, 16))
        else:
            self.setSpacing(4)
            self.setIconSize(QSize(20, 20))
            
    def resizeToSuitableSize(self):
        """ Resize to suitable size """
        if isinstance(self.panel, VerticalToolPanel):
            self.panel.resizeToSuitableHeight()
        else:
            self.panel.resizeToSuitableWidth()
            
    def getToolData(self):
        """ Export tool data """
        return self.panel.getToolData()
        
    def toolButtons(self):
        """ Get all tool buttons """
        return self.panel.toolButtons()
        
    # 信号委托
    @property
    def toolClicked(self):
        """ Tool clicked signal """
        return self.panel.toolClicked
        
    @property
    def toolChanged(self):
        """ Tool changed signal """
        return self.panel.toolChanged
