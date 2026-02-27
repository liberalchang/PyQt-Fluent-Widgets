# coding:utf-8
import sys
import os

# Add parent directory to sys.path to import qfluentwidgets
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QFrame, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon

from qfluentwidgets import (NavigationItemPosition, FluentWindow,
                            FluentIcon as FIF, Theme, setTheme, DrawerWindow, PrimaryPushButton,
                            ScrollArea, SettingCardGroup, OptionsSettingCard, ExpandLayout,
                            OptionsConfigItem, OptionsValidator, QConfig, qconfig)


class Config(QConfig):
    themeMode = OptionsConfigItem("Theme", "ThemeMode", Theme.LIGHT, OptionsValidator(Theme), serializer=lambda x: x.value)
    windowEffect = OptionsConfigItem("Theme", "WindowEffect", "Acrylic", OptionsValidator(["Mica", "Acrylic", "None"]), serializer=lambda x: x)

cfg = Config()


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = QLabel(text, self)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))


class SettingInterface(ScrollArea):
    """ Setting interface """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)
        self.setObjectName("setting-interface")

        # Init layout
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.viewport().setObjectName("viewport")
        self.scrollWidget.setObjectName("scrollWidget")

        # Personalization
        self.personalGroup = SettingCardGroup("Personalization", self.scrollWidget)
        self.expandLayout.addWidget(self.personalGroup)

        # Theme
        self.themeCard = OptionsSettingCard(
            cfg.themeMode,
            FIF.BRUSH,
            'Application Theme',
            "Change the appearance of your application",
            texts=["Light", "Dark", "Use system setting"],
            parent=self.personalGroup
        )
        self.personalGroup.addSettingCard(self.themeCard)

        # Effect
        self.effectCard = OptionsSettingCard(
            cfg.windowEffect,
            FIF.TRANSPARENT,
            'Window Effect',
            "Switch between Mica, Acrylic or None",
            texts=["Mica", "Acrylic", "None"],
            parent=self.personalGroup
        )
        self.personalGroup.addSettingCard(self.effectCard)

        # Connect
        cfg.themeMode.valueChanged.connect(setTheme)
        cfg.windowEffect.valueChanged.connect(self.onWindowEffectChanged)
        
        # Set background transparent to show effect
        self.setStyleSheet("QWidget{background: transparent}")

    def onWindowEffectChanged(self, effect):
        window = self.window()
        if not isinstance(window, FluentWindow):
            return

        if effect == "Mica":
            window.setMicaEffectEnabled(True)
        elif effect == "Acrylic":
            window.setAcrylicEffectEnabled(True)
        else:
            window.setMicaEffectEnabled(False)
            window.setAcrylicEffectEnabled(False)


class SearchInterface(DrawerWindow):
    """ Search interface with drawer """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("search-interface")
        
        # Central widget
        self.central_widget = QWidget()
        self.set_central_widget(self.central_widget)
        
        # Layout
        self.vBoxLayout = QVBoxLayout(self.central_widget)
        self.vBoxLayout.setContentsMargins(30, 30, 30, 30)
        self.vBoxLayout.setAlignment(Qt.AlignCenter)
        
        self.label = QLabel("Search Interface with Drawer", self.central_widget)
        self.label.setStyleSheet("font-size: 24px; font-weight: bold;")
        
        # Buttons to open drawers
        self.openRightDrawerBtn = PrimaryPushButton("Open Filters (Right)", self.central_widget)
        self.openRightDrawerBtn.clicked.connect(lambda: self.show_drawer('right', 300, "Search Filters"))
        
        self.openBottomDrawerBtn = PrimaryPushButton("Open Console (Bottom)", self.central_widget)
        self.openBottomDrawerBtn.clicked.connect(lambda: self.show_drawer('bottom', 200, "Console Output"))
        
        self.vBoxLayout.addWidget(self.label)
        self.vBoxLayout.addSpacing(20)
        self.vBoxLayout.addWidget(self.openRightDrawerBtn)
        self.vBoxLayout.addWidget(self.openBottomDrawerBtn)
        
        # Populate Right Drawer
        self.right_drawer.content_layout.setContentsMargins(15, 15, 15, 15)
        self.right_drawer.content_layout.addWidget(QLabel("Filter Options:"))
        self.right_drawer.content_layout.addWidget(PrimaryPushButton("Apply Filter"))
        self.right_drawer.content_layout.addStretch(1)
        
        # Populate Bottom Drawer
        self.bottom_drawer.content_layout.setContentsMargins(15, 15, 15, 15)
        self.bottom_drawer.content_layout.addWidget(QLabel("System Logs..."))


class Window(FluentWindow):

    def __init__(self):
        super().__init__(showReturnButton=False)

        # 启用窗口特效（Windows 11）
        # 注意：亚克力/云母在窗口 show 之前设置，可能不会立刻生效
        self._applyInitialWindowEffect()

        # create sub interfaces
        self.searchInterface = SearchInterface(self)
        self.musicInterface = Widget('Music Interface', self)
        self.videoInterface = Widget('Video Interface', self)
        self.folderInterface = Widget('Folder Interface', self)
        self.settingInterface = SettingInterface(self)

        # add items to navigation interface
        self.initNavigation()
        self.navigationInterface.setAutoResizeEnabled(True)

        self.resize(900, 700)
        self.setWindowIcon(QIcon(FIF.SEARCH.path(None)))
        self.setWindowTitle('Navigation Test')

    def _applyInitialWindowEffect(self):
        """根据配置启用初始窗口特效"""
        effect = cfg.windowEffect.value
        if effect == "Mica":
            self.setMicaEffectEnabled(True)
        elif effect == "Acrylic":
            self.setAcrylicEffectEnabled(True)
        else:
            self.setMicaEffectEnabled(False)
            self.setAcrylicEffectEnabled(False)

    def _triggerSizeChange(self):
        """触发微小尺寸变化，促使 DWM 重新刷新窗口合成效果"""
        current_size = self.size()
        self.resize(current_size.width() + 1, current_size.height())
        self.resize(current_size)

    def showEvent(self, e):
        super().showEvent(e)
        # 窗口显示后再应用一次特效，避免启动时亚克力不生效
        from PySide6.QtCore import QTimer
        QTimer.singleShot(150, self._applyInitialWindowEffect)
        QTimer.singleShot(250, self._triggerSizeChange)

    def initNavigation(self):
        self.addSubInterface(self.searchInterface, FIF.SEARCH, 'Search')
        self.addSubInterface(self.musicInterface, FIF.MUSIC, 'Music')
        self.addSubInterface(self.videoInterface, FIF.VIDEO, 'Video')
        self.addSubInterface(self.folderInterface, FIF.FOLDER, 'Folder Library', NavigationItemPosition.SCROLL)
        
        self.navigationInterface.addSeparator()

        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)
    
    # def resizeEvent(self, e):
    #     """重写 resizeEvent 以确保窗口特效在最大化后仍然有效"""
    #     super().resizeEvent(e)
    #     # 注意：由于 FluentWidget 现在已经内置了 OpenGL 修复和延迟初始化，
    #     # 这个方法主要是为了向后兼容和额外保险


if __name__ == '__main__':
    # 设置主题（可选择 Theme.LIGHT 或 Theme.DARK）
    setTheme(Theme.LIGHT, save=False)  # 使用亮色主题以更好展示云母特效
    
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())
