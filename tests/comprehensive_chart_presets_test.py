# coding:utf-8
"""
图表预设综合测试
包含所有图表预设功能的完整测试和演示
"""

import sys
import os
import random
from PySide6.QtCore import Qt, QTimer
from PySide6.QtQuick import QQuickWindow, QSGRendererInterface
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QScrollArea

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qfluentwidgets import FluentWindow, SubtitleLabel
from qfluentwidgets import FluentIcon as FIF, AntDesignIcon as ADI
from qfluentwidgets.components.charts import EChartsWidget

# 导入所有预设函数
from qfluentwidgets.components.charts.presets import (
    # 折线图
    basic_line_chart,
    smooth_line_chart,
    area_chart,
    stacked_line_chart,
    # 柱状图
    basic_bar_chart,
    aligned_bar_chart,
    custom_color_bar_chart,
    # 环形图
    rounded_pie_chart,
    donut_chart,
    semi_donut_chart,
    # 散点图
    basic_scatter_chart,
    # 仪表盘
    basic_gauge_chart,
    animated_gauge_chart,
    speed_gauge_chart,
    level_gauge_chart,
    # 雷达图
    basic_radar_chart,
    # 管理版预设
    managed_basic_line_chart,
    managed_basic_bar_chart,
    managed_donut_chart,
    managed_gauge_chart
)

# 导入图表管理器
from qfluentwidgets.components.charts import (
    get_chart_manager,
    update_chart
)


