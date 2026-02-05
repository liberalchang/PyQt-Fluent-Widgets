Smooth Scroll 平滑滚动模块
============================

Smooth Scroll 模块提供平滑滚动功能，支持多种滚动模式和自适应引擎。
该模块主要用于QScrollArea和QAbstractScrollArea，提供流畅的滚动体验，支持高DPI显示器。

主要功能
--------

- **平滑滚动** - 提供流畅的滚动体验
- **多种模式** - 支持线性、二次、余弦等滚动模式
- **自适应引擎** - 根据屏幕DPI动态选择滚动引擎
- **高DPI支持** - 优化高分辨率显示器的滚动效果
- **加速控制** - 支持滚动加速和减速效果

核心组件
--------

SmoothScroll
~~~~~~~~~~~~

平滑滚动控制器，管理滚动行为和引擎选择。

.. code-block:: python

   from qfluentwidgets.common.smooth_scroll import SmoothScroll, SmoothMode
   from PySide6.QtWidgets import QScrollArea, QTextEdit
   from PySide6.QtCore import Qt
   
   # 创建滚动区域
   scroll_area = QScrollArea()
   text_edit = QTextEdit()
   
   # 启用平滑滚动
   smooth_scroll = SmoothScroll(scroll_area, orient=Qt.Vertical)
   
   # 设置滚动模式
   smooth_scroll.setSmoothMode(SmoothMode.LINEAR)
   
   # 启用动态引擎
   smooth_scroll.setDynamicEngineEnabled(True)

**主要参数：**
- ``widget`` - 要应用平滑滚动的控件
- ``orient`` - 滚动方向，默认为垂直
- ``dynamicEngineEnabled`` - 是否启用动态引擎，默认为True

SmoothMode
~~~~~~~~~~

滚动模式枚举，定义不同的滚动曲线。

.. code-block:: python

   from qfluentwidgets.common.smooth_scroll import SmoothMode
   
   # 滚动模式
   SmoothMode.NO_SMOOTH    # 无平滑
   SmoothMode.CONSTANT     # 恒定速度
   SmoothMode.LINEAR       # 线性插值
   SmoothMode.QUADRATI     # 二次插值
   SmoothMode.COSINE       # 余弦插值

滚动引擎
--------

SmoothScrollEngineBase
~~~~~~~~~~~~~~~~~~~~~

滚动引擎基类，提供平滑滚动的核心功能。

.. code-block:: python

   from qfluentwidgets.common.smooth_scroll import SmoothScrollEngineBase
   
   # 自定义滚动引擎
   class CustomScrollEngine(SmoothScrollEngineBase):
       def wheelEvent(self, e, delta):
           # 自定义滚动逻辑
           pass
       
       def _getTotalDelta(self):
           # 计算滚动增量
           return 0.0

FixedStepSmoothScrollEngine
~~~~~~~~~~~~~~~~~~~~~~~~~~~

固定步长平滑滚动引擎，基于帧数的滚动实现。

.. code-block:: python

   from qfluentwidgets.common.smooth_scroll import FixedStepSmoothScrollEngine
   
   # 创建固定步长引擎
   engine = FixedStepSmoothScrollEngine(scroll_area, Qt.Vertical)
   
   # 设置参数
   engine.fps = 60              # 帧率
   engine.duration = 400        # 滚动持续时间(ms)
   engine.stepRatio = 1.5       # 步长比例
   engine.acceleration = 1.0     # 加速度

AdaptiveSmoothScrollEngine
~~~~~~~~~~~~~~~~~~~~~~~~~

自适应平滑滚动引擎，基于时间的滚动实现，适合高DPI显示器。

.. code-block:: python

   from qfluentwidgets.common.smooth_scroll import AdaptiveSmoothScrollEngine
   
   # 创建自适应引擎
   engine = AdaptiveSmoothScrollEngine(scroll_area, Qt.Vertical)
   
   # 设置参数
   engine.maxQueueSize = 3       # 最大队列大小
   engine.minDuration = 120      # 最小持续时间(ms)

实际应用
--------

基本平滑滚动
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.smooth_scroll import SmoothScroll, SmoothMode
   from qfluentwidgets import ScrollArea, CardWidget
   from PySide6.QtWidgets import QVBoxLayout, QLabel
   from PySide6.QtCore import Qt
   
   class SmoothScrollWidget(ScrollArea):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_smooth_scroll()
       
       def setup_ui(self):
           # 创建内容控件
           content = CardWidget()
           layout = QVBoxLayout()
           
           # 添加大量内容
           for i in range(100):
               label = QLabel(f"内容项 {i}")
               layout.addWidget(label)
           
           content.setLayout(layout)
           self.setWidget(content)
       
       def setup_smooth_scroll(self):
           """设置平滑滚动"""
           # 创建平滑滚动
           self.smooth_scroll = SmoothScroll(self, Qt.Vertical)
           
           # 设置滚动模式
           self.smooth_scroll.setSmoothMode(SmoothMode.COSINE)
           
           # 启用动态引擎
           self.smooth_scroll.setDynamicEngineEnabled(True)
   
   # 使用
   widget = SmoothScrollWidget()
   widget.show()

