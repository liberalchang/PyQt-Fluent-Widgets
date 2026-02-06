Acrylic Menu 亚克力菜单模块
=============================

Acrylic Menu 模块提供亚克力风格的菜单组件，支持透明效果和现代化设计。
该模块结合了亚克力视觉效果和菜单功能，提供美观的选项选择界面。

主要功能
--------

- **亚克力效果** - 提供现代化的亚克力视觉效果
- **菜单功能** - 支持标准的菜单操作
- **自动完成** - 提供自动完成菜单功能
- **可勾选** - 支持可勾选的菜单项
- **系统托盘** - 提供系统托盘菜单支持

核心组件
--------

AcrylicMenu
~~~~~~~~~~

亚克力菜单，提供标准的菜单功能。

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_menu import AcrylicMenu
   from qfluentwidgets import Action
   from PySide6.QtWidgets import QApplication
   
   # 创建亚克力菜单
   menu = AcrylicMenu("菜单标题", parent)
   
   # 添加菜单项
   menu.addAction(Action("选项1"))
   menu.addAction(Action("选项2"))
   
   # 显示菜单
   menu.exec(pos)

**主要方法：**
- ``addAction()`` - 添加菜单项
- ``exec()`` - 显示菜单
- ``setTitle()`` - 设置菜单标题

AcrylicCompleterMenu
~~~~~~~~~~~~~~~~~~~

亚克力自动完成菜单，用于输入框的自动完成功能。

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_menu import AcrylicCompleterMenu
   from qfluentwidgets import LineEdit
   
   # 创建输入框
   line_edit = LineEdit()
   
   # 创建自动完成菜单
   completer_menu = AcrylicCompleterMenu(line_edit)
   
   # 设置完成项
   completer_menu.setItems(["选项1", "选项2", "选项3"])

AcrylicCheckableMenu
~~~~~~~~~~~~~~~~~~~

可勾选的亚克力菜单，支持多选功能。

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_menu import AcrylicCheckableMenu
   from qfluentwidgets import Action
   
   # 创建可勾选菜单
   checkable_menu = AcrylicCheckableMenu("选择选项", parent)
   
   # 添加可勾选项
   checkable_menu.addAction(Action("选项1", checkable=True))
   checkable_menu.addAction(Action("选项2", checkable=True))

实际应用
--------

