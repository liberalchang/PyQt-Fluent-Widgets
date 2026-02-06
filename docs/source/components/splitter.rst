Splitter 分割器模块
=====================

Splitter 模块提供Fluent Design风格的分割器组件，支持面板折叠和展开功能。
该模块提供现代化的分割器界面，包含主题色手柄、悬停效果和折叠按钮等特性。

主要功能
--------

- **分割面板** - 支持水平和垂直方向的面板分割
- **折叠功能** - 支持面板的折叠和展开操作
- **主题样式** - 提供Fluent Design风格的主题色手柄
- **悬停效果** - 支持鼠标悬停时的宽度变化动画
- **按钮交互** - 集成折叠按钮提供便捷操作

核心组件
--------

FluentSplitter
~~~~~~~~~~~~~~

Fluent Design风格的分割器，提供完整的分割功能。

.. code-block:: python

   from qfluentwidgets.components.layout.splitter import FluentSplitter
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QWidget
   from PySide6.QtCore import Qt
   
   # 创建水平分割器
   splitter = FluentSplitter(Qt.Horizontal)
   
   # 添加子控件
   left_widget = QWidget()
   right_widget = QWidget()
   
   splitter.addWidget(left_widget)
   splitter.addWidget(right_widget)
   
   # 设置初始尺寸比例
   splitter.setSizes([300, 200])

**主要方法：**
- ``addWidget()`` - 添加子控件
- ``setSizes()`` - 设置面板尺寸
- ``setOrientation()`` - 设置分割方向
- ``_toggleCollapse()`` - 切换面板折叠状态

FluentSplitterHandle
~~~~~~~~~~~~~~~~~~~~

分割器手柄，提供主题色样式和折叠按钮。

.. code-block:: python

   from qfluentwidgets.components.layout.splitter import FluentSplitterHandle
   from PySide6.QtCore import Qt
   
   # 创建分割器手柄
   handle = FluentSplitterHandle(Qt.Horizontal, parent_splitter)
   
   # 访问折叠按钮
   collapse_button = handle.collapseButton

CollapseButton
~~~~~~~~~~~~~~

分割器手柄上的折叠按钮。

.. code-block:: python

   from qfluentwidgets.components.layout.splitter import CollapseButton
   from PySide6.QtCore import Qt
   
   # 创建折叠按钮
   collapse_button = CollapseButton(Qt.Horizontal)
   
   # 设置折叠状态
   collapse_button.setCollapsed(True)

实际应用
--------

基本分割器
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.layout.splitter import FluentSplitter
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout, QWidget
   from PySide6.QtCore import Qt
   
   class BasicSplitterWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
       
       def setup_ui(self):
           # 创建主布局
           main_layout = QVBoxLayout()
           
           # 创建水平分割器
           self.horizontal_splitter = FluentSplitter(Qt.Horizontal)
           
           # 左侧面板
           left_panel = QWidget()
           left_panel.setStyleSheet("background-color: #e3f2fd; border-radius: 8px;")
           left_layout = QVBoxLayout(left_panel)
           
           left_title = Label("左侧面板")
           left_title.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           left_content = Label("这是左侧的内容区域")
           left_content.setStyleSheet("padding: 10px;")
           
           left_layout.addWidget(left_title)
           left_layout.addWidget(left_content)
           
           # 右侧面板
           right_panel = QWidget()
           right_panel.setStyleSheet("background-color: #f3e5f5; border-radius: 8px;")
           right_layout = QVBoxLayout(right_panel)
           
           right_title = Label("右侧面板")
           right_title.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           right_content = Label("这是右侧的内容区域")
           right_content.setStyleSheet("padding: 10px;")
           
           right_layout.addWidget(right_title)
           right_layout.addWidget(right_content)
           
           # 添加到分割器
           self.horizontal_splitter.addWidget(left_panel)
           self.horizontal_splitter.addWidget(right_panel)
           
           # 设置初始尺寸
           self.horizontal_splitter.setSizes([250, 250])
           
           main_layout.addWidget(self.horizontal_splitter)
           self.setLayout(main_layout)

