# coding:utf-8
import sys
import os
import random
import time
from datetime import datetime
from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qfluentwidgets import FluentWindow, SubtitleLabel
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets.components.charts import EChartsWidget

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
        
        # Initialize data
        self.x_data = []
        self.y_data = []
        
        # Setup Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateData)
        self.timer.start(1000)
        
        # Initialize Chart
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
        
        self.chart.chartClicked.connect(self.onChartClicked)
        
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
    
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())
