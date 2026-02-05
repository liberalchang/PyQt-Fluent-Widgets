Date Picker 日期选择器模块
=============================

Date Picker 模块提供滚轮式日期选择功能，支持多种日期格式和本地化显示。
该模块提供Fluent Design风格的日期选择界面，支持年、月、日的独立选择和自定义格式化。

主要功能
--------

- **滚轮选择** - 提供直观的滚轮式日期选择
- **多种格式** - 支持MM-DD-YYYY和YYYY-MM-DD格式
- **本地化支持** - 支持中文和英文月份显示
- **自定义格式化** - 支持自定义日期格式化器
- **动态天数** - 根据年月自动调整可选天数

核心组件
--------

DatePicker
~~~~~~~~~~

标准日期选择器，提供基本的滚轮式日期选择功能。

.. code-block:: python

   from qfluentwidgets.components.date_time.date_picker import DatePicker
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QDate
   
   # 创建日期选择器
   date_picker = DatePicker()
   
   # 设置日期格式
   date_picker.setDateFormat(DatePicker.MM_DD_YYYY)  # 月-日-年格式
   # date_picker.setDateFormat(DatePicker.YYYY_MM_DD)  # 年-月-日格式
   
   # 连接信号
   date_picker.dateChanged.connect(on_date_changed)
   
   # 设置日期
   date_picker.setDate(QDate.currentDate())

**日期格式：**
- ``MM_DD_YYYY`` - 月-日-年格式
- ``YYYY_MM_DD`` - 年-月-日格式

**主要信号：**
- ``dateChanged`` - 日期变化信号

**主要属性：**
- ``date`` - 选中日期
- ``dateFormat`` - 日期格式

ZhDatePicker
~~~~~~~~~~~~

中文日期选择器，提供中文格式的日期选择。

.. code-block:: python

   from qfluentwidgets.components.date_time.date_picker import ZhDatePicker
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QDate
   
   # 创建中文日期选择器
   zh_date_picker = ZhDatePicker()
   
   # 连接信号
   zh_date_picker.dateChanged.connect(on_date_changed)
   
   # 设置日期
   zh_date_picker.setDate(QDate.currentDate())

**特点：**
- 年份显示为 "XXXX年"
- 月份显示为 "XX月"
- 日期显示为 "XX日"

实际应用
--------

基本日期选择
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.date_picker import DatePicker
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import QDate
   
   class BasicDatePickerWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("选择日期")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建日期选择器
           self.date_picker = DatePicker()
           self.date_picker.setDateFormat(DatePicker.MM_DD_YYYY)
           self.date_picker.setDate(QDate.currentDate())
           
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
           layout.addWidget(self.date_picker)
           layout.addWidget(self.selected_date_label)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.date_picker.dateChanged.connect(self.on_date_changed)
       
       def on_date_changed(self, date):
           """日期变化处理"""
           if date.isValid():
               date_str = date.toString("yyyy年MM月dd日")
               self.selected_date_label.setText(f"已选择: {date_str}")
           else:
               self.selected_date_label.setText("未选择日期")
       
       def set_today(self):
           """设置为今天"""
           self.date_picker.setDate(QDate.currentDate())
       
       def clear_date(self):
           """清空日期"""
           self.date_picker.setDate(QDate())

