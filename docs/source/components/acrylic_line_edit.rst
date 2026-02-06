Acrylic Line Edit 亚克力输入框模块
=====================================

Acrylic Line Edit 模块提供亚克力风格的输入框组件，支持透明效果和现代化设计。
该模块结合了亚克力视觉效果和输入框功能，提供美观的文本输入界面。

主要功能
--------

- **亚克力效果** - 提供现代化的亚克力视觉效果
- **文本输入** - 支持标准的文本输入功能
- **搜索功能** - 提供专门的搜索输入框
- **自动完成** - 支持自动完成功能
- **右键菜单** - 提供亚克力风格的右键菜单

核心组件
--------

AcrylicLineEdit
~~~~~~~~~~~~~~~

亚克力输入框，提供标准的文本输入功能。

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_line_edit import AcrylicLineEdit
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   
   # 创建亚克力输入框
   line_edit = AcrylicLineEdit()
   line_edit.setPlaceholderText("请输入文本...")
   
   # 连接信号
   line_edit.textChanged.connect(on_text_changed)

**主要信号：**
- ``textChanged`` - 文本变化信号
- ``textEdited`` - 文本编辑信号
- ``returnPressed`` - 回车键按下信号

AcrylicSearchLineEdit
~~~~~~~~~~~~~~~~~~~~~

亚克力搜索输入框，提供搜索功能。

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_line_edit import AcrylicSearchLineEdit
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   
   # 创建亚克力搜索输入框
   search_edit = AcrylicSearchLineEdit()
   search_edit.setPlaceholderText("搜索...")
   
   # 连接信号
   search_edit.textChanged.connect(on_search_text_changed)

AcrylicLineEditBase
~~~~~~~~~~~~~~~~~~~

亚克力输入框基类，提供基础功能。

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_line_edit import AcrylicLineEditBase
   
   # 创建自定义输入框
   class CustomLineEdit(AcrylicLineEditBase):
       def __init__(self):
           super().__init__()
           self.setup_custom_ui()

实际应用
--------

