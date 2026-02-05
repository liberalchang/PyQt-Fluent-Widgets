Picker Base 选择器基类模块
=============================

Picker Base 模块提供选择器的基础组件和功能，支持滚轮式选择和自定义格式化。
该模块是日期选择器、时间选择器等组件的基础框架，提供灵活的扩展能力。

主要功能
--------

- **基础框架** - 提供选择器的通用基础功能
- **滚轮选择** - 支持循环滚轮式选择界面
- **格式化支持** - 提供灵活的数据格式化机制
- **面板管理** - 管理选择器面板的显示和交互
- **主题适配** - 完美适配Fluent Design主题

核心组件
--------

PickerBase
~~~~~~~~~~

选择器基类，提供选择器的核心功能。

.. code-block:: python

   from qfluentwidgets.components.date_time.picker_base import PickerBase
   from PySide6.QtWidgets import QVBoxLayout
   
   class CustomPicker(PickerBase):
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_columns()
       
       def setup_columns(self):
           """设置选择列"""
           # 添加年列
           self.addColumn("年", range(2020, 2031), 80)
           
           # 添加月列
           self.addColumn("月", range(1, 13), 80)
           
           # 添加日列
           self.addColumn("日", range(1, 32), 80)

**主要方法：**
- ``addColumn()`` - 添加选择列
- ``setColumnValue()`` - 设置列值
- ``getColumnValue()`` - 获取列值
- ``setColumnWidth()`` - 设置列宽

PickerColumnFormatter
~~~~~~~~~~~~~~~~~~~~~

选择列格式化器，用于数据的编码和解码。

.. code-block:: python

   from qfluentwidgets.components.date_time.picker_base import PickerColumnFormatter
   
   class CustomFormatter(PickerColumnFormatter):
       def encode(self, value):
           """编码显示值"""
           return f"第{value}个"
       
       def decode(self, value):
           """解码实际值"""
           return int(value.replace("第", "").replace("个", ""))

PickerPanel
~~~~~~~~~~~

选择器面板，管理选择器的显示和交互。

.. code-block:: python

   from qfluentwidgets.components.date_time.picker_base import PickerPanel
   from PySide6.QtWidgets import QVBoxLayout
   
   # 创建选择器面板
   panel = PickerPanel()
   
   # 连接确认信号
   panel.confirmed.connect(on_confirmed)

**主要信号：**
- ``confirmed`` - 确认选择信号

实际应用
--------

基本选择器
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.picker_base import PickerBase, PickerColumnFormatter
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   
   class BasicPickerWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建自定义选择器
           self.picker = CustomPicker()
           
           # 显示选择结果
           self.result_label = Label("未选择")
           
           layout.addWidget(self.picker)
           layout.addWidget(self.result_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.picker.confirmed.connect(self.on_confirmed)
       
       def on_confirmed(self, values):
           """确认选择处理"""
           if len(values) >= 3:
               year, month, day = values[0], values[1], values[2]
               self.result_label.setText(f"选择了: {year}年{month}月{day}日")
   
   class CustomPicker(PickerBase):
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_columns()
       
       def setup_columns(self):
           """设置选择列"""
           # 添加年列
           self.addColumn("年", range(2020, 2031), 80)
           
           # 添加月列
           self.addColumn("月", range(1, 13), 80)
           
           # 添加日列
           self.addColumn("日", range(1, 32), 80)

自定义格式化选择器
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.picker_base import PickerBase, PickerColumnFormatter
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   
   class WeekdayFormatter(PickerColumnFormatter):
       """星期格式化器"""
       
       weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
       
       def encode(self, value):
           """编码显示值"""
           if isinstance(value, int) and 1 <= value <= 7:
               return self.weekdays[value - 1]
           return str(value)
       
       def decode(self, value):
           """解码实际值"""
           if value in self.weekdays:
               return self.weekdays.index(value) + 1
           return int(value)
   
   class WeekdayPicker(PickerBase):
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_columns()
       
       def setup_columns(self):
           """设置选择列"""
           # 添加星期列
           weekday_formatter = WeekdayFormatter()
           self.addColumn("星期", range(1, 8), 100, Qt.AlignCenter, weekday_formatter)
           
           # 添加时间列
           self.addColumn("小时", range(0, 24), 80)
           self.addColumn("分钟", range(0, 60), 80)
   
   class CustomFormatPickerWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建自定义格式选择器
           self.weekday_picker = WeekdayPicker()
           
           # 显示选择结果
           self.result_label = Label("未选择")
           
           layout.addWidget(self.weekday_picker)
           layout.addWidget(self.result_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.weekday_picker.confirmed.connect(self.on_confirmed)
       
       def on_confirmed(self, values):
           """确认选择处理"""
           if len(values) >= 3:
               weekday, hour, minute = values[0], values[1], values[2]
               self.result_label.setText(f"选择了: {weekday} {hour:02d}:{minute:02d}")

高级用法
--------

多列联动选择器
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.picker_base import PickerBase
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   
   class LinkedPicker(PickerBase):
       """联动选择器"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_columns()
       
       def setup_columns(self):
           """设置选择列"""
           # 添加年份列
           self.yearIndex = 0
           self.monthIndex = 1
           self.dayIndex = 2
           
           self.addColumn("年", range(2020, 2031), 80)
           self.addColumn("月", range(1, 13), 80)
           self.addColumn("日", range(1, 32), 80)
       
       def _onColumnValueChanged(self, panel, index, value):
           """列值变化处理"""
           if index in [self.yearIndex, self.monthIndex]:
               # 年或月变化时更新天数
               self.update_days(panel)
       
       def update_days(self, panel):
           """更新天数"""
           year = self.decodeValue(self.yearIndex, panel.columnValue(self.yearIndex))
           month = self.decodeValue(self.monthIndex, panel.columnValue(self.monthIndex))
           
           # 计算该月的天数
           if month in [4, 6, 9, 11]:
               days = 30
           elif month == 2:
               # 闰年判断
               if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                   days = 29
               else:
                   days = 28
           else:
               days = 31
           
           # 更新天数列
           self.setColumnItems(self.dayIndex, range(1, days + 1))
   
   class LinkedPickerWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建联动选择器
           self.linked_picker = LinkedPicker()
           
           # 显示选择结果
           self.result_label = Label("未选择")
           
           layout.addWidget(self.linked_picker)
           layout.addWidget(self.result_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.linked_picker.confirmed.connect(self.on_confirmed)
       
       def on_confirmed(self, values):
           """确认选择处理"""
           if len(values) >= 3:
               year, month, day = values[0], values[1], values[2]
               self.result_label.setText(f"选择了: {year}年{month}月{day}日")

最佳实践
--------

1. **继承设计** - 通过继承PickerBase创建自定义选择器
2. **格式化器** - 使用PickerColumnFormatter实现数据格式化
3. **联动逻辑** - 在_onColumnValueChanged中实现列间联动
4. **用户体验** - 提供合理的默认值和范围限制
5. **性能优化** - 避免频繁的列更新操作

注意事项
--------

- 选择器的列索引需要正确管理
- 格式化器的encode和decode方法需要对应
- 联动逻辑需要考虑边界情况
- 大量数据可能影响选择器性能
- 自定义样式需要与主题保持一致

相关模块
--------

- :doc:`components.date_time.date_picker` - 日期选择器
- :doc:`components.widgets.cycle_list_widget` - 循环列表组件
- :doc:`common.style_sheet` - 样式表管理
