CommunicationBridge 通信桥接模块
==============================

CommunicationBridge 模块提供Qt和QML之间的通信桥接功能。支持双向数据传输和方法调用。

主要功能
--------

- **Qt-QML通信** - 提供Qt和QML之间的通信桥梁
- **双向传输** - 支持数据的双向传输
- **方法调用** - 支持跨语言的方法调用
- **事件处理** - 提供完整的事件处理机制
- **类型转换** - 自动处理数据类型转换

核心组件
--------

CommunicationBridge
~~~~~~~~~~~~~~~~~~

通信桥接控件，提供基础的通信功能。

使用示例
--------

基础通信桥接使用：

.. code-block:: python

   from qfluentwidgets.hybrid.communication_bridge import CommunicationBridge
   
   # 创建通信桥接
   bridge = CommunicationBridge()
   
   # 注册方法供QML调用
   bridge.registerMethod("methodName", self.method_handler)

注意事项
--------

1. **方法注册** - 正确注册需要暴露的方法
2. **数据类型** - 注意Qt和QML之间的数据类型转换
3. **线程安全** - 确保跨线程调用的安全性

相关组件
--------

- :doc:`fluent_hybrid_window` - 混合窗口控件
- :doc:`qml_manager` - QML管理器
