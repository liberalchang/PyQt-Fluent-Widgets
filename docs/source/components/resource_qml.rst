ResourceQml QML资源模块
======================

ResourceQml 模块提供QML资源管理功能。支持QML资源的加载和管理。

主要功能
--------

- **资源加载** - 支持QML资源的加载
- **路径管理** - 管理QML资源路径
- **缓存机制** - 提供资源缓存功能
- **类型检查** - 支持资源类型检查
- **错误处理** - 完整的资源加载错误处理

使用示例
--------

基础QML资源使用：

.. code-block:: python

   from qfluentwidgets.hybrid.resource_qml import ResourceQml
   
   # 加载QML资源
   resource = ResourceQml("resource.qml")

注意事项
--------

1. **资源路径** - 确保资源路径正确
2. **类型匹配** - 确保资源类型匹配
3. **内存管理** - 注意资源的内存管理

相关组件
--------

- :doc:`qml_manager` - QML管理器
- :doc:`communication_bridge` - 通信桥接模块
