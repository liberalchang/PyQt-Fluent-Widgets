import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QColor

from qfluentwidgets import (FluentWindow, NavigationItemPosition,
                            FluentIcon as FIF, Theme, setTheme)
from qfluentwidgets.hybrid import HybridSplashScreen


class DemoWindow(FluentWindow):
    def __init__(self):
        super().__init__(showReturnButton=True)
        self.setWindowTitle('QML Splash Demo')
        self.resize(900, 700)
        from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout
        def make_page(text):
            w = QWidget()
            w.setObjectName(text)
            v = QVBoxLayout(w)
            label = QLabel(text, w)
            label.setAlignment(Qt.AlignCenter)
            v.addWidget(label, 1)
            return w
        self.addSubInterface(make_page('首页'), FIF.HOME, 'Home', NavigationItemPosition.TOP)
        self.addSubInterface(make_page('设置'), FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)


if __name__ == '__main__':
    setTheme(Theme.LIGHT, save=False)

    app = QApplication(sys.argv)

    splash = HybridSplashScreen()
    splash.setIcon(FIF.ROBOT)
    splash.setIconColor(QColor(255, 0, 0))
    splash.setTitle("你的应用名123")
    splash.setDescription("正在加载，请稍候…")

    window = DemoWindow()
    def show_main():
        window.show()
        QTimer.singleShot(2000, app.quit)
    splash.showFor(13000, onFinished=show_main)

    sys.exit(app.exec())
