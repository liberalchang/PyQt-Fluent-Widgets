Expand Layout 扩展布局模块
=============================

Expand Layout 模块提供垂直扩展布局功能，支持动态高度调整。
该模块允许子控件在垂直方向上自动扩展，根据内容动态调整布局高度。

主要功能
--------

- **垂直扩展** - 支持子控件在垂直方向上的自动扩展
- **动态高度** - 根据子控件内容动态调整布局高度
- **事件过滤** - 监听子控件的尺寸变化事件
- **最小尺寸** - 自动计算布局的最小尺寸要求
- **间距管理** - 支持子控件间的间距设置

核心组件
--------

ExpandLayout
~~~~~~~~~~~~

扩展布局，提供垂直方向的自动扩展功能。

.. code-block:: python

   from qfluentwidgets.components.layout.expand_layout import ExpandLayout
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QWidget
   
   # 创建扩展布局
   expand_layout = ExpandLayout()
   
   # 添加子控件
   label1 = Label("标签1")
   label2 = Label("标签2")
   button1 = PushButton("按钮1")
   
   expand_layout.addWidget(label1)
   expand_layout.addWidget(label2)
   expand_layout.addWidget(button1)
   
   # 设置到父控件
   widget = QWidget()
   widget.setLayout(expand_layout)

**主要方法：**
- ``addWidget()`` - 添加子控件
- ``addItem()`` - 添加布局项
- ``heightForWidth()`` - 根据宽度计算高度
- ``minimumSize()`` - 获取最小尺寸

实际应用
--------

