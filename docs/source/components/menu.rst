Menu 菜单控件模块
==================

Menu 模块提供菜单控件，用于创建上下文菜单和下拉菜单。支持多种动画效果和菜单类型。

主要功能
--------

- **多种菜单** - 支持上下文菜单、下拉菜单等
- **动画效果** - 提供多种菜单动画效果
- **菜单项类型** - 支持普通、可勾选、单选等菜单项
- **系统集成** - 支持系统托盘菜单
- **样式定制** - 提供Fluent Design样式

核心组件
--------

RoundMenu
~~~~~~~~~

圆形菜单控件，提供基础的菜单功能。

**主要子类：**
- ``EditMenu`` - 编辑菜单
- ``LineEditMenu`` - 行编辑器菜单
- ``TextEditMenu`` - 文本编辑器菜单
- ``SystemTrayMenu`` - 系统托盘菜单
- ``CheckableSystemTrayMenu`` - 可勾选系统托盘菜单

MenuAnimationManager
~~~~~~~~~~~~~~~~~~

菜单动画管理器，提供动画效果。

MenuItemDelegate
~~~~~~~~~~~~~~~~

菜单项委托，用于自定义菜单项显示。

使用示例
--------

基础菜单使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.menu import RoundMenu
   
   # 创建菜单
   menu = RoundMenu(parent=self)
   
   # 添加菜单项
   menu.addAction("打开")
   menu.addAction("保存")
   menu.addSeparator()
   menu.addAction("退出")
   
   # 显示菜单
   menu.exec(pos)

注意事项
--------

1. **菜单类型** - 根据使用场景选择合适的菜单类型
2. **动画效果** - 选择合适的动画效果
3. **系统集成** - 系统托盘菜单需要特殊处理

相关组件
--------

- :doc:`button` - 按钮控件
- :doc:`menu_bar` - 菜单栏控件
