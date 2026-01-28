# coding:utf-8
from typing import Union, List

from PySide6.QtCore import Qt, Signal, QPoint, QEvent
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton

from ...common.icon import FluentIconBase, Icon
from ...common.style_sheet import FluentStyleSheet
from .menu import RoundMenu, CheckableMenu, MenuIndicatorType


class MenuBarItem(QPushButton):
    """菜单栏项（触发按钮）
    
    表示菜单栏中的一个顶级菜单项，点击时弹出关联的下拉菜单。
    
    Examples
    --------
    >>> menuBar = MenuBar()
    >>> fileMenu = RoundMenu("File", menuBar)
    >>> fileMenu.addAction(QAction("New", fileMenu))
    >>> menuBarItem = MenuBarItem("File", fileMenu, menuBar)
    """
    
    clicked = Signal()  # 点击信号
    
    def __init__(self, text: str, menu: RoundMenu = None, parent=None):
        """初始化菜单项按钮
        
        Parameters
        ----------
        text: str
            菜单项文本（如"文件"、"编辑"）
            
        menu: RoundMenu
            关联的下拉菜单对象
            
        parent: QWidget
            父组件
        """
        super().__init__(text, parent)
        self._menu = menu
        self._isActive = False
        
        # 设置按钮样式属性
        self.setObjectName("menuBarItem")
        self.setCheckable(True)
        self.setCursor(Qt.PointingHandCursor)
        
        # 连接点击事件
        super().clicked.connect(self._onClicked)
    
    def setMenu(self, menu: RoundMenu):
        """设置关联的下拉菜单
        
        Parameters
        ----------
        menu: RoundMenu
            下拉菜单对象
        """
        self._menu = menu
    
    def menu(self) -> RoundMenu:
        """获取关联的下拉菜单
        
        Returns
        -------
        menu: RoundMenu
            下拉菜单对象
        """
        return self._menu
    
    def showMenu(self):
        """显示下拉菜单
        
        在当前按钮下方左对齐显示菜单
        """
        if not self._menu:
            return
        
        # 计算菜单位置：在按钮下方左对齐
        pos = self.mapToGlobal(QPoint(0, self.height()))
        
        # 设置激活状态
        self.setChecked(True)
        self._isActive = True
        
        # 显示菜单（exec 会阻塞直到菜单关闭）
        self._menu.exec(pos)
        
        # 菜单关闭后恢复状态
        self.setChecked(False)
        self._isActive = False
    
    def _onClicked(self):
        """处理点击事件"""
        self.showMenu()
    
    def isActive(self) -> bool:
        """返回是否处于激活状态
        
        Returns
        -------
        isActive: bool
            True 表示菜单正在显示
        """
        return self._isActive


