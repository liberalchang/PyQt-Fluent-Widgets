ComboBox 下拉框控件模块
=======================

ComboBox 模块提供Fluent Design风格的下拉框控件，支持标准下拉框和可编辑下拉框两种模式。该模块实现了现代化的下拉框样式，提供流畅的动画效果和丰富的交互功能。

主要功能
--------

- **两种模式** - 支持标准下拉框和可编辑下拉框
- **图标支持** - 下拉项支持图标显示
- **用户数据** - 支持为每个项设置自定义数据
- **动画效果** - 提供平滑的下拉/收起动画
- **占位文本** - 支持占位符文本显示
- **项管理** - 完整的增删改查功能
- **信号机制** - 丰富的状态变化信号

核心组件
--------

ComboBox
~~~~~~~~

标准下拉框控件，提供选择功能，不可直接编辑文本。

.. code-block:: python

   from qfluentwidgets.components.widgets.combo_box import ComboBox
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建下拉框
   combo_box = ComboBox(parent=parent)
   
   # 添加选项
   combo_box.addItem("选项1")
   combo_box.addItem("选项2", FIF.DOWNLOAD)  # 带图标
   combo_box.addItem("选项3", userData="custom_data")
   
   # 设置占位文本
   combo_box.setPlaceholderText("请选择一个选项")
   
   # 连接信号
   combo_box.currentIndexChanged.connect(self.on_index_changed)
   combo_box.textActivated.connect(self.on_text_activated)

**构造函数：**
- ``ComboBox(parent: QWidget = None)``

**主要方法：**
- ``addItem(text: str, icon=None, userData=None)`` - 添加选项
- ``addItems(texts: Iterable[str])`` - 批量添加选项
- ``removeItem(index: int)`` - 移除选项
- ``clear()`` - 清空所有选项
- ``setCurrentIndex(index: int)`` - 设置当前选中索引
- ``setCurrentText(text: str)`` - 设置当前选中文本
- ``setPlaceholderText(text: str)`` - 设置占位文本
- ``findText(text: str)`` - 查找文本对应的索引
- ``findData(data)`` - 查找数据对应的索引
- ``count()`` - 获取选项数量
- ``currentIndex()`` - 获取当前选中索引
- ``currentText()`` - 获取当前选中文本
- ``currentData()`` - 获取当前选中数据

**项操作方法：**
- ``setItemText(index: int, text: str)`` - 设置项文本
- ``setItemIcon(index: int, icon)`` - 设置项图标
- ``setItemData(index: int, value)`` - 设置项数据
- ``setItemEnabled(index: int, isEnabled: bool)`` - 设置项启用状态
- ``itemText(index: int)`` - 获取项文本
- ``itemIcon(index: int)`` - 获取项图标
- ``itemData(index: int)`` - 获取项数据

**信号：**
- ``currentIndexChanged(index: int)`` - 当前索引变化时发出
- ``currentTextChanged(text: str)`` - 当前文本变化时发出
- ``activated(index: int)`` - 项被激活时发出
- ``textActivated(text: str)`` - 文本被激活时发出

EditableComboBox
~~~~~~~~~~~~~~~~

可编辑下拉框控件，允许用户直接输入文本或从下拉列表中选择。

.. code-block:: python

   from qfluentwidgets.components.widgets.combo_box import EditableComboBox
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建可编辑下拉框
   editable_combo = EditableComboBox(parent=parent)
   
   # 添加预设选项
   editable_combo.addItem("预设选项1")
   editable_combo.addItem("预设选项2", FIF.FOLDER)
   
   # 设置占位文本
   editable_combo.setPlaceholderText("输入或选择选项")
   
   # 连接信号
   editable_combo.currentIndexChanged.connect(self.on_index_changed)
   editable_combo.textChanged.connect(self.on_text_changed)
   editable_combo.returnPressed.connect(self.on_return_pressed)

**构造函数：**
- ``EditableComboBox(parent: QWidget = None)``

**特点：**
- 继承自LineEdit，支持文本编辑
- 输入新文本后按回车可自动添加为新选项
- 支持自动完成功能
- 保留标准ComboBox的所有功能

**特殊信号：**
- ``textChanged(text: str)`` - 文本变化时发出（继承自LineEdit）
- ``returnPressed`` - 回车键按下时发出（继承自LineEdit）

ComboItem
~~~~~~~~~

下拉框项数据类，封装了选项的文本、图标、用户数据和启用状态。

