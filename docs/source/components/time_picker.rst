Time Picker 时间选择器模块
=============================

Time Picker 模块提供滚轮式时间选择功能，支持24小时制和12小时制。
该模块提供Fluent Design风格的时间选择界面，支持小时、分钟、秒的选择和自定义显示格式。

主要功能
--------

- **滚轮选择** - 提供直观的滚轮式时间选择
- **多种格式** - 支持24小时制和12小时制
- **秒数显示** - 可选择是否显示秒数
- **格式化支持** - 支持自定义时间格式化
- **实时更新** - 支持时间的实时选择和更新

核心组件
--------

TimePicker
~~~~~~~~~~

24小时制时间选择器，提供标准的时间选择功能。

.. code-block:: python

   from qfluentwidgets.components.date_time.time_picker import TimePicker
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QTime
   
   # 创建时间选择器
   time_picker = TimePicker()
   
   # 设置是否显示秒数
   time_picker.setSecondVisible(True)
   
   # 连接信号
   time_picker.timeChanged.connect(on_time_changed)
   
   # 设置时间
   time_picker.setTime(QTime.currentTime())

**主要信号：**
- ``timeChanged`` - 时间变化信号

**主要属性：**
- ``time`` - 选中时间
- ``secondVisible`` - 是否显示秒数

AMTimePicker
~~~~~~~~~~~~

12小时制时间选择器，支持AM/PM格式。

.. code-block:: python

   from qfluentwidgets.components.date_time.time_picker import AMTimePicker
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QTime
   
   # 创建12小时制时间选择器
   am_time_picker = AMTimePicker()
   
   # 设置是否显示秒数
   am_time_picker.setSecondVisible(True)
   
   # 连接信号
   am_time_picker.timeChanged.connect(on_time_changed)
   
   # 设置时间
   am_time_picker.setTime(QTime.currentTime())

**特点：**
- 支持12小时制显示
- 包含AM/PM选择列
- 自动处理12小时制转换

实际应用
--------

基本时间选择
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.time_picker import TimePicker
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import QTime
   
   class BasicTimePickerWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("选择时间")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建时间选择器
           self.time_picker = TimePicker()
           self.time_picker.setSecondVisible(True)
           self.time_picker.setTime(QTime.currentTime())
           
           # 显示选中的时间
           self.selected_time_label = Label("未选择时间")
           self.selected_time_label.setAlignment(Qt.AlignCenter)
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           now_btn = PushButton("当前时间")
           clear_btn = PushButton("清空")
           
           now_btn.clicked.connect(self.set_current_time)
           clear_btn.clicked.connect(self.clear_time)
           
           button_layout.addWidget(now_btn)
           button_layout.addWidget(clear_btn)
           
           layout.addWidget(title_label)
           layout.addWidget(self.time_picker)
           layout.addWidget(self.selected_time_label)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.time_picker.timeChanged.connect(self.on_time_changed)
       
       def on_time_changed(self, time):
           """时间变化处理"""
           if time.isValid():
               time_str = time.toString("HH:mm:ss")
               self.selected_time_label.setText(f"已选择: {time_str}")
           else:
               self.selected_time_label.setText("未选择时间")
       
       def set_current_time(self):
           """设置为当前时间"""
           self.time_picker.setTime(QTime.currentTime())
       
       def clear_time(self):
           """清空时间"""
           self.time_picker.setTime(QTime())

12小时制时间选择
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.time_picker import AMTimePicker
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import QTime
   
   class AMTimePickerWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("选择时间 (12小时制)")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建12小时制时间选择器
           self.am_time_picker = AMTimePicker()
           self.am_time_picker.setSecondVisible(True)
           self.am_time_picker.setTime(QTime.currentTime())
           
           # 显示选中的时间
           self.selected_time_label = Label("未选择时间")
           self.selected_time_label.setAlignment(Qt.AlignCenter)
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           now_btn = PushButton("当前时间")
           clear_btn = PushButton("清空")
           
           now_btn.clicked.connect(self.set_current_time)
           clear_btn.clicked.connect(self.clear_time)
           
           button_layout.addWidget(now_btn)
           button_layout.addWidget(clear_btn)
           
           layout.addWidget(title_label)
           layout.addWidget(self.am_time_picker)
           layout.addWidget(self.selected_time_label)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.am_time_picker.timeChanged.connect(self.on_time_changed)
       
       def on_time_changed(self, time):
           """时间变化处理"""
           if time.isValid():
               time_str_12 = time.toString("hh:mm:ss AP")
               time_str_24 = time.toString("HH:mm:ss")
               self.selected_time_label.setText(f"12小时制: {time_str_12}\n24小时制: {time_str_24}")
           else:
               self.selected_time_label.setText("未选择时间")
       
       def set_current_time(self):
           """设置为当前时间"""
           self.am_time_picker.setTime(QTime.currentTime())
       
       def clear_time(self):
           """清空时间"""
           self.am_time_picker.setTime(QTime())

