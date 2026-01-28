# coding:utf-8
from enum import Enum

class ChartResource(Enum):
    """ Chart resource """

    ECHARTS_HTML = "echarts.html"
    ECHARTS_JS = "echarts.min.js"
    QWEBCHANNEL_JS = "qwebchannel.js"

    def path(self):
        return f"qrc:/html/html/{self.value}"
