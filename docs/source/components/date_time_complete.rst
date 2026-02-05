日期时间组件 (Date Time)
=======================

本节介绍 PySide6-Fluent-Widgets 中的日期时间相关组件。

CalendarPicker
--------------

日历选择器，带有下拉日历的日期选择器。

.. code-block:: python

   from qfluentwidgets import CalendarPicker

   # 创建日历选择器
   calendar_picker = CalendarPicker()
   calendar_picker.setFixedSize(300, 40)
   
   # 连接信号
   calendar_picker.dateChanged.connect(lambda date: print(f'选择日期: {date}'))

FastCalendarPicker
------------------

快速日历选择器，优化的日历选择器。

.. code-block:: python

   from qfluentwidgets import FastCalendarPicker

   # 创建快速日历选择器
   fast_calendar = FastCalendarPicker()
   fast_calendar.setFixedSize(300, 40)
   
   # 连接信号
   fast_calendar.dateChanged.connect(lambda date: print(f'快速选择日期: {date}'))

DatePickerBase
--------------

日期选择器基类。

.. code-block:: python

   from qfluentwidgets import DatePickerBase

   # 创建自定义日期选择器
   class CustomDatePicker(DatePickerBase):
       def __init__(self, parent=None):
           super().__init__(parent)
           # 自定义实现

DatePicker
-----------

日期选择器，用于选择单个日期。

.. code-block:: python

   from qfluentwidgets import DatePicker

   # 创建日期选择器
   date_picker = DatePicker()
   date_picker.setFixedSize(300, 40)
   
   # 设置日期
   from PySide6.QtCore import QDate
   date_picker.setDate(QDate.currentDate())
   
   # 连接信号
   date_picker.dateChanged.connect(lambda date: print(f'选择日期: {date.toString()}'))

ZhDatePicker
------------

中文日期选择器，支持中文日期格式。

.. code-block:: python

   from qfluentwidgets import ZhDatePicker

   # 创建中文日期选择器
   zh_date_picker = ZhDatePicker()
   zh_date_picker.setFixedSize(300, 40)
   
   # 连接信号
   zh_date_picker.dateChanged.connect(lambda date: print(f'中文日期: {date.toString()}'))

PickerBase
----------

选择器基类。

.. code-block:: python

   from qfluentwidgets import PickerBase

   # 创建自定义选择器
   class CustomPicker(PickerBase):
       def __init__(self, parent=None):
           super().__init__(parent)
           # 自定义实现

PickerPanel
-----------

选择器面板。

.. code-block:: python

   from qfluentwidgets import PickerPanel

   # 创建选择器面板
   panel = PickerPanel()
   panel.setFixedSize(300, 200)

PickerColumnFormatter
--------------------

选择器列格式化器。

.. code-block:: python

   from qfluentwidgets import PickerColumnFormatter

   # 创建格式化器
   formatter = PickerColumnFormatter()
   formatter.setFormat('yyyy-MM-dd')

TimePicker
----------

时间选择器，用于选择时间。

.. code-block:: python

   from qfluentwidgets import TimePicker

   # 创建时间选择器
   time_picker = TimePicker()
   time_picker.setFixedSize(200, 40)
   
   # 设置时间
   from PySide6.QtCore import QTime
   time_picker.setTime(QTime.currentTime())
   
   # 连接信号
   time_picker.timeChanged.connect(lambda time: print(f'选择时间: {time.toString()}'))

AMTimePicker
------------

AM/PM 时间选择器，支持12小时制。

.. code-block:: python

   from qfluentwidgets import AMTimePicker

   # 创建AM/PM时间选择器
   am_time_picker = AMTimePicker()
   am_time_picker.setFixedSize(250, 40)
   
   # 连接信号
   am_time_picker.timeChanged.connect(lambda time: print(f'AM/PM时间: {time.toString()}'))

完整示例
--------