.. code-block:: python

   from qfluentwidgets.components.widgets.combo_box import ComboItem
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建下拉框项（通常不需要直接使用）
   item = ComboItem(
       text="选项文本",
       icon=FIF.SETTING,
       userData="custom_data",
       isEnabled=True
   )

**构造函数：**
- ``ComboItem(text: str, icon=None, userData=None, isEnabled=True)``

**属性：**
- ``text`` - 选项文本
- ``icon`` - 选项图标
- ``userData`` - 用户自定义数据
- ``isEnabled`` - 是否启用

ComboBoxBase
~~~~~~~~~~~~

下拉框基类，提供核心功能和数据管理。

.. code-block:: python

   from qfluentwidgets.components.widgets.combo_box import ComboBoxBase
   
   # 基类通常不直接使用，而是通过ComboBox或EditableComboBox使用
   # 提供了所有下拉框的核心功能

**主要功能：**
- 选项数据管理
- 索引和文本操作
- 下拉菜单控制
- 信号发射机制

ComboBoxMenu
~~~~~~~~~~~~

下拉框菜单控件，继承自RoundMenu，提供下拉选项的显示界面。

.. code-block:: python

   from qfluentwidgets.components.widgets.combo_box import ComboBoxMenu
   
   # 菜单类通常不需要直接使用，由ComboBox自动创建和管理
   # 提供了下拉选项的显示和交互功能

**特点：**
- 支持下拉和上拉两种动画方向
- 自动调整大小和位置
- 支持最大可见项数量限制
- 提供选中项指示器

使用示例
--------

