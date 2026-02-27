# coding:utf-8
import json
import numpy as np
from PySide6.QtCore import Slot, QUrl, Signal, QObject, Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

from ...common.chart_resource import ChartResource

try:
    from PySide6.QtWebEngineWidgets import QWebEngineView
    from qframelesswindow.webengine import FramelessWebEngineView
    from PySide6.QtWebChannel import QWebChannel
    WEBENGINE_AVAILABLE = True
except ImportError as e:
    WEBENGINE_AVAILABLE = False
    IMPORT_ERROR = str(e)
    # Define dummy classes to avoid NameError
    class QWebEngineView(QWidget):
        pass
    class QWebChannel(QObject): 
        pass


class ChartBridge(QObject):
    """ Bridge between Python and JavaScript """
    
    @Slot(str)
    def print(self, msg):
        """ print message from javascript """
        print(f"JS: {msg}")

    @Slot(str)
    def onChartClick(self, params):
        """ chart click event """
        try:
            data = json.loads(params)
            self.parent().chartClicked.emit(data)
        except Exception as e:
            print(f"Error parsing click data: {e}")

class EChartsWidget(FramelessWebEngineView):
    """ ECharts widget """
    
    chartClicked = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        
        if not WEBENGINE_AVAILABLE:
            layout = QVBoxLayout(self)
            layout.addWidget(QLabel(f"Error: PySide6-WebEngine not available.\n{IMPORT_ERROR}", self))
            print(f"Error: PySide6-WebEngine not available. {IMPORT_ERROR}")
            return

        self.bridge = ChartBridge(self)
        self.channel = QWebChannel(self.page())
        self.page().setWebChannel(self.channel)
        
        # Register the bridge object
        self.channel.registerObject("bridge", self.bridge)

        # Load HTML
        self.setUrl(QUrl(ChartResource.ECHARTS_HTML.path()))

        # Set transparent background to match Fluent Design
        self.page().setBackgroundColor(Qt.transparent)
        
        self.isLoaded = False
        self._cachedOption = None
        # Debug loading
        self.loadFinished.connect(self._onLoadFinished)

    def _onLoadFinished(self, ok):
        if not ok:
            print("Failed to load ECharts HTML")
        else:
            self.isLoaded = True
            print("ECharts HTML loaded successfully")
            # Trigger initial resize
            self.resizeEvent(None)
            # Apply cached option
            if self._cachedOption:
                self.setOption(self._cachedOption)
                self._cachedOption = None

    def setOption(self, option: dict):
        """ set chart option """
        if not WEBENGINE_AVAILABLE:
            return
            
        if not self.isLoaded:
            self._cachedOption = option
            return
            
        self.page().runJavaScript(f"setOption({json.dumps(option)})")

    def resizeEvent(self, e):
        super().resizeEvent(e)
        if not WEBENGINE_AVAILABLE or not self.isLoaded:
            return
        self.page().runJavaScript("resize()")
    
    def pushData(self, data: np.ndarray, seriesIndex: int = 0):
        """ push numpy data to chart 
        
        Parameters
        ----------
        data: np.ndarray
            the data to push
            
        seriesIndex: int
            the index of series to update
        """
        if not WEBENGINE_AVAILABLE:
            return

        if isinstance(data, np.ndarray):
            data = data.tolist()
            
        option = {
            'series': [
                {
                    'data': data
                }
            ]
        }
        
        if seriesIndex > 0:
            series = [None] * seriesIndex
            series.append({'data': data})
            option['series'] = series
            
        self.setOption(option)
