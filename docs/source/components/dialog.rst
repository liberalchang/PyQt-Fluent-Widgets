Dialog 对话框模块
==================

Dialog 模块提供标准的对话框和消息框功能，支持模态和非模态显示。
该模块提供Fluent Design风格的对话框界面，包含标题、内容和操作按钮等标准元素。

主要功能
--------

- **标准对话框** - 提供标准的对话框界面
- **消息框** - 提供模态消息框功能
- **无边框设计** - 支持无边框的现代化界面
- **阴影效果** - 提供专业的阴影和遮罩效果
- **文本自适应** - 支持文本内容的自动换行

核心组件
--------

Dialog
~~~~~~

标准对话框，提供基础的对话框功能。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.dialog import Dialog
   from PySide6.QtWidgets import QApplication
   
   # 创建对话框
   dialog = Dialog("标题", "对话框内容", parent)
   
   # 连接信号
   dialog.yesSignal.connect(on_yes_clicked)
   dialog.cancelSignal.connect(on_cancel_clicked)
   
   # 显示对话框
   if dialog.exec():
       print("用户点击了确定")

**主要信号：**
- ``yesSignal`` - 确定按钮点击信号
- ``cancelSignal`` - 取消按钮点击信号

**主要方法：**
- ``setTitleBarVisible()`` - 设置标题栏可见性

MessageBox
~~~~~~~~~~

消息框，提供模态的消息显示功能。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.dialog import MessageBox
   
   # 创建消息框
   message_box = MessageBox("提示", "操作成功完成！", parent)
   
   # 连接信号
   message_box.yesSignal.connect(on_yes_clicked)
   message_box.cancelSignal.connect(on_cancel_clicked)
   
   # 显示消息框
   message_box.exec()

**特点：**
- 模态显示，带遮罩效果
- 自动调整大小适应内容
- 支持阴影效果

实际应用
--------

