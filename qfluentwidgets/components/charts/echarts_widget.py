# coding:utf-8
import json
import numpy as np
from PySide6.QtCore import Slot, QUrl, Signal, QObject, Qt, QPoint, QEvent
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFileDialog, QApplication
from qfluentwidgets import RoundMenu, Action, FluentIcon as FIF
from qfluentwidgets.components.widgets import InfoBar, InfoBarPosition


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
    # Define dummy classes to avoid NameError
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

class EChartsWidget(FramelessWebEngineView):
    """ ECharts widget """
    
    chartClicked = Signal(dict)
    pageReloaded = Signal()  # 添加页面重新加载信号

    def __init__(self, parent=None):
        super().__init__(parent)
        
        if not WEBENGINE_AVAILABLE:
            layout = QVBoxLayout(self)
            layout.addWidget(QLabel(f"Error: PySide6-WebEngine not available.\n{IMPORT_ERROR}", self))
            print(f"Error: PySide6-WebEngine not available. {IMPORT_ERROR}")
            return

        # 启用自定义右键菜单
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self._showContextMenu)

        # 安装事件过滤器来拦截右键事件
        self.installEventFilter(self)

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
            
            # 发出页面重新加载信号，让测试应用重新初始化图表
            self.pageReloaded.emit()

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

    def eventFilter(self, obj, event):
        """ 事件过滤器：拦截右键事件 """
        if obj is self:
            if event.type() == QEvent.Type.MouseButtonPress:
                if event.button() == Qt.MouseButton.RightButton:
                    print("[EChartsWidget] RightButtonPress intercepted at:", event.pos())
                    self._showContextMenu(event.pos())
                    return True  # 拦截事件，阻止默认菜单
            elif event.type() == QEvent.Type.ContextMenu:
                print("[EChartsWidget] ContextMenu event intercepted at:", event.pos())
                self._showContextMenu(event.pos())
                return True  # 拦截事件，阻止默认菜单
        return super().eventFilter(obj, event)

    def contextMenuEvent(self, event):
        """ 重写 contextMenuEvent 以显示自定义菜单 """
        print("[EChartsWidget] contextMenuEvent triggered at:", event.pos())
        # 显示自定义菜单
        self._showContextMenu(event.pos())
        # 阻止默认菜单
        event.accept()

    def _onContextMenuRequested(self, request):
        """ QtWebEngine 要弹出菜单前触发，我们用它来显示自定义菜单 """
        print("[EChartsWidget] contextMenuRequested triggered")
        # 拒绝默认菜单
        try:
            request.reject()
        except Exception:
            try:
                request.setAccepted(False)
            except Exception:
                pass

        # 获取鼠标位置并显示自定义菜单
        pos = request.position() if hasattr(request, 'position') else QPoint(0, 0)
        self._showContextMenu(pos)
    
    def _showContextMenu(self, pos):
        """ 显示自定义右键菜单 """
        print("[EChartsWidget] _showContextMenu called at pos:", pos)
        menu = RoundMenu(parent=self)

        # Reload
        reloadAction = Action(FIF.SYNC, self.tr("Reload"), triggered=self._reload)
        menu.addAction(reloadAction)

        # Save page
        savePageAction = Action(FIF.SAVE, self.tr("Save page"), triggered=self._savePage)
        menu.addAction(savePageAction)

        # Save image
        saveImageAction = Action(FIF.SAVE_AS, self.tr("Save image"), triggered=self._saveImage)
        menu.addAction(saveImageAction)

        # Copy image
        copyImageAction = Action(FIF.COPY, self.tr("Copy image"), triggered=self._copyImage)
        menu.addAction(copyImageAction)

        global_pos = self.mapToGlobal(pos)
        menu.exec(global_pos)

    def _reload(self):
        """ 重新加载页面 """
        # 简单重新加载页面，不尝试恢复配置以避免与测试应用冲突
        self.setUrl(QUrl(ChartResource.ECHARTS_HTML.path()))

    def _savePage(self):
        """ 保存页面为 HTML """
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            self.tr("Save Page"),
            "echarts_page.html",
            "HTML Files (*.html);;All Files (*)"
        )
        if file_path:
            try:
                self.page().save(file_path)
                InfoBar.success(
                    title=self.tr("Success"),
                    content=self.tr("Page saved successfully"),
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=3000,
                    parent=self
                )
            except Exception as e:
                InfoBar.error(
                    title=self.tr("Error"),
                    content=self.tr("Failed to save page: {}").format(str(e)),
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=5000,
                    parent=self
                )

    def _saveImage(self):
        """ 保存图表截图 """
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            self.tr("Save Image"),
            "echarts_chart.png",
            "PNG Files (*.png);;JPEG Files (*.jpg);;All Files (*)"
        )
        if file_path:
            try:
                pixmap = self.grab()
                pixmap.save(file_path)
                InfoBar.success(
                    title=self.tr("Success"),
                    content=self.tr("Image saved successfully"),
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=3000,
                    parent=self
                )
            except Exception as e:
                InfoBar.error(
                    title=self.tr("Error"),
                    content=self.tr("Failed to save image: {}").format(str(e)),
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=5000,
                    parent=self
                )

    def _copyImage(self):
        """ 复制图表截图到剪贴板 """
        try:
            pixmap = self.grab()
            QApplication.clipboard().setPixmap(pixmap)
            InfoBar.success(
                title=self.tr("Success"),
                content=self.tr("Image copied to clipboard"),
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=3000,
                parent=self
            )
        except Exception as e:
            InfoBar.error(
                title=self.tr("Error"),
                content=self.tr("Failed to copy image: {}").format(str(e)),
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=5000,
                parent=self
            )
    
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
