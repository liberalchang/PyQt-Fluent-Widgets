# coding:utf-8
from typing import Optional
from PySide6.QtCore import Qt, QRect, QPropertyAnimation, QEasingCurve, Property, Signal
from PySide6.QtGui import QPainter, QColor, QPaintEvent, QMouseEvent, QEnterEvent
from PySide6.QtWidgets import QSplitter, QSplitterHandle, QWidget, QPushButton

from ...common.style_sheet import themeColor, isDarkTheme, FluentStyleSheet
from ...common.icon import AntDesignIcon as Icon


class CollapseButton(QPushButton):
    """分割器手柄上的折叠按钮"""

    def __init__(self, orientation: Qt.Orientation, parent=None):
        super().__init__(parent)
        self._orientation = orientation
        self._collapsed = False
        self.setFixedSize(20, 20)  # 增大按钮尺寸以完整显示图标
        self.setCursor(Qt.ArrowCursor)
        self._updateIcon()

    def setOrientation(self, orientation: Qt.Orientation):
        """设置按钮方向"""
        self._orientation = orientation
        self._updateIcon()

    def setCollapsed(self, collapsed: bool):
        """设置折叠状态"""
        self._collapsed = collapsed
        self._updateIcon()

    def _getComplementaryColor(self) -> QColor:
        """获取主题色的互补色"""
        theme_color = themeColor()
        # 从QColor中获取RGB值
        r, g, b = theme_color.red(), theme_color.green(), theme_color.blue()
        # 计算互补色 (255 - R, 255 - G, 255 - B)
        comp_r = 255 - r
        comp_g = 255 - g
        comp_b = 255 - b
        return QColor(comp_r, comp_g, comp_b)

    def _updateIcon(self):
        """根据方向和状态更新图标"""
        # 获取主题色的互补色
        comp_color = self._getComplementaryColor()
        
        if self._orientation == Qt.Horizontal:
            # 水平分割器: 左右折叠
            icon = Icon.CARET_RIGHT if self._collapsed else Icon.CARET_LEFT
        else:
            # 垂直分割器: 上下折叠
            icon = Icon.CARET_DOWN if self._collapsed else Icon.CARET_UP
        
        # 使用互补色创建图标
        self.setIcon(icon.icon(color=comp_color))


