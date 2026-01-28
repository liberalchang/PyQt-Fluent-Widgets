# coding:utf-8
from PySide6.QtCore import QSize, Qt, Signal, QPoint, QRectF, QPropertyAnimation, Property, QEasingCurve, QTimer
from PySide6.QtGui import QColor, QMouseEvent, QPainter, QPainterPath
from PySide6.QtWidgets import QProxyStyle, QSlider, QStyle, QStyleOptionSlider, QWidget, QToolTip

from ...common.style_sheet import FluentStyleSheet, themeColor, isDarkTheme, ThemeColor
from ...common.icon import FluentIcon as FIF
from ...common.color import autoFallbackThemeColor
from ...common.overload import singledispatchmethod



class SliderHandle(QWidget):
    """ Slider handle """

    pressed = Signal()
    released = Signal()

    def __init__(self, parent: QSlider):
        super().__init__(parent=parent)
        self.setFixedSize(22, 22)
        self._radius = 5
        self.lightHandleColor = QColor()
        self.darkHandleColor = QColor()
        self.radiusAni = QPropertyAnimation(self, b'radius', self)
        self.radiusAni.setDuration(100)

    @Property(int)
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self.update()

    def setHandleColor(self, light, dark):
        self.lightHandleColor = QColor(light)
        self.darkHandleColor = QColor(dark)
        self.update()

    def enterEvent(self, e):
        self._startAni(6)

    def leaveEvent(self, e):
        self._startAni(5)

    def mousePressEvent(self, e):
        self._startAni(4)
        self.pressed.emit()

    def mouseReleaseEvent(self, e):
        self._startAni(6)
        self.released.emit()

    def _startAni(self, radius):
        self.radiusAni.stop()
        self.radiusAni.setStartValue(self.radius)
        self.radiusAni.setEndValue(radius)
        self.radiusAni.start()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)

        # draw outer circle
        isDark = isDarkTheme()
        painter.setPen(QColor(0, 0, 0, 90 if isDark else 25))
        painter.setBrush(QColor(69, 69, 69) if isDark else Qt.GlobalColor.white)
        painter.drawEllipse(self.rect().adjusted(1, 1, -1, -1))

        # draw innert circle
        painter.setBrush(autoFallbackThemeColor(self.lightHandleColor, self.darkHandleColor))
        painter.drawEllipse(QPoint(11, 11), self.radius, self.radius)



