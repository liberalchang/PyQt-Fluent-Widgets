Calendar View 日历视图模块
=============================

Calendar View 模块提供完整的日历视图功能，支持年、月、日三种视图模式。
该模块提供Fluent Design风格的日历界面，支持日期选择、视图切换和自定义样式。

主要功能
--------

- **多视图模式** - 支持年视图、月视图、日视图
- **日期选择** - 支持单击和双击日期选择
- **视图切换** - 支持在不同视图间平滑切换
- **自定义样式** - 支持自定义日期项的显示样式
- **滚动支持** - 支持平滑滚动和快速定位

核心组件
--------

CalendarView
~~~~~~~~~~~

主日历视图控件，整合年、月、日三种视图模式。

.. code-block:: python

   from qfluentwidgets.components.date_time.calendar_view import CalendarView
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QDate
   
   # 创建日历视图
   calendar_view = CalendarView()
   
   # 连接信号
   calendar_view.dateChanged.connect(on_date_changed)
   calendar_view.resetted.connect(on_reset)
   
   # 设置日期
   calendar_view.setDate(QDate.currentDate())

**主要信号：**
- ``dateChanged`` - 日期变化信号
- ``resetted`` - 重置信号

**主要方法：**
- ``setDate()`` - 设置选中日期
- ``setResetEnabled()`` - 设置重置按钮状态

YearCalendarView
~~~~~~~~~~~~~~~~

年视图日历，显示整年的日历概览。

.. code-block:: python

   from qfluentwidgets.components.date_time.calendar_view import YearCalendarView
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QDate
   
   # 创建年视图
   year_view = YearCalendarView()
   
   # 设置年份
   current_year = QDate.currentDate().year()
   year_view.setDate(QDate(current_year, 1, 1))
   
   # 连接信号
   year_view.dateChanged.connect(on_date_selected)

MonthCalendarView
~~~~~~~~~~~~~~~~~

月视图日历，显示单月的详细日历。

.. code-block:: python

   from qfluentwidgets.components.date_time.calendar_view import MonthCalendarView
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QDate
   
   # 创建月视图
   month_view = MonthCalendarView()
   
   # 设置月份
   current_date = QDate.currentDate()
   month_view.setDate(current_date)
   
   # 连接信号
   month_view.dateChanged.connect(on_date_selected)

DayCalendarView
~~~~~~~~~~~~~~~

日视图日历，显示单日的详细信息和周视图。

.. code-block:: python

   from qfluentwidgets.components.date_time.calendar_view import DayCalendarView
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QDate
   
   # 创建日视图
   day_view = DayCalendarView()
   
   # 设置日期
   current_date = QDate.currentDate()
   day_view.setDate(current_date)
   
   # 连接信号
   day_view.dateChanged.connect(on_date_selected)

实际应用
--------

基本日历视图
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.calendar_view import CalendarView
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import QDate
   
   class BasicCalendarWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("日历视图")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建日历视图
           self.calendar_view = CalendarView()
           self.calendar_view.setResetEnabled(True)
           
           # 设置当前日期
           self.calendar_view.setDate(QDate.currentDate())
           
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
           layout.addWidget(self.calendar_view)
           layout.addWidget(self.selected_date_label)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.calendar_view.dateChanged.connect(self.on_date_changed)
           self.calendar_view.resetted.connect(self.on_reset)
       
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
           self.calendar_view.setDate(QDate.currentDate())
       
       def clear_date(self):
           """清空日期"""
           self.calendar_view.reset()

