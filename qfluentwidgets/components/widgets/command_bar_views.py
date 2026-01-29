# coding:utf-8
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from .command_bar import VerticalCommandBar, ResponsiveCommandBar, MovableCommandBar
from .flyout import FlyoutViewBase


class VerticalCommandBarView(FlyoutViewBase):
    """ Vertical command bar view - 竖直命令栏视图封装 """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.bar = VerticalCommandBar(self)
        self.vBoxLayout = QVBoxLayout(self)

        self.vBoxLayout.setContentsMargins(6, 6, 6, 6)
        self.vBoxLayout.addWidget(self.bar)
        self.vBoxLayout.setSizeConstraint(QVBoxLayout.SetMinAndMaxSize)

        # 设置默认样式
        self.setButtonTight(True)
        self.setIconSize(QSize(14, 14))

    # 委托所有方法到内部的 bar
    def addWidget(self, widget: QWidget):
        self.bar.addWidget(widget)

    def addAction(self, action):
        return self.bar.addAction(action)

    def addActions(self, actions):
        self.bar.addActions(actions)

    def addHiddenAction(self, action):
        self.bar.addHiddenAction(action)

    def addHiddenActions(self, actions):
        self.bar.addHiddenActions(actions)

    def insertAction(self, before, action):
        return self.bar.insertAction(before, action)

    def addSeparator(self):
        self.bar.addSeparator()

    def insertSeparator(self, index: int):
        self.bar.insertSeparator(index)

    def removeAction(self, action):
        self.bar.removeAction(action)

    def removeWidget(self, widget: QWidget):
        self.bar.removeWidget(widget)

    def removeHiddenAction(self, action):
        self.bar.removeHiddenAction(action)

    def setToolButtonStyle(self, style):
        self.bar.setToolButtonStyle(style)

    def toolButtonStyle(self):
        return self.bar.toolButtonStyle()

    def setButtonTight(self, isTight: bool):
        self.bar.setButtonTight(isTight)

    def isButtonTight(self):
        return self.bar.isButtonTight()

    def setIconSize(self, size):
        self.bar.setIconSize(size)

    def iconSize(self):
        return self.bar.iconSize()

    def setFont(self, font):
        self.bar.setFont(font)

    def setSpacing(self, spacing: int):
        self.bar.setSpacing(spacing)

    def spacing(self):
        return self.bar.spacing()

    def suitableHeight(self):
        m = self.contentsMargins()
        return m.top() + m.bottom() + self.bar.suitableHeight()

    def resizeToSuitableHeight(self):
        self.bar.resizeToSuitableHeight()
        self.setFixedHeight(self.suitableHeight())

    def actions(self):
        return self.bar.actions()


class ResponsiveCommandBarView(FlyoutViewBase):
    """ Responsive command bar view - 响应式命令栏视图封装 """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.bar = ResponsiveCommandBar(self)
        self.hBoxLayout = QHBoxLayout(self)

        self.hBoxLayout.setContentsMargins(6, 6, 6, 6)
        self.hBoxLayout.addWidget(self.bar)
        self.hBoxLayout.setSizeConstraint(QHBoxLayout.SetMinAndMaxSize)

        # 设置默认样式
        self.setButtonTight(True)
        self.setIconSize(QSize(14, 14))

    # 响应式特有方法
    def setResponsive(self, enabled: bool):
        """ 设置响应式模式 """
        self.bar.setResponsive(enabled)

    def isResponsive(self):
        """ 获取响应式状态 """
        return self.bar.isResponsive()

    # 委托所有基础方法到内部的 bar
    def addWidget(self, widget: QWidget):
        self.bar.addWidget(widget)

    def addAction(self, action):
        return self.bar.addAction(action)

    def addActions(self, actions):
        self.bar.addActions(actions)

    def addHiddenAction(self, action):
        self.bar.addHiddenAction(action)

    def addHiddenActions(self, actions):
        self.bar.addHiddenActions(actions)

    def insertAction(self, before, action):
        return self.bar.insertAction(before, action)

    def addSeparator(self):
        self.bar.addSeparator()

    def insertSeparator(self, index: int):
        self.bar.insertSeparator(index)

    def removeAction(self, action):
        self.bar.removeAction(action)

    def removeWidget(self, widget: QWidget):
        self.bar.removeWidget(widget)

    def removeHiddenAction(self, action):
        self.bar.removeHiddenAction(action)

    def setToolButtonStyle(self, style):
        self.bar.setToolButtonStyle(style)

    def toolButtonStyle(self):
        return self.bar.toolButtonStyle()

    def setButtonTight(self, isTight: bool):
        self.bar.setButtonTight(isTight)

    def isButtonTight(self):
        return self.bar.isButtonTight()

    def setIconSize(self, size):
        self.bar.setIconSize(size)

    def iconSize(self):
        return self.bar.iconSize()

    def setFont(self, font):
        self.bar.setFont(font)

    def setSpacing(self, spacing: int):
        self.bar.setSpacing(spacing)

    def spacing(self):
        return self.bar.spacing()

    def suitableWidth(self):
        m = self.contentsMargins()
        return m.left() + m.right() + self.bar.suitableWidth()

    def resizeToSuitableWidth(self):
        self.bar.resizeToSuitableWidth()
        self.setFixedWidth(self.suitableWidth())

    def actions(self):
        return self.bar.actions()


