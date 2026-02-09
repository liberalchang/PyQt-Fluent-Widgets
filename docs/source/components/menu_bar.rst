MenuBar 菜单栏控件模块
======================

MenuBar 模块提供菜单栏控件，用于创建应用程序的主菜单栏。支持Fluent Design样式和自定义菜单项。

主要功能
--------

- **菜单栏管理** - 提供完整的菜单栏功能
- **菜单项支持** - 支持多种菜单项类型
- **样式定制** - 提供Fluent Design样式
- **事件处理** - 完整的菜单事件处理

核心组件
--------

MenuBar
~~~~~~~~

菜单栏控件，提供主菜单栏功能。

MenuBarItem
~~~~~~~~~~~

菜单栏项控件，用于菜单栏中的单个菜单项。

使用示例
--------

基础菜单栏使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.menu_bar import MenuBar, MenuBarItem
   
   # 创建菜单栏
   menu_bar = MenuBar()
   
   # 添加菜单项
   file_menu = MenuBarItem("文件")
   edit_menu = MenuBarItem("编辑")
   view_menu = MenuBarItem("视图")
   
   menu_bar.addMenu(file_menu)
   menu_bar.addMenu(edit_menu)
   menu_bar.addMenu(view_menu)

注意事项
--------

1. **菜单组织** - 合理组织菜单结构
2. **快捷键** - 为常用功能设置快捷键
3. **图标使用** - 为菜单项添加合适的图标

相关组件
--------

- :doc:`menu` - 菜单控件
- :doc:`button` - 按钮控件
