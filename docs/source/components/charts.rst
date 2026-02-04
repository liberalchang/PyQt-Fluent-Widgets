图表组件 (Charts)
================

本节介绍 PySide6-Fluent-Widgets 中的图表相关组件。

EchartsWidget
-------------

基于 ECharts 的图表组件，支持丰富的图表类型。

.. code-block:: python

   from qfluentwidgets import EchartsWidget

   # 创建图表组件
   chart = EchartsWidget()
   chart.setFixedSize(600, 400)
   
   # 设置图表选项
   option = {
       'title': {
           'text': '销售数据'
       },
       'tooltip': {},
       'xAxis': {
           'type': 'category',
           'data': ['一月', '二月', '三月', '四月', '五月']
       },
       'yAxis': {
           'type': 'value'
       },
       'series': [{
           'name': '销售额',
           'type': 'bar',
           'data': [120, 200, 150, 80, 170]
       }]
   }
   
   chart.setOption(option)

折线图
------

.. code-block:: python

   # 创建折线图
   line_chart_option = {
       'title': {
           'text': '趋势分析'
       },
       'tooltip': {
           'trigger': 'axis'
       },
       'xAxis': {
           'type': 'category',
           'data': ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
       },
       'yAxis': {
           'type': 'value'
       },
       'series': [{
           'name': '访问量',
           'type': 'line',
           'data': [820, 932, 901, 934, 1290, 1330, 1320],
           'smooth': True
       }]
   }
   
   chart.setOption(line_chart_option)

柱状图
------

.. code-block:: python

   # 创建柱状图
   bar_chart_option = {
       'title': {
           'text': '月度统计'
       },
       'tooltip': {
           'trigger': 'axis'
       },
       'xAxis': {
           'type': 'category',
           'data': ['产品A', '产品B', '产品C', '产品D', '产品E']
       },
       'yAxis': {
           'type': 'value'
       },
       'series': [{
           'name': '销量',
           'type': 'bar',
           'data': [320, 302, 301, 334, 390],
           'itemStyle': {
               'color': '#0078d4'
           }
       }]
   }
   
   chart.setOption(bar_chart_option)

饼图
----

