# coding:utf-8
import sys
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

from qfluentwidgets import (MenuBar, RoundMenu, CheckableMenu, MenuIndicatorType, 
                            FluentIcon, FluentWindow, setTheme, Theme, Action)


class MenuBarDemo(QWidget):
    """MenuBar 独立组件演示"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MenuBar Demo - 独立组件')
        self.resize(800, 600)
        
        # 创建布局
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # 创建 MenuBar
        self.menuBar = MenuBar(self)
        layout.addWidget(self.menuBar)
        
        # 添加内容区域
        contentLabel = QLabel('这是内容区域\n\n演示包括：\n'
                             '- 基础菜单（文件菜单）\n'
                             '- 分组菜单（编辑菜单）\n'
                             '- 嵌套菜单（视图菜单）\n'
                             '- 可复选菜单（选项菜单）\n'
                             '- 可单选菜单（主题菜单）', self)
        contentLabel.setAlignment(Qt.AlignCenter)
        contentLabel.setStyleSheet('QLabel { font-size: 16px; padding: 20px; }')
        layout.addWidget(contentLabel, 1)
        
        # 初始化菜单
        self._createMenus()
    
    def _createMenus(self):
        """创建所有菜单"""
        self._createFileMenu()
        self._createEditMenu()
        self._createViewMenu()
        self._createOptionsMenu()
        self._createThemeMenu()
        self._createHelpMenu()
    
    def _createFileMenu(self):
        """创建文件菜单（基础菜单）"""
        fileMenu = self.menuBar.addMenu('文件', FluentIcon.DOCUMENT)
        
        # 添加菜单项
        fileMenu.addAction(Action(FluentIcon.ADD, '新建', triggered=lambda: self._showMessage('新建文件')))
        fileMenu.addAction(Action(FluentIcon.FOLDER, '打开', triggered=lambda: self._showMessage('打开文件')))
        fileMenu.addAction(Action(FluentIcon.SAVE, '保存', triggered=lambda: self._showMessage('保存文件')))
        fileMenu.addAction(Action(FluentIcon.SAVE_AS, '另存为', triggered=lambda: self._showMessage('另存为')))
        
        fileMenu.addSeparator()
        
        fileMenu.addAction(Action(FluentIcon.CLOSE, '退出', triggered=self.close))
    
    def _createEditMenu(self):
        """创建编辑菜单（分组菜单）"""
        editMenu = self.menuBar.addMenu('编辑', FluentIcon.EDIT)
        
        # 第一组：剪贴板操作
        editMenu.addAction(Action(FluentIcon.COPY, '复制', triggered=lambda: self._showMessage('复制')))
        editMenu.addAction(Action(FluentIcon.CUT, '剪切', triggered=lambda: self._showMessage('剪切')))
        editMenu.addAction(Action(FluentIcon.PASTE, '粘贴', triggered=lambda: self._showMessage('粘贴')))
        
        editMenu.addSeparator()  # 分隔线
        
        # 第二组：撤销/重做
        editMenu.addAction(Action(FluentIcon.RETURN, '撤销', triggered=lambda: self._showMessage('撤销')))
        editMenu.addAction(Action(FluentIcon.SYNC, '重做', triggered=lambda: self._showMessage('重做')))
        
        editMenu.addSeparator()
        
        # 第三组：查找
        editMenu.addAction(Action(FluentIcon.SEARCH, '查找', triggered=lambda: self._showMessage('查找')))
        editMenu.addAction(Action(FluentIcon.SEARCH, '替换', triggered=lambda: self._showMessage('替换')))
    
    def _createViewMenu(self):
        """创建视图菜单（嵌套菜单）"""
        viewMenu = self.menuBar.addMenu('视图', FluentIcon.VIEW)
        
        # 添加基础菜单项
        viewMenu.addAction(Action(FluentIcon.ZOOM_IN, '放大', triggered=lambda: self._showMessage('放大')))
        viewMenu.addAction(Action(FluentIcon.ZOOM_OUT, '缩小', triggered=lambda: self._showMessage('缩小')))
        viewMenu.addAction(Action(FluentIcon.FIT_PAGE, '适应窗口', triggered=lambda: self._showMessage('适应窗口')))
        
        viewMenu.addSeparator()
        
        # 添加子菜单：工具栏
        toolbarMenu = RoundMenu('工具栏', self)
        toolbarMenu.setIcon(FluentIcon.MENU)
        toolbarMenu.addAction(Action(FluentIcon.CHECKBOX, '主工具栏', triggered=lambda: self._showMessage('显示主工具栏')))
        toolbarMenu.addAction(Action(FluentIcon.CHECKBOX, '格式工具栏', triggered=lambda: self._showMessage('显示格式工具栏')))
        toolbarMenu.addAction(Action(FluentIcon.CHECKBOX, '状态栏', triggered=lambda: self._showMessage('显示状态栏')))
        viewMenu.addMenu(toolbarMenu)
        
        # 添加子菜单：面板
        panelMenu = RoundMenu('面板', self)
        panelMenu.setIcon(FluentIcon.APPLICATION)
        panelMenu.addAction(Action(FluentIcon.CHAT, '控制台', triggered=lambda: self._showMessage('显示控制台')))
        panelMenu.addAction(Action(FluentIcon.FOLDER, '文件浏览器', triggered=lambda: self._showMessage('显示文件浏览器')))
        panelMenu.addAction(Action(FluentIcon.SEARCH, '搜索', triggered=lambda: self._showMessage('显示搜索面板')))
        viewMenu.addMenu(panelMenu)
        
        viewMenu.addSeparator()
        
        viewMenu.addAction(Action(FluentIcon.FULL_SCREEN, '全屏', triggered=lambda: self._showMessage('全屏模式')))
    
    def _createOptionsMenu(self):
        """创建选项菜单（可复选菜单）"""
        # 使用 addCheckableMenu 方法创建复选框菜单
        optionsMenu = self.menuBar.addCheckableMenu('选项', MenuIndicatorType.CHECK, FluentIcon.SETTING)
        
        # 添加可复选项
        action1 = Action(FluentIcon.CHECKBOX, '自动保存', checkable=True)
        action1.triggered.connect(lambda: self._showMessage(f'自动保存: {action1.isChecked()}'))
        optionsMenu.addAction(action1)
        
        action2 = Action(FluentIcon.CHECKBOX, '显示行号', checkable=True, checked=True)
        action2.triggered.connect(lambda: self._showMessage(f'显示行号: {action2.isChecked()}'))
        optionsMenu.addAction(action2)
        
        action3 = Action(FluentIcon.CHECKBOX, '自动换行', checkable=True)
        action3.triggered.connect(lambda: self._showMessage(f'自动换行: {action3.isChecked()}'))
        optionsMenu.addAction(action3)
        
        optionsMenu.addSeparator()
        
        action4 = Action(FluentIcon.CHECKBOX, '启用拼写检查', checkable=True)
        action4.triggered.connect(lambda: self._showMessage(f'拼写检查: {action4.isChecked()}'))
        optionsMenu.addAction(action4)
        
        action5 = Action(FluentIcon.CHECKBOX, '启用代码提示', checkable=True, checked=True)
        action5.triggered.connect(lambda: self._showMessage(f'代码提示: {action5.isChecked()}'))
        optionsMenu.addAction(action5)
    
    def _createThemeMenu(self):
        """创建主题菜单（可单选菜单）"""
        # 使用 addCheckableMenu 方法创建单选菜单
        themeMenu = self.menuBar.addCheckableMenu('主题', MenuIndicatorType.RADIO, FluentIcon.PALETTE)
        
        # 添加单选项
        lightAction = Action(FluentIcon.BRIGHTNESS, '浅色', checkable=True, checked=True)
        lightAction.triggered.connect(lambda: self._changeTheme(Theme.LIGHT))
        themeMenu.addAction(lightAction)
        
        darkAction = Action(FluentIcon.CONSTRACT, '深色', checkable=True)
        darkAction.triggered.connect(lambda: self._changeTheme(Theme.DARK))
        themeMenu.addAction(darkAction)
        
        autoAction = Action(FluentIcon.TRANSPARENT, '自动', checkable=True)
        autoAction.triggered.connect(lambda: self._changeTheme(Theme.AUTO))
        themeMenu.addAction(autoAction)
    
    def _createHelpMenu(self):
        """创建帮助菜单"""
        helpMenu = self.menuBar.addMenu('帮助', FluentIcon.HELP)
        
        helpMenu.addAction(Action(FluentIcon.DOCUMENT, '文档', 
                          triggered=lambda: QDesktopServices.openUrl(QUrl('https://qfluentwidgets.com'))))
        helpMenu.addAction(Action(FluentIcon.GITHUB, 'GitHub', 
                          triggered=lambda: QDesktopServices.openUrl(QUrl('https://github.com/zhiyiYo/PyQt-Fluent-Widgets'))))
        
        helpMenu.addSeparator()
        
        helpMenu.addAction(Action(FluentIcon.INFO, '关于', triggered=lambda: self._showMessage('QFluentWidgets MenuBar Demo')))
    
    def _showMessage(self, text):
        """显示消息"""
        print(f'[Action] {text}')
    
    def _changeTheme(self, theme):
        """切换主题"""
        setTheme(theme)
        print(f'[Theme] Changed to {theme}')


class FluentWindowDemo(FluentWindow):
    """FluentWindow 集成演示"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MenuBar Demo - FluentWindow 集成')
        self.resize(900, 700)
        
        # 创建 MenuBar
        menuBar = MenuBar(self)
        self.setMenuBar(menuBar)
        
        # 创建菜单
        self._createMenus(menuBar)
        
        # 添加导航界面（可选）
        homePage = QLabel('Home Page\n\n这是 FluentWindow 中集成 MenuBar 的示例', self)
        homePage.setObjectName('homePage')
        homePage.setAlignment(Qt.AlignCenter)
        self.addSubInterface(
            homePage,
            FluentIcon.HOME,
            'Home'
        )
        
        settingsPage = QLabel('Settings Page', self)
        settingsPage.setObjectName('settingsPage')
        settingsPage.setAlignment(Qt.AlignCenter)
        self.addSubInterface(
            settingsPage,
            FluentIcon.SETTING,
            'Settings'
        )
    
    def _createMenus(self, menuBar):
        """创建菜单（简化版）"""
        # 文件菜单
        fileMenu = menuBar.addMenu('文件', FluentIcon.DOCUMENT)
        fileMenu.addAction(Action(FluentIcon.ADD, '新建'))
        fileMenu.addAction(Action(FluentIcon.FOLDER, '打开'))
        fileMenu.addAction(Action(FluentIcon.SAVE, '保存'))
        fileMenu.addSeparator()
        fileMenu.addAction(Action(FluentIcon.CLOSE, '退出', triggered=self.close))
        
        # 编辑菜单
        editMenu = menuBar.addMenu('编辑', FluentIcon.EDIT)
        editMenu.addAction(Action(FluentIcon.COPY, '复制'))
        editMenu.addAction(Action(FluentIcon.CUT, '剪切'))
        editMenu.addAction(Action(FluentIcon.PASTE, '粘贴'))
        
        # 帮助菜单
        helpMenu = menuBar.addMenu('帮助', FluentIcon.HELP)
        helpMenu.addAction(Action(FluentIcon.INFO, '关于'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 演示1：独立组件
    demo1 = MenuBarDemo()
    demo1.show()
    
    # 演示2：FluentWindow 集成
    demo2 = FluentWindowDemo()
    demo2.show()
    
    sys.exit(app.exec())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 演示1：独立组件
    demo1 = MenuBarDemo()
    demo1.show()
    
    # 演示2：FluentWindow 集成
    demo2 = FluentWindowDemo()
    demo2.show()
    
    sys.exit(app.exec())