基本扩展布局
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.layout.expand_layout import ExpandLayout
   from qfluentwidgets import CardWidget, Label, PushButton, LineEdit
   from PySide6.QtWidgets import QVBoxLayout, QWidget
   
   class BasicExpandLayoutWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
       
       def setup_ui(self):
           # 创建主布局
           main_layout = QVBoxLayout()
           
           # 创建扩展布局容器
           expand_widget = QWidget()
           expand_widget.setStyleSheet("background-color: #f0f0f0; border-radius: 8px;")
           
           # 创建扩展布局
           self.expand_layout = ExpandLayout()
           expand_widget.setLayout(self.expand_layout)
           
           # 添加子控件
           title_label = Label("扩展布局示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           content_label = Label("这是一个扩展布局的示例内容。")
           content_label.setStyleSheet("padding: 10px;")
           content_label.setWordWrap(True)
           
           input_label = Label("输入框:")
           input_label.setStyleSheet("padding: 10px;")
           
           input_field = LineEdit()
           input_field.setPlaceholderText("请输入内容...")
           input_field.setStyleSheet("margin: 0 10px 10px 10px;")
           
           button = PushButton("提交")
           button.setStyleSheet("margin: 10px;")
           
           # 添加到扩展布局
           self.expand_layout.addWidget(title_label)
           self.expand_layout.addWidget(content_label)
           self.expand_layout.addWidget(input_label)
           self.expand_layout.addWidget(input_field)
           self.expand_layout.addWidget(button)
           
           # 设置间距
           self.expand_layout.setSpacing(5)
           self.expand_layout.setContentsMargins(10, 10, 10, 10)
           
           # 添加到主布局
           main_layout.addWidget(expand_widget)
           self.setLayout(main_layout)

动态内容扩展布局
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.layout.expand_layout import ExpandLayout
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QWidget, QTextEdit
   
   class DynamicExpandLayoutWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           # 创建主布局
           main_layout = QVBoxLayout()
           
           # 控制按钮
           button_layout = QVBoxLayout()
           
           self.add_text_btn = PushButton("添加文本")
           self.add_label_btn = PushButton("添加标签")
           self.clear_btn = PushButton("清空内容")
           
           button_layout.addWidget(self.add_text_btn)
           button_layout.addWidget(self.add_label_btn)
           button_layout.addWidget(self.clear_btn)
           
           # 扩展布局容器
           self.expand_widget = QWidget()
           self.expand_widget.setStyleSheet("background-color: #f8f9fa; border-radius: 8px;")
           
           # 创建扩展布局
           self.expand_layout = ExpandLayout()
           self.expand_widget.setLayout(self.expand_layout)
           
           # 设置间距和边距
           self.expand_layout.setSpacing(8)
           self.expand_layout.setContentsMargins(15, 15, 15, 15)
           
           # 添加初始内容
           self.add_initial_content()
           
           # 布局
           content_layout = QHBoxLayout()
           content_layout.addLayout(button_layout)
           content_layout.addWidget(self.expand_widget, 1)
           
           main_layout.addLayout(content_layout)
           self.setLayout(main_layout)
       
       def setup_connections(self):
           """设置连接"""
           self.add_text_btn.clicked.connect(self.add_text_content)
           self.add_label_btn.clicked.connect(self.add_label_content)
           self.clear_btn.clicked.connect(self.clear_content)
       
       def add_initial_content(self):
           """添加初始内容"""
           title = Label("动态扩展布局")
           title.setStyleSheet("font-size: 18px; font-weight: bold; color: #333;")
           
           desc = Label("这个布局会根据内容自动调整高度。")
           desc.setStyleSheet("color: #666; padding: 5px 0;")
           
           self.expand_layout.addWidget(title)
           self.expand_layout.addWidget(desc)
       
       def add_text_content(self):
           """添加文本内容"""
           text_edit = QTextEdit()
           text_edit.setMaximumHeight(100)
           text_edit.setPlaceholderText("输入多行文本...")
           text_edit.setStyleSheet("border: 1px solid #ddd; border-radius: 4px; padding: 8px;")
           
           self.expand_layout.addWidget(text_edit)
           self.expand_widget.updateGeometry()
       
       def add_label_content(self):
           """添加标签内容"""
           import random
           
           colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"]
           texts = ["重要信息", "注意事项", "提示内容", "警告信息", "成功状态"]
           
           color = random.choice(colors)
           text = random.choice(texts)
           
           label = Label(f"📌 {text}")
           label.setStyleSheet(f"""
               background-color: {color}; 
               color: white; 
               padding: 8px 12px; 
               border-radius: 4px;
               margin: 2px 0;
           """)
           
           self.expand_layout.addWidget(label)
           self.expand_widget.updateGeometry()
       
       def clear_content(self):
           """清空内容"""
           while self.expand_layout.count() > 0:
               item = self.expand_layout.takeAt(0)
               if item and item.widget():
                   item.widget().deleteLater()
           
           self.add_initial_content()
           self.expand_widget.updateGeometry()

高级用法
--------

自定义扩展布局
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.layout.expand_layout import ExpandLayout
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QWidget, QFrame
   from PySide6.QtGui import QColor
   
   class CustomExpandLayout(ExpandLayout):
       """自定义扩展布局"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           self.widget_colors = {}
           self.alternate_colors = [QColor("#f8f9fa"), QColor("#ffffff")]
       
       def addWidget(self, widget):
           """重写添加控件方法"""
           super().addWidget(widget)
           
           # 为控件设置交替背景色
           index = len(self.__widgets) - 1
           color = self.alternate_colors[index % len(self.alternate_colors)]
           widget.setStyleSheet(f"background-color: {color.name()}; border-radius: 4px; padding: 8px;")
       
       def __doLayout(self, rect, move):
           """重写布局方法"""
           margin = self.contentsMargins()
           x = rect.x() + margin.left()
           y = rect.y() + margin.top()
           width = rect.width() - margin.left() - margin.right()
           
           for i, w in enumerate(self.__widgets):
               if w.isHidden():
                   continue
               
               # 添加间距
               y += (i > 0) * self.spacing()
               
               # 添加卡片效果
               card_margin = 4
               card_rect = QRect(
                   x + card_margin, 
                   y + card_margin, 
                   width - 2 * card_margin, 
                   w.height()
               )
               
               if move:
                   w.setGeometry(card_rect)
               
               y += w.height() + 2 * card_margin
           
           return y - rect.y()
   
   class CustomExpandLayoutWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
       
       def setup_ui(self):
           # 创建主布局
           main_layout = QVBoxLayout()
           
           # 创建自定义扩展布局容器
           expand_widget = QWidget()
           expand_widget.setStyleSheet("background-color: #e9ecef; border-radius: 8px;")
           
           # 创建自定义扩展布局
           custom_layout = CustomExpandLayout()
           expand_widget.setLayout(custom_layout)
           
           # 添加内容
           items = [
               ("📋 任务列表", "待办事项管理"),
               ("📈 数据统计", "图表和数据展示"),
               ("⚙️ 系统设置", "应用配置选项"),
               ("🔔 通知中心", "消息和提醒管理"),
               ("👤 用户资料", "个人信息设置")
           ]
           
           for icon, title in items:
               content_widget = QWidget()
               content_layout = QVBoxLayout(content_widget)
               
               # 标题
               title_label = Label(f"{icon} {title}")
               title_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #333;")
               
               # 描述
               desc_label = Label("点击查看详细信息")
               desc_label.setStyleSheet("color: #666; font-size: 12px;")
               
               content_layout.addWidget(title_label)
               content_layout.addWidget(desc_label)
               content_layout.setContentsMargins(8, 4, 8, 4)
               
               custom_layout.addWidget(content_widget)
           
           # 设置布局属性
           custom_layout.setSpacing(2)
           custom_layout.setContentsMargins(8, 8, 8, 8)
           
           main_layout.addWidget(expand_widget)
           self.setLayout(main_layout)

响应式扩展布局
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.layout.expand_layout import ExpandLayout
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout, QWidget
   from PySide6.QtCore import QTimer
   
   class ResponsiveExpandLayoutWidget(CardWidget):
       """响应式扩展布局"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_timer()
       
       def setup_ui(self):
           # 创建主布局
           main_layout = QVBoxLayout()
           
           # 扩展布局容器
           self.expand_widget = QWidget()
           self.expand_widget.setStyleSheet("background-color: #f8f9fa; border-radius: 8px;")
           
           # 创建扩展布局
           self.expand_layout = ExpandLayout()
           self.expand_widget.setLayout(self.expand_layout)
           
           # 添加响应式内容
           self.add_responsive_content()
           
           main_layout.addWidget(self.expand_widget)
           self.setLayout(main_layout)
       
       def add_responsive_content(self):
           """添加响应式内容"""
           # 标题
           title = Label("响应式扩展布局")
           title.setStyleSheet("font-size: 18px; font-weight: bold; color: #333; padding: 10px;")
           
           # 状态信息
           self.status_label = Label("状态: 正常")
           self.status_label.setStyleSheet("color: #666; padding: 5px 10px;")
           
           # 内容区域
           self.content_label = Label("内容会根据窗口大小自动调整")
           self.content_label.setStyleSheet("color: #666; padding: 10px;")
           self.content_label.setWordWrap(True)
           
           # 添加到布局
           self.expand_layout.addWidget(title)
           self.expand_layout.addWidget(self.status_label)
           self.expand_layout.addWidget(self.content_label)
           
           # 设置布局属性
           self.expand_layout.setSpacing(8)
           self.expand_layout.setContentsMargins(15, 15, 15, 15)
       
       def setup_timer(self):
           """设置定时器用于演示响应式效果"""
           self.timer = QTimer()
           self.timer.timeout.connect(self.update_content)
           self.timer.start(3000)  # 每3秒更新一次
       
       def update_content(self):
           """更新内容以演示响应式效果"""
           import random
           
           states = ["状态: 正常", "状态: 警告", "状态: 错误", "状态: 更新中"]
           contents = [
               "内容会根据窗口大小自动调整布局高度。",
               "这是一个动态更新的内容示例，展示扩展布局的响应能力。",
               "扩展布局能够根据子控件的内容变化自动调整整体高度。",
               "当子控件的尺寸发生变化时，布局会自动重新计算和调整。"
           ]
           
           # 随机更新状态和内容
           self.status_label.setText(random.choice(states))
           self.content_label.setText(random.choice(contents))
           
           # 根据内容状态设置不同颜色
           if "警告" in self.status_label.text():
               self.status_label.setStyleSheet("color: #f39c12; padding: 5px 10px;")
           elif "错误" in self.status_label.text():
               self.status_label.setStyleSheet("color: #e74c3c; padding: 5px 10px;")
           elif "更新" in self.status_label.text():
               self.status_label.setStyleSheet("color: #3498db; padding: 5px 10px;")
           else:
               self.status_label.setStyleSheet("color: #27ae60; padding: 5px 10px;")
           
           # 触发布局更新
           self.expand_widget.updateGeometry()

最佳实践
--------

1. **动态内容** - 适用于内容高度会变化的场景
2. **事件监听** - 正确处理子控件的尺寸变化事件
3. **性能优化** - 避免频繁的布局重计算
4. **间距管理** - 合理设置控件间的间距
5. **最小尺寸** - 确保布局有合适的最小尺寸

注意事项
--------

- 扩展布局主要在垂直方向上扩展
- 子控件的尺寸变化会触发布局重计算
- 需要合理设置间距和边距
- 大量子控件可能影响性能
- 布局的高度会根据内容自动调整

相关模块
--------

- :doc:`components.layout.flow_layout` - 流式布局
- :doc:`components.layout.splitter` - 分割器布局
- :doc:`components.layout.v_box_layout` - 垂直布局
