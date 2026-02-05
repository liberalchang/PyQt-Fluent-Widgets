ECharts Widget 图表组件模块
=============================

ECharts Widget 模块提供基于ECharts的图表组件，支持多种图表类型和交互功能。
该模块使用PySide6-WebEngine嵌入ECharts图表，提供丰富的数据可视化功能。

主要功能
--------

- **图表展示** - 支持ECharts的所有图表类型
- **数据更新** - 支持动态数据更新和实时图表
- **交互功能** - 支持图表点击、缩放等交互
- **主题适配** - 自动适配Fluent Design主题
- **数据桥接** - Python与JavaScript的双向通信

核心组件
--------

EChartsWidget
~~~~~~~~~~~~~

ECharts图表控件，基于WebEngine的图表展示组件。

.. code-block:: python

   from qfluentwidgets.components.charts.echarts_widget import EChartsWidget
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   
   # 创建图表控件
   chart_widget = EChartsWidget()
   
   # 设置图表选项
   option = {
       'title': {
           'text': '示例图表'
       },
       'xAxis': {
           'type': 'category',
           'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
       },
       'yAxis': {
           'type': 'value'
       },
       'series': [{
           'data': [120, 200, 150, 80, 70, 110, 130],
           'type': 'bar'
       }]
   }
   
   chart_widget.setOption(option)
   
   # 添加到布局
   card = CardWidget()
   layout = QVBoxLayout()
   layout.addWidget(chart_widget)
   card.setLayout(layout)

**主要信号：**
- ``chartClicked`` - 图表点击信号

**主要方法：**
- ``setOption()`` - 设置图表选项
- ``pushData()`` - 推送数据到图表
- ``resizeEvent()`` - 处理大小变化

ChartBridge
~~~~~~~~~~~

图表桥接器，实现Python与JavaScript的通信。

.. code-block:: python

   from qfluentwidgets.components.charts.echarts_widget import ChartBridge
   from PySide6.QtCore import QObject, Slot
   
   class CustomChartBridge(ChartBridge):
       """自定义图表桥接器"""
       
       @Slot(str)
       def onChartHover(self, params):
           """图表悬停事件"""
           print(f"图表悬停: {params}")
       
       @Slot(str)
       def onChartLegendSelectChanged(self, params):
           """图例选择变化事件"""
           print(f"图例选择: {params}")

实际应用
--------

