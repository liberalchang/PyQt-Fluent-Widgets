InfoBar 信息栏模块
==================

InfoBar 模块提供信息栏控件，用于显示重要通知和消息。支持多种位置和样式配置。

主要功能
--------

- **多种位置** - 支持顶部、底部、角落等多种显示位置
- **图标支持** - 内置多种信息图标
- **自动管理** - 智能的位置管理和堆叠显示
- **关闭功能** - 支持手动和自动关闭
- **桌面显示** - 支持桌面级信息栏

核心组件
--------

InfoBar
~~~~~~~~

信息栏控件，提供通知显示功能。

.. code-block:: python

   from qfluentwidgets.components.widgets.info_bar import InfoBar, InfoBarIcon
   
   # 创建信息栏
   info_bar = InfoBar(
       title="提示",
       content="操作成功完成",
       icon=InfoBarIcon.INFORMATION,
       isClosable=True,
       parent=parent
   )

**主要特点：**
- 支持标题和内容
- 可配置图标
- 支持关闭按钮
- 自动样式适配

InfoBarManager
~~~~~~~~~~~~~

信息栏管理器，处理位置和显示逻辑。

**管理器子类：**
- ``TopInfoBarManager`` - 顶部管理器
- ``TopRightInfoBarManager`` - 右上角管理器
- ``BottomRightInfoBarManager`` - 右下角管理器
- ``TopLeftInfoBarManager`` - 左上角管理器
- ``BottomLeftInfoBarManager`` - 左下角管理器
- ``BottomInfoBarManager`` - 底部管理器

DesktopInfoBarView
~~~~~~~~~~~~~~~~~~

桌面级信息栏视图，用于系统级通知显示。

使用示例
--------

基础信息栏：

.. code-block:: python

   from qfluentwidgets.components.widgets.info_bar import InfoBar, InfoBarIcon
   
   # 显示成功信息
   InfoBar.success(
       title="成功",
       content="文件保存成功",
       duration=3000,
       parent=self
   )
   
   # 显示错误信息
   InfoBar.error(
       title="错误",
       content="文件保存失败",
       duration=5000,
       parent=self
   )

注意事项
--------

1. **位置选择** - 根据界面布局选择合适的位置
2. **持续时间** - 设置合适的显示时长
3. **内容简洁** - 保持信息简洁明了

相关组件
--------

- :doc:`flyout` - 弹出控件
- :doc:`info_badge` - 信息徽章控件