自定义滚动区域
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.smooth_scroll import SmoothScroll, SmoothMode
   from PySide6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QPushButton
   from PySide6.QtCore import Qt
   
   class CustomScrollArea(QScrollArea):
       def __init__(self):
           super().__init__()
           self.setup_smooth_scroll()
       
       def setup_smooth_scroll(self):
           """设置平滑滚动"""
           # 创建平滑滚动
           self.smooth_scroll = SmoothScroll(
               self, 
               orient=Qt.Vertical,
               dynamicEngineEnabled=True
           )
           
           # 设置为余弦模式
           self.smooth_scroll.setSmoothMode(SmoothMode.COSINE)
       
       def wheelEvent(self, event):
           """重写滚轮事件"""
           if hasattr(self, 'smooth_scroll'):
               self.smooth_scroll.wheelEvent(event)
           else:
               super().wheelEvent(event)
   
   # 使用自定义滚动区域
   scroll_area = CustomScrollArea()

滚动模式切换
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.smooth_scroll import SmoothScroll, SmoothMode
   from qfluentwidgets import ComboBox, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QWidget
   
   class ScrollModeSelector(QWidget):
       def __init__(self, scroll_area):
           super().__init__()
           self.scroll_area = scroll_area
           self.setup_ui()
           self.setup_smooth_scroll()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 模式选择下拉框
           self.mode_combo = ComboBox()
           self.mode_combo.addItems([
               "无平滑", "恒定速度", "线性插值", 
               "二次插值", "余弦插值"
           ])
           self.mode_combo.currentTextChanged.connect(self.change_mode)
           
           # 动态引擎开关
           self.dynamic_btn = PushButton("切换动态引擎")
           self.dynamic_btn.clicked.connect(self.toggle_dynamic)
           
           layout.addWidget(self.mode_combo)
           layout.addWidget(self.dynamic_btn)
           self.setLayout(layout)
       
       def setup_smooth_scroll(self):
           """设置平滑滚动"""
           self.smooth_scroll = SmoothScroll(self.scroll_area)
           self.dynamic_enabled = True
       
       def change_mode(self, text):
           """改变滚动模式"""
           mode_map = {
               "无平滑": SmoothMode.NO_SMOOTH,
               "恒定速度": SmoothMode.CONSTANT,
               "线性插值": SmoothMode.LINEAR,
               "二次插值": SmoothMode.QUADRATI,
               "余弦插值": SmoothMode.COSINE
           }
           
           mode = mode_map.get(text, SmoothMode.LINEAR)
           self.smooth_scroll.setSmoothMode(mode)
       
       def toggle_dynamic(self):
           """切换动态引擎"""
           self.dynamic_enabled = not self.dynamic_enabled
           self.smooth_scroll.setDynamicEngineEnabled(self.dynamic_enabled)
           self.dynamic_btn.setText(f"动态引擎: {'开' if self.dynamic_enabled else '关'}")

高级用法
--------

性能优化
~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.smooth_scroll import SmoothScroll, SmoothMode
   from PySide6.QtWidgets import QApplication
   
   class PerformanceOptimizedScroll:
       def __init__(self, scroll_area):
           self.scroll_area = scroll_area
           self.setup_optimized_scroll()
       
       def setup_optimized_scroll(self):
           """设置优化的平滑滚动"""
           # 创建平滑滚动
           self.smooth_scroll = SmoothScroll(self.scroll_area)
           
           # 根据系统性能调整参数
           self.adjust_for_performance()
       
       def adjust_for_performance(self):
           """根据性能调整参数"""
           # 获取屏幕信息
           screen = QApplication.primaryScreen()
           dpi = screen.logicalDotsPerInch()
           width = screen.geometry().width()
           
           # 高DPI屏幕使用自适应引擎
           if dpi > 120 or width > 2560:
               self.smooth_scroll.setDynamicEngineEnabled(True)
               self.smooth_scroll.setSmoothMode(SmoothMode.COSINE)
           else:
               # 普通屏幕使用固定步长引擎
               self.smooth_scroll.setDynamicEngineEnabled(False)
               self.smooth_scroll.setSmoothMode(SmoothMode.LINEAR)
           
           # 调整引擎参数
           if hasattr(self.smooth_scroll, 'fixedStepScrollEngine'):
               engine = self.smooth_scroll.fixedStepScrollEngine
               engine.fps = 60 if dpi <= 120 else 120
               engine.duration = 300 if dpi <= 120 else 200