class ChartDemoWidget(QWidget):
    """单个图表演示组件"""
    
    def __init__(self, chart_type: str, title: str, parent=None):
        super().__init__(parent)
        self.setObjectName(f"ChartDemo_{chart_type}")
        self.chart_type = chart_type
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # 标题
        title_label = SubtitleLabel(title, self)
        layout.addWidget(title_label, 0, Qt.AlignTop)
        
        # 图表 - 设置最小高度
        self.chart = EChartsWidget(self)
        self.chart.setMinimumHeight(300)  # 设置最小高度
        layout.addWidget(self.chart, 1)
        
        # 控制按钮（只保留随机数据按钮）
        controls = QHBoxLayout()
        
        # 随机数据按钮
        random_btn = QPushButton("随机数据", self)
        random_btn.clicked.connect(self.random_data)
        controls.addWidget(random_btn)
        
        controls.addStretch()
        layout.addLayout(controls)
        
        # 初始化图表
        self.init_chart()
    
    def init_chart(self):
        """初始化图表"""
        config = self.get_chart_config()
        self.chart.setOption(config)
        
        # 如果是管理版图表，注册到管理器
        if self.is_managed_chart():
            chart_id = self.chart_type.replace('managed_', '')
            manager = get_chart_manager()
            manager.register_chart(chart_id, self.chart, config)
    
    def is_managed_chart(self):
        """检查是否是管理版图表"""
        return self.chart_type.startswith('managed_')
    
    def get_chart_config(self):
        """获取图表配置"""
        if self.chart_type == 'basic_line':
            x_data = ['1月', '2月', '3月', '4月', '5月', '6月']
            y_data = [120, 200, 150, 80, 70, 110]
            return basic_line_chart(x_data, y_data, "基础折线图")
        
        elif self.chart_type == 'smooth_line':
            x_data = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
            y_data = [820, 932, 901, 934, 1290, 1330, 1320]
            return smooth_line_chart(x_data, y_data, "平滑折线图")
        
        elif self.chart_type == 'area':
            x_data = ['2010', '2011', '2012', '2013', '2014', '2015']
            y_data = [56, 58, 62, 69, 73, 78]
            return area_chart(x_data, y_data, "面积图")
        
        elif self.chart_type == 'stacked_line':
            x_data = ['1月', '2月', '3月', '4月', '5月', '6月']
            series_data = [
                {'name': '产品A', 'data': [120, 132, 101, 134, 90, 230]},
                {'name': '产品B', 'data': [220, 182, 191, 234, 290, 330]}
            ]
            return stacked_line_chart(x_data, series_data, "堆叠折线图")
        
        elif self.chart_type == 'basic_bar':
            x_data = ['产品A', '产品B', '产品C', '产品D', '产品E']
            y_data = [120, 200, 150, 80, 70]
            return basic_bar_chart(x_data, y_data, "基础柱状图")
        
        elif self.chart_type == 'aligned_bar':
            x_data = ['周一', '周二', '周三', '周四', '周五']
            y_data = [120, 200, 150, 80, 70]
            return aligned_bar_chart(x_data, y_data, "对齐柱状图")
        
        elif self.chart_type == 'custom_bar':
            x_data = ['Q1', 'Q2', 'Q3', 'Q4']
            y_data = [120, 200, 150, 80]
            colors = ['#5470c6', '#91cc75', '#fac858', '#ee6666']
            return custom_color_bar_chart(x_data, y_data, colors, "自定义颜色柱状图")
        
        elif self.chart_type == 'rounded_pie':
            data = [
                {'name': '直接访问', 'value': 335},
                {'name': '邮件营销', 'value': 310},
                {'name': '联盟广告', 'value': 234},
                {'name': '视频广告', 'value': 135},
                {'name': '搜索引擎', 'value': 1548}
            ]
            return rounded_pie_chart(data, "圆角环形图")
        
        elif self.chart_type == 'donut':
            data = [
                {'name': '直接访问', 'value': 335},
                {'name': '邮件营销', 'value': 310},
                {'name': '联盟广告', 'value': 234},
                {'name': '视频广告', 'value': 135},
                {'name': '搜索引擎', 'value': 1548}
            ]
            return donut_chart(data, "环形图")
        
        elif self.chart_type == 'semi_donut':
            data = [
                {'name': '已完成', 'value': 75},
                {'name': '进行中', 'value': 20},
                {'name': '待开始', 'value': 5}
            ]
            return semi_donut_chart(data, "半环形图")
        
        elif self.chart_type == 'scatter':
            data = [
                [10.0, 8.04], [8.0, 6.95], [13.0, 7.58], [9.0, 8.81],
                [11.0, 8.33], [14.0, 9.96], [6.0, 7.24], [4.0, 4.26],
                [12.0, 10.84], [7.0, 4.82], [5.0, 5.68]
            ]
            return basic_scatter_chart(data, "基础散点图")
        
        elif self.chart_type == 'basic_gauge':
            value = 75.5
            return basic_gauge_chart(value, "基础仪表盘")
        
        elif self.chart_type == 'animated_gauge':
            value = random.uniform(0, 100)
            return animated_gauge_chart(value, "动画仪表盘")
        
        elif self.chart_type == 'speed_gauge':
            value = random.uniform(0, 200)
            return speed_gauge_chart(value, "速度仪表盘")
        
        elif self.chart_type == 'level_gauge':
            value = random.uniform(0, 5)
            return level_gauge_chart(value, "等级仪表盘")
        
        elif self.chart_type == 'radar':
            indicators = [
                {'name': '销售', 'max': 6500},
                {'name': '管理', 'max': 16000},
                {'name': '信息技术', 'max': 30000},
                {'name': '客服', 'max': 38000},
                {'name': '研发', 'max': 52000},
                {'name': '市场', 'max': 25000}
            ]
            data = [
                {
                    'value': [4200, 3000, 20000, 35000, 50000, 18000],
                    'name': '预算分配'
                },
                {
                    'value': [5000, 14000, 28000, 26000, 42000, 21000],
                    'name': '实际开销'
                }
            ]
            return basic_radar_chart(data, indicators, "基础雷达图")
        
        # 管理版图表
        elif self.chart_type == 'managed_line':
            x_data = ['1月', '2月', '3月', '4月', '5月', '6月']
            y_data = [120, 200, 150, 80, 70, 110]
            return managed_basic_line_chart("managed_line", x_data, y_data, "管理版折线图")
        
        elif self.chart_type == 'managed_bar':
            x_data = ['产品A', '产品B', '产品C', '产品D', '产品E']
            y_data = [120, 200, 150, 80, 70]
            return managed_basic_bar_chart("managed_bar", x_data, y_data, "管理版柱状图")
        
        elif self.chart_type == 'managed_donut':
            data = [
                {'name': '直接访问', 'value': 335},
                {'name': '邮件营销', 'value': 310},
                {'name': '联盟广告', 'value': 234},
                {'name': '视频广告', 'value': 135},
                {'name': '搜索引擎', 'value': 1548}
            ]
            return managed_donut_chart("managed_donut", data, "管理版环形图")
        
        elif self.chart_type == 'managed_gauge':
            value = 75.5
            return managed_gauge_chart("managed_gauge", value, "管理版仪表盘")
        
        else:
            return basic_line_chart(['1', '2', '3'], [1, 2, 3], "默认图表")
    
    def random_data(self):
        """生成随机数据"""
        if self.chart_type in ['basic_line', 'smooth_line', 'area']:
            x_data = ['1月', '2月', '3月', '4月', '5月', '6月']
            y_data = [random.randint(50, 200) for _ in range(6)]
            
            if self.chart_type == 'basic_line':
                config = basic_line_chart(x_data, y_data, "随机折线图")
            elif self.chart_type == 'smooth_line':
                config = smooth_line_chart(x_data, y_data, "随机平滑折线图")
            elif self.chart_type == 'area':
                config = area_chart(x_data, y_data, "随机面积图")
            
            self.chart.setOption(config)
        
        elif self.chart_type in ['basic_bar', 'aligned_bar', 'custom_bar']:
            x_data = ['产品A', '产品B', '产品C', '产品D', '产品E']
            y_data = [random.randint(50, 200) for _ in range(5)]
            
            if self.chart_type == 'basic_bar':
                config = basic_bar_chart(x_data, y_data, "随机柱状图")
            elif self.chart_type == 'aligned_bar':
                config = aligned_bar_chart(x_data, y_data, "随机对齐柱状图")
            elif self.chart_type == 'custom_bar':
                colors = ['#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de']
                config = custom_color_bar_chart(x_data, y_data, colors, "随机自定义柱状图")
            
            self.chart.setOption(config)
        
        elif self.chart_type in ['rounded_pie', 'donut', 'semi_donut']:
            names = ['类别A', '类别B', '类别C', '类别D', '类别E']
            data = [{'name': name, 'value': random.randint(50, 500)} for name in names]
            
            if self.chart_type == 'rounded_pie':
                config = rounded_pie_chart(data, "随机圆角环形图")
            elif self.chart_type == 'donut':
                config = donut_chart(data, "随机环形图")
            elif self.chart_type == 'semi_donut':
                config = semi_donut_chart(data, "随机半环形图")
            
            self.chart.setOption(config)
        
        elif self.chart_type in ['basic_gauge', 'animated_gauge', 'speed_gauge', 'level_gauge']:
            if self.chart_type == 'basic_gauge':
                value = random.uniform(0, 100)
                config = basic_gauge_chart(value, "随机基础仪表盘")
            elif self.chart_type == 'animated_gauge':
                value = random.uniform(0, 100)
                config = animated_gauge_chart(value, "随机动画仪表盘")
            elif self.chart_type == 'speed_gauge':
                value = random.uniform(0, 200)
                config = speed_gauge_chart(value, "随机速度仪表盘")
            elif self.chart_type == 'level_gauge':
                value = random.uniform(0, 5)
                config = level_gauge_chart(value, "随机等级仪表盘")
            
            self.chart.setOption(config)
        
        elif self.chart_type == 'scatter':
            data = [[random.uniform(0, 20), random.uniform(0, 15)] for _ in range(20)]
            config = basic_scatter_chart(data, "随机散点图")
            self.chart.setOption(config)
        
        elif self.chart_type == 'radar':
            indicators = [
                {'name': '指标A', 'max': 100},
                {'name': '指标B', 'max': 100},
                {'name': '指标C', 'max': 100},
                {'name': '指标D', 'max': 100},
                {'name': '指标E', 'max': 100},
                {'name': '指标F', 'max': 100}
            ]
            data = [
                {
                    'value': [random.randint(20, 100) for _ in range(6)],
                    'name': '随机数据'
                }
            ]
            config = basic_radar_chart(data, indicators, "随机雷达图")
            self.chart.setOption(config)
        
        # 管理版图表随机数据
        elif self.chart_type.startswith('managed_'):
            chart_type = self.chart_type.replace('managed_', '')
            chart_id = chart_type
            
            if chart_type == 'line':
                x_data = ['1月', '2月', '3月', '4月', '5月', '6月']
                y_data = [random.randint(50, 200) for _ in range(6)]
                config = managed_basic_line_chart(chart_id, x_data, y_data, "随机管理版折线图")
                update_chart(chart_id, config)
            elif chart_type == 'bar':
                x_data = ['产品A', '产品B', '产品C', '产品D', '产品E']
                y_data = [random.randint(50, 200) for _ in range(5)]
                config = managed_basic_bar_chart(chart_id, x_data, y_data, "随机管理版柱状图")
                update_chart(chart_id, config)
            elif chart_type == 'donut':
                names = ['类别A', '类别B', '类别C', '类别D', '类别E']
                data = [{'name': name, 'value': random.randint(50, 500)} for name in names]
                config = managed_donut_chart(chart_id, data, "随机管理版环形图")
                update_chart(chart_id, config)
            elif chart_type == 'gauge':
                value = random.uniform(0, 100)
                config = managed_gauge_chart(chart_id, value, "随机管理版仪表盘")
                update_chart(chart_id, config)


