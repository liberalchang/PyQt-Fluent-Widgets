Fast Calendar View 快速日历视图模块
===================================

Fast Calendar View 模块提供优化的快速日历视图功能，支持年、月、日三种视图模式。
该模块基于FlyoutViewBase，提供更高效的日历界面和流畅的用户体验。

主要功能
--------

- **快速视图** - 优化的日历视图渲染性能
- **多视图模式** - 支持年、月、日三种视图
- **弹出式设计** - 基于Flyout的弹出式界面
- **高效渲染** - 优化的滚动项委托和渲染逻辑
- **主题适配** - 完美适配Fluent Design主题

核心组件
--------

FastCalendarView
~~~~~~~~~~~~~~~

快速日历视图控件，整合年、月、日三种视图模式。

.. code-block:: python

   from qfluentwidgets.components.date_time.fast_calendar_view import FastCalendarView
   from qfluentwidgets import CardWidget, PushButton
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QDate
   
   # 创建快速日历视图
   fast_calendar = FastCalendarView()
   
   # 连接信号
   fast_calendar.dateChanged.connect(on_date_changed)
   fast_calendar.resetted.connect(on_reset)
   
   # 设置日期
   fast_calendar.setDate(QDate.currentDate())

**主要信号：**
- ``dateChanged`` - 日期变化信号
- ``resetted`` - 重置信号

**主要方法：**
- ``setDate()`` - 设置选中日期
- ``setResetEnabled()`` - 设置重置按钮状态

FastYearCalendarView
~~~~~~~~~~~~~~~~~~~~

快速年视图日历，显示整年的日历概览。

.. code-block:: python

   from qfluentwidgets.components.date_time.fast_calendar_view import FastYearCalendarView
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QDate
   
   # 创建快速年视图
   fast_year_view = FastYearCalendarView()
   
   # 设置年份
   current_year = QDate.currentDate().year()
   fast_year_view.setDate(QDate(current_year, 1, 1))
   
   # 连接信号
   fast_year_view.dateChanged.connect(on_date_selected)

FastMonthCalendarView
~~~~~~~~~~~~~~~~~~~~~

快速月视图日历，显示单月的详细日历。

.. code-block:: python

   from qfluentwidgets.components.date_time.fast_calendar_view import FastMonthCalendarView
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QDate
   
   # 创建快速月视图
   fast_month_view = FastMonthCalendarView()
   
   # 设置月份
   current_date = QDate.currentDate()
   fast_month_view.setDate(current_date)
   
   # 连接信号
   fast_month_view.dateChanged.connect(on_date_selected)

FastDayCalendarView
~~~~~~~~~~~~~~~~~~~

快速日视图日历，显示单日的详细信息和周视图。

.. code-block:: python

   from qfluentwidgets.components.date_time.fast_calendar_view import FastDayCalendarView
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QDate
   
   # 创建快速日视图
   fast_day_view = FastDayCalendarView()
   
   # 设置日期
   current_date = QDate.currentDate()
   fast_day_view.setDate(current_date)
   
   # 连接信号
   fast_day_view.dateChanged.connect(on_date_selected)

实际应用
--------

基本快速日历
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.fast_calendar_view import FastCalendarView
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import QDate
   
   class BasicFastCalendarWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("快速日历视图")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建快速日历视图
           self.fast_calendar = FastCalendarView()
           self.fast_calendar.setResetEnabled(True)
           self.fast_calendar.setDate(QDate.currentDate())
           
           # 显示选中的日期
           self.selected_date_label = Label("未选择日期")
           self.selected_date_label.setAlignment(Qt.AlignCenter)
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           today_btn = PushButton("今天")
           clear_btn = PushButton("清空")
           
           today_btn.clicked.connect(self.set_today)
           clear_btn.clicked.connect(self.clear_date)
           
           button_layout.addWidget(today_btn)
           button_layout.addWidget(clear_btn)
           
           layout.addWidget(title_label)
           layout.addWidget(self.selected_date_label)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.fast_calendar.dateChanged.connect(self.on_date_changed)
           self.fast_calendar.resetted.connect(self.on_reset)
       
       def on_date_changed(self, date):
           """日期变化处理"""
           if date.isValid():
               date_str = date.toString("yyyy年MM月dd日 dddd")
               self.selected_date_label.setText(f"已选择: {date_str}")
           else:
               self.selected_date_label.setText("未选择日期")
       
       def on_reset(self):
           """重置处理"""
           self.selected_date_label.setText("已重置")
       
       def set_today(self):
           """设置为今天"""
           self.fast_calendar.setDate(QDate.currentDate())
       
       def clear_date(self):
           """清空日期"""
           self.fast_calendar.reset()

