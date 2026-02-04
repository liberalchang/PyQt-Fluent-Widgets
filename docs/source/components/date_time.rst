日期时间组件 (Date Time)
=======================

本节介绍 PySide6-Fluent-Widgets 中的日期时间相关组件。

Calendar
--------

日历组件，用于显示和选择日期。

.. code-block:: python

   from qfluentwidgets import Calendar

   # 创建日历
   calendar = Calendar()
   calendar.setFixedSize(400, 300)
   
   # 连接信号
   calendar.selectionChanged.connect(lambda date: print(f'选择日期: {date}'))

DatePicker
----------

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

DateTimePicker
--------------

日期时间选择器，用于同时选择日期和时间。

.. code-block:: python

   from qfluentwidgets import DateTimePicker

   # 创建日期时间选择器
   datetime_picker = DateTimePicker()
   datetime_picker.setFixedSize(350, 40)
   
   # 连接信号
   datetime_picker.dateTimeChanged.connect(
       lambda datetime: print(f'选择日期时间: {datetime.toString()}')
   )

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
           self.add_calendar_section(layout)
           self.add_date_picker_section(layout)
           self.add_time_picker_section(layout)
           self.add_datetime_picker_section(layout)

       def add_calendar_section(self, layout):
           """添加日历组件"""
           group = QGroupBox('日历组件')
           group_layout = QVBoxLayout(group)
           
           # 创建日历
           self.calendar = Calendar()
           self.calendar.setFixedSize(400, 250)
           group_layout.addWidget(self.calendar)
           
           # 添加按钮
           button_layout = QHBoxLayout()
           
           today_btn = PushButton('今天')
           today_btn.clicked.connect(self.go_to_today)
           
           clear_btn = PushButton('清除选择')
           clear_btn.clicked.connect(self.clear_selection)
           
           button_layout.addWidget(today_btn)
           button_layout.addWidget(clear_btn)
           button_layout.addStretch()
           
           group_layout.addLayout(button_layout)
           
           # 日期显示标签
           self.date_label = QLabel('未选择日期')
           self.date_label.setAlignment(Qt.AlignCenter)
           group_layout.addWidget(self.date_label)
           
           # 连接信号
           self.calendar.selectionChanged.connect(self.on_date_selected)
           
           layout.addWidget(group)

       def add_date_picker_section(self, layout):
           """添加日期选择器"""
           group = QGroupBox('日期选择器')
           group_layout = QVBoxLayout(group)
           
           # 创建日期选择器
           self.date_picker = DatePicker()
           self.date_picker.setFixedSize(300, 40)
           group_layout.addWidget(self.date_picker)
           
           # 创建日历选择器
           self.calendar_picker = CalendarPicker()
           self.calendar_picker.setFixedSize(300, 40)
           group_layout.addWidget(self.calendar_picker)
           
           # 连接信号
           self.date_picker.dateChanged.connect(self.on_date_picker_changed)
           self.calendar_picker.dateChanged.connect(self.on_calendar_picker_changed)
           
           layout.addWidget(group)

       def add_time_picker_section(self, layout):
           """添加时间选择器"""
           group = QGroupBox('时间选择器')
           group_layout = QVBoxLayout(group)
           
           # 创建时间选择器
           self.time_picker = TimePicker()
           self.time_picker.setFixedSize(200, 40)
           group_layout.addWidget(self.time_picker)
           
           # 时间显示标签
           self.time_label = QLabel('当前时间: ' + QTime.currentTime().toString())
           group_layout.addWidget(self.time_label)
           
           # 连接信号
           self.time_picker.timeChanged.connect(self.on_time_changed)
           
           layout.addWidget(group)

       def add_datetime_picker_section(self, layout):
           """添加日期时间选择器"""
           group = QGroupBox('日期时间选择器')
           group_layout = QVBoxLayout(group)
           
           # 创建日期时间选择器
           self.datetime_picker = DateTimePicker()
           self.datetime_picker.setFixedSize(350, 40)
           group_layout.addWidget(self.datetime_picker)
           
           # 日期时间显示标签
           self.datetime_label = QLabel('当前日期时间: ' + QDateTime.currentDateTime().toString())
           group_layout.addWidget(self.datetime_label)
           
           # 连接信号
           self.datetime_picker.dateTimeChanged.connect(self.on_datetime_changed)
           
           layout.addWidget(group)

       def go_to_today(self):
           """跳转到今天"""
           self.calendar.selectDate(QDate.currentDate())

       def clear_selection(self):
           """清除选择"""
           self.calendar.clearSelection()
           self.date_label.setText('未选择日期')

       def on_date_selected(self, date):
           """日期选择处理"""
           self.date_label.setText(f'选择日期: {date.toString("yyyy年MM月dd日")}')

       def on_date_picker_changed(self, date):
           """日期选择器变化处理"""
           InfoBar.info(f'日期选择器: {date.toString()}', parent=self)

       def on_calendar_picker_changed(self, date):
           """日历选择器变化处理"""
           InfoBar.info(f'日历选择器: {date.toString()}', parent=self)

       def on_time_changed(self, time):
           """时间变化处理"""
           self.time_label.setText(f'当前时间: {time.toString("hh:mm:ss")}')

       def on_datetime_changed(self, datetime):
           """日期时间变化处理"""
           self.datetime_label.setText(f'当前日期时间: {datetime.toString("yyyy年MM月dd日 hh:mm:ss")}')

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