垂直分割器
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.layout.splitter import FluentSplitter
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout, QWidget
   from PySide6.QtCore import Qt
   
   class VerticalSplitterWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
       
       def setup_ui(self):
           # 创建主布局
           main_layout = QVBoxLayout()
           
           # 创建垂直分割器
           self.vertical_splitter = FluentSplitter(Qt.Vertical)
           
           # 上方面板
           top_panel = QWidget()
           top_panel.setStyleSheet("background-color: #e8f5e8; border-radius: 8px;")
           top_layout = QVBoxLayout(top_panel)
           
           top_title = Label("上方面板")
           top_title.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           top_content = Label("这是上方的内容区域")
           top_content.setStyleSheet("padding: 10px;")
           
           top_layout.addWidget(top_title)
           top_layout.addWidget(top_content)
           
           # 下方面板
           bottom_panel = QWidget()
           bottom_panel.setStyleSheet("background-color: #fff3e0; border-radius: 8px;")
           bottom_layout = QVBoxLayout(bottom_panel)
           
           bottom_title = Label("下方面板")
           bottom_title.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           bottom_content = Label("这是下方的内容区域")
           bottom_content.setStyleSheet("padding: 10px;")
           
           bottom_layout.addWidget(bottom_title)
           bottom_layout.addWidget(bottom_content)
           
           # 添加到分割器
           self.vertical_splitter.addWidget(top_panel)
           self.vertical_splitter.addWidget(bottom_panel)
           
           # 设置初始尺寸
           self.vertical_splitter.setSizes([200, 200])
           
           main_layout.addWidget(self.vertical_splitter)
           self.setLayout(main_layout)

高级用法
--------

多面板分割器
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.layout.splitter import FluentSplitter
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout
   from PySide6.QtCore import Qt
   
   class MultiPanelSplitterWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           # 创建主布局
           main_layout = QVBoxLayout()
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           self.collapse_left_btn = PushButton("折叠左侧")
           self.expand_all_btn = PushButton("展开全部")
           self.collapse_right_btn = PushButton("折叠右侧")
           
           button_layout.addWidget(self.collapse_left_btn)
           button_layout.addWidget(self.expand_all_btn)
           button_layout.addWidget(self.collapse_right_btn)
           
           # 创建三面板分割器
           self.splitter = FluentSplitter(Qt.Horizontal)
           
           # 左侧面板
           left_panel = self.create_panel("左侧面板", "#e3f2fd")
           
           # 中间面板
           center_panel = self.create_panel("中间面板", "#f3e5f5")
           
           # 右侧面板
           right_panel = self.create_panel("右侧面板", "#e8f5e8")
           
           # 添加到分割器
           self.splitter.addWidget(left_panel)
           self.splitter.addWidget(center_panel)
           self.splitter.addWidget(right_panel)
           
           # 设置初始尺寸
           self.splitter.setSizes([200, 300, 200])
           
           main_layout.addLayout(button_layout)
           main_layout.addWidget(self.splitter)
           self.setLayout(main_layout)
       
       def create_panel(self, title, color):
           """创建面板"""
           panel = QWidget()
           panel.setStyleSheet(f"background-color: {color}; border-radius: 8px;")
           
           layout = QVBoxLayout(panel)
           
           title_label = Label(title)
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           content_label = Label(f"这是{title}的内容区域")
           content_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(content_label)
           
           return panel
       
       def setup_connections(self):
           """设置连接"""
           self.collapse_left_btn.clicked.connect(self.collapse_left_panel)
           self.expand_all_btn.clicked.connect(self.expand_all_panels)
           self.collapse_right_btn.clicked.connect(self.collapse_right_panel)
       
       def collapse_left_panel(self):
           """折叠左侧面板"""
           self.splitter._toggleCollapse(1)  # 折叠第一个手柄左侧的面板
       
       def expand_all_panels(self):
           """展开所有面板"""
           sizes = self.splitter.sizes()
           for i, size in enumerate(sizes):
               if size == 0:
                   # 展开第i个面板
                   self.splitter._toggleCollapse(i)
       
       def collapse_right_panel(self):
           """折叠右侧面板"""
           self.splitter._toggleCollapse(2)  # 折叠第二个手柄左侧的面板

嵌套分割器
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.layout.splitter import FluentSplitter
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout, QWidget
   from PySide6.QtCore import Qt
   
   class NestedSplitterWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
       
       def setup_ui(self):
           # 创建主布局
           main_layout = QVBoxLayout()
           
           # 创建主分割器（水平）
           main_splitter = FluentSplitter(Qt.Horizontal)
           
           # 左侧面板
           left_panel = self.create_panel("左侧面板", "#e3f2fd")
           
           # 右侧嵌套分割器（垂直）
           right_splitter = FluentSplitter(Qt.Vertical)
           
           # 右上方面板
           top_right_panel = self.create_panel("右上方面板", "#f3e5f5")
           
           # 右下方面板
           bottom_right_panel = self.create_panel("右下方面板", "#e8f5e8")
           
           # 构建嵌套结构
           right_splitter.addWidget(top_right_panel)
           right_splitter.addWidget(bottom_right_panel)
           right_splitter.setSizes([150, 150])
           
           main_splitter.addWidget(left_panel)
           main_splitter.addWidget(right_splitter)
           main_splitter.setSizes([250, 350])
           
           main_layout.addWidget(main_splitter)
           self.setLayout(main_layout)
       
       def create_panel(self, title, color):
           """创建面板"""
           panel = QWidget()
           panel.setStyleSheet(f"background-color: {color}; border-radius: 8px;")
           
           layout = QVBoxLayout(panel)
           
           title_label = Label(title)
           title_label.setStyleSheet("font-size: 14px; font-weight: bold; padding: 8px;")
           
           content_label = Label(f"这是{title}的内容")
           content_label.setStyleSheet("padding: 8px;")
           
           layout.addWidget(title_label)
           layout.addWidget(content_label)
           
           return panel