基本亚克力输入框
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_line_edit import AcrylicLineEdit
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   
   class BasicAcrylicLineEditWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("亚克力输入框示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建亚克力输入框
           self.line_edit = AcrylicLineEdit()
           self.line_edit.setPlaceholderText("请输入您的姓名...")
           
           # 显示输入内容
           self.content_label = Label("输入内容: 无")
           self.content_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.line_edit)
           layout.addWidget(self.content_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.line_edit.textChanged.connect(self.on_text_changed)
           self.line_edit.returnPressed.connect(self.on_return_pressed)
       
       def on_text_changed(self, text):
           """文本变化处理"""
           if text:
               self.content_label.setText(f"输入内容: {text}")
           else:
               self.content_label.setText("输入内容: 无")
       
       def on_return_pressed(self):
           """回车键处理"""
           text = self.line_edit.text()
           if text:
               self.content_label.setText(f"已提交: {text}")

搜索输入框
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_line_edit import AcrylicSearchLineEdit
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   
   class SearchLineEditWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("搜索输入框示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建搜索输入框
           self.search_edit = AcrylicSearchLineEdit()
           self.search_edit.setPlaceholderText("搜索文件、文件夹或应用...")
           
           # 显示搜索结果
           self.result_label = Label("搜索结果: 无")
           self.result_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.search_edit)
           layout.addWidget(self.result_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.search_edit.textChanged.connect(self.on_search_text_changed)
       
       def on_search_text_changed(self, text):
           """搜索文本变化处理"""
           if text:
               # 模拟搜索结果
               results = [
                   f"找到 {len(text)} 个与 '{text}' 相关的结果",
                   f"文件: {text}.txt",
                   f"文件夹: {text}_files",
                   f"应用: {text}_app.exe"
               ]
               
               result_text = "\n".join(results[:3])  # 显示前3个结果
               self.result_label.setText(f"搜索结果:\n{result_text}")
           else:
               self.result_label.setText("搜索结果: 无")

高级用法
--------

自动完成输入框
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_line_edit import AcrylicLineEdit
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QStringListModel
   
   class AutoCompleteLineEditWidget(CardWidget):
       """自动完成输入框"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自动完成输入框")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建输入框
           self.line_edit = AcrylicLineEdit()
           self.line_edit.setPlaceholderText("输入编程语言名称...")
           
           # 设置自动完成
           self.setup_completer()
           
           # 显示选择结果
           self.result_label = Label("选择结果: 无")
           self.result_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.line_edit)
           layout.addWidget(self.result_label)
           self.setLayout(layout)
       
       def setup_completer(self):
           """设置自动完成"""
           from PySide6.QtWidgets import QCompleter
           
           # 编程语言列表
           languages = [
               "Python", "JavaScript", "TypeScript", "Java", "C++",
               "C#", "Go", "Rust", "Swift", "Kotlin", "Ruby",
               "PHP", "Perl", "R", "MATLAB", "Scala", "Dart"
           ]
           
           # 创建自动完成器
           completer = QCompleter(languages)
           completer.setCaseSensitivity(False)
           completer.setFilterMode(Qt.MatchContains)
           
           # 设置到输入框
           self.line_edit.setCompleter(completer)
       
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
               self.result_label.setText(f"已选择语言: {text}")

多行输入框组合
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_line_edit import AcrylicLineEdit, AcrylicSearchLineEdit
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   
   class MultiLineEditWidget(CardWidget):
       """多行输入框组合"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("多行输入框组合")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 姓名输入框
           name_label = Label("姓名:")
           self.name_edit = AcrylicLineEdit()
           self.name_edit.setPlaceholderText("请输入姓名")
           
           # 邮箱输入框
           email_label = Label("邮箱:")
           self.email_edit = AcrylicLineEdit()
           self.email_edit.setPlaceholderText("请输入邮箱地址")
           
           # 搜索框
           search_label = Label("搜索:")
           self.search_edit = AcrylicSearchLineEdit()
           self.search_edit.setPlaceholderText("搜索内容...")
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           self.submit_btn = PushButton("提交")
           self.clear_btn = PushButton("清空")
           
           button_layout.addStretch()
           button_layout.addWidget(self.submit_btn)
           button_layout.addWidget(self.clear_btn)
           
           # 显示结果
           self.result_label = Label("未提交")
           self.result_label.setStyleSheet("padding: 10px;")
           
           # 添加到布局
           layout.addWidget(title_label)
           layout.addWidget(name_label)
           layout.addWidget(self.name_edit)
           layout.addWidget(email_label)
           layout.addWidget(self.email_edit)
           layout.addWidget(search_label)
           layout.addWidget(self.search_edit)
           layout.addLayout(button_layout)
           layout.addWidget(self.result_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.submit_btn.clicked.connect(self.submit_form)
           self.clear_btn.clicked.connect(self.clear_form)
           
           self.search_edit.textChanged.connect(self.on_search_changed)
       
       def submit_form(self):
           """提交表单"""
           name = self.name_edit.text().strip()
           email = self.email_edit.text().strip()
           
           if name and email:
               result_text = f"已提交:\n姓名: {name}\n邮箱: {email}"
               self.result_label.setText(result_text)
           else:
               self.result_label.setText("请填写完整信息")
       
       def clear_form(self):
           """清空表单"""
           self.name_edit.clear()
           self.email_edit.clear()
           self.search_edit.clear()
           self.result_label.setText("已清空")
       
       def on_search_changed(self, text):
           """搜索变化处理"""
           if text:
               self.result_label.setText(f"搜索中: {text}")
           else:
               self.result_label.setText("未提交")

自定义输入框
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_line_edit import AcrylicLineEditBase
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QValidator
   
   class CustomValidator(QValidator):
       """自定义验证器"""
       
       def validate(self, text, pos):
           # 只允许数字
           if text.isdigit() or text == "":
               return QValidator.Acceptable, text, pos
           else:
               return QValidator.Invalid, text, pos
   
   class CustomAcrylicLineEdit(AcrylicLineEditBase):
       """自定义亚克力输入框"""
       
       def __init__(self):
           super().__init__()
           self.setup_custom_ui()
       
       def setup_custom_ui(self):
           """设置自定义界面"""
           # 设置数字验证器
           self.setValidator(CustomValidator())
           self.setPlaceholderText("请输入数字...")
           
           # 设置最大长度
           self.setMaxLength(10)
           
           # 设置样式
           self.setStyleSheet("""
               AcrylicLineEdit {
                   border: 2px solid #3498db;
                   border-radius: 8px;
                   padding: 8px;
                   font-size: 14px;
               }
               AcrylicLineEdit:focus {
                   border-color: #2980b9;
               }
           """)
   
   class CustomLineEditWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自定义输入框")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建自定义输入框
           self.custom_edit = CustomAcrylicLineEdit()
           
           # 显示输入结果
           self.result_label = Label("输入数字: 无")
           self.result_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.custom_edit)
           layout.addWidget(self.result_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.custom_edit.textChanged.connect(self.on_text_changed)
       
       def on_text_changed(self, text):
           """文本变化处理"""
           if text:
               if text.isdigit():
                   self.result_label.setText(f"输入数字: {text}")
               else:
                   self.result_label.setText("输入数字: 无效输入")
           else:
               self.result_label.setText("输入数字: 无")

最佳实践
--------

1. **输入验证** - 使用验证器确保输入数据的正确性
2. **占位符文本** - 提供清晰的占位符文本指导用户输入
3. **自动完成** - 为常用输入提供自动完成功能
4. **样式一致** - 保持与应用整体风格的一致性
5. **用户体验** - 提供即时的输入反馈和验证

注意事项
--------

- 亚克力效果需要正确的背景支持
- 自动完成功能需要合理的数据源
- 验证器需要正确处理各种输入情况
- 右键菜单会自动使用亚克力风格
- 搜索输入框适合用于搜索场景

相关模块
--------

- :doc:`components.material.acrylic_menu` - 亚克力菜单
- :doc:`components.widgets.line_edit` - 标准输入框
- :doc:`components.widgets.menu` - 菜单组件
