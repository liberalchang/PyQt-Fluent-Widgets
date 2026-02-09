QmlManager QML管理器模块
========================

QmlManager 模块提供QML文件管理和加载功能。支持QML文件的动态加载和资源管理。

主要功能
--------

- **QML加载** - 支持QML文件的动态加载
- **资源管理** - 提供QML资源的管理功能
- **上下文管理** - 管理QML执行上下文
- **错误处理** - 完整的QML加载错误处理
- **性能优化** - 针对QML加载优化

核心组件
--------

HybridQml
~~~~~~~~~~

混合QML控件，提供基础的QML管理功能。

使用示例
--------

基础QML管理器使用：

.. code-block:: python

   from qfluentwidgets.hybrid.qml_manager import HybridQml
   
   # 创建QML管理器
   qml_manager = HybridQml()
   
   # 加载QML文件
   qml_manager.load("component.qml")

注意事项
--------

1. **文件路径** - 确保QML文件路径正确
2. **依赖管理** - 正确管理QML文件的依赖关系
3. **错误处理** - 妥善处理QML加载错误

相关组件
--------

- :doc:`communication_bridge` - 通信桥接模块
- :doc:`fluent_hybrid_window` - 混合窗口控件