动态分割器管理器
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.layout.splitter import FluentSplitter
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout
   from PySide6.QtCore import Qt
   
   class DynamicSplitterManager(CardWidget):
       """动态分割器管理器"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
           self.panel_count = 2
       
       def setup_ui(self):
           # 创建主布局
           main_layout = QVBoxLayout()
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           self.add_panel_btn = PushButton("添加面板")
           self.remove_panel_btn = PushButton("移除面板")
           self.reset_btn = PushButton("重置布局")
           
           button_layout.addWidget(self.add_panel_btn)
           button_layout.addWidget(self.remove_panel_btn)
           button_layout.addWidget(self.reset_btn)
           
           # 创建分割器
           self.splitter = FluentSplitter(Qt.Horizontal)
           
           # 添加初始面板
           self.add_initial_panels()
           
           main_layout.addLayout(button_layout)
           main_layout.addWidget(self.splitter)
           self.setLayout(main_layout)
       
       def add_initial_panels(self):
           """添加初始面板"""
           colors = ["#e3f2fd", "#f3e5f5"]
           titles = ["面板1", "面板2"]
           
           for title, color in zip(titles, colors):
               panel = self.create_panel(title, color)
               self.splitter.addWidget(panel)
           
           self.splitter.setSizes([200, 200])
       
       def create_panel(self, title, color):
           """创建面板"""
           panel = QWidget()
           panel.setStyleSheet(f"background-color: {color}; border-radius: 8px;")
           
           layout = QVBoxLayout(panel)
           
           title_label = Label(title)
           title_label.setStyleSheet("font-size: 14px; font-weight: bold; padding: 8px;")
           
           content_label = Label(f"这是{title}的内容")
           content_label.setStyleSheet("padding: 8px;")
           
           layout.addWidget(title_label)
           layout.addWidget(content_label)
           
           return panel
       
       def setup_connections(self):
           """设置连接"""
           self.add_panel_btn.clicked.connect(self.add_panel)
           self.remove_panel_btn.clicked.connect(self.remove_panel)
           self.reset_btn.clicked.connect(self.reset_layout)
       
       def add_panel(self):
           """添加新面板"""
           if self.splitter.count() < 5:  # 限制最大面板数
               import random
               
               colors = ["#e8f5e8", "#fff3e0", "#fce4ec", "#f1f8e9"]
               titles = [f"面板{self.panel_count + 1}"]
               
               color = random.choice(colors)
               title = titles[0]
               
               panel = self.create_panel(title, color)
               self.splitter.addWidget(panel)
               
               # 重新分配尺寸
               total_size = sum(self.splitter.sizes())
               new_size = total_size // self.splitter.count()
               sizes = [new_size] * self.splitter.count()
               self.splitter.setSizes(sizes)
               
               self.panel_count += 1
       
       def remove_panel(self):
           """移除最后一个面板"""
           if self.splitter.count() > 1:
               last_widget = self.splitter.widget(self.splitter.count() - 1)
               self.splitter.removeWidget(last_widget)
               last_widget.deleteLater()
       
       def reset_layout(self):
           """重置布局"""
           # 清空所有面板
           while self.splitter.count() > 0:
               widget = self.splitter.widget(0)
               self.splitter.removeWidget(widget)
               widget.deleteLater()
           
           # 重新添加初始面板
           self.panel_count = 2
           self.add_initial_panels()

最佳实践
--------

1. **合理布局** - 根据内容需求选择合适的分割方向
2. **尺寸管理** - 设置合理的初始尺寸比例
3. **折叠功能** - 充分利用折叠功能优化界面空间
4. **嵌套使用** - 合理使用嵌套分割器创建复杂布局
5. **性能考虑** - 避免过多的嵌套层级影响性能

注意事项
--------

- 分割器手柄支持悬停效果和折叠功能
- 折叠按钮会根据分割方向自动调整图标
- 面板折叠后会保存原始尺寸以便恢复
- 嵌套分割器需要注意层级关系
- 动态添加/移除面板时需要正确处理内存

相关模块
--------

- :doc:`components.layout.expand_layout` - 扩展布局
- :doc:`components.layout.flow_layout` - 流式布局
- :doc:`components.layout.v_box_layout` - 垂直布局
