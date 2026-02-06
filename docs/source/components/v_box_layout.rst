V Box Layout 垂直布局模块
=============================

V Box Layout 模块提供增强的垂直布局功能，支持批量操作和控件管理。
该模块继承自QVBoxLayout，提供了更便捷的控件添加、移除和管理功能。

主要功能
--------

- **垂直排列** - 支持子控件在垂直方向上的排列
- **批量添加** - 支持一次性添加多个控件
- **控件管理** - 提供控件的添加、移除和删除功能
- **自动显示** - 添加控件时自动显示
- **内存管理** - 提供安全的控件删除功能

核心组件
--------

VBoxLayout
~~~~~~~~~~

增强的垂直布局，提供便捷的控件管理功能。

.. code-block:: python

   from qfluentwidgets.components.layout.v_box_layout import VBoxLayout
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QWidget
   from PySide6.QtCore import Qt
   
   # 创建垂直布局
   v_layout = VBoxLayout(parent)
   
   # 添加单个控件
   label1 = Label("标签1")
   v_layout.addWidget(label1, stretch=0, alignment=Qt.AlignTop)
   
   # 批量添加控件
   widgets = [Label("标签2"), PushButton("按钮")]
   v_layout.addWidgets(widgets, stretch=0, alignment=Qt.AlignTop)
   
   # 设置到父控件
   widget = QWidget()
   widget.setLayout(v_layout)

**主要方法：**
- ``addWidget()`` - 添加单个控件
- ``addWidgets()`` - 批量添加控件
- ``removeWidget()`` - 移除控件但不删除
- ``deleteWidget()`` - 移除并删除控件
- ``removeAllWidget()`` - 移除所有控件

实际应用
--------

基本垂直布局
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.layout.v_box_layout import VBoxLayout
   from qfluentwidgets import CardWidget, Label, PushButton, LineEdit
   from PySide6.QtWidgets import QWidget
   from PySide6.QtCore import Qt
   
   class BasicVBoxLayoutWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
       
       def setup_ui(self):
           # 创建垂直布局
           self.v_layout = VBoxLayout(self)
           
           # 创建控件
           title_label = Label("垂直布局示例")
           title_label.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")
           
           content_label = Label("这是一个垂直布局的示例，展示了控件的垂直排列。")
           content_label.setStyleSheet("padding: 10px;")
           content_label.setWordWrap(True)
           
           input_label = Label("输入框:")
           input_label.setStyleSheet("padding: 5px 10px;")
           
           input_field = LineEdit()
           input_field.setPlaceholderText("请输入内容...")
           input_field.setStyleSheet("margin: 0 10px 10px 10px;")
           
           button = PushButton("提交")
           button.setStyleSheet("margin: 10px;")
           
           # 添加控件到布局
           self.v_layout.addWidget(title_label, stretch=0, alignment=Qt.AlignTop)
           self.v_layout.addWidget(content_label, stretch=0, alignment=Qt.AlignTop)
           self.v_layout.addWidget(input_label, stretch=0, alignment=Qt.AlignTop)
           self.v_layout.addWidget(input_field, stretch=0, alignment=Qt.AlignTop)
           self.v_layout.addWidget(button, stretch=0, alignment=Qt.AlignTop)
           
           # 设置布局属性
           self.v_layout.setSpacing(8)
           self.v_layout.setContentsMargins(15, 15, 15, 15)

