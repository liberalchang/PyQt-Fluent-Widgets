# coding:utf-8
import json
import numpy as np
from PySide6.QtCore import Slot, QUrl, Signal, QObject, Qt, QEvent
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QMenu, QApplication

from ...common.chart_resource import ChartResource

try:
    from PySide6.QtWebEngineWidgets import QWebEngineView
    from PySide6.QtWebEngineCore import QWebEnginePage
    from qframelesswindow.webengine import FramelessWebEngineView
    from PySide6.QtWebChannel import QWebChannel
    WEBENGINE_AVAILABLE = True
except ImportError as e:
    WEBENGINE_AVAILABLE = False
    IMPORT_ERROR = str(e)

    class QWebEngineView(QWidget):
        pass

    class QWebEnginePage(QObject):
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


class _NoContextMenuPage(QWebEnginePage):
    """ 禁用 WebEngine 右键菜单的页面 """

    def contextMenuEvent(self, event):
        # 直接吞掉右键菜单事件
        event.accept()

    def createStandardContextMenu(self):
        # 返回空菜单，避免 Chromium 弹出默认菜单
        return QMenu()


class _GlobalContextMenuBlocker(QObject):
    """ 全局事件过滤器：只屏蔽 EChartsWidget 内部对象触发的右键菜单 """

    def __init__(self, owner: QObject):
        super().__init__(owner)
        self._owner = owner

    def _belongsToOwner(self, obj: QObject) -> bool:
        o = obj
        while o is not None:
            if o is self._owner:
                return True
            o = o.parent()
        return False

    def eventFilter(self, obj, event):
        if self._owner is None:
            return False

        if not self._belongsToOwner(obj):
            return False

        et = event.type()
        if et == QEvent.Type.ContextMenu:
            return True

        if et in (QEvent.Type.MouseButtonPress, QEvent.Type.MouseButtonRelease, QEvent.Type.MouseButtonDblClick):
            try:
                if event.button() == Qt.MouseButton.RightButton:
                    return True
            except Exception:
                return False

        return False


class EChartsWidgetStrict(FramelessWebEngineView):
    """ ECharts widget（严格禁用右键菜单版） """

    chartClicked = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)

        if not WEBENGINE_AVAILABLE:
            layout = QVBoxLayout(self)
            layout.addWidget(QLabel(f"Error: PySide6-WebEngine not available.\n{IMPORT_ERROR}", self))
            print(f"Error: PySide6-WebEngine not available. {IMPORT_ERROR}")
            return

        # 强制走 Qt 的自定义右键菜单策略，避免默认菜单弹出
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(lambda _: None)

        # 安装事件过滤器，吞掉右键相关事件（WebEngine 内部子控件也会触发菜单）
        self.installEventFilter(self)

        # 安装全局事件过滤器，覆盖 QtWebEngine 内部非 QWidget 对象/延迟创建对象
        app = QApplication.instance()
        self._globalContextMenuBlocker = None
        if app is not None:
            self._globalContextMenuBlocker = _GlobalContextMenuBlocker(self)
            app.installEventFilter(self._globalContextMenuBlocker)

        # 额外设置自定义 Page
        self.setPage(_NoContextMenuPage(self))

        # 设置 page 禁用策略（不同版本写法可能不同）
        pagePolicy = getattr(QWebEnginePage, 'NoContextMenu', None)
        if pagePolicy is None:
            try:
                pagePolicy = QWebEnginePage.ContextMenuPolicy.NoContextMenu
            except Exception:
                pagePolicy = None

        if pagePolicy is not None:
            try:
                self.page().setContextMenuPolicy(pagePolicy)
            except Exception:
                pass

        # Qt6 WebEngine: 在弹出菜单前会发出 contextMenuRequested，直接 reject
        try:
            self.page().contextMenuRequested.connect(self._onContextMenuRequested)
        except Exception:
            pass

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
        self.loadFinished.connect(self._onLoadFinished)

    def _onLoadFinished(self, ok):
        if not ok:
            print("Failed to load ECharts HTML")
            return

        self.isLoaded = True
        print("ECharts HTML loaded successfully")

        # 页面加载完成后从 JS 层面禁用右键菜单
        self.page().runJavaScript(
            "document.addEventListener('contextmenu', function(e){e.preventDefault(); return false;}, true);"
        )
        self.page().runJavaScript(
            "window.oncontextmenu = function(e){ if(e){ e.preventDefault(); } return false; };"
        )

        # 给内部子控件也安装事件过滤器
        for w in self.findChildren(QWidget):
            try:
                w.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
                w.installEventFilter(self)
            except Exception:
                pass

        self.resizeEvent(None)

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

    def _onContextMenuRequested(self, request):
        try:
            request.reject()
        except Exception:
            try:
                request.setAccepted(False)
            except Exception:
                pass

    def contextMenuEvent(self, event):
        event.accept()

    def eventFilter(self, obj, event):
        et = event.type()
        if et == QEvent.Type.ContextMenu:
            return True

        if et in (QEvent.Type.MouseButtonPress, QEvent.Type.MouseButtonRelease, QEvent.Type.MouseButtonDblClick):
            try:
                if event.button() == Qt.MouseButton.RightButton:
                    return True
            except Exception:
                pass

        return super().eventFilter(obj, event)

    def closeEvent(self, event):
        app = QApplication.instance()
        if app is not None and getattr(self, '_globalContextMenuBlocker', None) is not None:
            try:
                app.removeEventFilter(self._globalContextMenuBlocker)
            except Exception:
                pass

        return super().closeEvent(event)

    def pushData(self, data: np.ndarray, seriesIndex: int = 0):
        """ push numpy data to chart """
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
