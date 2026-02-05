Calendar Picker 日历选择器模块
===============================

Calendar Picker 模块提供日期选择功能，支持标准日历视图和快速日历视图。
该模块提供Fluent Design风格的日期选择界面，支持日期格式化和重置功能。

主要功能
--------

- **日期选择** - 提供直观的日期选择界面
- **多种视图** - 支持标准日历和快速日历视图
- **日期格式** - 支持多种日期格式显示
- **重置功能** - 支持一键重置日期
- **信号通知** - 日期变化时发送信号

核心组件
--------

CalendarPicker
~~~~~~~~~~~~~~

标准日历选择器，提供基本的日期选择功能。

.. code-block:: python

   from qfluentwidgets.components.date_time.calendar_picker import CalendarPicker
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QDate
   
   # 创建日历选择器
   calendar_picker = CalendarPicker()
   
   # 连接日期变化信号
   calendar_picker.dateChanged.connect(on_date_changed)
   
   # 设置日期
   calendar_picker.setDate(QDate.currentDate())
   
   # 设置日期格式
   calendar_picker.setDateFormat(Qt.DateFormat.ISODate)
   
   # 启用重置按钮
   calendar_picker.setResetEnabled(True)

**主要信号：**
- ``dateChanged`` - 日期变化信号

**主要属性：**
- ``date`` - 选中日期
- ``dateFormat`` - 日期格式
- ``resetEnabled`` - 重置按钮是否启用

FastCalendarPicker
~~~~~~~~~~~~~~~~~

快速日历选择器，提供更高效的日期选择体验。

.. code-block:: python

   from qfluentwidgets.components.date_time.calendar_picker import FastCalendarPicker
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QDate
   
   # 创建快速日历选择器
   fast_calendar = FastCalendarPicker()
   
   # 设置动画类型
   from qfluentwidgets.components.widgets.flyout import FlyoutAnimationType
   fast_calendar.setFlyoutAnimationType(FlyoutAnimationType.DROP_DOWN)
   
   # 设置日期
   fast_calendar.setDate(QDate.currentDate())

实际应用
--------

基本日期选择
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.calendar_picker import CalendarPicker
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import QDate
   
   class DateSelectionWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标签
           self.date_label = Label("请选择日期:")
           
           # 创建日历选择器
           self.calendar_picker = CalendarPicker()
           self.calendar_picker.setResetEnabled(True)
           
           # 显示选中的日期
           self.selected_date_label = Label("未选择日期")
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           today_btn = PushButton("今天")
           clear_btn = PushButton("清空")
           
           today_btn.clicked.connect(self.set_today)
           clear_btn.clicked.connect(self.clear_date)
           
           button_layout.addWidget(today_btn)
           button_layout.addWidget(clear_btn)
           
           layout.addWidget(self.date_label)
           layout.addWidget(self.calendar_picker)
           layout.addWidget(self.selected_date_label)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.calendar_picker.dateChanged.connect(self.on_date_changed)
       
       def on_date_changed(self, date):
           """日期变化处理"""
           if date.isValid():
               date_str = date.toString("yyyy年MM月dd日")
               self.selected_date_label.setText(f"已选择: {date_str}")
           else:
               self.selected_date_label.setText("未选择日期")
       
       def set_today(self):
           """设置为今天"""
           self.calendar_picker.setDate(QDate.currentDate())
       
       def clear_date(self):
           """清空日期"""
           self.calendar_picker.reset()