class MenuBar(QWidget):
    """菜单栏组件
    
    提供水平排列的顶级菜单项，点击时弹出下拉菜单。
    支持基础菜单、分组菜单、嵌套菜单、可复选菜单和可单选菜单。
    
    Examples
    --------
    >>> menuBar = MenuBar()
    >>> 
    >>> # 添加文件菜单
    >>> fileMenu = menuBar.addMenu("File")
    >>> fileMenu.addAction(QAction("New", fileMenu))
    >>> fileMenu.addAction(QAction("Open", fileMenu))
    >>> fileMenu.addSeparator()
    >>> fileMenu.addAction(QAction("Exit", fileMenu))
    >>> 
    >>> # 添加编辑菜单（带图标）
    >>> from qfluentwidgets import FluentIcon
    >>> editMenu = menuBar.addMenu("Edit", FluentIcon.EDIT)
    >>> editMenu.addAction(QAction("Cut", editMenu))
    >>> editMenu.addAction(QAction("Copy", editMenu))
    >>> 
    >>> # 添加可复选菜单
    >>> viewMenu = menuBar.addCheckableMenu("View", MenuIndicatorType.CHECK)
    >>> viewMenu.addAction(QAction("Toolbar", viewMenu))
    >>> viewMenu.addAction(QAction("Status Bar", viewMenu))
    """
    
    def __init__(self, parent=None):
        """初始化菜单栏
        
        Parameters
        ----------
        parent: QWidget
            父组件
        """
        super().__init__(parent)
        
        self.hBoxLayout = QHBoxLayout(self)
        self.menuItems: List[MenuBarItem] = []
        self._menus: List[RoundMenu] = []
        
        self.__initWidgets()
        self.__initLayout()
    
    def __initWidgets(self):
        """初始化组件"""
        self.setObjectName("menuBar")
        
        # 应用样式
        FluentStyleSheet.MENU_BAR.apply(self)
    
    def __initLayout(self):
        """初始化布局"""
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.addStretch(1)
    
    def addMenu(self, text: str, icon: Union[QIcon, FluentIconBase, str] = None) -> RoundMenu:
        """添加菜单项
        
        Parameters
        ----------
        text: str
            菜单项文本（如"文件"、"编辑"）
            
        icon: QIcon | FluentIconBase | str
            菜单项图标（可选）
            
        Returns
        -------
        menu: RoundMenu
            创建的下拉菜单对象
        """
        menu = RoundMenu(text, self)
        
        if icon:
            if isinstance(icon, FluentIconBase):
                icon = Icon(icon)
            elif isinstance(icon, str):
                icon = QIcon(icon)
            menu.setIcon(icon)
        
        # 创建菜单项按钮
        menuItem = MenuBarItem(text, menu, self)
        
        # 添加到布局（在 stretch 之前）
        self.hBoxLayout.insertWidget(len(self.menuItems), menuItem)
        
        # 保存引用
        self.menuItems.append(menuItem)
        self._menus.append(menu)
        
        return menu
    
    def addCheckableMenu(self, text: str, 
                         indicatorType: MenuIndicatorType = MenuIndicatorType.CHECK,
                         icon: Union[QIcon, FluentIconBase, str] = None) -> CheckableMenu:
        """添加可复选/可单选菜单项
        
        Parameters
        ----------
        text: str
            菜单项文本
            
        indicatorType: MenuIndicatorType
            指示器类型：
            - MenuIndicatorType.CHECK: 复选框（多选）
            - MenuIndicatorType.RADIO: 单选按钮（单选）
            
        icon: QIcon | FluentIconBase | str
            菜单项图标（可选）
            
        Returns
        -------
        menu: CheckableMenu
            创建的可复选菜单对象
        """
        menu = CheckableMenu(text, self, indicatorType)
        
        if icon:
            if isinstance(icon, FluentIconBase):
                icon = Icon(icon)
            elif isinstance(icon, str):
                icon = QIcon(icon)
            menu.setIcon(icon)
        
        # 创建菜单项按钮
        menuItem = MenuBarItem(text, menu, self)
        
        # 添加到布局（在 stretch 之前）
        self.hBoxLayout.insertWidget(len(self.menuItems), menuItem)
        
        # 保存引用
        self.menuItems.append(menuItem)
        self._menus.append(menu)
        
        return menu
    
    def insertMenu(self, before: RoundMenu, text: str, 
                   icon: Union[QIcon, FluentIconBase, str] = None) -> RoundMenu:
        """在指定菜单前插入新菜单项
        
        Parameters
        ----------
        before: RoundMenu
            在此菜单之前插入
            
        text: str
            菜单项文本
            
        icon: QIcon | FluentIconBase | str
            菜单项图标（可选）
            
        Returns
        -------
        menu: RoundMenu
            创建的下拉菜单对象
        """
        if before not in self._menus:
            raise ValueError("The 'before' menu is not in the menu bar")
        
        index = self._menus.index(before)
        
        menu = RoundMenu(text, self)
        
        if icon:
            if isinstance(icon, FluentIconBase):
                icon = Icon(icon)
            elif isinstance(icon, str):
                icon = QIcon(icon)
            menu.setIcon(icon)
        
        # 创建菜单项按钮
        menuItem = MenuBarItem(text, menu, self)
        
        # 插入到指定位置
        self.hBoxLayout.insertWidget(index, menuItem)
        
        # 保存引用
        self.menuItems.insert(index, menuItem)
        self._menus.insert(index, menu)
        
        return menu
    
    def removeMenu(self, menu: RoundMenu):
        """移除指定菜单项
        
        Parameters
        ----------
        menu: RoundMenu
            要移除的菜单对象
        """
        if menu not in self._menus:
            return
        
        index = self._menus.index(menu)
        
        # 移除菜单项按钮
        menuItem = self.menuItems[index]
        self.hBoxLayout.removeWidget(menuItem)
        menuItem.deleteLater()
        
        # 移除引用
        self.menuItems.pop(index)
        self._menus.pop(index)
    
    def clear(self):
        """清空所有菜单项"""
        while self.menuItems:
            menuItem = self.menuItems.pop()
            self.hBoxLayout.removeWidget(menuItem)
            menuItem.deleteLater()
        
        self._menus.clear()
    
    def menus(self) -> List[RoundMenu]:
        """获取所有菜单对象
        
        Returns
        -------
        menus: List[RoundMenu]
            菜单对象列表
        """
        return self._menus.copy()
    
    def menuItemAt(self, index: int) -> MenuBarItem:
        """获取指定索引的菜单项按钮
        
        Parameters
        ----------
        index: int
            菜单项索引
            
        Returns
        -------
        menuItem: MenuBarItem
            菜单项按钮对象
        """
        if 0 <= index < len(self.menuItems):
            return self.menuItems[index]
        return None
    
    def count(self) -> int:
        """返回菜单项数量
        
        Returns
        -------
        count: int
            菜单项数量
        """
        return len(self.menuItems)