基本亚克力菜单
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_menu import AcrylicMenu
   from qfluentwidgets import PushButton, CardWidget, Action
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   
   class BasicAcrylicMenuWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建触发按钮
           self.file_menu_btn = PushButton("文件菜单")
           self.edit_menu_btn = PushButton("编辑菜单")
           self.view_menu_btn = PushButton("视图菜单")
           
           layout.addWidget(self.file_menu_btn)
           layout.addWidget(self.edit_menu_btn)
           layout.addWidget(self.view_menu_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.file_menu_btn.clicked.connect(self.show_file_menu)
           self.edit_menu_btn.clicked.connect(self.show_edit_menu)
           self.view_menu_btn.clicked.connect(self.show_view_menu)
       
       def show_file_menu(self):
           """显示文件菜单"""
           menu = AcrylicMenu("文件", self)
           
           # 添加菜单项
           new_action = Action("新建")
           open_action = Action("打开")
           save_action = Action("保存")
           exit_action = Action("退出")
           
           # 连接信号
           new_action.triggered.connect(lambda: print("新建文件"))
           open_action.triggered.connect(lambda: print("打开文件"))
           save_action.triggered.connect(lambda: print("保存文件"))
           exit_action.triggered.connect(lambda: print("退出程序"))
           
           menu.addAction(new_action)
           menu.addAction(open_action)
           menu.addAction(save_action)
           menu.addSeparator()
           menu.addAction(exit_action)
           
           # 显示菜单
           pos = self.file_menu_btn.mapToGlobal(
               self.file_menu_btn.rect().bottomLeft()
           )
           menu.exec(pos)
       
       def show_edit_menu(self):
           """显示编辑菜单"""
           menu = AcrylicMenu("编辑", self)
           
           # 添加菜单项
           undo_action = Action("撤销")
           redo_action = Action("重做")
           cut_action = Action("剪切")
           copy_action = Action("复制")
           paste_action = Action("粘贴")
           
           # 连接信号
           undo_action.triggered.connect(lambda: print("撤销操作"))
           redo_action.triggered.connect(lambda: print("重做操作"))
           cut_action.triggered.connect(lambda: print("剪切操作"))
           copy_action.triggered.connect(lambda: print("复制操作"))
           paste_action.triggered.connect(lambda: print("粘贴操作"))
           
           menu.addAction(undo_action)
           menu.addAction(redo_action)
           menu.addSeparator()
           menu.addAction(cut_action)
           menu.addAction(copy_action)
           menu.addAction(paste_action)
           
           # 显示菜单
           pos = self.edit_menu_btn.mapToGlobal(
               self.edit_menu_btn.rect().bottomLeft()
           )
           menu.exec(pos)
       
       def show_view_menu(self):
           """显示视图菜单"""
           menu = AcrylicMenu("视图", self)
           
           # 添加菜单项
           zoom_in_action = Action("放大")
           zoom_out_action = Action("缩小")
           reset_action = Action("重置缩放")
           fullscreen_action = Action("全屏")
           
           # 连接信号
           zoom_in_action.triggered.connect(lambda: print("放大视图"))
           zoom_out_action.triggered.connect(lambda: print("缩小视图"))
           reset_action.triggered.connect(lambda: print("重置缩放"))
           fullscreen_action.triggered.connect(lambda: print("切换全屏"))
           
           menu.addAction(zoom_in_action)
           menu.addAction(zoom_out_action)
           menu.addAction(reset_action)
           menu.addSeparator()
           menu.addAction(fullscreen_action)
           
           # 显示菜单
           pos = self.view_menu_btn.mapToGlobal(
               self.view_menu_btn.rect().bottomLeft()
           )
           menu.exec(pos)

自动完成菜单
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_menu import AcrylicCompleterMenu
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   
   class AutoCompleteMenuWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自动完成菜单示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建输入框
           from qfluentwidgets import LineEdit
           
           self.line_edit = LineEdit()
           self.line_edit.setPlaceholderText("输入编程语言名称...")
           
           # 创建自动完成菜单
           self.completer_menu = AcrylicCompleterMenu(self.line_edit)
           
           # 设置完成项
           languages = [
               "Python", "JavaScript", "TypeScript", "Java", "C++",
               "C#", "Go", "Rust", "Swift", "Kotlin", "Ruby",
               "PHP", "Perl", "R", "MATLAB", "Scala", "Dart"
           ]
           
           self.completer_menu.setItems(languages)
           
           # 显示选择结果
           self.result_label = Label("选择结果: 无")
           self.result_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.line_edit)
           layout.addWidget(self.result_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.line_edit.textChanged.connect(self.on_text_changed)
           self.line_edit.returnPressed.connect(self.on_return_pressed)
       
       def on_text_changed(self, text):
           """文本变化处理"""
           if text:
               self.result_label.setText(f"当前输入: {text}")
           else:
               self.result_label.setText("选择结果: 无")
       
       def on_return_pressed(self):
           """回车键处理"""
           text = self.line_edit.text()
           if text:
               self.result_label.setText(f"已选择: {text}")

可勾选菜单
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_menu import AcrylicCheckableMenu
   from qfluentwidgets import PushButton, CardWidget, Action
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   
   class CheckableMenuWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
           self.selected_options = set()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建触发按钮
           self.options_btn = PushButton("选择选项")
           self.show_selected_btn = PushButton("显示已选")
           
           layout.addWidget(self.options_btn)
           layout.addWidget(self.show_selected_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.options_btn.clicked.connect(self.show_checkable_menu)
           self.show_selected_btn.clicked.connect(self.show_selected_options)
       
       def show_checkable_menu(self):
           """显示可勾选菜单"""
           menu = AcrylicCheckableMenu("选择选项", self)
           
           # 创建可勾选项
           option1 = Action("选项1", checkable=True)
           option2 = Action("选项2", checkable=True)
           option3 = Action("选项3", checkable=True)
           option4 = Action("选项4", checkable=True)
           option5 = Action("选项5", checkable=True)
           
           # 设置初始状态
           if "选项1" in self.selected_options:
               option1.setChecked(True)
           if "选项2" in self.selected_options:
               option2.setChecked(True)
           if "选项3" in self.selected_options:
               option3.setChecked(True)
           if "选项4" in self.selected_options:
               option4.setChecked(True)
           if "选项5" in self.selected_options:
               option5.setChecked(True)
           
           # 连接信号
           option1.triggered.connect(lambda: self.toggle_option("选项1"))
           option2.triggered.connect(lambda: self.toggle_option("选项2"))
           option3.triggered.connect(lambda: self.toggle_option("选项3"))
           option4.triggered.connect(lambda: self.toggle_option("选项4"))
           option5.triggered.connect(lambda: self.toggle_option("选项5"))
           
           menu.addAction(option1)
           menu.addAction(option2)
           menu.addAction(option3)
           menu.addAction(option4)
           menu.addAction(option5)
           
           # 显示菜单
           pos = self.options_btn.mapToGlobal(
               self.options_btn.rect().bottomLeft()
           )
           menu.exec(pos)
       
       def toggle_option(self, option_name):
           """切换选项状态"""
           if option_name in self.selected_options:
               self.selected_options.remove(option_name)
           else:
               self.selected_options.add(option_name)
       
       def show_selected_options(self):
           """显示已选择的选项"""
           if self.selected_options:
               selected_text = "已选择: " + ", ".join(self.selected_options)
               print(selected_text)
           else:
               print("未选择任何选项")

高级用法
--------

系统托盘菜单
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_menu import AcrylicSystemTrayMenu, AcrylicCheckableSystemTrayMenu
   from qfluentwidgets import Action
   from PySide6.QtWidgets import QSystemTrayIcon, QApplication
   from PySide6.QtGui import QIcon
   
   class SystemTrayMenuExample:
       """系统托盘菜单示例"""
       
       def __init__(self):
           self.setup_tray()
       
       def setup_tray(self):
           """设置系统托盘"""
           # 创建系统托盘图标
           self.tray_icon = QSystemTrayIcon()
           
           # 创建托盘菜单
           self.tray_menu = AcrylicSystemTrayMenu()
           
           # 添加菜单项
           show_action = Action("显示主窗口")
           settings_action = Action("设置")
           about_action = Action("关于")
           exit_action = Action("退出")
           
           # 连接信号
           show_action.triggered.connect(self.show_main_window)
           settings_action.triggered.connect(self.show_settings)
           about_action.triggered.connect(self.show_about)
           exit_action.triggered.connect(QApplication.quit)
           
           self.tray_menu.addAction(show_action)
           self.tray_menu.addSeparator()
           self.tray_menu.addAction(settings_action)
           self.tray_menu.addAction(about_action)
           self.tray_menu.addSeparator()
           self.tray_menu.addAction(exit_action)
           
           # 设置托盘图标和菜单
           self.tray_icon.setContextMenu(self.tray_menu)
           self.tray_icon.show()
       
       def show_main_window(self):
           """显示主窗口"""
           print("显示主窗口")
       
       def show_settings(self):
           """显示设置"""
           print("显示设置")
       
       def show_about(self):
           """显示关于"""
           print("显示关于")

动态菜单
~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_menu import AcrylicMenu
   from qfluentwidgets import PushButton, CardWidget, Action
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   
   class DynamicMenuWidget(CardWidget):
       """动态菜单示例"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
           self.menu_items = []
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建触发按钮
           self.dynamic_menu_btn = PushButton("动态菜单")
           self.add_item_btn = PushButton("添加菜单项")
           self.clear_menu_btn = PushButton("清空菜单")
           
           layout.addWidget(self.dynamic_menu_btn)
           layout.addWidget(self.add_item_btn)
           layout.addWidget(self.clear_menu_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.dynamic_menu_btn.clicked.connect(self.show_dynamic_menu)
           self.add_item_btn.clicked.connect(self.add_menu_item)
           self.clear_menu_btn.clicked.connect(self.clear_menu)
       
       def show_dynamic_menu(self):
           """显示动态菜单"""
           menu = AcrylicMenu("动态菜单", self)
           
           # 添加已存在的菜单项
           for action in self.menu_items:
               menu.addAction(action)
           
           # 如果没有菜单项，添加提示
           if not self.menu_items:
               empty_action = Action("暂无菜单项")
               empty_action.setEnabled(False)
               menu.addAction(empty_action)
           
           # 显示菜单
           pos = self.dynamic_menu_btn.mapToGlobal(
               self.dynamic_menu_btn.rect().bottomLeft()
           )
           menu.exec(pos)
       
       def add_menu_item(self):
           """添加菜单项"""
           import random
           
           item_names = ["新建项目", "打开文件", "保存文档", "导出数据", "导入配置"]
           item_name = random.choice(item_names) + str(random.randint(1, 99))
           
           action = Action(item_name)
           action.triggered.connect(lambda: print(f"执行: {item_name}"))
           
           self.menu_items.append(action)
           print(f"已添加菜单项: {item_name}")
       
       def clear_menu(self):
           """清空菜单"""
           self.menu_items.clear()
           print("已清空所有菜单项")

最佳实践
--------

1. **菜单组织** - 合理组织菜单项的层次结构
2. **快捷键** - 为常用菜单项设置快捷键
3. **图标使用** - 使用合适的图标增强视觉效果
4. **分隔符** - 使用分隔符分组相关菜单项
5. **状态管理** - 正确管理可勾选菜单的状态

注意事项
--------

- 亚克力效果需要正确的背景支持
- 菜单位置需要根据触发控件合理设置
- 自动完成菜单需要合适的数据源
- 可勾选菜单需要正确管理选中状态
- 系统托盘菜单需要正确处理系统事件

相关模块
--------

- :doc:`components.material.acrylic_widget` - 亚克力控件基类
- :doc:`components.widgets.menu` - 标准菜单
- :doc:`components.widgets.line_edit` - 输入框组件
