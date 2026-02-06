# coding:utf-8
from enum import Enum
from . import resource_qml
from PySide6.QtCore import QUrl

class HybridQml(Enum):
    """ Hybrid QML Resource Paths """
    TITLE_BAR = "qrc:/qml/TitleBar.qml"
    SIDE_NAV = "qrc:/qml/SideNavigation.qml"
    SPLASH = "qrc:/qml/Splash.qml"

    @property
    def path(self):
        return self.value
