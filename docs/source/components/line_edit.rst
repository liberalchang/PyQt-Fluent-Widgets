LineEdit 行编辑控件模块
=======================

LineEdit 模块提供行编辑控件，用于单行文本输入。支持多种输入类型和自动完成功能。

主要功能
--------

- **多种输入** - 支持普通文本、密码、搜索等输入类型
- **自动完成** - 支持自动完成和下拉菜单
- **按钮集成** - 支持内置按钮和图标
- **样式定制** - 提供Fluent Design样式
- **验证支持** - 支持输入验证和格式化

核心组件
--------

LineEdit
~~~~~~~~~

行编辑控件，提供基础的文本输入功能。

**主要子类：**
- ``SearchLineEdit`` - 搜索框
- ``PasswordLineEdit`` - 密码输入框
- ``TextEdit`` - 多行文本编辑器
- ``PlainTextEdit`` - 纯文本编辑器
- ``TextBrowser`` - 文本浏览器

LineEditButton
~~~~~~~~~~~~~~

行编辑按钮控件，用于行编辑器中的按钮。

CompleterMenu
~~~~~~~~~~~~~~

自动完成菜单，提供自动完成功能。

使用示例
--------

基础行编辑器：

.. code-block:: python

   from qfluentwidgets.components.widgets.line_edit import LineEdit, SearchLineEdit
   
   # 创建普通行编辑器
   line_edit = LineEdit()
   line_edit.setPlaceholderText("请输入文本")
   
   # 创建搜索框
   search_edit = SearchLineEdit()
   search_edit.setPlaceholderText("搜索内容")

注意事项
--------

1. **输入类型** - 根据需求选择合适的输入类型
2. **验证规则** - 设置合适的输入验证规则
3. **自动完成** - 合理配置自动完成功能

相关组件
--------

- :doc:`button` - 按钮控件
- :doc:`menu` - 菜单控件
