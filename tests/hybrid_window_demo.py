import sys
import os
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtQuick import QQuickWindow, QSGRendererInterface

# Ensure qfluentwidgets is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import CaptionLabel, PrimaryPushButton, ListWidget, ComboBox
from qfluentwidgets.hybrid import FluentHybridWindow, HybridSplashScreen
from qfluentwidgets.common.config import Theme, WindowEffect, qconfig
from qfluentwidgets.common.style_sheet import setTheme

class HomeInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(24, 24, 24, 24)

        title = CaptionLabel("Home Interface", self)
        title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        title.setStyleSheet("font-size: 24px;")
        layout.addWidget(title)

        desc = CaptionLabel("用于验证 QML 标题栏与侧边导航联动", self)
        desc.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        desc.setStyleSheet("font-size: 14px; color: #666;")
        layout.addWidget(desc)

        self.statusLabel = CaptionLabel("等待操作", self)
        self.statusLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.statusLabel.setStyleSheet("font-size: 13px; color: #333;")
        layout.addWidget(self.statusLabel)

        panel = QWidget(self)
        panelLayout = QHBoxLayout(panel)
        panelLayout.setContentsMargins(0, 0, 0, 0)
        panelLayout.setSpacing(12)

        left = ListWidget(panel)
        left.addItems(["Card A", "Card B", "Card C", "Card D"])
        left.setFixedWidth(200)

        right = QWidget(panel)
        rightLayout = QVBoxLayout(right)
        rightLayout.setContentsMargins(0, 0, 0, 0)
        rightLayout.setSpacing(8)

        btn1 = PrimaryPushButton("主要操作", right)
        btn2 = PrimaryPushButton("次要操作", right)
        btn3 = PrimaryPushButton("危险操作", right)
        rightLayout.addWidget(btn1)
        rightLayout.addWidget(btn2)
        rightLayout.addWidget(btn3)
        rightLayout.addStretch(1)

        panelLayout.addWidget(left)
        panelLayout.addWidget(right, 1)
        layout.addWidget(panel, 1)

        btn1.clicked.connect(lambda: self.statusLabel.setText("已执行主要操作"))
        btn2.clicked.connect(lambda: self.statusLabel.setText("已执行次要操作"))
        btn3.clicked.connect(lambda: self.statusLabel.setText("已执行危险操作"))
        left.currentTextChanged.connect(lambda text: self.statusLabel.setText(f"已选择 {text}" if text else "等待操作"))

        self.setObjectName("Home")

class SettingInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(24, 24, 24, 24)

        title = CaptionLabel("Setting Interface", self)
        title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        title.setStyleSheet("font-size: 24px;")
        layout.addWidget(title)

        desc = CaptionLabel("用于验证主题切换与控件刷新", self)
        desc.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        desc.setStyleSheet("font-size: 14px; color: #666;")
        layout.addWidget(desc)

        self.statusLabel = CaptionLabel("等待操作", self)
        self.statusLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.statusLabel.setStyleSheet("font-size: 13px; color: #333;")
        layout.addWidget(self.statusLabel)

        row = QWidget(self)
        rowLayout = QHBoxLayout(row)
        rowLayout.setContentsMargins(0, 0, 0, 0)
        rowLayout.setSpacing(8)

        applyButton = PrimaryPushButton("应用", row)
        resetButton = PrimaryPushButton("重置", row)
        rowLayout.addWidget(applyButton)
        rowLayout.addWidget(resetButton)
        rowLayout.addStretch(1)
        layout.addWidget(row)
        layout.addStretch(1)

        applyButton.clicked.connect(lambda: self.statusLabel.setText("已点击应用"))
        resetButton.clicked.connect(lambda: self.statusLabel.setText("已点击重置"))

        # 主题与窗口风格切换控件（仅用于测试联动，不做控件主题适配）
        themeRow = QWidget(self)
        themeLayout = QHBoxLayout(themeRow)
        themeLayout.setContentsMargins(0, 0, 0, 0)
        themeLayout.setSpacing(8)
        themeLabel = CaptionLabel("主题模式：", themeRow)
        self.themeCombo = ComboBox(themeRow)
        # 使用中文选项，分别对应 Light/Dark/Auto
        self.themeCombo.addItems(["亮色", "暗色", "跟随系统"])
        # 初始化为当前配置
        currentThemeMode = qconfig.get(qconfig.themeMode)
        if currentThemeMode == Theme.LIGHT:
            self.themeCombo.setCurrentIndex(0)
        elif currentThemeMode == Theme.DARK:
            self.themeCombo.setCurrentIndex(1)
        else:
            self.themeCombo.setCurrentIndex(2)
        themeLayout.addWidget(themeLabel)
        themeLayout.addWidget(self.themeCombo)
        themeLayout.addStretch(1)
        layout.addWidget(themeRow)

        effectRow = QWidget(self)
        effectLayout = QHBoxLayout(effectRow)
        effectLayout.setContentsMargins(0, 0, 0, 0)
        effectLayout.setSpacing(8)
        effectLabel = CaptionLabel("窗口风格：", effectRow)
        self.effectCombo = ComboBox(effectRow)
        # 使用中文选项，分别对应 Mica/Acrylic/Disable
        self.effectCombo.addItems(["云母", "亚克力", "无"])
        # 初始化为当前配置
        currentEffect = qconfig.get(qconfig.windowEffect)
        if currentEffect == WindowEffect.MICA:
            self.effectCombo.setCurrentIndex(0)
        elif currentEffect == WindowEffect.ACRYLIC:
            self.effectCombo.setCurrentIndex(1)
        else:
            self.effectCombo.setCurrentIndex(2)
        effectLayout.addWidget(effectLabel)
        effectLayout.addWidget(self.effectCombo)
        effectLayout.addStretch(1)
        layout.addWidget(effectRow)

        # 连接信号：widget 触发主题/风格变化 -> 通知 qconfig，从而联动 QML
        self.themeCombo.currentIndexChanged.connect(self._onThemeModeChanged)
        self.effectCombo.currentIndexChanged.connect(self._onWindowEffectChanged)

    def _onThemeModeChanged(self, index: int):
        # 根据选择切换主题，仅更改主题，不做控件样式适配
        if index == 0:
            setTheme(Theme.LIGHT, save=False)
        elif index == 1:
            setTheme(Theme.DARK, save=False)
        else:
            setTheme(Theme.AUTO, save=False)
        self.statusLabel.setText("已切换主题模式")

    def _onWindowEffectChanged(self, index: int):
        w = self.window()
        if index == 0:
            qconfig.set(qconfig.windowEffect, WindowEffect.MICA, save=False)
            try:
                w.setWindowEffect(WindowEffect.MICA)
            except Exception:
                pass
        elif index == 1:
            qconfig.set(qconfig.windowEffect, WindowEffect.ACRYLIC, save=False)
            try:
                w.setWindowEffect(WindowEffect.ACRYLIC)
            except Exception:
                pass
        else:
            qconfig.set(qconfig.windowEffect, WindowEffect.DISABLE, save=False)
            try:
                w.setWindowEffect(WindowEffect.DISABLE)
            except Exception:
                pass
        self.statusLabel.setText("已切换窗口风格")

        self.setObjectName("Settings")


class DataInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(24, 24, 24, 24)

        title = CaptionLabel("Data Interface", self)
        title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        title.setStyleSheet("font-size: 24px;")
        layout.addWidget(title)

        listWidget = ListWidget(self)
        listWidget.addItems([f"数据项 {i}" for i in range(1, 11)])
        layout.addWidget(listWidget, 1)

        self.setObjectName("Data")

if __name__ == "__main__":
    # 启用高 DPI 支持
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_SCALE_FACTOR"] = "1"
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Basic"

    # 使用软件渲染提升 QQuickWidget 兼容性
    QQuickWindow.setGraphicsApi(QSGRendererInterface.GraphicsApi.Software)
    
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("你的应用名")
    
    # 设置系统层窗口标题（任务栏/Alt+Tab 等），不等同于 QML 顶部显示文字
    splash = HybridSplashScreen()
    splash.setIcon(FIF.ROBOT)
    splash.setTitle("你的应用名")
    splash.setDescription("正在加载，请稍候…")

    window = FluentHybridWindow()
    window.setWindowTitle("Fluent Hybrid Window Demo")
    window.setRoundedCornersEnabled(True)
    window.bridge.setTransitionDurationMs(800)

    # 添加测试页面
    window.addSubInterface(HomeInterface(), FIF.HOME, "Home", "top")
    window.addSubInterface(DataInterface(), FIF.LAYOUT, "Data", "scroll")
    window.addSubInterface(SettingInterface(), FIF.SETTING, "Settings", "bottom")
    
    def show_main():
        window.show()

    splash.showFor(1000, onFinished=show_main)
    app.exec()