class FluentSplitterHandle(QSplitterHandle):
    """Fluent Design风格的分割器手柄
    
    特性:
    - 主题色样式
    - 悬停时宽度增加动画
    - 集成折叠按钮
    """

    def __init__(self, orientation: Qt.Orientation, parent: QSplitter):
        super().__init__(orientation, parent)
        self._handleWidth = 10  # 默认宽度(增大以适配按钮)
        self._hoverWidth = 16  # 悬停时宽度(增大拉动区域)
        self._currentWidth = self._handleWidth
        self._isHovered = False
        
        # 创建折叠按钮
        self.collapseButton = CollapseButton(orientation, self)
        self.collapseButton.clicked.connect(self._onCollapseClicked)
        
        # 创建宽度动画
        self._widthAnimation = QPropertyAnimation(self, b'handleWidth')
        self._widthAnimation.setDuration(100)
        self._widthAnimation.setEasingCurve(QEasingCurve.OutCubic)
        
        self._updateLayout()

    def _updateLayout(self):
        """更新折叠按钮位置"""
        if self.orientation() == Qt.Horizontal:
            x = (self.width() - self.collapseButton.width()) // 2
            y = (self.height() - self.collapseButton.height()) // 2
        else:
            x = (self.width() - self.collapseButton.width()) // 2
            y = (self.height() - self.collapseButton.height()) // 2
        
        self.collapseButton.move(x, y)

    @Property(int)
    def handleWidth(self):
        """获取当前手柄宽度"""
        return self._currentWidth

    @handleWidth.setter
    def handleWidth(self, width: int):
        """设置手柄宽度"""
        self._currentWidth = width
        self.update()

    def paintEvent(self, event: QPaintEvent):
        """绘制手柄"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # 获取主题色
        theme_color = themeColor()
        
        # 根据是否悬停选择颜色和透明度
        if self._isHovered:
            color = QColor(theme_color)
        else:
            # 非悬停状态使用浅灰色
            if isDarkTheme():
                color = QColor(200, 200, 200, 120)  # 深色模式下的浅灰色
            else:
                color = QColor(220, 220, 220, 150)  # 浅色模式下的浅灰色
        
        # 计算手柄矩形
        if self.orientation() == Qt.Horizontal:
            # 垂直手柄(用于水平分割器)
            x = (self.width() - self._currentWidth) // 2
            rect = QRect(x, 0, self._currentWidth, self.height())
            # 根据宽度动态设置圆角半径 (宽度的一半，形成完全圆角的效果)
            radius = self._currentWidth // 2
        else:
            # 水平手柄(用于垂直分割器)
            y = (self.height() - self._currentWidth) // 2
            rect = QRect(0, y, self.width(), self._currentWidth)
            # 根据高度动态设置圆角半径
            radius = self._currentWidth // 2
        
        # 绘制圆角矩形 (使用动态圆角半径)
        painter.setPen(Qt.NoPen)
        painter.setBrush(color)
        painter.drawRoundedRect(rect, radius, radius)

    def enterEvent(self, event: QEnterEvent):
        """鼠标进入事件"""
        super().enterEvent(event)
        self._isHovered = True
        self._widthAnimation.stop()
        self._widthAnimation.setStartValue(self._currentWidth)
        self._widthAnimation.setEndValue(self._hoverWidth)
        self._widthAnimation.start()

    def leaveEvent(self, event):
        """鼠标离开事件"""
        super().leaveEvent(event)
        self._isHovered = False
        self._widthAnimation.stop()
        self._widthAnimation.setStartValue(self._currentWidth)
        self._widthAnimation.setEndValue(self._handleWidth)
        self._widthAnimation.start()

    def resizeEvent(self, event):
        """尺寸改变事件"""
        super().resizeEvent(event)
        self._updateLayout()

    def sizeHint(self):
        """返回建议尺寸"""
        size = super().sizeHint()
        if self.orientation() == Qt.Horizontal:
            size.setWidth(self._handleWidth)
        else:
            size.setHeight(self._handleWidth)
        return size

    def _onCollapseClicked(self):
        """折叠按钮点击处理"""
        splitter = self.splitter()
        if not splitter:
            return
        
        # 获取当前手柄的索引
        index = splitter.indexOf(self)
        if index < 0:
            return
        
        # 通知父分割器执行折叠
        if isinstance(splitter, FluentSplitter):
            splitter._toggleCollapse(index)


class FluentSplitter(QSplitter):
    """Fluent Design风格的分割器
    
    提供符合Windows 11 Fluent Design规范的分割器组件,支持:
    - 水平和垂直方向分割
    - 主题色手柄样式
    - 悬停交互效果
    - 面板折叠/展开功能
    """

    def __init__(self, orientation: Qt.Orientation = Qt.Horizontal, parent: Optional[QWidget] = None):
        super().__init__(orientation, parent)
        self.setHandleWidth(10)  # 与FluentSplitterHandle._handleWidth一致
        self.setChildrenCollapsible(True)
        
        # 存储折叠前的尺寸
        self._collapsedSizes = {}
        
        # 应用样式
        FluentStyleSheet.SPLITTER.apply(self)

    def createHandle(self) -> QSplitterHandle:
        """创建自定义手柄"""
        return FluentSplitterHandle(self.orientation(), self)

    def _toggleCollapse(self, handleIndex: int):
        """切换面板折叠状态
        
        Parameters
        ----------
        handleIndex: int
            手柄索引,折叠其左侧/上侧的面板
        """
        # 获取要折叠的面板索引(手柄左侧/上侧的面板)
        panelIndex = handleIndex
        
        if panelIndex < 0 or panelIndex >= self.count():
            return
        
        sizes = self.sizes()
        currentSize = sizes[panelIndex]
        
        # 判断当前是否已折叠
        if currentSize == 0:
            # 展开面板
            if panelIndex in self._collapsedSizes:
                sizes[panelIndex] = self._collapsedSizes[panelIndex]
                del self._collapsedSizes[panelIndex]
            else:
                # 如果没有保存的尺寸,平均分配空间
                totalSize = sum(sizes)
                sizes[panelIndex] = totalSize // self.count()
            
            # 更新按钮状态
            handle = self.handle(handleIndex)
            if isinstance(handle, FluentSplitterHandle):
                handle.collapseButton.setCollapsed(False)
        else:
            # 折叠面板
            self._collapsedSizes[panelIndex] = currentSize
            sizes[panelIndex] = 0
            
            # 更新按钮状态
            handle = self.handle(handleIndex)
            if isinstance(handle, FluentSplitterHandle):
                handle.collapseButton.setCollapsed(True)
        
        self.setSizes(sizes)

    def setOrientation(self, orientation: Qt.Orientation):
        """设置分割器方向"""
        super().setOrientation(orientation)
        # 更新所有手柄的方向
        for i in range(self.count() - 1):
            handle = self.handle(i + 1)
            if isinstance(handle, FluentSplitterHandle):
                handle.collapseButton.setOrientation(orientation)
                handle._updateLayout()
