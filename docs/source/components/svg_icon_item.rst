SvgIconItem SVG图标项模块
==========================

SvgIconItem 模块提供SVG图标项控件，用于在QML中显示SVG图标。支持图标缩放和颜色定制。

主要功能
--------

- **SVG显示** - 支持SVG图标的显示
- **图标缩放** - 支持图标的动态缩放
- **颜色定制** - 支持图标颜色的动态修改
- **QML集成** - 专门为QML环境设计
- **性能优化** - 针对SVG渲染优化

核心组件
--------

SvgIconItem
~~~~~~~~~~~~

SVG图标项控件，提供基础的SVG图标显示功能。

使用示例
--------

基础SVG图标项使用：

.. code-block:: python

   from qfluentwidgets.hybrid.svg_icon_item import SvgIconItem
   
   # 创建SVG图标项
   svg_icon = SvgIconItem("icon.svg")
   svg_icon.setSize(32, 32)

注意事项
--------

1. **文件路径** - 确保SVG文件路径正确
2. **尺寸设置** - 合理设置图标尺寸
3. **颜色管理** - 注意图标颜色的动态修改

相关组件
--------

- :doc:`qml_manager` - QML管理器
- :doc:`communication_bridge` - 通信桥接模块
