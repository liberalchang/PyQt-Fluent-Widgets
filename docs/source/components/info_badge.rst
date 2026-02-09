InfoBadge 信息徽章模块
======================

InfoBadge 模块提供信息徽章控件，用于在界面上显示状态指示器和通知数量。支持多种样式和位置管理。

主要功能
--------

- **多种级别** - 支持信息、成功、警告、错误等多种级别
- **灵活位置** - 支持多个预设位置和自定义位置
- **多种样式** - 支持文本徽章、点状徽章、图标徽章
- **位置管理** - 可扩展的位置管理系统
- **自动适配** - 自动适应父控件尺寸和主题

核心组件
--------

InfoBadge
~~~~~~~~~~

信息徽章控件，提供基础的徽章显示功能。

.. code-block:: python

   from qfluentwidgets.components.widgets.info_badge import InfoBadge, InfoLevel
   
   # 创建信息徽章
   badge = InfoBadge("5", InfoLevel.ERROR, parent=parent)
   badge.setFixedSize(20, 20)

**主要子类：**
- ``DotInfoBadge`` - 点状徽章
- ``IconInfoBadge`` - 图标徽章

**特点：**
- 支持多种信息级别
- 自动样式适配
- 圆角设计

InfoBadgeManager
~~~~~~~~~~~~~~~~

徽章位置管理器，提供位置计算和管理功能。

**管理器子类：**
- ``TopRightInfoBadgeManager`` - 右上角管理器
- ``RightInfoBadgeManager`` - 右侧管理器
- ``BottomRightInfoBadgeManager`` - 右下角管理器
- ``TopLeftInfoBadgeManager`` - 左上角管理器
- ``LeftInfoBadgeManager`` - 左侧管理器
- ``BottomLeftInfoBadgeManager`` - 左下角管理器

使用示例
--------

基础徽章使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.info_badge import InfoBadge, InfoLevel
   
   # 创建不同级别的徽章
   info_badge = InfoBadge("新", InfoLevel.INFOAMTION, parent)
   success_badge = InfoBadge("✓", InfoLevel.SUCCESS, parent)
   warning_badge = InfoBadge("!", InfoLevel.WARNING, parent)
   error_badge = InfoBadge("3", InfoLevel.ERROR, parent)

注意事项
--------

1. **级别选择** - 根据信息重要性选择合适的级别
2. **位置管理** - 使用管理器确保徽章位置正确
3. **尺寸适配** - 徽章会根据内容自动调整大小

相关组件
--------

- :doc:`label` - 标签控件，InfoBadge的基类
- :doc:`info_bar` - 信息栏控件