日期格式化
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.calendar_picker import CalendarPicker
   from qfluentwidgets import CardWidget, Label, ComboBox
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import QDate, Qt
   
   class DateFormatWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 日期格式选择
           format_layout = QHBoxLayout()
           
           format_label = Label("日期格式:")
           self.format_combo = ComboBox()
           
           # 添加日期格式选项
           self.format_combo.addItems([
               "ISO格式 (YYYY-MM-DD)",
               "本地格式",
               "短格式",
               "长格式",
               "中文格式"
           ])
           
           format_layout.addWidget(format_label)
           format_layout.addWidget(self.format_combo)
           
           # 日历选择器
           self.calendar_picker = CalendarPicker()
           
           # 显示格式化结果
           self.result_label = Label("选择日期查看格式")
           
           layout.addLayout(format_layout)
           layout.addWidget(self.calendar_picker)
           layout.addWidget(self.result_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.format_combo.currentTextChanged.connect(self.change_date_format)
           self.calendar_picker.dateChanged.connect(self.update_result)
       
       def change_date_format(self, format_text):
           """改变日期格式"""
           format_map = {
               "ISO格式 (YYYY-MM-DD)": Qt.DateFormat.ISODate,
               "本地格式": Qt.DateFormat.DefaultLocaleLongDate,
               "短格式": Qt.DateFormat.DefaultLocaleShortDate,
               "长格式": Qt.DateFormat.DefaultLocaleLongDate,
               "中文格式": "yyyy年MM月dd日"
           }
           
           format_value = format_map.get(format_text, Qt.DateFormat.ISODate)
           self.calendar_picker.setDateFormat(format_value)
           
           # 更新显示
           self.update_result(self.calendar_picker.date)
       
       def update_result(self, date):
           """更新结果显示"""
           if date.isValid():
               format_text = self.format_combo.currentText()
               if format_text == "中文格式":
                   result = date.toString("yyyy年MM月dd日")
               else:
                   result = date.toString(self.calendar_picker.dateFormat)
               
               self.result_label.setText(f"格式化结果: {result}")
           else:
               self.result_label.setText("请选择日期")

快速日历选择
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.calendar_picker import FastCalendarPicker
   from qfluentwidgets import CardWidget, Label
   from qfluentwidgets.components.widgets.flyout import FlyoutAnimationType
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import QDate
   
   class FastCalendarWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建快速日历选择器
           self.fast_calendar = FastCalendarPicker()
           self.fast_calendar.setResetEnabled(True)
           
           # 动画类型选择
           animation_layout = QHBoxLayout()
           
           animation_label = Label("动画类型:")
           from qfluentwidgets import ComboBox
           
           self.animation_combo = ComboBox()
           self.animation_combo.addItems([
               "下拉动画",
               "淡入淡出",
               "缩放动画"
           ])
           
           self.animation_combo.currentTextChanged.connect(self.change_animation)
           
           animation_layout.addWidget(animation_label)
           animation_layout.addWidget(self.animation_combo)
           
           # 显示选中的日期
           self.date_display = Label("未选择日期")
           
           layout.addLayout(animation_layout)
           layout.addWidget(self.fast_calendar)
           layout.addWidget(self.date_display)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.fast_calendar.dateChanged.connect(self.on_date_changed)
       
       def change_animation(self, animation_text):
           """改变动画类型"""
           animation_map = {
               "下拉动画": FlyoutAnimationType.DROP_DOWN,
               "淡入淡出": FlyoutAnimationType.FADE_IN,
               "缩放动画": FlyoutAnimationType.SCALE
           }
           
           animation_type = animation_map.get(animation_text, FlyoutAnimationType.DROP_DOWN)
           self.fast_calendar.setFlyoutAnimationType(animation_type)
       
       def on_date_changed(self, date):
           """日期变化处理"""
           if date.isValid():
               date_str = date.toString("yyyy年MM月dd日 dddd")
               self.date_display.setText(f"已选择: {date_str}")
           else:
               self.date_display.setText("未选择日期")

高级用法
--------

自定义日历选择器
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.calendar_picker import CalendarPicker
   from qfluentwidgets import FluentIcon
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QDate, Signal
   
   class CustomCalendarPicker(CalendarPicker):
       """自定义日历选择器"""
       
       # 自定义信号
       dateSelected = Signal(QDate)
       dateCleared = Signal()
       
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_custom_features()
       
       def setup_custom_features(self):
           """设置自定义功能"""
           # 设置自定义样式
           self.setText("选择日期")
           self.setResetEnabled(True)
           
           # 设置默认日期为今天
           self.setDate(QDate.currentDate())
       
       def _showCalendarView(self):
           """重写日历视图显示"""
           # 调用父类方法
           super()._showCalendarView()
           
           # 添加自定义逻辑
           self.on_calendar_shown()
       
       def on_calendar_shown(self):
           """日历显示时的自定义处理"""
           # 可以在这里添加自定义逻辑
           print("日历已显示")
       
       def _onDateChanged(self, date):
           """重写日期变化处理"""
           super()._onDateChanged(date)
           
           # 发送自定义信号
           if date.isValid():
               self.dateSelected.emit(date)
           else:
               self.dateCleared.emit()
       
       def setToday(self):
           """设置为今天"""
           self.setDate(QDate.currentDate())
       
       def setYesterday(self):
           """设置为昨天"""
           yesterday = QDate.currentDate().addDays(-1)
           self.setDate(yesterday)
       
       def setTomorrow(self):
           """设置为明天"""
           tomorrow = QDate.currentDate().addDays(1)
           self.setDate(tomorrow)

日期范围选择
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.calendar_picker import CalendarPicker
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QGroupBox
   from PySide6.QtCore import QDate
   
   class DateRangeWidget(CardWidget):
       """日期范围选择器"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 开始日期选择
           start_group = QGroupBox("开始日期")
           start_layout = QVBoxLayout()
           
           self.start_calendar = CalendarPicker()
           self.start_calendar.setResetEnabled(True)
           self.start_date_label = Label("未选择")
           
           start_layout.addWidget(self.start_calendar)
           start_layout.addWidget(self.start_date_label)
           start_group.setLayout(start_layout)
           
           # 结束日期选择
           end_group = QGroupBox("结束日期")
           end_layout = QVBoxLayout()
           
           self.end_calendar = CalendarPicker()
           self.end_calendar.setResetEnabled(True)
           self.end_date_label = Label("未选择")
           
           end_layout.addWidget(self.end_calendar)
           end_layout.addWidget(self.end_date_label)
           end_group.setLayout(end_layout)
           
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
           self.range_label = Label("未选择日期范围")
           
           layout.addWidget(start_group)
           layout.addWidget(end_group)
           layout.addLayout(button_layout)
           layout.addWidget(self.range_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.start_calendar.dateChanged.connect(self.on_date_changed)
           self.end_calendar.dateChanged.connect(self.on_date_changed)
       
       def on_date_changed(self):
           """日期变化处理"""
           start_date = self.start_calendar.date
           end_date = self.end_calendar.date
           
           # 更新显示
           if start_date.isValid():
               start_str = start_date.toString("yyyy-MM-dd")
               self.start_date_label.setText(f"开始: {start_str}")
           else:
               self.start_date_label.setText("未选择")
           
           if end_date.isValid():
               end_str = end_date.toString("yyyy-MM-dd")
               self.end_date_label.setText(f"结束: {end_str}")
           else:
               self.end_date_label.setText("未选择")
           
           # 更新范围显示
           self.update_range_display()
       
       def update_range_display(self):
           """更新范围显示"""
           start_date = self.start_calendar.date
           end_date = self.end_calendar.date
           
           if start_date.isValid() and end_date.isValid():
               if start_date <= end_date:
                   days = start_date.daysTo(end_date) + 1
                   self.range_label.setText(f"日期范围: {days} 天")
               else:
                   self.range_label.setText("开始日期不能晚于结束日期")
           else:
               self.range_label.setText("请选择完整的日期范围")
       
       def set_this_week(self):
           """设置为本周"""
           today = QDate.currentDate()
           day_of_week = today.dayOfWeek()
           
           # 计算本周一
           monday = today.addDays(-day_of_week + 1)
           
           # 计算本周日
           sunday = today.addDays(7 - day_of_week)
           
           self.start_calendar.setDate(monday)
           self.end_calendar.setDate(sunday)
       
       def set_this_month(self):
           """设置为本月"""
           today = QDate.currentDate()
           
           # 本月第一天
           first_day = QDate(today.year(), today.month(), 1)
           
           # 本月最后一天
           last_day = QDate(today.year(), today.month(), today.daysInMonth())
           
           self.start_calendar.setDate(first_day)
           self.end_calendar.setDate(last_day)
       
       def clear_range(self):
           """清空范围"""
           self.start_calendar.reset()
           self.end_calendar.reset()

最佳实践
--------

1. **日期验证** - 确保选择的日期在有效范围内
2. **用户体验** - 提供快捷日期选择选项
3. **格式一致** - 在整个应用中保持日期格式一致
4. **国际化** - 考虑不同地区的日期格式
5. **性能优化** - 避免频繁的日期更新操作

注意事项
--------

- 日期格式需要根据地区进行调整
- 重置功能需要明确的状态指示
- 日历视图的显示位置可能需要调整
- 日期信号可能频繁触发，需要防抖处理
- 不同地区的周起始日可能不同

相关模块
--------

- :doc:`components.date_time.calendar_view` - 日历视图
- :doc:`components.widgets.flyout` - 弹出层组件
- :doc:`common.style_sheet` - 样式表管理