基本图表展示
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.charts.echarts_widget import EChartsWidget
   from qfluentwidgets import CardWidget, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   import numpy as np
   
   class BasicChartWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_chart()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建图表控件
           self.chart = EChartsWidget()
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           line_btn = PushButton("折线图")
           bar_btn = PushButton("柱状图")
           pie_btn = PushButton("饼图")
           
           line_btn.clicked.connect(lambda: self.show_line_chart())
           bar_btn.clicked.connect(lambda: self.show_bar_chart())
           pie_btn.clicked.connect(lambda: self.show_pie_chart())
           
           button_layout.addWidget(line_btn)
           button_layout.addWidget(bar_btn)
           button_layout.addWidget(pie_btn)
           
           layout.addWidget(self.chart)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_chart(self):
           """设置图表"""
           # 连接点击事件
           self.chart.chartClicked.connect(self.on_chart_clicked)
           
           # 默认显示折线图
           self.show_line_chart()
       
       def show_line_chart(self):
           """显示折线图"""
           option = {
               'title': {'text': '折线图示例'},
               'tooltip': {'trigger': 'axis'},
               'xAxis': {
                   'type': 'category',
                   'data': ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
               },
               'yAxis': {'type': 'value'},
               'series': [{
                   'name': '销售额',
                   'type': 'line',
                   'data': [120, 200, 150, 80, 70, 110, 130],
                   'smooth': True
               }]
           }
           self.chart.setOption(option)
       
       def show_bar_chart(self):
           """显示柱状图"""
           option = {
               'title': {'text': '柱状图示例'},
               'tooltip': {'trigger': 'axis'},
               'xAxis': {
                   'type': 'category',
                   'data': ['产品A', '产品B', '产品C', '产品D', '产品E']
               },
               'yAxis': {'type': 'value'},
               'series': [{
                   'name': '销量',
                   'type': 'bar',
                   'data': [320, 302, 301, 334, 390],
                   'itemStyle': {
                       'color': '#1890ff'
                   }
               }]
           }
           self.chart.setOption(option)
       
       def show_pie_chart(self):
           """显示饼图"""
           option = {
               'title': {
                   'text': '饼图示例',
                   'left': 'center'
               },
               'tooltip': {
                   'trigger': 'item',
                   'formatter': '{a} <br/>{b}: {c} ({d}%)'
               },
               'series': [{
                   'name': '访问来源',
                   'type': 'pie',
                   'radius': '50%',
                   'data': [
                       {'value': 1048, 'name': '搜索引擎'},
                       {'value': 735, 'name': '直接访问'},
                       {'value': 580, 'name': '邮件营销'},
                       {'value': 484, 'name': '联盟广告'},
                       {'value': 300, 'name': '视频广告'}
                   ],
                   'emphasis': {
                       'itemStyle': {
                           'shadowBlur': 10,
                           'shadowOffsetX': 0,
                           'shadowColor': 'rgba(0, 0, 0, 0.5)'
                       }
                   }
               }]
           }
           self.chart.setOption(option)
       
       def on_chart_clicked(self, data):
           """图表点击事件"""
           print(f"图表被点击: {data}")

实时数据更新
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.charts.echarts_widget import EChartsWidget
   from qfluentwidgets import CardWidget, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import QTimer, QDateTime
   import numpy as np
   import random
   
   class RealTimeChartWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_chart()
           self.setup_timer()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建图表控件
           self.chart = EChartsWidget()
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           self.start_btn = PushButton("开始")
           self.stop_btn = PushButton("停止")
           self.clear_btn = PushButton("清空")
           
           self.start_btn.clicked.connect(self.start_update)
           self.stop_btn.clicked.connect(self.stop_update)
           self.clear_btn.clicked.connect(self.clear_chart)
           
           button_layout.addWidget(self.start_btn)
           button_layout.addWidget(self.stop_btn)
           button_layout.addWidget(self.clear_btn)
           
           layout.addWidget(self.chart)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_chart(self):
           """设置图表"""
           self.data_points = []
           self.time_points = []
           self.max_points = 50
           
           option = {
               'title': {'text': '实时数据监控'},
               'tooltip': {'trigger': 'axis'},
               'xAxis': {
                   'type': 'category',
                   'data': self.time_points
               },
               'yAxis': {
                   'type': 'value',
                   'scale': True
               },
               'series': [{
                   'name': '数值',
                   'type': 'line',
                   'data': self.data_points,
                   'smooth': True,
                   'lineStyle': {'color': '#1890ff'},
                   'itemStyle': {'color': '#1890ff'}
               }]
           }
           
           self.chart.setOption(option)
       
       def setup_timer(self):
           """设置定时器"""
           self.timer = QTimer()
           self.timer.timeout.connect(self.update_data)
           self.is_updating = False
       
       def start_update(self):
           """开始更新"""
           if not self.is_updating:
               self.is_updating = True
               self.timer.start(1000)  # 每秒更新一次
               self.start_btn.setEnabled(False)
               self.stop_btn.setEnabled(True)
       
       def stop_update(self):
           """停止更新"""
           if self.is_updating:
               self.is_updating = False
               self.timer.stop()
               self.start_btn.setEnabled(True)
               self.stop_btn.setEnabled(False)
       
       def clear_chart(self):
           """清空图表"""
           self.data_points.clear()
           self.time_points.clear()
           self.update_chart_option()
       
       def update_data(self):
           """更新数据"""
           # 生成随机数据
           new_value = random.randint(20, 80)
           current_time = QDateTime.currentDateTime().toString('hh:mm:ss')
           
           # 添加数据点
           self.data_points.append(new_value)
           self.time_points.append(current_time)
           
           # 限制数据点数量
           if len(self.data_points) > self.max_points:
               self.data_points.pop(0)
               self.time_points.pop(0)
           
           # 更新图表
           self.update_chart_option()
       
       def update_chart_option(self):
           """更新图表选项"""
           option = {
               'xAxis': {'data': self.time_points},
               'series': [{'data': self.data_points}]
           }
           
           self.chart.setOption(option)

