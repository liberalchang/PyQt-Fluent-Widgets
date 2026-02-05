Chart Resource 图表资源模块
=============================

Chart Resource 模块提供图表相关资源的统一管理，主要用于 ECharts 图表组件的资源文件路径管理。
该模块确保图表组件能够正确加载所需的 HTML 和 JavaScript 资源文件。

主要功能
--------

- **资源枚举** - 定义所有图表相关资源
- **路径管理** - 统一的资源路径生成
- **QRC 集成** - 支持 Qt 资源系统
- **类型安全** - 使用枚举确保资源名称正确

核心组件
--------

ChartResource
~~~~~~~~~~~~~

图表资源枚举类，定义所有可用的图表资源。

.. code-block:: python

   from qfluentwidgets.common.chart_resource import ChartResource
   
   # 获取资源路径
   html_path = ChartResource.ECHARTS_HTML.path()
   js_path = ChartResource.ECHARTS_JS.path()
   qwebchannel_path = ChartResource.QWEBCHANNEL_JS.path()
   
   print(f"HTML文件路径: {html_path}")
   print(f"JS文件路径: {js_path}")
   print(f"QWebChannel文件路径: {qwebchannel_path}")

资源类型
--------

ECHARTS_HTML
~~~~~~~~~~~~

ECharts 的 HTML 模板文件。

.. code-block:: python

   # 获取HTML模板路径
   html_path = ChartResource.ECHARTS_HTML.path()
   # 返回: "qrc:/html/html/echarts.html"

**用途：**
- 图表组件的 HTML 容器
- ECharts 初始化模板
- WebEngine 视图的基础模板

ECHARTS_JS
~~~~~~~~~~

ECharts 的 JavaScript 库文件。

.. code-block:: python

   # 获取ECharts库路径
   js_path = ChartResource.ECHARTS_JS.path()
   # 返回: "qrc:/html/html/echarts.min.js"

**用途：**
- 加载 ECharts 核心库
- 提供图表渲染功能
- 支持各种图表类型

QWEBCHANNEL_JS
~~~~~~~~~~~~~~

Qt WebChannel 的 JavaScript 桥接文件。

.. code-block:: python

   # 获取QWebChannel路径
   qwebchannel_path = ChartResource.QWEBCHANNEL_JS.path()
   # 返回: "qrc:/html/html/qwebchannel.js"

**用途：**
- Qt 与 JavaScript 通信
- 数据传输桥接
- 事件处理机制

使用方法
--------

基本用法
~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.chart_resource import ChartResource
   from qfluentwidgets.components import EChartsWidget
   
   # 创建图表组件
   chart = EChartsWidget()
   
   # 获取资源路径（内部使用）
   html_resource = ChartResource.ECHARTS_HTML
   js_resource = ChartResource.ECHARTS_JS
   
   # 图表组件会自动使用这些资源
   chart.setOption({
       'title': {'text': '示例图表'},
       'xAxis': {'type': 'category', 'data': ['A', 'B', 'C']},
       'yAxis': {'type': 'value'},
       'series': [{'type': 'bar', 'data': [10, 20, 30]}]
   })

自定义组件集成
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.chart_resource import ChartResource
   from PySide6.QtWebEngineWidgets import QWebEngineView
   from PySide6.QtCore import QUrl
   
   class CustomChartWidget(QWebEngineView):
       def __init__(self):
           super().__init__()
           self._load_resources()
           
       def _load_resources(self):
           # 加载HTML模板
           html_path = ChartResource.ECHARTS_HTML.path()
           self.load(QUrl(html_path))
           
       def inject_libraries(self):
           # 注入必要的JavaScript库
           js_libraries = [
               ChartResource.QWEBCHANNEL_JS.path(),
               ChartResource.ECHARTS_JS.path()
           ]
           
           for js_lib in js_libraries:
               self.page().runJavaScript(f"""
                   fetch('{js_lib}')
                       .then(response => response.text())
                       .then(code => eval(code));
               """)

资源管理
--------

路径验证
~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.chart_resource import ChartResource
   from PySide6.QtCore import QFile, QFileInfo
   
   def validate_resources():
       """验证所有资源文件是否存在"""
       resources = [
           ChartResource.ECHARTS_HTML,
           ChartResource.ECHARTS_JS,
           ChartResource.QWEBCHANNEL_JS
       ]
       
       for resource in resources:
           path = resource.path()
           file = QFile(path)
           
           if file.exists():
               size = file.size()
               print(f"✓ {resource.name}: {path} ({size} bytes)")
           else:
               print(f"✗ {resource.name}: {path} (文件不存在)")
   
   # 验证资源
   validate_resources()

资源信息获取
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.chart_resource import ChartResource
   
   def get_resource_info():
       """获取所有资源的详细信息"""
       print("图表资源列表:")
       print("-" * 40)
       
       for resource in ChartResource:
           path = resource.path()
           name = resource.name
           value = resource.value
           
           print(f"名称: {name}")
           print(f"值: {value}")
           print(f"路径: {path}")
           print("-" * 40)
   
   # 获取资源信息
   get_resource_info()

最佳实践
--------

1. **使用枚举** - 始终通过 ChartResource 枚举访问资源，避免硬编码路径
2. **路径检查** - 在使用前检查资源文件是否存在
3. **错误处理** - 妥善处理资源加载失败的情况
4. **性能优化** - 避免重复加载相同的资源

注意事项
--------

- 资源文件必须正确打包到 QRC 资源系统中
- 路径格式为 Qt 资源系统格式 (qrc:/)
- 确保所有依赖的资源文件都存在
- 在发布应用时包含所有必要的资源文件

相关模块
--------

- :doc:`components.charts` - 图表组件
- :doc:`common.config` - 配置管理
- :doc:`_rc.resource` - 资源管理