基本对话框
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.dialog import Dialog
   from qfluentwidgets import PushButton, CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   
   class BasicDialogWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建触发按钮
           self.show_dialog_btn = PushButton("显示对话框")
           
           layout.addWidget(self.show_dialog_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.show_dialog_btn.clicked.connect(self.show_dialog)
       
       def show_dialog(self):
           """显示对话框"""
           dialog = Dialog("确认", "确定要执行此操作吗？", self)
           
           # 连接信号
           dialog.yesSignal.connect(self.on_dialog_yes)
           dialog.cancelSignal.connect(self.on_dialog_cancel)
           
           # 显示对话框
           dialog.exec()
       
       def on_dialog_yes(self):
           """对话框确定处理"""
           print("用户确认了操作")
       
       def on_dialog_cancel(self):
           """对话框取消处理"""
           print("用户取消了操作")

消息框应用
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.dialog import MessageBox
   from qfluentwidgets import PushButton, CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   
   class MessageBoxWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建不同类型的消息框按钮
           self.info_btn = PushButton("信息消息")
           self.warning_btn = PushButton("警告消息")
           self.error_btn = PushButton("错误消息")
           self.success_btn = PushButton("成功消息")
           
           layout.addWidget(self.info_btn)
           layout.addWidget(self.warning_btn)
           layout.addWidget(self.error_btn)
           layout.addWidget(self.success_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.info_btn.clicked.connect(self.show_info_message)
           self.warning_btn.clicked.connect(self.show_warning_message)
           self.error_btn.clicked.connect(self.show_error_message)
           self.success_btn.clicked.connect(self.show_success_message)
       
       def show_info_message(self):
           """显示信息消息"""
           message_box = MessageBox("信息", "这是一条信息消息。", self)
           message_box.exec()
       
       def show_warning_message(self):
           """显示警告消息"""
           message_box = MessageBox("警告", "请注意，这可能存在风险！", self)
           message_box.exec()
       
       def show_error_message(self):
           """显示错误消息"""
           message_box = MessageBox("错误", "操作失败，请重试。", self)
           message_box.exec()
       
       def show_success_message(self):
           """显示成功消息"""
           message_box = MessageBox("成功", "操作已成功完成！", self)
           message_box.exec()

高级用法
--------

自定义对话框
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.dialog import Dialog
   from qfluentwidgets import CardWidget, Label, LineEdit, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   
   class CustomDialog(Dialog):
       """自定义对话框"""
       
       def __init__(self, parent=None):
           super().__init__("输入对话框", "请输入您的姓名：", parent)
           self.setup_custom_ui()
       
       def setup_custom_ui(self):
           """设置自定义界面"""
           # 创建输入框
           self.name_input = LineEdit()
           self.name_input.setPlaceholderText("请输入姓名")
           
           # 添加到内容布局
           self.textLayout.addWidget(self.name_input)
           
           # 设置焦点
           self.name_input.setFocus()
       
       def get_name(self):
           """获取输入的姓名"""
           return self.name_input.text()
   
   class CustomDialogWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建触发按钮
           self.show_custom_dialog_btn = PushButton("显示自定义对话框")
           
           # 显示结果
           self.result_label = Label("未输入")
           
           layout.addWidget(self.show_custom_dialog_btn)
           layout.addWidget(self.result_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.show_custom_dialog_btn.clicked.connect(self.show_custom_dialog)
       
       def show_custom_dialog(self):
           """显示自定义对话框"""
           custom_dialog = CustomDialog(self)
           
           # 连接信号
           custom_dialog.yesSignal.connect(self.on_custom_dialog_yes)
           custom_dialog.cancelSignal.connect(self.on_custom_dialog_cancel)
           
           # 显示对话框
           if custom_dialog.exec():
               name = custom_dialog.get_name()
               if name:
                   self.result_label.setText(f"输入的姓名: {name}")
               else:
                   self.result_label.setText("未输入姓名")
       
       def on_custom_dialog_yes(self):
           """自定义对话框确定处理"""
           print("用户确认了输入")
       
       def on_custom_dialog_cancel(self):
           """自定义对话框取消处理"""
           print("用户取消了输入")

确认对话框
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.dialog import MessageBox
   from qfluentwidgets import PushButton, CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   
   class ConfirmDialogWidget(CardWidget):
       """确认对话框示例"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建不同类型的确认按钮
           self.delete_btn = PushButton("删除文件")
           self.save_btn = PushButton("保存更改")
           self.exit_btn = PushButton("退出应用")
           
           layout.addWidget(self.delete_btn)
           layout.addWidget(self.save_btn)
           layout.addWidget(self.exit_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.delete_btn.clicked.connect(self.confirm_delete)
           self.save_btn.clicked.connect(self.confirm_save)
           self.exit_btn.clicked.connect(self.confirm_exit)
       
       def confirm_delete(self):
           """确认删除"""
           message_box = MessageBox(
               "确认删除", 
               "确定要删除选中的文件吗？此操作不可撤销。", 
               self
           )
           
           if message_box.exec():
               print("文件已删除")
           else:
               print("取消删除")
       
       def confirm_save(self):
           """确认保存"""
           message_box = MessageBox(
               "确认保存", 
               "是否保存当前的更改？", 
               self
           )
           
           if message_box.exec():
               print("更改已保存")
           else:
               print("未保存更改")
       
       def confirm_exit(self):
           """确认退出"""
           message_box = MessageBox(
               "确认退出", 
               "确定要退出应用程序吗？未保存的更改将丢失。", 
               self
           )
           
           if message_box.exec():
               print("应用程序已退出")
               QApplication.quit()
           else:
               print("取消退出")

最佳实践
--------

1. **简洁明了** - 对话框内容要简洁明了
2. **操作确认** - 重要操作需要用户确认
3. **用户体验** - 提供清晰的反馈信息
4. **模态显示** - 重要消息使用模态显示
5. **错误处理** - 正确处理用户的选择

注意事项
--------

- 对话框需要正确设置父窗口
- 模态对话框会阻塞主线程
- 长文本内容需要考虑换行处理
- 自定义对话框需要正确处理布局
- 信号连接需要在显示对话框之前完成

相关模块
--------

- :doc:`components.dialog_box.mask_dialog_base` - 遮罩对话框基类
- :doc:`components.widgets.button` - 按钮组件
- :doc:`components.widgets.label` - 标签组件