class LineChartsDemo(QWidget):
    """折线图演示"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("LineChartsDemo")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        # 标题
        title = SubtitleLabel("折线图预设演示", self)
        layout.addWidget(title, 0, Qt.AlignTop)
        
        # 创建滚动区域以容纳多个图表
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
        # 图表容器
        charts_widget = QWidget()
        charts_layout = QVBoxLayout(charts_widget)
        charts_layout.setSpacing(15)
        
        # 基础折线图
        self.basicLine = ChartDemoWidget('basic_line', '基础折线图', self)
        self.basicLine.setMinimumHeight(350)  # 设置组件最小高度
        charts_layout.addWidget(self.basicLine)
        
        # 平滑折线图
        self.smoothLine = ChartDemoWidget('smooth_line', '平滑折线图', self)
        self.smoothLine.setMinimumHeight(350)
        charts_layout.addWidget(self.smoothLine)
        
        # 面积图
        self.areaChart = ChartDemoWidget('area', '面积图', self)
        self.areaChart.setMinimumHeight(350)
        charts_layout.addWidget(self.areaChart)
        
        # 堆叠折线图
        self.stackedLine = ChartDemoWidget('stacked_line', '堆叠折线图', self)
        self.stackedLine.setMinimumHeight(350)
        charts_layout.addWidget(self.stackedLine)
        
        # 添加弹性空间
        charts_layout.addStretch()
        
        scroll_area.setWidget(charts_widget)
        layout.addWidget(scroll_area, 1)


class BarChartsDemo(QWidget):
    """柱状图演示"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("BarChartsDemo")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        # 标题
        title = SubtitleLabel("柱状图预设演示", self)
        layout.addWidget(title, 0, Qt.AlignTop)
        
        # 创建滚动区域
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
        # 图表容器
        charts_widget = QWidget()
        charts_layout = QVBoxLayout(charts_widget)
        charts_layout.setSpacing(15)
        
        # 基础柱状图
        self.basicBar = ChartDemoWidget('basic_bar', '基础柱状图', self)
        self.basicBar.setMinimumHeight(350)
        charts_layout.addWidget(self.basicBar)
        
        # 对齐柱状图
        self.alignedBar = ChartDemoWidget('aligned_bar', '对齐柱状图', self)
        self.alignedBar.setMinimumHeight(350)
        charts_layout.addWidget(self.alignedBar)
        
        # 自定义颜色柱状图
        self.customBar = ChartDemoWidget('custom_bar', '自定义颜色柱状图', self)
        self.customBar.setMinimumHeight(350)
        charts_layout.addWidget(self.customBar)
        
        # 添加弹性空间
        charts_layout.addStretch()
        
        scroll_area.setWidget(charts_widget)
        layout.addWidget(scroll_area, 1)