格式切换
~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.date_picker import DatePicker
   from qfluentwidgets import CardWidget, Label, ComboBox, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import QDate
   
   class FormatSwitchDatePickerWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 格式选择
           format_layout = QHBoxLayout()
           
           format_label = Label("日期格式:")
           self.format_combo = ComboBox()
           self.format_combo.addItems([
               "月-日-年 (MM-DD-YYYY)",
               "年-月-日 (YYYY-MM-DD)"
           ])
           
           format_layout.addWidget(format_label)
           format_layout.addWidget(self.format_combo)
           
           # 创建日期选择器
           self.date_picker = DatePicker()
           self.date_picker.setDate(QDate.currentDate())
           
           # 显示选中的日期
           self.selected_date_label = Label("未选择日期")
           self.selected_date_label.setAlignment(Qt.AlignCenter)
           
           # 应用格式按钮
           apply_btn = PushButton("应用格式")
           apply_btn.clicked.connect(self.apply_format)
           
           layout.addLayout(format_layout)
           layout.addWidget(self.date_picker)
           layout.addWidget(self.selected_date_label)
           layout.addWidget(apply_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.date_picker.dateChanged.connect(self.on_date_changed)
           self.format_combo.currentTextChanged.connect(self.on_format_changed)
       
       def on_date_changed(self, date):
           """日期变化处理"""
           if date.isValid():
               format_text = self.format_combo.currentText()
               if "MM-DD-YYYY" in format_text:
                   date_str = date.toString("MM-dd-yyyy")
               else:
                   date_str = date.toString("yyyy-MM-dd")
               
               self.selected_date_label.setText(f"已选择: {date_str}")
           else:
               self.selected_date_label.setText("未选择日期")
       
       def on_format_changed(self, format_text):
           """格式变化处理"""
           if "MM-DD-YYYY" in format_text:
               self.date_picker.setDateFormat(DatePicker.MM_DD_YYYY)
           else:
               self.date_picker.setDateFormat(DatePicker.YYYY_MM_DD)
           
           # 更新显示
           self.on_date_changed(self.date_picker.date)
       
       def apply_format(self):
           """应用格式"""
           self.on_format_changed(self.format_combo.currentText())

中文日期选择
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.date_picker import ZhDatePicker
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import QDate
   
   class ChineseDatePickerWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("选择日期 (中文格式)")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建中文日期选择器
           self.zh_date_picker = ZhDatePicker()
           self.zh_date_picker.setDate(QDate.currentDate())
           
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
           layout.addWidget(self.zh_date_picker)
           layout.addWidget(self.selected_date_label)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.zh_date_picker.dateChanged.connect(self.on_date_changed)
       
       def on_date_changed(self, date):
           """日期变化处理"""
           if date.isValid():
               date_str = date.toString("yyyy年MM月dd日 dddd")
               self.selected_date_label.setText(f"已选择: {date_str}")
           else:
               self.selected_date_label.setText("未选择日期")
       
       def set_today(self):
           """设置为今天"""
           self.zh_date_picker.setDate(QDate.currentDate())
       
       def clear_date(self):
           """清空日期"""
           self.zh_date_picker.setDate(QDate())

高级用法
--------

自定义格式化器
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.date_picker import DatePickerBase, PickerColumnFormatter
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QDate
   
   class CustomFormatter(PickerColumnFormatter):
       """自定义格式化器"""
       
       def __init__(self, prefix="", suffix=""):
           super().__init__()
           self.prefix = prefix
           self.suffix = suffix
       
       def encode(self, value):
           """编码值"""
           return f"{self.prefix}{value}{self.suffix}"
       
       def decode(self, value):
           """解码值"""
           # 移除前缀和后缀
           if value.startswith(self.prefix):
               value = value[len(self.prefix):]
           if value.endswith(self.suffix):
               value = value[:-len(self.suffix)]
           return int(value)
   
   class CustomDatePicker(DatePickerBase):
       """自定义日期选择器"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_custom_formatters()
           self.setup_columns()
       
       def setup_custom_formatters(self):
           """设置自定义格式化器"""
           self.custom_year_formatter = CustomFormatter("Y", "")
           self.custom_month_formatter = CustomFormatter("M", "")
           self.custom_day_formatter = CustomFormatter("D", "")
       
       def setup_columns(self):
           """设置列"""
           # 这里需要实现具体的列设置逻辑
           # 参考DatePicker的实现
           pass
       
       def setDate(self, date: QDate):
           """设置日期"""
           self._date = date
           # 更新列值
           # 这里需要实现具体的更新逻辑
           pass
   
   class CustomDatePickerWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自定义格式日期选择器")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建自定义日期选择器
           self.custom_picker = CustomDatePicker()
           self.custom_picker.setDate(QDate.currentDate())
           
           # 显示选中的日期
           self.selected_date_label = Label("未选择日期")
           self.selected_date_label.setAlignment(Qt.AlignCenter)
           
           layout.addWidget(title_label)
           layout.addWidget(self.custom_picker)
           layout.addWidget(self.selected_date_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.custom_picker.dateChanged.connect(self.on_date_changed)
       
       def on_date_changed(self, date):
           """日期变化处理"""
           if date.isValid():
               date_str = date.toString("yyyy-MM-dd")
               self.selected_date_label.setText(f"已选择: {date_str}")
           else:
               self.selected_date_label.setText("未选择日期")

日期范围限制
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.date_time.date_picker import DatePicker
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import QDate
   
   class RangeLimitedDatePickerWidget(CardWidget):
       """日期范围限制选择器"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
           self.setup_date_range()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("选择日期 (有限制范围)")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建日期选择器
           self.date_picker = DatePicker()
           self.date_picker.setDate(QDate.currentDate())
           
           # 显示范围信息
           self.range_label = Label("日期范围: 未设置")
           self.range_label.setAlignment(Qt.AlignCenter)
           
           # 显示选中的日期
           self.selected_date_label = Label("未选择日期")
           self.selected_date_label.setAlignment(Qt.AlignCenter)
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           set_min_btn = PushButton("设置最小日期")
           set_max_btn = PushButton("设置最大日期")
           clear_range_btn = PushButton("清除限制")
           
           set_min_btn.clicked.connect(self.set_min_date)
           set_max_btn.clicked.connect(self.set_max_date)
           clear_range_btn.clicked.connect(self.clear_range)
           
           button_layout.addWidget(set_min_btn)
           button_layout.addWidget(set_max_btn)
           button_layout.addWidget(clear_range_btn)
           
           layout.addWidget(title_label)
           layout.addWidget(self.date_picker)
           layout.addWidget(self.range_label)
           layout.addWidget(self.selected_date_label)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.date_picker.dateChanged.connect(self.on_date_changed)
       
       def setup_date_range(self):
           """设置日期范围"""
           # 设置默认范围：当前日期前后30天
           current_date = QDate.currentDate()
           self.min_date = current_date.addDays(-30)
           self.max_date = current_date.addDays(30)
           
           self.update_range_display()
       
       def on_date_changed(self, date):
           """日期变化处理"""
           if date.isValid():
               # 检查日期是否在范围内
               if self.min_date and date < self.min_date:
                   self.date_picker.setDate(self.min_date)
                   self.selected_date_label.setText(f"日期不能早于 {self.min_date.toString('yyyy-MM-dd')}")
               elif self.max_date and date > self.max_date:
                   self.date_picker.setDate(self.max_date)
                   self.selected_date_label.setText(f"日期不能晚于 {self.max_date.toString('yyyy-MM-dd')}")
               else:
                   date_str = date.toString("yyyy-MM-dd")
                   self.selected_date_label.setText(f"已选择: {date_str}")
           else:
               self.selected_date_label.setText("未选择日期")
       
       def set_min_date(self):
           """设置最小日期"""
           current_date = self.date_picker.date
           if current_date.isValid():
               self.min_date = current_date.addDays(-7)
               self.update_range_display()
               self.on_date_changed(current_date)
       
       def set_max_date(self):
           """设置最大日期"""
           current_date = self.date_picker.date
           if current_date.isValid():
               self.max_date = current_date.addDays(7)
               self.update_range_display()
               self.on_date_changed(current_date)
       
       def clear_range(self):
           """清除范围限制"""
           self.min_date = None
           self.max_date = None
           self.update_range_display()
           self.selected_date_label.setText("已清除日期范围限制")
       
       def update_range_display(self):
           """更新范围显示"""
           if self.min_date and self.max_date:
               range_text = f"日期范围: {self.min_date.toString('yyyy-MM-dd')} 到 {self.max_date.toString('yyyy-MM-dd')}"
           elif self.min_date:
               range_text = f"最小日期: {self.min_date.toString('yyyy-MM-dd')}"
           elif self.max_date:
               range_text = f"最大日期: {self.max_date.toString('yyyy-MM-dd')}"
           else:
               range_text = "日期范围: 无限制"
           
           self.range_label.setText(range_text)

最佳实践
--------

1. **格式选择** - 根据用户地区选择合适的日期格式
2. **范围验证** - 实现日期范围的有效性验证
3. **用户体验** - 提供快捷日期选择功能
4. **国际化** - 支持多语言的月份和日期显示
5. **性能优化** - 避免频繁的日期更新操作

注意事项
--------

- 日期格式需要根据用户习惯进行选择
- 闰年二月的天数会自动调整
- 不同地区的月份显示可能不同
- 日期验证需要在应用层面进行
- 自定义格式化器需要正确处理编码和解码

相关模块
--------

- :doc:`components.date_time.calendar_picker` - 日历选择器
- :doc:`components.date_time.calendar_view` - 日历视图
- :doc:`components.widgets.picker_base` - 选择器基类