高级用法
--------

多系列图表
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.charts.echarts_widget import EChartsWidget
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   import numpy as np
   
   class MultiSeriesChartWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_chart()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           self.chart = EChartsWidget()
           layout.addWidget(self.chart)
           self.setLayout(layout)
       
       def setup_chart(self):
           """设置多系列图表"""
           # 生成示例数据
           x_data = ['1月', '2月', '3月', '4月', '5月', '6月']
           series1_data = [820, 932, 901, 934, 1290, 1330]
           series2_data = [620, 732, 701, 734, 1090, 1130]
           series3_data = [120, 132, 101, 134, 290, 330]
           
           option = {
               'title': {'text': '多系列图表示例'},
               'tooltip': {'trigger': 'axis'},
               'legend': {
                   'data': ['产品A', '产品B', '产品C'],
                   'top': '5%'
               },
               'xAxis': {
                   'type': 'category',
                   'data': x_data
               },
               'yAxis': {'type': 'value'},
               'series': [
                   {
                       'name': '产品A',
                       'type': 'bar',
                       'data': series1_data,
                       'itemStyle': {'color': '#5470c6'}
                   },
                   {
                       'name': '产品B',
                       'type': 'bar',
                       'data': series2_data,
                       'itemStyle': {'color': '#91cc75'}
                   },
                   {
                       'name': '产品C',
                       'type': 'line',
                       'data': series3_data,
                       'smooth': True,
                       'lineStyle': {'color': '#fac858'},
                       'itemStyle': {'color': '#fac858'}
                   }
               ]
           }
           
           self.chart.setOption(option)
           
           # 连接点击事件
           self.chart.chartClicked.connect(self.on_chart_clicked)
       
       def on_chart_clicked(self, data):
           """图表点击事件"""
           print(f"点击了: {data}")

自定义主题
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.charts.echarts_widget import EChartsWidget
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   from qfluentwidgets.common.config import qconfig, Theme
   
   class ThemedChartWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_chart()
           self.setup_theme_listener()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           self.chart = EChartsWidget()
           layout.addWidget(self.chart)
           self.setLayout(layout)
       
       def setup_chart(self):
           """设置图表"""
           self.update_chart_theme()
       
       def setup_theme_listener(self):
           """设置主题监听"""
           qconfig.themeChanged.connect(self.update_chart_theme)
       
       def update_chart_theme(self):
           """更新图表主题"""
           is_dark = qconfig.theme == Theme.DARK
           
           theme_config = self.get_theme_config(is_dark)
           
           option = {
               'backgroundColor': 'transparent',
               'title': {
                   'text': '主题适配图表',
                   'textStyle': theme_config['textStyle']
               },
               'tooltip': {
                   'backgroundColor': theme_config['backgroundColor'],
                   'borderColor': theme_config['borderColor'],
                   'textStyle': theme_config['textStyle']
               },
               'legend': {
                   'textStyle': theme_config['textStyle']
               },
               'xAxis': {
                   'type': 'category',
                   'data': ['A', 'B', 'C', 'D', 'E'],
                   'axisLine': {
                       'lineStyle': {'color': theme_config['axisColor']}
                   },
                   'axisLabel': {
                       'color': theme_config['textColor']
                   }
               },
               'yAxis': {
                   'type': 'value',
                   'axisLine': {
                       'lineStyle': {'color': theme_config['axisColor']}
                   },
                   'axisLabel': {
                       'color': theme_config['textColor']
                   },
                   'splitLine': {
                       'lineStyle': {'color': theme_config['splitLineColor']}
                   }
               },
               'series': [{
                   'name': '数据',
                   'type': 'bar',
                   'data': [12, 23, 34, 45, 56],
                   'itemStyle': {
                       'color': theme_config['primaryColor']
                   }
               }]
           }
           
           self.chart.setOption(option)
       
       def get_theme_config(self, is_dark):
           """获取主题配置"""
           if is_dark:
               return {
                   'backgroundColor': '#2d2d30',
                   'borderColor': '#3e3e42',
                   'textColor': '#cccccc',
                   'textStyle': {'color': '#cccccc'},
                   'axisColor': '#3e3e42',
                   'splitLineColor': '#3e3e42',
                   'primaryColor': '#1890ff'
               }
           else:
               return {
                   'backgroundColor': '#ffffff',
                   'borderColor': '#e4e7ed',
                   'textColor': '#606266',
                   'textStyle': {'color': '#606266'},
                   'axisColor': '#e4e7ed',
                   'splitLineColor': '#e4e7ed',
                   'primaryColor': '#409eff'
               }