class PieChartsDemo(QWidget):
    """环形图演示"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("PieChartsDemo")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        # 标题
        title = SubtitleLabel("环形图预设演示", self)
        layout.addWidget(title, 0, Qt.AlignTop)
        
        # 创建滚动区域
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
        # 图表容器
        charts_widget = QWidget()
        charts_layout = QVBoxLayout(charts_widget)
        charts_layout.setSpacing(15)
        
        # 圆角环形图
        self.roundedPie = ChartDemoWidget('rounded_pie', '圆角环形图', self)
        self.roundedPie.setMinimumHeight(350)
        charts_layout.addWidget(self.roundedPie)
        
        # 环形图
        self.donut = ChartDemoWidget('donut', '环形图', self)
        self.donut.setMinimumHeight(350)
        charts_layout.addWidget(self.donut)
        
        # 半环形图
        self.semiDonut = ChartDemoWidget('semi_donut', '半环形图', self)
        self.semiDonut.setMinimumHeight(350)
        charts_layout.addWidget(self.semiDonut)
        
        # 添加弹性空间
        charts_layout.addStretch()
        
        scroll_area.setWidget(charts_widget)
        layout.addWidget(scroll_area, 1)


class OtherChartsDemo(QWidget):
    """其他图表演示"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("OtherChartsDemo")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        # 标题
        title = SubtitleLabel("其他图表预设演示", self)
        layout.addWidget(title, 0, Qt.AlignTop)
        
        # 创建滚动区域
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
        # 图表容器
        charts_widget = QWidget()
        charts_layout = QVBoxLayout(charts_widget)
        charts_layout.setSpacing(15)
        
        # 散点图
        self.scatter = ChartDemoWidget('scatter', '散点图', self)
        self.scatter.setMinimumHeight(350)
        charts_layout.addWidget(self.scatter)
        
        # 雷达图
        self.radar = ChartDemoWidget('radar', '雷达图', self)
        self.radar.setMinimumHeight(350)
        charts_layout.addWidget(self.radar)
        
        # 添加弹性空间
        charts_layout.addStretch()
        
        scroll_area.setWidget(charts_widget)
        layout.addWidget(scroll_area, 1)