.. code-block:: python

   # 创建饼图
   pie_chart_option = {
       'title': {
           'text': '市场份额',
           'left': 'center'
       },
       'tooltip': {
           'trigger': 'item'
       },
       'series': [{
           'name': '市场份额',
           'type': 'pie',
           'radius': '50%',
           'data': [
               {'value': 335, 'name': '产品A'},
               {'value': 310, 'name': '产品B'},
               {'value': 234, 'name': '产品C'},
               {'value': 135, 'name': '产品D'},
               {'value': 1548, 'name': '产品E'}
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
   
   chart.setOption(pie_chart_option)

散点图
------

.. code-block:: python

   # 创建散点图
   scatter_chart_option = {
       'title': {
           'text': '数据分布'
       },
       'xAxis': {
           'type': 'value'
       },
       'yAxis': {
           'type': 'value'
       },
       'series': [{
           'name': '数据点',
           'type': 'scatter',
           'data': [
               [10.0, 8.04],
               [8.0, 6.95],
               [13.0, 7.58],
               [9.0, 8.81],
               [11.0, 8.33],
               [14.0, 9.96],
               [6.0, 7.24],
               [4.0, 4.26],
               [12.0, 10.84],
               [7.0, 4.82],
               [5.0, 5.68]
           ]
       }]
   }
   
   chart.setOption(scatter_chart_option)

完整示例
--------

下面是一个完整的图表使用示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                                QWidget, QPushButton, QComboBox, QLabel)
   from PySide6.QtCore import Qt
   from qfluentwidgets import *

   class ChartDemoWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           self.setWindowTitle('图表组件示例')
           self.resize(900, 700)
           
           # 创建界面
           self.setup_ui()

       def setup_ui(self):
           """设置界面"""
           central_widget = QWidget()
           self.setCentralWidget(central_widget)
           
           layout = QVBoxLayout(central_widget)
           
           # 标题和控制栏
           control_layout = QHBoxLayout()
           
           title = SubtitleLabel('图表组件示例')
           control_layout.addWidget(title)
           control_layout.addStretch()
           
           # 图表类型选择
           chart_type_label = QLabel('图表类型:')
           self.chart_type_combo = QComboBox()
           self.chart_type_combo.addItems(['柱状图', '折线图', '饼图', '散点图'])
           self.chart_type_combo.currentTextChanged.connect(self.change_chart_type)
           
           control_layout.addWidget(chart_type_label)
           control_layout.addWidget(self.chart_type_combo)
           
           # 刷新按钮
           refresh_btn = PrimaryPushButton('刷新数据')
           refresh_btn.clicked.connect(self.refresh_data)
           control_layout.addWidget(refresh_btn)
           
           layout.addLayout(control_layout)
           
           # 图表组件
           self.chart = EchartsWidget()
           layout.addWidget(self.chart)
           
           # 初始化显示柱状图
           self.show_bar_chart()

       def show_bar_chart(self):
           """显示柱状图"""
           option = {
               'title': {
                   'text': '月度销售统计',
                   'left': 'center'
               },
               'tooltip': {
                   'trigger': 'axis',
                   'axisPointer': {
                       'type': 'shadow'
                   }
               },
               'grid': {
                   'left': '3%',
                   'right': '4%',
                   'bottom': '3%',
                   'containLabel': True
               },
               'xAxis': {
                   'type': 'category',
                   'data': ['一月', '二月', '三月', '四月', '五月', '六月'],
                   'axisTick': {
                       'alignWithLabel': True
                   }
               },
               'yAxis': {
                   'type': 'value'
               },
               'series': [{
                   'name': '销售额',
                   'type': 'bar',
                   'barWidth': '60%',
                   'data': [320, 302, 301, 334, 390, 330],
                   'itemStyle': {
                       'color': '#0078d4'
                   }
               }]
           }
           
           self.chart.setOption(option)

       def show_line_chart(self):
           """显示折线图"""
           option = {
               'title': {
                   'text': '访问量趋势',
                   'left': 'center'
               },
               'tooltip': {
                   'trigger': 'axis'
               },
               'legend': {
                   'data': ['网站访问量', '移动端访问量'],
                   'top': '10%'
               },
               'grid': {
                   'left': '3%',
                   'right': '4%',
                   'bottom': '3%',
                   'containLabel': True
               },
               'xAxis': {
                   'type': 'category',
                   'boundaryGap': False,
                   'data': ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
               },
               'yAxis': {
                   'type': 'value'
               },
               'series': [
                   {
                       'name': '网站访问量',
                       'type': 'line',
                       'stack': '总量',
                       'data': [820, 932, 901, 934, 1290, 1330, 1320],
                       'itemStyle': {
                           'color': '#0078d4'
                       }
                   },
                   {
                       'name': '移动端访问量',
                       'type': 'line',
                       'stack': '总量',
                       'data': [120, 132, 101, 134, 290, 330, 320],
                       'itemStyle': {
                           'color': '#107c10'
                       }
                   }
               ]
           }
           
           self.chart.setOption(option)

       def show_pie_chart(self):
           """显示饼图"""
           option = {
               'title': {
                   'text': '产品市场份额',
                   'left': 'center'
               },
               'tooltip': {
                   'trigger': 'item',
                   'formatter': '{a} <br/>{b}: {c} ({d}%)'
               },
               'legend': {
                   'orient': 'vertical',
                   'left': 'left',
                   'data': ['产品A', '产品B', '产品C', '产品D', '产品E']
               },
               'series': [{
                   'name': '市场份额',
                   'type': 'pie',
                   'radius': '50%',
                   'center': ['50%', '60%'],
                   'data': [
                       {'value': 335, 'name': '产品A'},
                       {'value': 310, 'name': '产品B'},
                       {'value': 234, 'name': '产品C'},
                       {'value': 135, 'name': '产品D'},
                       {'value': 1548, 'name': '产品E'}
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

       def show_scatter_chart(self):
           """显示散点图"""
           option = {
               'title': {
                   'text': '身高体重分布',
                   'left': 'center'
               },
               'tooltip': {
                   'trigger': 'item'
               },
               'xAxis': {
                   'type': 'value',
                   'name': '身高(cm)',
                   'splitLine': {
                       'lineStyle': {
                           'type': 'dashed'
                       }
                   }
               },
               'yAxis': {
                   'type': 'value',
                   'name': '体重(kg)',
                   'splitLine': {
                       'lineStyle': {
                           'type': 'dashed'
                       }
                   }
               },
               'series': [{
                   'name': '数据点',
                   'type': 'scatter',
                   'data': [
                       [165, 55], [170, 60], [175, 65], [180, 70], [185, 75],
                       [160, 50], [168, 58], [172, 62], [178, 68], [182, 72],
                       [155, 45], [163, 52], [167, 56], [173, 64], [177, 66]
                   ],
                   'itemStyle': {
                       'color': '#0078d4'
                   }
               }]
           }
           
           self.chart.setOption(option)

       def change_chart_type(self, chart_type):
           """切换图表类型"""
           if chart_type == '柱状图':
               self.show_bar_chart()
           elif chart_type == '折线图':
               self.show_line_chart()
           elif chart_type == '饼图':
               self.show_pie_chart()
           elif chart_type == '散点图':
               self.show_scatter_chart()

       def refresh_data(self):
           """刷新数据"""
           # 模拟数据刷新
           import random
           
           current_type = self.chart_type_combo.currentText()
           
           if current_type == '柱状图':
               # 生成新的随机数据
               data = [random.randint(200, 400) for _ in range(6)]
               option = {
                   'title': {'text': '月度销售统计', 'left': 'center'},
                   'xAxis': {'type': 'category', 'data': ['一月', '二月', '三月', '四月', '五月', '六月']},
                   'yAxis': {'type': 'value'},
                   'series': [{
                       'name': '销售额',
                       'type': 'bar',
                       'data': data,
                       'itemStyle': {'color': '#0078d4'}
                   }]
               }
               self.chart.setOption(option)
           
           InfoBar.success('数据已刷新', parent=self)

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       window = ChartDemoWindow()
       window.show()
       sys.exit(app.exec())

最佳实践
--------

1. **图表选择**: 
   - 柱状图适合比较不同类别的数据
   - 折线图适合显示趋势变化
   - 饼图适合显示占比关系
   - 散点图适合显示数据分布

2. **数据可视化**: 
   - 使用合适的颜色方案
   - 添加必要的图例和标签
   - 设置合适的坐标轴范围

3. **交互功能**: 
   - 添加工具提示显示详细信息
   - 支持图表缩放和平移
   - 提供数据筛选功能

4. **性能优化**: 
   - 大量数据时使用数据采样
   - 避免频繁更新图表
   - 合理设置动画效果
