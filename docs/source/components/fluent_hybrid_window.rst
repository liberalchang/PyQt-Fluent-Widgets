FluentHybridWindow 混合窗口模块
==============================

FluentHybridWindow 模块提供Qt和QML混合的窗口控件。支持在Qt应用中嵌入QML界面。

主要功能
--------

- **混合界面** - 支持Qt和QML界面的混合使用
- **无缝集成** - 提供Qt和QML的无缝集成
- **通信支持** - 内置Qt和QML通信机制
- **样式统一** - 统一的Fluent Design样式
- **性能优化** - 针对混合应用优化

核心组件
--------

FluentHybridWindow
~~~~~~~~~~~~~~~~~~

混合窗口控件，提供基础的混合界面功能。

Widget
~~~~~~~

混合控件，用于嵌入QML内容。

使用示例
--------

基础混合窗口使用：

.. code-block:: python

   from qfluentwidgets.hybrid.fluent_hybrid_window import FluentHybridWindow
   
   # 创建混合窗口
   window = FluentHybridWindow()
   
   # 加载QML文件
   window.loadQml("app.qml")

注意事项
--------

1. **QML路径** - 确保QML文件路径正确
2. **通信机制** - 正确使用Qt和QML通信机制
3. **性能考虑** - 注意混合应用的性能优化

相关组件
--------

- :doc:`communication_bridge` - 通信桥接模块
- :doc:`qml_manager` - QML管理器