class MovableCommandBarView(FlyoutViewBase):
    """ Movable command bar view - 可拖动命令栏视图封装 """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.bar = MovableCommandBar(self)
        self.hBoxLayout = QHBoxLayout(self)

        self.hBoxLayout.setContentsMargins(6, 6, 6, 6)
        self.hBoxLayout.addWidget(self.bar)
        self.hBoxLayout.setSizeConstraint(QHBoxLayout.SetMinAndMaxSize)

        # 设置默认样式
        self.setButtonTight(True)
        self.setIconSize(QSize(14, 14))

    # 拖动特有方法
    def setDockPosition(self, position):
        """ 设置停靠位置 """
        self.bar.setDockPosition(position)

    def dockPosition(self):
        """ 获取停靠位置 """
        return self.bar.dockPosition()

    def setResponsive(self, enabled: bool):
        """ 设置响应式模式 """
        self.bar.setResponsive(enabled)

    def isResponsive(self):
        """ 获取响应式状态 """
        return self.bar.isResponsive()

    # 委托所有基础方法到内部的 bar
    def addWidget(self, widget: QWidget):
        self.bar.addWidget(widget)

    def addAction(self, action):
        return self.bar.addAction(action)

    def addActions(self, actions):
        self.bar.addActions(actions)

    def addHiddenAction(self, action):
        self.bar.addHiddenAction(action)

    def addHiddenActions(self, actions):
        self.bar.addHiddenActions(actions)

    def insertAction(self, before, action):
        return self.bar.insertAction(before, action)

    def addSeparator(self):
        self.bar.addSeparator()

    def insertSeparator(self, index: int):
        self.bar.insertSeparator(index)

    def removeAction(self, action):
        self.bar.removeAction(action)

    def removeWidget(self, widget: QWidget):
        self.bar.removeWidget(widget)

    def removeHiddenAction(self, action):
        self.bar.removeHiddenAction(action)

    def setToolButtonStyle(self, style):
        self.bar.setToolButtonStyle(style)

    def toolButtonStyle(self):
        return self.bar.toolButtonStyle()

    def setButtonTight(self, isTight: bool):
        self.bar.setButtonTight(isTight)

    def isButtonTight(self):
        return self.bar.isButtonTight()

    def setIconSize(self, size):
        self.bar.setIconSize(size)

    def iconSize(self):
        return self.bar.iconSize()

    def setFont(self, font):
        self.bar.setFont(font)

    def setSpacing(self, spacing: int):
        self.bar.setSpacing(spacing)

    def spacing(self):
        return self.bar.spacing()

    def suitableWidth(self):
        m = self.contentsMargins()
        return m.left() + m.right() + self.bar.suitableWidth()

    def suitableHeight(self):
        m = self.contentsMargins()
        return m.top() + m.bottom() + self.bar.suitableHeight()

    def resizeToSuitableWidth(self):
        self.bar.resizeToSuitableWidth()
        self.setFixedWidth(self.suitableWidth())

    def resizeToSuitableHeight(self):
        self.bar.resizeToSuitableHeight()
        self.setFixedHeight(self.suitableHeight())

    def actions(self):
        return self.bar.actions()