class Slider(QSlider):
    """ A slider can be clicked

    Constructors
    ------------
    * Slider(`parent`: QWidget = None)
    * Slider(`orient`: Qt.Orientation, `parent`: QWidget = None)
    """

    clicked = Signal(int)

    @singledispatchmethod
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self._postInit()

    @__init__.register
    def _(self, orientation: Qt.Orientation, parent: QWidget = None):
        super().__init__(orientation, parent=parent)
        self._postInit()

    def _postInit(self):
        self.handle = SliderHandle(self)
        self._pressedPos = QPoint()
        self.lightGrooveColor = QColor()
        self.darkGrooveColor = QColor()
        self.setOrientation(self.orientation())

        self.handle.pressed.connect(self.sliderPressed)
        self.handle.released.connect(self.sliderReleased)
        self.valueChanged.connect(self._adjustHandlePos)

    def setThemeColor(self, light, dark):
        self.lightGrooveColor = QColor(light)
        self.darkGrooveColor = QColor(dark)
        self.handle.setHandleColor(light, dark)
        self.update()

    def setOrientation(self, orientation: Qt.Orientation) -> None:
        super().setOrientation(orientation)
        if orientation == Qt.Orientation.Horizontal:
            self.setMinimumHeight(22)
        else:
            self.setMinimumWidth(22)

    def mousePressEvent(self, e: QMouseEvent):
        self._pressedPos = e.pos()
        self.setValue(self._posToValue(e.pos()))
        self.clicked.emit(self.value())

    def mouseMoveEvent(self, e: QMouseEvent):
        self.setValue(self._posToValue(e.pos()))
        self._pressedPos = e.pos()
        self.sliderMoved.emit(self.value())

    @property
    def grooveLength(self):
        l = self.width() if self.orientation() == Qt.Orientation.Horizontal else self.height()
        return l - self.handle.width()

    def _adjustHandlePos(self):
        total = max(self.maximum() - self.minimum(), 1)
        delta = int((self.value() - self.minimum()) / total * self.grooveLength)

        if self.orientation() == Qt.Orientation.Vertical:
            self.handle.move(0, delta)
        else:
            self.handle.move(delta, 0)

    def _posToValue(self, pos: QPoint):
        pd = self.handle.width() / 2
        gs = max(self.grooveLength, 1)
        v = pos.x() if self.orientation() == Qt.Orientation.Horizontal else pos.y()
        return int((v - pd) / gs * (self.maximum() - self.minimum()) + self.minimum())

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor(255, 255, 255, 115) if isDarkTheme() else QColor(0, 0, 0, 100))

        if self.orientation() == Qt.Orientation.Horizontal:
            self._drawHorizonGroove(painter)
            self._drawHorizonTick(painter)
        else:
            self._drawVerticalGroove(painter)
            self._drawVerticalTick(painter)

    def _drawHorizonTick(self, painter: QPainter):
        pass

    def _drawVerticalTick(self, painter: QPainter):
        pass

    def _drawHorizonGroove(self, painter: QPainter):
        w, r = self.width(), self.handle.width() / 2
        painter.drawRoundedRect(QRectF(r, r-2, w-r*2, 4), 2, 2)

        if self.maximum() - self.minimum() == 0:
            return

        painter.setBrush(autoFallbackThemeColor(self.lightGrooveColor, self.darkGrooveColor))
        aw = (self.value() - self.minimum()) / (self.maximum() - self.minimum()) * (w - r*2)
        painter.drawRoundedRect(QRectF(r, r-2, aw, 4), 2, 2)

    def _drawVerticalGroove(self, painter: QPainter):
        h, r = self.height(), self.handle.width() / 2
        painter.drawRoundedRect(QRectF(r-2, r, 4, h-2*r), 2, 2)

        if self.maximum() - self.minimum() == 0:
            return

        painter.setBrush(autoFallbackThemeColor(self.lightGrooveColor, self.darkGrooveColor))
        ah = (self.value() - self.minimum()) / (self.maximum() - self.minimum()) * (h - r*2)
        painter.drawRoundedRect(QRectF(r-2, r, 4, ah), 2, 2)

    def resizeEvent(self, e):
        self._adjustHandlePos()


class ClickableSlider(QSlider):
    """ A slider can be clicked """

    clicked = Signal(int)

    def mousePressEvent(self, e: QMouseEvent):
        super().mousePressEvent(e)

        if self.orientation() == Qt.Horizontal:
            value = int(e.pos().x() / self.width() * self.maximum())
        else:
            value = int((self.height()-e.pos().y()) /
                        self.height() * self.maximum())

        self.setValue(value)
        self.clicked.emit(self.value())