弹出式日历选择器
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.fast_calendar_view import FastCalendarView
   from qfluentwidgets import PushButton, Flyout, FlyoutAnimationType
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QDate, QPoint
   
   class PopupCalendarWidget(QWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建触发按钮
           self.trigger_btn = PushButton("选择日期")
           self.trigger_btn.clicked.connect(self.show_calendar)
           
           # 显示选中的日期
           self.date_label = Label("未选择日期")
           self.date_label.setAlignment(Qt.AlignCenter)
           
           layout.addWidget(self.trigger_btn)
           layout.addWidget(self.date_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           pass
       
       def show_calendar(self):
           """显示日历弹出层"""
           # 创建快速日历视图
           calendar = FastCalendarView()
           calendar.setDate(QDate.currentDate())
           calendar.setResetEnabled(True)
           
           # 连接信号
           calendar.dateChanged.connect(self.on_date_selected)
           calendar.resetted.connect(self.on_reset)
           
           # 计算弹出位置
           button_rect = self.trigger_btn.geometry()
           pos = self.trigger_btn.mapToGlobal(button_rect.bottomLeft())
           
           # 创建弹出层
           flyout = Flyout.make(
               calendar, 
               self.trigger_btn, 
               self, 
               FlyoutAnimationType.DROP_DOWN
           )
           
           # 日期选择后关闭弹出层
           calendar.dateChanged.connect(flyout.close)
           calendar.resetted.connect(flyout.close)
       
       def on_date_selected(self, date):
           """日期选择处理"""
           if date.isValid():
               date_str = date.toString("yyyy年MM月dd日")
               self.date_label.setText(f"已选择: {date_str}")
           else:
               self.date_label.setText("未选择日期")
       
       def on_reset(self):
           """重置处理"""
           self.date_label.setText("已重置")

多视图快速切换
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.fast_calendar_view import (
       FastCalendarView, FastYearCalendarView, FastMonthCalendarView, FastDayCalendarView
   )
   from qfluentwidgets import CardWidget, Label, ComboBox, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import QDate
   
   class MultiViewFastCalendarWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
           self.current_date = QDate.currentDate()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 视图选择
           view_layout = QHBoxLayout()
           
           view_label = Label("视图模式:")
           self.view_combo = ComboBox()
           self.view_combo.addItems(["年视图", "月视图", "日视图"])
           
           view_layout.addWidget(view_label)
           view_layout.addWidget(self.view_combo)
           
           # 显示当前日期
           self.current_date_label = Label()
           self.update_date_display()
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           show_btn = PushButton("显示日历")
           today_btn = PushButton("今天")
           
           show_btn.clicked.connect(self.show_calendar)
           today_btn.clicked.connect(self.set_today)
           
           button_layout.addWidget(show_btn)
           button_layout.addWidget(today_btn)
           
           layout.addLayout(view_layout)
           layout.addWidget(self.current_date_label)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.view_combo.currentTextChanged.connect(self.on_view_changed)
       
       def on_view_changed(self, view_text):
           """视图变化处理"""
           self.update_date_display()
       
       def show_calendar(self):
           """显示对应视图的日历"""
           view_text = self.view_combo.currentText()
           
           if view_text == "年视图":
               calendar = FastYearCalendarView()
           elif view_text == "月视图":
               calendar = FastMonthCalendarView()
           else:
               calendar = FastDayCalendarView()
           
           calendar.setDate(self.current_date)
           calendar.setResetEnabled(True)
           
           # 连接信号
           calendar.dateChanged.connect(self.on_date_selected)
           calendar.resetted.connect(self.on_reset)
           
           # 创建弹出层
           from qfluentwidgets import Flyout, FlyoutAnimationType
           flyout = Flyout.make(
               calendar,
               self,
               self,
               FlyoutAnimationType.DROP_DOWN
           )
           
           # 选择后关闭
           calendar.dateChanged.connect(flyout.close)
           calendar.resetted.connect(flyout.close)
       
       def on_date_selected(self, date):
           """日期选择处理"""
           self.current_date = date
           self.update_date_display()
       
       def on_reset(self):
           """重置处理"""
           self.current_date = QDate()
           self.update_date_display()
       
       def set_today(self):
           """设置为今天"""
           self.current_date = QDate.currentDate()
           self.update_date_display()
       
       def update_date_display(self):
           """更新日期显示"""
           if self.current_date.isValid():
               view_text = self.view_combo.currentText()
               date_str = self.current_date.toString("yyyy年MM月dd日 dddd")
               self.current_date_label.setText(f"{view_text} - {date_str}")
           else:
               self.current_date_label.setText("未选择日期")

高级用法
--------

自定义快速日历样式
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.fast_calendar_view import FastCalendarView, FastScrollItemDelegate
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QDate, Qt
   from PySide6.QtGui import QColor, QPainter
   
   class CustomFastScrollItemDelegate(FastScrollItemDelegate):
       """自定义快速滚动项委托"""
       
       def __init__(self, min, max):
           super().__init__(min, max)
           self.special_dates = set()
           self.holiday_color = QColor(255, 100, 100)
           self.today_color = QColor(100, 200, 255)
       
       def set_special_dates(self, dates):
           """设置特殊日期"""
           self.special_dates = set(dates)
       
       def _drawBackground(self, painter, option, index):
           """重写背景绘制"""
           date = index.data(Qt.UserRole)
           if not date:
               return
           
           painter.save()
           
           # 判断是否为特殊日期
           is_special = date in self.special_dates
           
           # 外圈颜色
           if date == self.selectedDate:
               if is_special:
                   painter.setPen(self.holiday_color)
               else:
                   painter.setPen(themeColor())
           else:
               painter.setPen(Qt.PenStyle.NoPen)
           
           # 背景色
           if date == self.currentDate:
               if index == self.pressedIndex:
                   painter.setBrush(ThemeColor.LIGHT_2.color())
               elif option.state & QStyle.StateFlag.State_MouseOver:
                   painter.setBrush(ThemeColor.LIGHT_1.color())
               else:
                   if is_special:
                       painter.setBrush(self.holiday_color)
                   else:
                       painter.setBrush(themeColor())
           else:
               c = 255 if isDarkTheme() else 0
               if index == self.pressedIndex:
                   painter.setBrush(QColor(c, c, c, 7))
               elif option.state & QStyle.StateFlag.State_MouseOver:
                   painter.setBrush(QColor(c, c, c, 9))
               else:
                   painter.setBrush(Qt.GlobalColor.transparent)
           
           m = self._itemMargin()
           painter.drawEllipse(option.rect.adjusted(m, m, -m, -m))
           painter.restore()
   
   class CustomFastCalendarView(FastCalendarView):
       """自定义快速日历视图"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_custom_style()
       
       def setup_custom_style(self):
           """设置自定义样式"""
           # 设置特殊日期
           from datetime import date
           self.special_dates = {
               QDate(2024, 1, 1),  # 元旦
               QDate(2024, 2, 14), # 情人节
               QDate(2024, 10, 1), # 国庆节
           }
           
           # 应用自定义委托到所有视图
           self.apply_custom_delegate()
       
       def apply_custom_delegate(self):
           """应用自定义委托"""
           # 这里需要访问内部的视图并设置自定义委托
           # 具体实现取决于FastCalendarView的内部结构
           pass
   
   class CustomFastCalendarWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建自定义快速日历
           self.custom_calendar = CustomFastCalendarView()
           self.custom_calendar.setDate(QDate.currentDate())
           
           # 显示特殊日期信息
           self.info_label = Label("点击日期查看信息")
           
           layout.addWidget(self.info_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.custom_calendar.dateChanged.connect(self.on_date_changed)
       
       def on_date_changed(self, date):
           """日期变化处理"""
           if date.isValid():
               if date in self.custom_calendar.special_dates:
                   self.info_label.setText(f"特殊日期: {date.toString('yyyy-MM-dd')}")
               else:
                   self.info_label.setText(f"普通日期: {date.toString('yyyy-MM-dd')}")
           else:
               self.info_label.setText("未选择日期")

性能优化日历
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.fast_calendar_view import FastCalendarView
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import QDate, QTimer
   from PySide6.QtGui import QPixmap
   
   class OptimizedFastCalendarWidget(CardWidget):
       """优化的快速日历组件"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
           self.setup_optimization()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建优化的快速日历
           self.fast_calendar = FastCalendarView()
           self.fast_calendar.setDate(QDate.currentDate())
           
           # 性能监控
           self.performance_label = Label("性能监控: 正常")
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           benchmark_btn = PushButton("性能测试")
           clear_btn = PushButton("清空")
           
           benchmark_btn.clicked.connect(self.run_benchmark)
           clear_btn.clicked.connect(self.clear_date)
           
           button_layout.addWidget(benchmark_btn)
           button_layout.addWidget(clear_btn)
           
           layout.addWidget(self.performance_label)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.fast_calendar.dateChanged.connect(self.on_date_changed)
       
       def setup_optimization(self):
           """设置优化选项"""
           # 启用渲染优化
           self.fast_calendar.setAttribute(Qt.WA_OpaquePaintEvent, True)
           self.fast_calendar.setAttribute(Qt.WA_NoSystemBackground, True)
           
           # 设置更新策略
           self.fast_calendar.setUpdateMode(QQuickView.FullScreenRefresh)
       
       def on_date_changed(self, date):
           """日期变化处理"""
           if date.isValid():
               date_str = date.toString("yyyy-MM-dd")
               self.performance_label.setText(f"已选择: {date_str}")
           else:
               self.performance_label.setText("未选择日期")
       
       def run_benchmark(self):
           """运行性能测试"""
           import time
           
           # 测试日期选择性能
           start_time = time.time()
           
           for i in range(100):
               test_date = QDate(2024, 1, 1).addDays(i)
               self.fast_calendar.setDate(test_date)
               
               # 强制更新
               self.fast_calendar.update()
               QApplication.processEvents()
           
           end_time = time.time()
           elapsed = end_time - start_time
           
           self.performance_label.setText(f"性能测试: 100次选择耗时 {elapsed:.3f} 秒")
       
       def clear_date(self):
           """清空日期"""
           self.fast_calendar.reset()

最佳实践
--------

1. **性能优先** - 快速日历视图专为性能优化设计
2. **弹出式使用** - 推荐与Flyout组件结合使用
3. **内存管理** - 及时清理不需要的视图对象
4. **响应式设计** - 适配不同屏幕尺寸的显示
5. **用户体验** - 提供流畅的动画和交互效果

注意事项
--------

- 快速日历视图基于FlyoutViewBase，适合弹出式使用
- 内部视图的访问可能需要了解具体实现结构
- 性能优化可能在某些情况下影响视觉效果
- 自定义委托需要正确处理日期数据
- 大量特殊日期可能影响渲染性能

相关模块
--------

- :doc:`components.date_time.calendar_view` - 标准日历视图
- :doc:`components.widgets.flyout` - 弹出层组件
- :doc:`common.style_sheet` - 样式表管理