多视图切换
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.calendar_view import (
       CalendarView, YearCalendarView, MonthCalendarView, DayCalendarView
   )
   from qfluentwidgets import CardWidget, Label, ComboBox
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QStackedWidget
   from PySide6.QtCore import QDate
   
   class MultiViewCalendarWidget(CardWidget):
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
           
           # 堆栈控件
           self.stacked_widget = QStackedWidget()
           
           # 创建不同视图
           self.year_view = YearCalendarView()
           self.month_view = MonthCalendarView()
           self.day_view = DayCalendarView()
           
           # 添加到堆栈控件
           self.stacked_widget.addWidget(self.year_view)
           self.stacked_widget.addWidget(self.month_view)
           self.stacked_widget.addWidget(self.day_view)
           
           # 显示当前日期
           self.current_date_label = Label()
           self.update_date_display()
           
           layout.addLayout(view_layout)
           layout.addWidget(self.stacked_widget)
           layout.addWidget(self.current_date_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.view_combo.currentTextChanged.connect(self.change_view)
           
           # 连接所有视图的信号
           self.year_view.dateChanged.connect(self.on_date_changed)
           self.month_view.dateChanged.connect(self.on_date_changed)
           self.day_view.dateChanged.connect(self.on_date_changed)
       
       def change_view(self, view_text):
           """切换视图"""
           view_map = {
               "年视图": 0,
               "月视图": 1,
               "日视图": 2
           }
           
           index = view_map.get(view_text, 1)
           self.stacked_widget.setCurrentIndex(index)
           
           # 更新当前视图的日期
           current_widget = self.stacked_widget.currentWidget()
           current_widget.setDate(self.current_date)
       
       def on_date_changed(self, date):
           """日期变化处理"""
           self.current_date = date
           self.update_date_display()
       
       def update_date_display(self):
           """更新日期显示"""
           if self.current_date.isValid():
               date_str = self.current_date.toString("yyyy年MM月dd日 dddd")
               view_text = self.view_combo.currentText()
               self.current_date_label.setText(f"{view_text} - {date_str}")
           else:
               self.current_date_label.setText("未选择日期")

自定义日历样式
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.calendar_view import CalendarView
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QDate, Qt
   from PySide6.QtGui import QColor, QPainter
   
   class CustomCalendarView(CalendarView):
       """自定义日历视图"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_custom_style()
       
       def setup_custom_style(self):
           """设置自定义样式"""
           # 设置特殊日期
           self.special_dates = {
               QDate(2024, 1, 1): "元旦",
               QDate(2024, 2, 14): "情人节",
               QDate(2024, 10, 1): "国庆节"
           }
           
           # 设置周末颜色
           self.weekend_color = QColor(255, 100, 100)
           self.holiday_color = QColor(255, 50, 50)
           self.today_color = QColor(50, 100, 255)
       
       def paintEvent(self, event):
           """重写绘制事件"""
           super().paintEvent(event)
           
           # 在这里可以添加自定义绘制逻辑
           # 例如：在日历上添加标记或装饰
       
       def is_special_date(self, date):
           """检查是否为特殊日期"""
           return date in self.special_dates
       
       def get_special_date_text(self, date):
           """获取特殊日期文本"""
           return self.special_dates.get(date, "")
   
   class CustomCalendarWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建自定义日历
           self.calendar = CustomCalendarView()
           self.calendar.setDate(QDate.currentDate())
           
           # 显示特殊日期信息
           self.info_label = Label("点击日期查看信息")
           
           layout.addWidget(self.calendar)
           layout.addWidget(self.info_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.calendar.dateChanged.connect(self.on_date_changed)
       
       def on_date_changed(self, date):
           """日期变化处理"""
           if date.isValid():
               if self.calendar.is_special_date(date):
                   special_text = self.calendar.get_special_date_text(date)
                   self.info_label.setText(f"特殊日期: {special_text}")
               else:
                   self.info_label.setText(f"普通日期: {date.toString('yyyy-MM-dd')}")
           else:
               self.info_label.setText("未选择日期")

高级用法
--------

日期范围选择
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.calendar_view import CalendarView
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import QDate
   
   class DateRangeCalendarWidget(CardWidget):
       """日期范围选择日历"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
           
           self.start_date = None
           self.end_date = None
           self.selecting_start = True
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建两个日历视图
           calendar_layout = QHBoxLayout()
           
           # 开始日期日历
           start_group = QVBoxLayout()
           start_label = Label("开始日期:")
           self.start_calendar = CalendarView()
           start_group.addWidget(start_label)
           start_group.addWidget(self.start_calendar)
           
           # 结束日期日历
           end_group = QVBoxLayout()
           end_label = Label("结束日期:")
           self.end_calendar = CalendarView()
           end_group.addWidget(end_label)
           end_group.addWidget(self.end_calendar)
           
           calendar_layout.addLayout(start_group)
           calendar_layout.addLayout(end_group)
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           this_week_btn = PushButton("本周")
           this_month_btn = PushButton("本月")
           clear_btn = PushButton("清空")
           
           this_week_btn.clicked.connect(self.set_this_week)
           this_month_btn.clicked.connect(self.set_this_month)
           clear_btn.clicked.connect(self.clear_range)
           
           button_layout.addWidget(this_week_btn)
           button_layout.addWidget(this_month_btn)
           button_layout.addWidget(clear_btn)
           
           # 显示范围
           self.range_label = Label("请选择日期范围")
           
           layout.addLayout(calendar_layout)
           layout.addLayout(button_layout)
           layout.addWidget(self.range_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.start_calendar.dateChanged.connect(self.on_start_date_changed)
           self.end_calendar.dateChanged.connect(self.on_end_date_changed)
       
       def on_start_date_changed(self, date):
           """开始日期变化"""
           self.start_date = date
           self.update_range_display()
       
       def on_end_date_changed(self, date):
           """结束日期变化"""
           self.end_date = date
           self.update_range_display()
       
       def update_range_display(self):
           """更新范围显示"""
           if self.start_date and self.end_date:
               if self.start_date <= self.end_date:
                   days = self.start_date.daysTo(self.end_date) + 1
                   self.range_label.setText(
                       f"日期范围: {self.start_date.toString('yyyy-MM-dd')} 到 "
                       f"{self.end_date.toString('yyyy-MM-dd')} ({days} 天)"
                   )
               else:
                   self.range_label.setText("开始日期不能晚于结束日期")
           else:
               self.range_label.setText("请选择完整的日期范围")
       
       def set_this_week(self):
           """设置为本周"""
           today = QDate.currentDate()
           day_of_week = today.dayOfWeek()
           
           # 计算本周一和周日
           monday = today.addDays(-day_of_week + 1)
           sunday = today.addDays(7 - day_of_week)
           
           self.start_calendar.setDate(monday)
           self.end_calendar.setDate(sunday)
       
       def set_this_month(self):
           """设置为本月"""
           today = QDate.currentDate()
           
           # 本月第一天和最后一天
           first_day = QDate(today.year(), today.month(), 1)
           last_day = QDate(today.year(), today.month(), today.daysInMonth())
           
           self.start_calendar.setDate(first_day)
           self.end_calendar.setDate(last_day)
       
       def clear_range(self):
           """清空范围"""
           self.start_calendar.reset()
           self.end_calendar.reset()
           self.start_date = None
           self.end_date = None
           self.range_label.setText("已清空日期范围")

事件标记日历
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.calendar_view import CalendarView
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import QDate
   from PySide6.QtGui import QColor
   
   class EventCalendarWidget(CardWidget):
       """带事件标记的日历"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
           self.setup_events()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建日历视图
           self.calendar = CalendarView()
           self.calendar.setDate(QDate.currentDate())
           
           # 事件控制
           control_layout = QHBoxLayout()
           
           add_event_btn = PushButton("添加事件")
           clear_events_btn = PushButton("清空事件")
           
           add_event_btn.clicked.connect(self.add_sample_event)
           clear_events_btn.clicked.connect(self.clear_events)
           
           control_layout.addWidget(add_event_btn)
           control_layout.addWidget(clear_events_btn)
           
           # 显示事件信息
           self.event_info_label = Label("点击日期查看事件")
           
           layout.addWidget(self.calendar)
           layout.addLayout(control_layout)
           layout.addWidget(self.event_info_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.calendar.dateChanged.connect(self.on_date_changed)
       
       def setup_events(self):
           """设置事件数据"""
           self.events = {
               # 格式: QDate: [事件列表]
               QDate(2024, 1, 15): ["会议", "项目截止"],
               QDate(2024, 1, 20): ["生日聚会"],
               QDate(2024, 2, 14): ["情人节晚餐"],
               QDate(2024, 3, 8): ["国际妇女节"],
           }
           
           # 事件类型颜色
           self.event_colors = {
               "会议": QColor(255, 100, 100),
               "项目截止": QColor(255, 150, 50),
               "生日聚会": QColor(100, 255, 100),
               "节日": QColor(100, 100, 255)
           }
       
       def on_date_changed(self, date):
           """日期变化处理"""
           if date.isValid() and date in self.events:
               events = self.events[date]
               if events:
                   event_text = "当日事件: " + ", ".join(events)
                   self.event_info_label.setText(event_text)
               else:
                   self.event_info_label.setText(f"{date.toString('yyyy-MM-dd')} 无事件")
           else:
               self.event_info_label.setText("未选择日期或无事件")
       
       def add_sample_event(self):
           """添加示例事件"""
           current_date = self.calendar.date
           if current_date.isValid():
               if current_date not in self.events:
                   self.events[current_date] = []
               
               self.events[current_date].append("新事件")
               self.event_info_label.setText("已添加新事件")
       
       def clear_events(self):
           """清空事件"""
           self.events.clear()
           self.event_info_label.setText("已清空所有事件")

最佳实践
--------

1. **性能优化** - 避免频繁的日期更新操作
2. **用户体验** - 提供快捷日期选择功能
3. **国际化** - 考虑不同地区的日历显示习惯
4. **可访问性** - 确保日历控件的可访问性
5. **响应式设计** - 适配不同屏幕尺寸的显示

注意事项
--------

- 不同地区的周起始日可能不同
- 日期格式需要根据地区进行调整
- 大量事件数据可能影响性能
- 自定义样式需要与主题保持一致
- 日期选择事件可能频繁触发，需要防抖处理

相关模块
--------

- :doc:`components.date_time.calendar_picker` - 日历选择器
- :doc:`components.date_time.fast_calendar_view` - 快速日历视图
- :doc:`common.style_sheet` - 样式表管理
