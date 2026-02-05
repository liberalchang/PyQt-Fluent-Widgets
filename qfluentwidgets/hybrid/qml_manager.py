# coding:utf-8
import os
from enum import Enum
from . import resource_qml
from PySide6.QtCore import QUrl

class HybridQml(Enum):
    """ Hybrid QML Resource Paths """
    TITLE_BAR = "qrc:/qml/TitleBar.qml"
    SIDE_NAV = "qrc:/qml/SideNavigation.qml"

    @property
    def path(self):
        local_path = os.path.join(os.path.dirname(__file__), "qml", os.path.basename(self.value))
        if os.path.exists(local_path):
            return QUrl.fromLocalFile(local_path).toString()
        return self.value