class HollowHandleStyle(QProxyStyle):
    """ Hollow handle style """

    def __init__(self, config: dict = None):
        """
        Parameters
        ----------
        config: dict
            style config
        """
        super().__init__()
        self.config = {
            "groove.height": 3,
            "sub-page.color": QColor(255, 255, 255),
            "add-page.color": QColor(255, 255, 255, 64),
            "handle.color": QColor(255, 255, 255),
            "handle.ring-width": 4,
            "handle.hollow-radius": 6,
            "handle.margin": 4
        }
        config = config if config else {}
        self.config.update(config)

        # get handle size
        w = self.config["handle.margin"]+self.config["handle.ring-width"] + \
            self.config["handle.hollow-radius"]
        self.config["handle.size"] = QSize(2*w, 2*w)

    def subControlRect(self, cc: QStyle.ComplexControl, opt: QStyleOptionSlider, sc: QStyle.SubControl, widget: QSlider):
        """ get the rectangular area occupied by the sub control """
        if cc != self.ComplexControl.CC_Slider or widget.orientation() != Qt.Horizontal \
                or sc == self.SubControl.SC_SliderTickmarks:
            return super().subControlRect(cc, opt, sc, widget)

        rect = widget.rect()

        if sc == self.SubControl.SC_SliderGroove:
            h = self.config["groove.height"]
            grooveRect = QRectF(0, (rect.height()-h)//2, rect.width(), h)
            return grooveRect.toRect()

        elif sc == self.SubControl.SC_SliderHandle:
            size = self.config["handle.size"]
            x = self.sliderPositionFromValue(
                widget.minimum(), widget.maximum(), widget.value(), rect.width())

            # solve the situation that the handle runs out of slider
            x *= (rect.width()-size.width())/rect.width()
            sliderRect = QRectF(x, 0, size.width(), size.height())
            return sliderRect.toRect()

    def drawComplexControl(self, cc: QStyle.ComplexControl, opt: QStyleOptionSlider, painter: QPainter, widget: QSlider):
        """ draw sub control """
        if cc != self.ComplexControl.CC_Slider or widget.orientation() != Qt.Horizontal:
            return super().drawComplexControl(cc, opt, painter, widget)

        grooveRect = self.subControlRect(cc, opt, self.SubControl.SC_SliderGroove, widget)
        handleRect = self.subControlRect(cc, opt, self.SubControl.SC_SliderHandle, widget)
        painter.setRenderHints(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        # paint groove
        painter.save()
        painter.translate(grooveRect.topLeft())

        # paint the crossed part
        w = handleRect.x()-grooveRect.x()
        h = self.config['groove.height']
        painter.setBrush(self.config["sub-page.color"])
        painter.drawRect(0, 0, w, h)

        # paint the uncrossed part
        x = w+self.config['handle.size'].width()
        painter.setBrush(self.config["add-page.color"])
        painter.drawRect(x, 0, grooveRect.width()-w, h)
        painter.restore()

        # paint handle
        ringWidth = self.config["handle.ring-width"]
        hollowRadius = self.config["handle.hollow-radius"]
        radius = ringWidth + hollowRadius

        path = QPainterPath()
        path.moveTo(0, 0)
        center = handleRect.center() + QPoint(1, 1)
        path.addEllipse(center, radius, radius)
        path.addEllipse(center, hollowRadius, hollowRadius)

        handleColor = self.config["handle.color"]  # type:QColor
        handleColor.setAlpha(255 if opt.activeSubControls !=
                             self.SubControl.SC_SliderHandle else 153)
        painter.setBrush(handleColor)
        painter.drawPath(path)

        # press handle
        if widget.isSliderDown():
            handleColor.setAlpha(255)
            painter.setBrush(handleColor)
            painter.drawEllipse(handleRect)


class ToolTipSlider(Slider):
    """ 带工具提示的滑动条
    
    当拖动滑动条时，在滑块上方显示当前数值
    """

    def __init__(self, orientation: Qt.Orientation = Qt.Horizontal, parent: QWidget = None):
        super().__init__(orientation, parent)
        
        # 注册Fluent Design样式
        FluentStyleSheet.SLIDER.apply(self)
        
        self._tooltip_timer = QTimer()
        self._tooltip_timer.setSingleShot(True)
        self._tooltip_timer.timeout.connect(self._show_tooltip)
        self._tooltip_delay = 500  # 延迟显示工具提示的时间（毫秒）
        self._tooltip_format = "{}"  # 工具提示格式
        self._tooltip_visible = False
        self._is_dragging = False  # 自定义拖动状态
        
        # 连接信号
        self.sliderPressed.connect(self._on_slider_pressed)
        self.sliderReleased.connect(self._on_slider_released)
        self.valueChanged.connect(self._on_value_changed)

    def setToolTipFormat(self, format_str: str):
        """ 设置工具提示格式字符串
        
        Parameters
        ----------
        format_str : str
            格式字符串，例如 "{}" 或 "值: {}" 或 "{:.1f}%"
        """
        self._tooltip_format = format_str

    def setToolTipDelay(self, delay_ms: int):
        """ 设置工具提示显示延迟时间
        
        Parameters
        ----------
        delay_ms : int
            延迟时间（毫秒）
        """
        self._tooltip_delay = max(0, delay_ms)
        self._tooltip_timer.setInterval(self._tooltip_delay)

    def _on_slider_pressed(self):
        """ 滑块被按下时的处理 """
        self._is_dragging = True
        if self._tooltip_delay == 0:
            self._show_tooltip()
        else:
            self._tooltip_timer.start()

    def _on_slider_released(self):
        """ 滑块被释放时的处理 """
        self._is_dragging = False
        self._tooltip_timer.stop()
        self._hide_tooltip()

    def _on_value_changed(self, value):
        """ 数值改变时的处理 """
        if self._is_dragging:
            # 如果滑块正在被拖动，始终更新工具提示位置和文本
            if self._tooltip_visible:
                # 立即更新工具提示位置和文本
                QToolTip.showText(self._get_tooltip_pos(), self._get_tooltip_text(), self)
            else:
                # 如果工具提示未显示，则显示它
                self._show_tooltip()

    def _show_tooltip(self):
        """ 显示工具提示 """
        if not self._tooltip_visible:
            self._tooltip_visible = True
            QToolTip.showText(self._get_tooltip_pos(), self._get_tooltip_text(), self)

    def _hide_tooltip(self):
        """ 隐藏工具提示 """
        if self._tooltip_visible:
            self._tooltip_visible = False
            QToolTip.hideText()

    def _get_tooltip_pos(self) -> QPoint:
        """ 获取工具提示显示位置 """
        handle_rect = self.handle.geometry()
        
        # 获取工具提示文本
        tooltip_text = self._get_tooltip_text()
        
        # 计算工具提示尺寸（估算）
        from PySide6.QtWidgets import QApplication
        from PySide6.QtGui import QFontMetrics
        font = QApplication.font()
        font_metrics = QFontMetrics(font)
        tooltip_width = font_metrics.horizontalAdvance(tooltip_text) + 20  # 加上内边距
        tooltip_height = font_metrics.height() + 16  # 加上内边距
        
        if self.orientation() == Qt.Horizontal:
            # 水平滑动条，工具提示显示在滑块正上方，水平居中对齐
            tooltip_x = handle_rect.center().x() - tooltip_width // 2   # 水平居中，水平位置（居中对齐）
            tooltip_y = handle_rect.top() - 20 - tooltip_height  # 调整工具提示到滑块的距离，增大这个值 = 增加距离
        else:
            # 垂直滑动条，工具提示显示在滑块右侧，垂直居中对齐
            tooltip_x = handle_rect.right() + 15  # 水平位置，调整工具提示到滑块的距离
            tooltip_y = handle_rect.center().y() - tooltip_height // 2 - 10 # 垂直居中
        
        # 转换为全局坐标
        return self.mapToGlobal(QPoint(tooltip_x, tooltip_y))

    def _get_tooltip_text(self) -> str:
        """ 获取工具提示文本 """
        try:
            return self._tooltip_format.format(self.value())
        except (ValueError, TypeError):
            # 如果格式化失败，使用简单的数值显示
            return str(self.value())

    def mousePressEvent(self, e: QMouseEvent):
        """ 鼠标按下事件 """
        super().mousePressEvent(e)
        # 如果点击时没有延迟，立即显示工具提示
        if self._tooltip_delay == 0:
            self._show_tooltip()

    def mouseMoveEvent(self, e: QMouseEvent):
        """ 鼠标移动事件 - 重写以支持工具提示跟随 """
        # 只有在拖动状态下才调用父类的mouseMoveEvent
        if self._is_dragging:
            super().mouseMoveEvent(e)
            # 强制更新工具提示位置和文本
            self._force_update_tooltip()

    def _force_update_tooltip(self):
        """ 强制更新工具提示 """
        if self._is_dragging:
            # 获取当前位置和文本
            pos = self._get_tooltip_pos()
            text = self._get_tooltip_text()
            
            # 直接显示工具提示，这会自动更新位置
            QToolTip.showText(pos, text, self)
            self._tooltip_visible = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        """ 鼠标释放事件 """
        super().mouseReleaseEvent(e)
        self._hide_tooltip()

    def hideEvent(self, e):
        """ 隐藏事件 """
        super().hideEvent(e)
        self._hide_tooltip()