批量操作布局
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.layout.v_box_layout import VBoxLayout
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QWidget, QHBoxLayout
   from PySide6.QtCore import Qt
   
   class BatchVBoxLayoutWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           # 创建主布局
           main_layout = QVBoxLayout()
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           self.add_items_btn = PushButton("添加项目")
           self.remove_last_btn = PushButton("移除最后")
           self.clear_all_btn = PushButton("清空全部")
           
           button_layout.addWidget(self.add_items_btn)
           button_layout.addWidget(self.remove_last_btn)
           button_layout.addWidget(self.clear_all_btn)
           
           # 创建垂直布局容器
           self.v_layout_widget = QWidget()
           self.v_layout_widget.setStyleSheet("background-color: #f8f9fa; border-radius: 8px;")
           
           # 创建垂直布局
           self.v_layout = VBoxLayout(self.v_layout_widget)
           self.v_layout_widget.setLayout(self.v_layout)
           
           # 设置布局属性
           self.v_layout.setSpacing(10)
           self.v_layout.setContentsMargins(15, 15, 15, 15)
           
           # 添加初始内容
           self.add_initial_items()
           
           main_layout.addLayout(button_layout)
           main_layout.addWidget(self.v_layout_widget)
           self.setLayout(main_layout)
       
       def setup_connections(self):
           """设置连接"""
           self.add_items_btn.clicked.connect(self.add_items)
           self.remove_last_btn.clicked.connect(self.remove_last_item)
           self.clear_all_btn.clicked.connect(self.clear_all_items)
       
       def add_initial_items(self):
           """添加初始项目"""
           title = Label("项目列表")
           title.setStyleSheet("font-size: 16px; font-weight: bold; color: #333;")
           
           self.v_layout.addWidget(title, stretch=0, alignment=Qt.AlignTop)
       
       def add_items(self):
           """批量添加项目"""
           import random
           
           items = [
               "重要任务", "紧急事项", "待处理项目", 
               "已完成工作", "计划中任务", "审核中项目"
           ]
           
           colors = ["#e74c3c", "#f39c12", "#3498db", "#27ae60", "#9b59b6", "#1abc9c"]
           
           # 随机选择2-3个项目
           num_items = random.randint(2, 3)
           selected_items = random.sample(items, num_items)
           
           widgets = []
           for item in selected_items:
               color = random.choice(colors)
               label = Label(f"📌 {item}")
               label.setStyleSheet(f"""
                   background-color: {color}; 
                   color: white; 
                   padding: 8px 12px; 
                   border-radius: 4px;
                   margin: 2px 0;
               """)
               widgets.append(label)
           
           # 批量添加
           self.v_layout.addWidgets(widgets, stretch=0, alignment=Qt.AlignTop)
       
       def remove_last_item(self):
           """移除最后一个项目"""
           if len(self.v_layout.widgets) > 1:  # 保留标题
               last_widget = self.v_layout.widgets[-1]
               self.v_layout.removeWidget(last_widget)
               last_widget.hide()
               last_widget.deleteLater()
       
       def clear_all_items(self):
           """清空所有项目"""
           # 移除所有控件
           self.v_layout.removeAllWidget()
           
           # 重新添加标题
           self.add_initial_items()

高级用法
--------