触摸设备适配
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.smooth_scroll import SmoothScroll, SmoothMode
   from PySide6.QtCore import QEvent
   from PySide6.QtGui import QTouchEvent
   
   class TouchOptimizedScroll:
       def __init__(self, scroll_area):
           self.scroll_area = scroll_area
           self.setup_touch_scroll()
       
       def setup_touch_scroll(self):
           """设置触摸优化的滚动"""
           self.smooth_scroll = SmoothScroll(self.scroll_area)
           
           # 触摸设备使用更平滑的模式
           self.smooth_scroll.setSmoothMode(SmoothMode.COSINE)
           
           # 启用动态引擎
           self.smooth_scroll.setDynamicEngineEnabled(True)
           
           # 安装事件过滤器
           self.scroll_area.installEventFilter(self)
       
       def eventFilter(self, obj, event):
           """事件过滤器"""
           if event.type() == QEvent.TouchBegin:
               # 触摸开始时的处理
               self.on_touch_begin(event)
           elif event.type() == QEvent.TouchEnd:
               # 触摸结束时的处理
               self.on_touch_end(event)
           
           return super().eventFilter(obj, event)
       
       def on_touch_begin(self, event):
           """触摸开始"""
           # 可以在这里添加触摸开始的特殊处理
           pass
       
       def on_touch_end(self, event):
           """触摸结束"""
           # 可以在这里添加触摸结束的特殊处理
           pass

滚动动画定制
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.smooth_scroll import SmoothScrollEngineBase, SmoothMode
   from math import sin, pi
   
   class BounceScrollEngine(SmoothScrollEngineBase):
       """弹跳滚动引擎"""
       
       def wheelEvent(self, e, delta):
           """处理滚轮事件"""
           now = QDateTime.currentDateTime().toMSecsSinceEpoch()
           self.scrollStamps.append(now)
           
           # 清理过期时间戳
           while self.scrollStamps and now - self.scrollStamps[0] > 500:
               self.scrollStamps.popleft()
           
           self.lastWheelPos = e.position()
           self.lastWheelGlobalPos = e.globalPosition()
           
           # 计算滚动参数
           self.stepsTotal = self.fps * self.duration / 1000
           scroll_delta = delta * self.stepRatio
           
           # 添加到队列
           self.stepsLeftQueue.append([scroll_delta, self.stepsTotal])
           
           # 启动定时器
           self.smoothMoveTimer.start(int(1000 / self.fps))
       
       def _getTotalDelta(self):
           """计算总滚动增量"""
           totalDelta = 0
           
           for i in self.stepsLeftQueue:
               totalDelta += self._bounceDelta(i[0], i[1])
               i[1] -= 1
           
           # 清理完成的队列项
           while self.stepsLeftQueue and self.stepsLeftQueue[0][1] == 0:
               self.stepsLeftQueue.popleft()
           
           return totalDelta
       
       def _bounceDelta(self, delta, stepsLeft):
           """弹跳插值计算"""
           progress = 1 - (stepsLeft / self.stepsTotal)
           
           # 使用正弦函数创建弹跳效果
           bounce = sin(progress * pi * 2) * 0.1
           return delta * (progress + bounce) / self.stepsTotal
   
   # 使用自定义引擎
   class BounceSmoothScroll(SmoothScroll):
       def __init__(self, widget, orient=Qt.Vertical):
           super().__init__(widget, orient)
           self.bounce_engine = BounceScrollEngine(widget, orient)
       
       def wheelEvent(self, e):
           delta = e.angleDelta().y() if e.angleDelta().y() != 0 else e.angleDelta().x()
           if self.smoothMode == SmoothMode.NO_SMOOTH:
               QAbstractScrollArea.wheelEvent(self.widget, e)
               return
           
           self.bounce_engine.wheelEvent(e, delta)

最佳实践
--------

1. **模式选择** - 根据使用场景选择合适的滚动模式
2. **性能考虑** - 在低性能设备上禁用动态引擎
3. **高DPI适配** - 在高分辨率显示器上启用自适应引擎
4. **触摸优化** - 为触摸设备选择更平滑的滚动模式
5. **参数调优** - 根据用户习惯调整滚动参数

注意事项
--------

- 平滑滚动会增加CPU使用率
- 某些系统可能已经提供了平滑滚动功能
- 高刷新率显示器可能需要调整FPS参数
- 触摸板滚动可能与鼠标滚轮行为不同

相关模块
--------

- :doc:`components.widgets` - UI组件
- :doc:`components.scroll_area` - 滚动区域组件
- :doc:`common.animation` - 动画模块