下面是一个完整的日期时间组件使用示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                                QWidget, QLabel, QPushButton, QGroupBox)
   from PySide6.QtCore import Qt, QDate, QTime, QDateTime
   from qfluentwidgets import *

   class DateTimeDemoWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           self.setWindowTitle('日期时间组件示例')
           self.resize(600, 500)
           
           # 创建界面
           self.setup_ui()

       def setup_ui(self):
           """设置界面"""
           central_widget = QWidget()
           self.setCentralWidget(central_widget)
           
           layout = QVBoxLayout(central_widget)
           layout.setSpacing(20)
           layout.setContentsMargins(20, 20, 20, 20)
           
           # 添加标题
           title = SubtitleLabel('日期时间组件示例')
           layout.addWidget(title)
           
           # 添加各种日期时间组件
           self.add_calendar_picker_section(layout)
           self.add_date_picker_section(layout)
           self.add_time_picker_section(layout)

       def add_calendar_picker_section(self, layout):
           """添加日历选择器组件"""
           group = QGroupBox('日历选择器')
           group_layout = QVBoxLayout(group)
           
           # 创建日历选择器
           self.calendar_picker = CalendarPicker()
           self.calendar_picker.setFixedSize(300, 40)
           group_layout.addWidget(self.calendar_picker)
           
           # 创建快速日历选择器
           self.fast_calendar = FastCalendarPicker()
           self.fast_calendar.setFixedSize(300, 40)
           group_layout.addWidget(self.fast_calendar)
           
           # 日期显示标签
           self.calendar_label = QLabel('未选择日期')
           self.calendar_label.setAlignment(Qt.AlignCenter)
           group_layout.addWidget(self.calendar_label)
           
           # 连接信号
           self.calendar_picker.dateChanged.connect(self.on_calendar_changed)
           self.fast_calendar.dateChanged.connect(self.on_fast_calendar_changed)
           
           layout.addWidget(group)

       def add_date_picker_section(self, layout):
           """添加日期选择器组件"""
           group = QGroupBox('日期选择器')
           group_layout = QVBoxLayout(group)
           
           # 创建日期选择器
           self.date_picker = DatePicker()
           self.date_picker.setFixedSize(300, 40)
           group_layout.addWidget(self.date_picker)
           
           # 创建中文日期选择器
           self.zh_date_picker = ZhDatePicker()
           self.zh_date_picker.setFixedSize(300, 40)
           group_layout.addWidget(self.zh_date_picker)
           
           # 日期显示标签
           self.date_label = QLabel('未选择日期')
           self.date_label.setAlignment(Qt.AlignCenter)
           group_layout.addWidget(self.date_label)
           
           # 连接信号
           self.date_picker.dateChanged.connect(self.on_date_changed)
           self.zh_date_picker.dateChanged.connect(self.on_zh_date_changed)
           
           layout.addWidget(group)

       def add_time_picker_section(self, layout):
           """添加时间选择器组件"""
           group = QGroupBox('时间选择器')
           group_layout = QVBoxLayout(group)
           
           # 创建时间选择器
           self.time_picker = TimePicker()
           self.time_picker.setFixedSize(200, 40)
           group_layout.addWidget(self.time_picker)
           
           # 创建AM/PM时间选择器
           self.am_time_picker = AMTimePicker()
           self.am_time_picker.setFixedSize(250, 40)
           group_layout.addWidget(self.am_time_picker)
           
           # 时间显示标签
           self.time_label = QLabel('当前时间: ' + QTime.currentTime().toString())
           group_layout.addWidget(self.time_label)
           
           # 连接信号
           self.time_picker.timeChanged.connect(self.on_time_changed)
           self.am_time_picker.timeChanged.connect(self.on_am_time_changed)
           
           layout.addWidget(group)

       def on_calendar_changed(self, date):
           """日历选择器变化处理"""
           self.calendar_label.setText(f'日历选择: {date.toString("yyyy年MM月dd日")}')
           InfoBar.info(f'日历选择: {date.toString()}', parent=self)

       def on_fast_calendar_changed(self, date):
           """快速日历选择器变化处理"""
           InfoBar.info(f'快速日历选择: {date.toString()}', parent=self)

       def on_date_changed(self, date):
           """日期选择器变化处理"""
           self.date_label.setText(f'日期选择: {date.toString("yyyy年MM月dd日")}')
           InfoBar.info(f'日期选择: {date.toString()}', parent=self)

       def on_zh_date_changed(self, date):
           """中文日期选择器变化处理"""
           InfoBar.info(f'中文日期: {date.toString()}', parent=self)

       def on_time_changed(self, time):
           """时间变化处理"""
           self.time_label.setText(f'当前时间: {time.toString("hh:mm:ss")}')

       def on_am_time_changed(self, time):
           """AM/PM时间变化处理"""
           InfoBar.info(f'AM/PM时间: {time.toString()}', parent=self)

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       window = DateTimeDemoWindow()
       window.show()
       sys.exit(app.exec())

最佳实践
--------

1. **本地化设置**: 
   - 根据用户地区设置日期格式
   - 使用合适的星期显示方式
   - ZhDatePicker 适合中文用户

2. **用户体验**: 
   - 提供快速跳转到今天的功能
   - 支持键盘导航
   - 添加日期范围限制

3. **数据验证**: 
   - 验证用户输入的日期有效性
   - 处理时区相关问题

4. **界面设计**: 
   - 保持与其他组件风格一致
   - 合理设置组件大小
   - 提供清晰的视觉反馈

组件对比
--------

| 组件 | 用途 | 特点 |
|------|------|------|
| CalendarPicker | 日历选择器 | 带下拉日历，直观易用 |
| FastCalendarPicker | 快速日历选择器 | 性能优化版本 |
| DatePicker | 标准日期选择器 | 基础日期选择功能 |
| ZhDatePicker | 中文日期选择器 | 支持中文格式 |
| TimePicker | 时间选择器 | 24小时制时间选择 |
| AMTimePicker | AM/PM时间选择器 | 12小时制时间选择 |