class GaugeChartsDemo(QWidget):
    """仪表盘演示"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("GaugeChartsDemo")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        # 标题
        title = SubtitleLabel("仪表盘预设演示", self)
        layout.addWidget(title, 0, Qt.AlignTop)
        
        # 创建滚动区域
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
        # 图表容器
        charts_widget = QWidget()
        charts_layout = QVBoxLayout(charts_widget)
        charts_layout.setSpacing(15)
        
        # 基础仪表盘
        self.basicGauge = ChartDemoWidget('basic_gauge', '基础仪表盘', self)
        self.basicGauge.setMinimumHeight(350)
        charts_layout.addWidget(self.basicGauge)
        
        # 动画仪表盘
        self.animatedGauge = ChartDemoWidget('animated_gauge', '动画仪表盘', self)
        self.animatedGauge.setMinimumHeight(350)
        charts_layout.addWidget(self.animatedGauge)
        
        # 速度仪表盘
        self.speedGauge = ChartDemoWidget('speed_gauge', '速度仪表盘', self)
        self.speedGauge.setMinimumHeight(350)
        charts_layout.addWidget(self.speedGauge)
        
        # 等级仪表盘
        self.levelGauge = ChartDemoWidget('level_gauge', '等级仪表盘', self)
        self.levelGauge.setMinimumHeight(350)
        charts_layout.addWidget(self.levelGauge)
        
        # 添加弹性空间
        charts_layout.addStretch()
        
        scroll_area.setWidget(charts_widget)
        layout.addWidget(scroll_area, 1)


class ManagedChartsDemo(QWidget):
    """管理版图表演示"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("ManagedChartsDemo")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        # 标题
        title = SubtitleLabel("管理版图表演示（支持通用reload）", self)
        layout.addWidget(title, 0, Qt.AlignTop)
        
        # 创建滚动区域
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
        # 图表容器
        charts_widget = QWidget()
        charts_layout = QVBoxLayout(charts_widget)
        charts_layout.setSpacing(15)
        
        # 管理版折线图
        self.managedLine = ChartDemoWidget('managed_line', '管理版折线图', self)
        self.managedLine.setMinimumHeight(350)
        charts_layout.addWidget(self.managedLine)
        
        # 管理版柱状图
        self.managedBar = ChartDemoWidget('managed_bar', '管理版柱状图', self)
        self.managedBar.setMinimumHeight(350)
        charts_layout.addWidget(self.managedBar)
        
        # 管理版环形图
        self.managedDonut = ChartDemoWidget('managed_donut', '管理版环形图', self)
        self.managedDonut.setMinimumHeight(350)
        charts_layout.addWidget(self.managedDonut)
        
        # 管理版仪表盘
        self.managedGauge = ChartDemoWidget('managed_gauge', '管理版仪表盘', self)
        self.managedGauge.setMinimumHeight(350)
        charts_layout.addWidget(self.managedGauge)
        
        # 添加弹性空间
        charts_layout.addStretch()
        
        scroll_area.setWidget(charts_widget)
        layout.addWidget(scroll_area, 1)