动态内容管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.layout.v_box_layout import VBoxLayout
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt, QTimer
   
   class DynamicVBoxLayoutWidget(CardWidget):
       """动态垂直布局管理器"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_timer()
       
       def setup_ui(self):
           # 创建主布局
           main_layout = QVBoxLayout()
           
           # 标题和状态
           title_layout = QHBoxLayout()
           
           title_label = Label("动态内容管理")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
           
           self.status_label = Label("状态: 正常")
           self.status_label.setStyleSheet("color: #666; margin-left: auto;")
           
           title_layout.addWidget(title_label)
           title_layout.addWidget(self.status_label)
           
           # 控制按钮
           control_layout = QHBoxLayout()
           
           self.add_content_btn = PushButton("添加内容")
           self.toggle_content_btn = PushButton("切换显示")
           self.cleanup_btn = PushButton("清理")
           
           control_layout.addWidget(self.add_content_btn)
           control_layout.addWidget(self.toggle_content_btn)
           control_layout.addWidget(self.cleanup_btn)
           
           # 垂直布局容器
           self.v_layout_widget = QWidget()
           self.v_layout_widget.setStyleSheet("background-color: #f8f9fa; border-radius: 8px;")
           
           # 创建垂直布局
           self.v_layout = VBoxLayout(self.v_layout_widget)
           self.v_layout_widget.setLayout(self.v_layout)
           
           # 设置布局属性
           self.v_layout.setSpacing(8)
           self.v_layout.setContentsMargins(15, 15, 15, 15)
           
           # 添加初始内容
           self.add_initial_content()
           
           main_layout.addLayout(title_layout)
           main_layout.addLayout(control_layout)
           main_layout.addWidget(self.v_layout_widget)
           self.setLayout(main_layout)
       
       def setup_timer(self):
           """设置定时器用于动态更新"""
           self.timer = QTimer()
           self.timer.timeout.connect(self.update_status)
           self.timer.start(3000)  # 每3秒更新一次
       
       def add_initial_content(self):
           """添加初始内容"""
           header = Label("内容区域")
           header.setStyleSheet("font-size: 14px; font-weight: bold; color: #333; padding: 5px;")
           
           self.v_layout.addWidget(header, stretch=0, alignment=Qt.AlignTop)
       
       def update_status(self):
           """更新状态显示"""
           count = len(self.v_layout.widgets)
           self.status_label.setText(f"项目数: {count}")
       
       def add_content(self):
           """添加动态内容"""
           import random
           
           content_types = [
               ("信息", "#3498db"),
               ("警告", "#f39c12"),
               ("成功", "#27ae60"),
               ("错误", "#e74c3c")
           ]
           
           content_type, color = random.choice(content_types)
           
           label = Label(f"📢 {content_type}: 系统消息 {random.randint(1000, 9999)}")
           label.setStyleSheet(f"""
               background-color: {color}; 
               color: white; 
               padding: 6px 10px; 
               border-radius: 4px;
               margin: 1px 0;
           """)
           
           self.v_layout.addWidget(label, stretch=0, alignment=Qt.AlignTop)
           self.update_status()
       
       def toggle_content(self):
           """切换内容显示"""
           for widget in self.v_layout.widgets[1:]:  # 跳过标题
               if widget.isVisible():
                   widget.hide()
               else:
                   widget.show()
       
       def cleanup(self):
           """清理旧内容"""
           # 保留最新的5个项目
           if len(self.v_layout.widgets) > 6:  # 标题 + 5个项目
               widgets_to_remove = self.v_layout.widgets[1:-5]  # 保留标题和最后5个项目
               
               for widget in widgets_to_remove:
                   self.v_layout.removeWidget(widget)
                   widget.hide()
                   widget.deleteLater()
               
               self.update_status()

自定义垂直布局
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.layout.v_box_layout import VBoxLayout
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QWidget, QVBoxLayout
   from PySide6.QtCore import Qt
   
   class CustomVBoxLayout(VBoxLayout):
       """自定义垂直布局"""
       
       def __init__(self, parent):
           super().__init__(parent)
           self.widget_styles = {}
           self.alternate_colors = ["#f8f9fa", "#ffffff"]
       
       def addWidget(self, widget, stretch=0, alignment=Qt.AlignTop):
           """重写添加控件方法"""
           super().addWidget(widget, stretch, alignment)
           
           # 为控件设置交替背景色
           index = len(self.widgets) - 1
           color = self.alternate_colors[index % len(self.alternate_colors)]
           
           widget.setStyleSheet(f"""
               background-color: {color}; 
               border-radius: 4px; 
               padding: 8px;
               margin: 2px 0;
           """)
           
           # 保存样式引用
           self.widget_styles[widget] = color
       
       def removeWidget(self, widget):
           """重写移除控件方法"""
           super().removeWidget(widget)
           
           # 清理样式引用
           if widget in self.widget_styles:
               del self.widget_styles[widget]
           
           # 重新设置剩余控件的样式
           self.update_widget_styles()
       
       def update_widget_styles(self):
           """更新所有控件的样式"""
           for i, widget in enumerate(self.widgets):
               color = self.alternate_colors[i % len(self.alternate_colors)]
               widget.setStyleSheet(f"""
                   background-color: {color}; 
                   border-radius: 4px; 
                   padding: 8px;
                   margin: 2px 0;
               """)
               self.widget_styles[widget] = color
   
   class CustomVBoxLayoutWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
       
       def setup_ui(self):
           # 创建主布局
           main_layout = QVBoxLayout()
           
           # 创建自定义垂直布局
           self.custom_layout = CustomVBoxLayout(self)
           
           # 添加内容
           items = [
               "📋 任务管理",
               "📊 数据统计", 
               "⚙️ 系统设置",
               "🔔 通知中心",
               "👤 用户资料"
           ]
           
           for item in items:
               label = Label(item)
               label.setStyleSheet("font-size: 14px; font-weight: bold;")
               self.custom_layout.addWidget(label, stretch=0, alignment=Qt.AlignTop)
           
           # 设置布局属性
           self.custom_layout.setSpacing(4)
           self.custom_layout.setContentsMargins(10, 10, 10, 10)
           
           main_layout.addLayout(self.custom_layout)
           self.setLayout(main_layout)

最佳实践
--------

1. **批量操作** - 使用addWidgets方法进行批量添加
2. **内存管理** - 使用deleteWidget方法正确释放内存
3. **布局属性** - 合理设置间距和边距
4. **控件对齐** - 根据需要设置合适的对齐方式
5. **动态管理** - 在运行时安全地添加和移除控件

注意事项
--------

- 添加控件时会自动显示控件
- removeWidget只移除控件不删除，需要手动管理内存
- deleteWidget会安全地删除控件
- removeAllWidget会移除所有控件但不删除
- 大量子控件可能影响布局性能

相关模块
--------

- :doc:`components.layout.expand_layout` - 扩展布局
- :doc:`components.layout.flow_layout` - 流式布局
- :doc:`components.layout.splitter` - 分割器布局