时间格式切换
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.time_picker import TimePicker, AMTimePicker
   from qfluentwidgets import CardWidget, Label, ComboBox, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QStackedWidget
   from PySide6.QtCore import QTime
   
   class FormatSwitchTimePickerWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
           self.current_time = QTime.currentTime()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 格式选择
           format_layout = QHBoxLayout()
           
           format_label = Label("时间格式:")
           self.format_combo = ComboBox()
           self.format_combo.addItems([
               "24小时制",
               "12小时制"
           ])
           
           format_layout.addWidget(format_label)
           format_layout.addWidget(self.format_combo)
           
           # 堆栈控件
           self.stacked_widget = QStackedWidget()
           
           # 创建不同格式的时间选择器
           self.time_24 = TimePicker()
           self.time_24.setSecondVisible(True)
           self.time_24.setTime(self.current_time)
           
           self.time_12 = AMTimePicker()
           self.time_12.setSecondVisible(True)
           self.time_12.setTime(self.current_time)
           
           # 添加到堆栈控件
           self.stacked_widget.addWidget(self.time_24)
           self.stacked_widget.addWidget(self.time_12)
           
           # 显示当前时间
           self.current_time_label = Label()
           self.update_time_display()
           
           # 秒数显示控制
           seconds_layout = QHBoxLayout()
           
           self.seconds_checkbox = QCheckBox("显示秒数")
           self.seconds_checkbox.setChecked(True)
           self.seconds_checkbox.stateChanged.connect(self.toggle_seconds)
           
           seconds_layout.addWidget(self.seconds_checkbox)
           
           layout.addLayout(format_layout)
           layout.addWidget(self.stacked_widget)
           layout.addWidget(self.current_time_label)
           layout.addLayout(seconds_layout)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.format_combo.currentTextChanged.connect(self.change_format)
           
           # 连接所有时间选择器的信号
           self.time_24.timeChanged.connect(self.on_time_changed)
           self.time_12.timeChanged.connect(self.on_time_changed)
       
       def change_format(self, format_text):
           """切换时间格式"""
           if format_text == "24小时制":
               self.stacked_widget.setCurrentIndex(0)
               self.time_24.setTime(self.current_time)
           else:
               self.stacked_widget.setCurrentIndex(1)
               self.time_12.setTime(self.current_time)
       
       def on_time_changed(self, time):
           """时间变化处理"""
           self.current_time = time
           self.update_time_display()
       
       def update_time_display(self):
           """更新时间显示"""
           if self.current_time.isValid():
               format_text = self.format_combo.currentText()
               if format_text == "24小时制":
                   time_str = self.current_time.toString("HH:mm:ss")
               else:
                   time_str = self.current_time.toString("hh:mm:ss AP")
               
               self.current_time_label.setText(f"当前时间: {time_str}")
           else:
               self.current_time_label.setText("未选择时间")
       
       def toggle_seconds(self, state):
           """切换秒数显示"""
           show_seconds = state == Qt.Checked
           self.time_24.setSecondVisible(show_seconds)
           self.time_12.setSecondVisible(show_seconds)

高级用法
--------