class ComprehensiveWindow(FluentWindow):
    """综合测试主窗口"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('图表预设综合测试')
        self.resize(1400, 900)
        
        # 折线图演示
        self.lineInterface = LineChartsDemo(self)
        self.addSubInterface(self.lineInterface, FIF.SPEED_HIGH, '折线图')
        
        # 柱状图演示
        self.barInterface = BarChartsDemo(self)
        self.addSubInterface(self.barInterface, ADI.BARCHART, '柱状图')
        
        # 环形图演示
        self.pieInterface = PieChartsDemo(self)
        self.addSubInterface(self.pieInterface, ADI.PIECHART, '环形图')
        
        # 仪表盘演示
        self.gaugeInterface = GaugeChartsDemo(self)
        self.addSubInterface(self.gaugeInterface, FIF.SPEED_OFF, '仪表盘')
        
        # 其他图表演示
        self.otherInterface = OtherChartsDemo(self)
        self.addSubInterface(self.otherInterface, ADI.LINECHART, '其他图表')
        
        # 管理版图表演示
        self.managedInterface = ManagedChartsDemo(self)
        self.addSubInterface(self.managedInterface, FIF.SETTING, '管理版图表')


if __name__ == '__main__':
    # Enable high DPI scaling
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_SCALE_FACTOR"] = "1.25"
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    
    if sys.platform.startswith("win"):
        os.environ.setdefault("QTWEBENGINE_DISABLE_GPU", "1")
        os.environ.setdefault("QTWEBENGINE_DISABLE_SANDBOX", "1")
        os.environ.setdefault("QTWEBENGINE_CHROMIUM_FLAGS", "--disable-gpu --disable-software-rasterizer")
        QQuickWindow.setGraphicsApi(QSGRendererInterface.GraphicsApi.Software)

    app = QApplication(sys.argv)
    w = ComprehensiveWindow()
    w.show()
    
    print("=" * 60)
    print("图表预设综合测试")
    print("=" * 60)
    print("功能说明：")
    print("1. 包含所有图表预设类型的完整演示")
    print("2. 支持随机数据生成")
    print("3. 管理版图表支持自动配置管理")
    print("4. 右键菜单支持Reload、Save page、Save image、Copy image")
    print("5. 页面重载后配置自动恢复")
    print("6. 支持图表注册状态查看")
    print("=" * 60)
    
    auto_close_ms = int(os.getenv("QFW_AUTO_CLOSE_MS", "0") or 0)
    if auto_close_ms > 0:
        QTimer.singleShot(auto_close_ms, app.quit)
    sys.exit(app.exec())