基础使用示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
   from qfluentwidgets.components.widgets.combo_box import ComboBox, EditableComboBox
   from qfluentwidgets import FluentIcon as FIF
   
   class ComboBoxDemo(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 标准下拉框
           self.standard_combo = ComboBox(self)
           self.standard_combo.setPlaceholderText("选择编程语言")
           
           # 添加带图标的选项
           languages = [
               ("Python", FIF.CODE),
               ("JavaScript", FIF.JAVASCRIPT),
               ("C++", FIF.CPP),
               ("Java", FIF.JAVA)
           ]
           
           for text, icon in languages:
               self.standard_combo.addItem(text, icon)
           
           # 可编辑下拉框
           self.editable_combo = EditableComboBox(self)
           self.editable_combo.setPlaceholderText("输入或选择框架")
           
           frameworks = ["React", "Vue", "Angular", "Django", "Flask"]
           self.editable_combo.addItems(frameworks)
           
           # 状态显示标签
           self.status_label = QLabel("请选择选项", self)
           
           # 连接信号
           self.standard_combo.currentIndexChanged.connect(self.on_standard_changed)
           self.editable_combo.currentIndexChanged.connect(self.on_editable_changed)
           
           # 添加到布局
           layout.addWidget(QLabel("标准下拉框："))
           layout.addWidget(self.standard_combo)
           layout.addWidget(QLabel("可编辑下拉框："))
           layout.addWidget(self.editable_combo)
           layout.addWidget(self.status_label)
           
       def on_standard_changed(self, index):
           text = self.standard_combo.currentText()
           data = self.standard_combo.currentData()
           self.status_label.setText(f"选择了: {text} (索引: {index})")
           
       def on_editable_changed(self, index):
           text = self.editable_combo.currentText()
           self.status_label.setText(f"可编辑框选择: {text} (索引: {index})")
   
   if __name__ == "__main__":
       app = QApplication(sys.argv)
       window = ComboBoxDemo()
       window.show()
       sys.exit(app.exec())

高级功能示例：

.. code-block:: python

   from PySide6.QtCore import Qt
   
   class AdvancedComboBoxDemo(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 创建带用户数据的下拉框
           self.combo = ComboBox(self)
           
           # 添加复杂选项
           users = [
               ("张三", FIF.PEOPLE, {"id": 1, "age": 25}),
               ("李四", FIF.PEOPLE, {"id": 2, "age": 30}),
               ("王五", FIF.PEOPLE, {"id": 3, "age": 28})
           ]
           
           for name, icon, data in users:
               self.combo.addItem(name, icon, data)
           
           # 动态管理选项
           self.add_btn = QPushButton("添加选项", self)
           self.remove_btn = QPushButton("移除当前", self)
           self.disable_btn = QPushButton("禁用当前", self)
           
           # 连接信号
           self.combo.activated.connect(self.on_activated)
           self.add_btn.clicked.connect(self.add_item)
           self.remove_btn.clicked.connect(self.remove_item)
           self.disable_btn.clicked.connect(self.toggle_item)
           
           # 添加到布局
           layout.addWidget(self.combo)
           layout.addWidget(self.add_btn)
           layout.addWidget(self.remove_btn)
           layout.addWidget(self.disable_btn)
           
       def on_activated(self, index):
           data = self.combo.currentData()
           if data:
               print(f"用户ID: {data['id']}, 年龄: {data['age']}")
               
       def add_item(self):
           # 动态添加选项
           text = f"新选项{self.combo.count() + 1}"
           self.combo.addItem(text, FIF.ADD)
           
       def remove_item(self):
           # 移除当前选项
           index = self.combo.currentIndex()
           if index >= 0:
               self.combo.removeItem(index)
               
       def toggle_item(self):
           # 切换当前选项的启用状态
           index = self.combo.currentIndex()
           if index >= 0:
               current_enabled = self.combo.items[index].isEnabled
               self.combo.setItemEnabled(index, not current_enabled)

动态数据管理示例：

.. code-block:: python

   class DynamicComboBox(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 创建下拉框
           self.combo = ComboBox(self)
           self.combo.setPlaceholderText("选择城市")
           
           # 初始化数据
           self.load_cities()
           
           # 搜索框
           from qfluentwidgets.components.widgets.line_edit import LineEdit
           self.search_box = LineEdit(self)
           self.search_box.setPlaceholderText("搜索城市...")
           self.search_box.textChanged.connect(self.filter_cities)
           
           layout.addWidget(self.search_box)
           layout.addWidget(self.combo)
           
       def load_cities(self):
           """加载城市数据"""
           cities = [
               ("北京", FIF.LOCATION),
               ("上海", FIF.LOCATION),
               ("广州", FIF.LOCATION),
               ("深圳", FIF.LOCATION),
               ("杭州", FIF.LOCATION),
               ("成都", FIF.LOCATION),
               ("武汉", FIF.LOCATION),
               ("西安", FIF.LOCATION)
           ]
           
           for city, icon in cities:
               self.combo.addItem(city, icon)
               
       def filter_cities(self, text):
           """过滤城市"""
           if not text:
               self.load_cities()
               return
               
           # 保存当前选择
           current_text = self.combo.currentText()
           
           # 清空并重新添加匹配项
           self.combo.clear()
           
           cities = ["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉", "西安"]
           for city in cities:
               if text.lower() in city.lower():
                   self.combo.addItem(city, FIF.LOCATION)
                   
           # 恢复选择
           if current_text:
               index = self.combo.findText(current_text)
               if index >= 0:
                   self.combo.setCurrentIndex(index)

样式自定义
----------

可以通过样式表自定义下拉框的外观：

.. code-block:: python

   # 自定义ComboBox样式
   combo_box = ComboBox()
   combo_box.setStyleSheet("""
       ComboBox {
           background-color: rgba(255, 255, 255, 0.1);
           border: 1px solid rgba(255, 255, 255, 0.2);
           border-radius: 6px;
           padding: 6px 12px;
           font-size: 14px;
       }
       ComboBox:hover {
           background-color: rgba(255, 255, 255, 0.15);
           border-color: rgba(255, 255, 255, 0.3);
       }
       ComboBox:pressed {
           background-color: rgba(255, 255, 255, 0.2);
       }
       ComboBox[isPlaceholderText="true"] {
           color: rgba(255, 255, 255, 0.6);
       }
   """)

设置最大可见项数量：

.. code-block:: python

   # 限制下拉菜单最大显示项数
   combo_box.setMaxVisibleItems(5)

注意事项
--------

1. **内存管理** - 下拉菜单会在关闭时自动销毁，但要注意循环引用
2. **性能考虑** - 大量选项时建议使用 ``setMaxVisibleItems()`` 限制显示数量
3. **数据一致性** - 修改项数据时注意同步更新相关状态
4. **信号处理** - 注意区分 ``currentIndexChanged`` 和 ``activated`` 信号的触发时机
5. **可编辑模式** - EditableComboBox会自动添加新输入的文本作为选项
6. **图标支持** - 支持多种图标类型：字符串路径、QIcon、FluentIconBase
7. **平台差异** - 不同平台下的菜单行为可能略有不同

相关组件
--------

- :doc:`line_edit` - 行编辑控件，EditableComboBox的基类
- :doc:`menu` - 菜单控件，ComboBoxMenu的基类
- :doc:`button` - 按钮控件，ComboBox的基类
- :doc:`icon` - 图标控件，用于下拉项图标显示