自定义时间选择器
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.time_picker import TimePickerBase, PickerColumnFormatter
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QTime, Qt
   
   class CustomTimeFormatter(PickerColumnFormatter):
       """自定义时间格式化器"""
       
       def encode(self, value):
           """编码显示值"""
           if isinstance(value, int):
               return f"{value:02d}时"
           return str(value)
       
       def decode(self, value):
           """解码实际值"""
           if isinstance(value, str) and value.endswith("时"):
               return int(value.replace("时", ""))
           return int(value)
   
   class CustomTimePicker(TimePickerBase):
       """自定义时间选择器"""
       
       def __init__(self, parent=None, showSeconds=False):
           super().__init__(parent, showSeconds)
           self.setup_columns()
       
       def setup_columns(self):
           """设置选择列"""
           # 添加小时列
           hour_formatter = CustomTimeFormatter()
           self.addColumn("小时", range(0, 24), 100, Qt.AlignCenter, hour_formatter)
           
           # 添加分钟列
           minute_formatter = CustomTimeFormatter()
           self.addColumn("分钟", range(0, 60), 100, Qt.AlignCenter, minute_formatter)
           
           # 添加秒数列
           if self.isSecondVisible():
               second_formatter = CustomTimeFormatter()
               self.addColumn("秒数", range(0, 60), 100, Qt.AlignCenter, second_formatter)
       
       def setTime(self, time: QTime):
           """设置时间"""
           if not time.isValid() or time.isNull():
               return
           
           self._time = time
           self.setColumnValue(0, time.hour())
           self.setColumnValue(1, time.minute())
           if self.isSecondVisible():
               self.setColumnValue(2, time.second())
       
       def setSecondVisible(self, isVisible: bool):
           """设置秒数显示"""
           self._isSecondVisible = isVisible
           # 重新设置列
           self.clearColumns()
           self.setup_columns()
   
   class CustomTimePickerWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建自定义时间选择器
           self.custom_time_picker = CustomTimePicker()
           self.custom_time_picker.setSecondVisible(True)
           self.custom_time_picker.setTime(QTime.currentTime())
           
           # 显示选中的时间
           self.selected_time_label = Label("未选择时间")
           
           layout.addWidget(self.custom_time_picker)
           layout.addWidget(self.selected_time_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.custom_time_picker.timeChanged.connect(self.on_time_changed)
       
       def on_time_changed(self, time):
           """时间变化处理"""
           if time.isValid():
               time_str = time.toString("HH:mm:ss")
               self.selected_time_label.setText(f"已选择: {time_str}")
           else:
               self.selected_time_label.setText("未选择时间")

时间范围选择
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.time_picker import TimePicker
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import QTime
   
   class TimeRangePickerWidget(CardWidget):
       """时间范围选择器"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 开始时间选择器
           start_group = QVBoxLayout()
           start_label = Label("开始时间:")
           self.start_time_picker = TimePicker()
           self.start_time_picker.setSecondVisible(True)
           start_group.addWidget(start_label)
           start_group.addWidget(self.start_time_picker)
           
           # 结束时间选择器
           end_group = QVBoxLayout()
           end_label = Label("结束时间:")
           self.end_time_picker = TimePicker()
           self.end_time_picker.setSecondVisible(True)
           end_group.addWidget(end_label)
           end_group.addWidget(self.end_time_picker)
           
           # 时间范围布局
           range_layout = QHBoxLayout()
           range_layout.addLayout(start_group)
           range_layout.addLayout(end_group)
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           work_hours_btn = PushButton("工作时间")
           lunch_time_btn = PushButton("午餐时间")
           clear_btn = PushButton("清空")
           
           work_hours_btn.clicked.connect(self.set_work_hours)
           lunch_time_btn.clicked.connect(self.set_lunch_time)
           clear_btn.clicked.connect(self.clear_range)
           
           button_layout.addWidget(work_hours_btn)
           button_layout.addWidget(lunch_time_btn)
           button_layout.addWidget(clear_btn)
           
           # 显示时间范围
           self.range_label = Label("请选择时间范围")
           
           layout.addLayout(range_layout)
           layout.addLayout(button_layout)
           layout.addWidget(self.range_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.start_time_picker.timeChanged.connect(self.on_time_changed)
           self.end_time_picker.timeChanged.connect(self.on_time_changed)
       
       def on_time_changed(self):
           """时间变化处理"""
           start_time = self.start_time_picker.time
           end_time = self.end_time_picker.time
           
           # 更新显示
           if start_time.isValid() and end_time.isValid():
               if start_time <= end_time:
                   duration = QTime(0, 0).addSecs(start_time.secsTo(end_time))
                   duration_str = duration.toString("HH:mm")
                   self.range_label.setText(
                       f"时间范围: {start_time.toString('HH:mm:ss')} - {end_time.toString('HH:mm:ss')} "
                       f"(时长: {duration_str})"
                   )
               else:
                   self.range_label.setText("开始时间不能晚于结束时间")
           else:
               self.range_label.setText("请选择完整的时间范围")
       
       def set_work_hours(self):
           """设置为工作时间"""
           self.start_time_picker.setTime(QTime(9, 0, 0))
           self.end_time_picker.setTime(QTime(18, 0, 0))
       
       def set_lunch_time(self):
           """设置为午餐时间"""
           self.start_time_picker.setTime(QTime(12, 0, 0))
           self.end_time_picker.setTime(QTime(13, 0, 0))
       
       def clear_range(self):
           """清空范围"""
           self.start_time_picker.setTime(QTime())
           self.end_time_picker.setTime(QTime())
           self.range_label.setText("已清空时间范围")

最佳实践
--------

1. **格式选择** - 根据用户习惯选择12小时制或24小时制
2. **秒数显示** - 根据精度需求决定是否显示秒数
3. **用户体验** - 提供当前时间快捷设置
4. **时间验证** - 实现时间范围的有效性验证
5. **国际化** - 支持多语言的时间显示

注意事项
--------

- 12小时制需要正确处理AM/PM转换
- 时间格式需要根据地区进行调整
- 时间范围验证需要在应用层面进行
- 自定义格式化器需要正确处理编码和解码
- 时间选择事件可能频繁触发，需要防抖处理

相关模块
--------

- :doc:`components.date_time.date_picker` - 日期选择器
- :doc:`components.date_time.picker_base` - 选择器基类
- :doc:`common.style_sheet` - 样式表管理