数据导出
~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.charts.echarts_widget import EChartsWidget
   from qfluentwidgets import CardWidget, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QFileDialog
   import json
   
   class ExportableChartWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_chart()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 图表控件
           self.chart = EChartsWidget()
           
           # 导出按钮
           button_layout = QHBoxLayout()
           
           export_json_btn = PushButton("导出JSON")
           export_png_btn = PushButton("导出PNG")
           
           export_json_btn.clicked.connect(self.export_json)
           export_png_btn.clicked.connect(self.export_png)
           
           button_layout.addWidget(export_json_btn)
           button_layout.addWidget(export_png_btn)
           
           layout.addWidget(self.chart)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_chart(self):
           """设置图表"""
           option = {
               'title': {'text': '可导出图表'},
               'xAxis': {
                   'type': 'category',
                   'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
               },
               'yAxis': {'type': 'value'},
               'series': [{
                   'data': [120, 200, 150, 80, 70, 110, 130],
                   'type': 'line',
                   'smooth': True
               }]
           }
           
           self.chart.setOption(option)
           self.current_option = option
       
       def export_json(self):
           """导出JSON格式"""
           file_path, _ = QFileDialog.getSaveFileName(
               self,
               "导出图表配置",
               "chart_config.json",
               "JSON Files (*.json)"
           )
           
           if file_path:
               with open(file_path, 'w', encoding='utf-8') as f:
                   json.dump(self.current_option, f, indent=2, ensure_ascii=False)
       
       def export_png(self):
           """导出PNG格式"""
           # 使用JavaScript的导出功能
           js_code = """
           var canvas = document.querySelector('canvas');
           if (canvas) {
               var url = canvas.toDataURL('image/png');
               bridge.exportImage(url);
           }
           """
           
           self.chart.page().runJavaScript(js_code)

最佳实践
--------

1. **依赖检查** - 确保PySide6-WebEngine可用
2. **性能优化** - 避免频繁的图表更新
3. **错误处理** - 处理图表加载失败的情况
4. **主题适配** - 根据应用主题调整图表样式
5. **数据管理** - 合理管理图表数据避免内存泄漏

注意事项
--------

- 需要安装PySide6-WebEngine依赖
- 图表加载需要时间，建议显示加载状态
- 大量数据可能影响性能
- JavaScript执行可能失败，需要错误处理
- 图表交互事件需要正确处理

相关模块
--------

- :doc:`common.chart_resource` - 图表资源管理
- :doc:`components.widgets` - UI组件
- :doc:`common.data` - 数据处理
