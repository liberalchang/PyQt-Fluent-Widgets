# coding:utf-8
import sys
import os
import random
import time
from datetime import datetime
from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtQuick import QQuickWindow, QSGRendererInterface
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qfluentwidgets import FluentWindow, SubtitleLabel
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets.components.charts import EChartsWidget

# import qfluentwidgets.components.charts.echarts_widget as _ew
# print("[echarts_test] echarts_widget path:", _ew.__file__)
# print("[echarts_test] QFW_ECHARTS_DEBUG_CTX:", os.getenv("QFW_ECHARTS_DEBUG_CTX"))

class DynamicLineChart(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("DynamicLineChart")
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setContentsMargins(30, 30, 30, 30)
        self.vBoxLayout.setSpacing(30)
        
        self.titleLabel = SubtitleLabel("Dynamic Line Chart (Time & Value)", self)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignTop)
        
        self.chart = EChartsWidget(self)
        self.vBoxLayout.addWidget(self.chart, 1)
        
        # 连接页面重新加载信号
        self.chart.pageReloaded.connect(self.onPageReloaded)
        
        # Initialize data
        self.x_data = []
        self.y_data = []
        
        # Setup Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateData)
        self.timer.start(1000)
        
        # Initialize Chart
        self.initChart()

    def onPageReloaded(self):
        """ 页面重新加载后重新初始化图表 """
        print("[DynamicLineChart] Page reloaded, reinitializing chart")
        # 清空数据并重新初始化
        self.x_data.clear()
        self.y_data.clear()
        self.initChart()

    def initChart(self):
        option = {
            'title': {'text': 'Real-time Data'},
            'tooltip': {'trigger': 'axis'},
            'xAxis': {
                'type': 'category',
                'boundaryGap': False,
                'data': self.x_data
            },
            'yAxis': {
                'type': 'value',
                'boundaryGap': [0, '100%']
            },
            'series': [{
                'name': 'Value',
                'type': 'line',
                'smooth': True,
                'data': self.y_data,
                'itemStyle': {'color': '#009faa'},
                'areaStyle': {'color': '#009faa33'}
            }]
        }
        self.chart.setOption(option)

    def updateData(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        value = random.randint(0, 100)
        
        self.x_data.append(current_time)
        self.y_data.append(value)
        
        # Keep only last 20 points
        if len(self.x_data) > 20:
            self.x_data.pop(0)
            self.y_data.pop(0)
            
        # Update chart
        option = {
            'xAxis': {'data': self.x_data},
            'series': [{'data': self.y_data}]
        }
        self.chart.setOption(option)


class InteractiveBarChart(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("InteractiveBarChart")
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setContentsMargins(30, 30, 30, 30)
        self.vBoxLayout.setSpacing(30)
        
        self.titleLabel = SubtitleLabel("Interactive Bar Chart (Click to Print Value)", self)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignTop)
        
        self.chart = EChartsWidget(self)
        self.vBoxLayout.addWidget(self.chart, 1)
        
        # 连接页面重新加载信号
        self.chart.pageReloaded.connect(self.onPageReloaded)
        
        self.chart.chartClicked.connect(self.onChartClicked)
        
        self.initChart()

    def onPageReloaded(self):
        """ 页面重新加载后重新初始化图表 """
        print("[InteractiveBarChart] Page reloaded, reinitializing chart")
        self.initChart()

    def initChart(self):
        option = {
            'title': {'text': 'Clickable Bar Chart'},
            'tooltip': {},
            'xAxis': {'data': ['A', 'B', 'C', 'D', 'E']},
            'yAxis': {},
            'series': [{
                'name': 'Value',
                'type': 'bar',
                'data': [random.randint(10, 100) for _ in range(5)],
                'itemStyle': {'color': '#ffaa00'}
            }]
        }
        self.chart.setOption(option)

    def onChartClicked(self, data):
        print(f"Chart Clicked! Series: {data.get('seriesName')}, Name: {data.get('name')}, Value: {data.get('value')}")


class Window(FluentWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('ECharts Interaction Demo')
        self.resize(1000, 700)
        
        # Dynamic Line Chart
        self.dynamicInterface = DynamicLineChart(self)
        self.addSubInterface(self.dynamicInterface, FIF.SPEED_HIGH, 'Dynamic Chart')
        
        # Interactive Bar Chart
        self.barInterface = InteractiveBarChart(self)
        self.addSubInterface(self.barInterface, FIF.MENU, 'Interactive Chart')

if __name__ == '__main__':
    # Enable high DPI scaling
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_SCALE_FACTOR"] = "1.25"
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    
    if sys.platform.startswith("win"):
        os.environ.setdefault("QTWEBENGINE_DISABLE_GPU", "1")
        os.environ.setdefault("QTWEBENGINE_DISABLE_SANDBOX", "1")
        os.environ.setdefault("QTWEBENGINE_CHROMIUM_FLAGS", "--disable-gpu --disable-software-rasterizer")
        QQuickWindow.setGraphicsApi(QSGRendererInterface.GraphicsApi.Software)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    auto_close_ms = int(os.getenv("QFW_AUTO_CLOSE_MS", "0") or 0)
    if auto_close_ms > 0:
        QTimer.singleShot(auto_close_ms, app.quit)
    sys.exit(app.exec())
