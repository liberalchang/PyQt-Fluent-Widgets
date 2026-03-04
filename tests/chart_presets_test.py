# coding:utf-8
import sys
import os
import random
from PySide6.QtCore import Qt, QTimer
from PySide6.QtQuick import QQuickWindow, QSGRendererInterface
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qfluentwidgets import FluentWindow, SubtitleLabel
from qfluentwidgets import FluentIcon as FIF, AntDesignIcon as ADI
from qfluentwidgets.components.charts import EChartsWidget
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
    aggregated_scatter_chart,  # noqa: F401
    regression_scatter_chart,  # noqa: F401
    # 仪表盘
    basic_gauge_chart,
    animated_gauge_chart,
    speed_gauge_chart,
    level_gauge_chart,
    # 雷达图
    basic_radar_chart,
    aqi_radar_chart
)


class ChartDemoWidget(QWidget):
    """单个图表演示组件"""
    
    def __init__(self, chart_type: str, title: str, parent=None):
        super().__init__(parent)
        self.setObjectName(f"ChartDemo_{chart_type}")
        self.chart_type = chart_type
        
        # 布局
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # 标题
        self.titleLabel = SubtitleLabel(title, self)
        layout.addWidget(self.titleLabel, 0, Qt.AlignTop)
        
        # 图表
        self.chart = EChartsWidget(self)
        layout.addWidget(self.chart, 1)
        
        # 控制按钮
        controls_layout = QHBoxLayout()
        
        # 刷新按钮
        self.refreshBtn = QPushButton("刷新数据", self)
        self.refreshBtn.clicked.connect(self.refreshData)
        controls_layout.addWidget(self.refreshBtn)
        
        # 动画按钮（如果支持）
        if self.supportsAnimation():
            self.animateBtn = QPushButton("播放动画", self)
            self.animateBtn.clicked.connect(self.playAnimation)
            controls_layout.addWidget(self.animateBtn)
        
        controls_layout.addStretch()
        layout.addLayout(controls_layout)
        
        # 初始化图表
        self.initChart()
    
    def supportsAnimation(self):
        """检查是否支持动画"""
        return self.chart_type in ['gauge', 'animated_gauge', 'speed_gauge', 'level_gauge']
    
    def initChart(self):
        """初始化图表"""
        config = self.getChartConfig()
        self.chart.setOption(config)
    
    def getChartConfig(self):
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
        
        elif self.chart_type == 'gauge':
            value = random.uniform(0, 100)
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
        
        elif self.chart_type == 'aqi_radar':
            data = [{'value': [50, 80, 30, 60, 90, 40], 'name': 'AQI指数'}]
            return aqi_radar_chart(data, "AQI雷达图")
        
        else:
            return basic_line_chart(['1', '2', '3'], [1, 2, 3], "默认图表")
    
    def refreshData(self):
        """刷新数据"""
        config = self.getChartConfig()
        self.chart.setOption(config)
    
    def playAnimation(self):
        """播放动画"""
        if self.chart_type in ['gauge', 'animated_gauge', 'speed_gauge', 'level_gauge']:
            # 仪表盘动画：逐渐增加数值
            self.animateValue(0, 100 if self.chart_type != 'speed_gauge' else 200)
    
    def animateValue(self, start, end, step=2, delay=50):
        """动画数值变化"""
        if start <= end:
            config = self.getChartConfig()
            self.chart.setOption(config)
            QTimer.singleShot(delay, lambda: self.animateValue(start + step, end, step, delay))


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
        
        # 图表网格
        charts_layout = QVBoxLayout()
        
        # 基础折线图
        self.basicLine = ChartDemoWidget('basic_line', '基础折线图', self)
        charts_layout.addWidget(self.basicLine)
        
        # 平滑折线图
        self.smoothLine = ChartDemoWidget('smooth_line', '平滑折线图', self)
        charts_layout.addWidget(self.smoothLine)
        
        # 面积图
        self.areaChart = ChartDemoWidget('area', '面积图', self)
        charts_layout.addWidget(self.areaChart)
        
        layout.addLayout(charts_layout)


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
        
        # 图表网格
        charts_layout = QVBoxLayout()
        
        # 基础柱状图
        self.basicBar = ChartDemoWidget('basic_bar', '基础柱状图', self)
        charts_layout.addWidget(self.basicBar)
        
        # 对齐柱状图
        self.alignedBar = ChartDemoWidget('aligned_bar', '对齐柱状图', self)
        charts_layout.addWidget(self.alignedBar)
        
        # 自定义颜色柱状图
        self.customBar = ChartDemoWidget('custom_bar', '自定义颜色柱状图', self)
        charts_layout.addWidget(self.customBar)
        
        layout.addLayout(charts_layout)


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
        
        # 图表网格
        charts_layout = QVBoxLayout()
        
        # 圆角环形图
        self.roundedPie = ChartDemoWidget('rounded_pie', '圆角环形图', self)
        charts_layout.addWidget(self.roundedPie)
        
        # 环形图
        self.donut = ChartDemoWidget('donut', '环形图', self)
        charts_layout.addWidget(self.donut)
        
        # 半环形图
        self.semiDonut = ChartDemoWidget('semi_donut', '半环形图', self)
        charts_layout.addWidget(self.semiDonut)
        
        layout.addLayout(charts_layout)


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
        
        # 图表网格
        charts_layout = QVBoxLayout()
        
        # 基础仪表盘
        self.basicGauge = ChartDemoWidget('gauge', '基础仪表盘', self)
        charts_layout.addWidget(self.basicGauge)
        
        # 动画仪表盘
        self.animatedGauge = ChartDemoWidget('animated_gauge', '动画仪表盘', self)
        charts_layout.addWidget(self.animatedGauge)
        
        # 速度仪表盘
        self.speedGauge = ChartDemoWidget('speed_gauge', '速度仪表盘', self)
        charts_layout.addWidget(self.speedGauge)
        
        # 等级仪表盘
        self.levelGauge = ChartDemoWidget('level_gauge', '等级仪表盘', self)
        charts_layout.addWidget(self.levelGauge)
        
        layout.addLayout(charts_layout)


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
        
        # 图表网格
        charts_layout = QVBoxLayout()
        
        # 散点图
        self.scatter = ChartDemoWidget('scatter', '散点图', self)
        charts_layout.addWidget(self.scatter)
        
        # 雷达图
        self.radar = ChartDemoWidget('radar', '雷达图', self)
        charts_layout.addWidget(self.radar)
        
        # AQI雷达图
        self.aqiRadar = ChartDemoWidget('aqi_radar', 'AQI雷达图', self)
        charts_layout.addWidget(self.aqiRadar)
        
        layout.addLayout(charts_layout)


class Window(FluentWindow):
    """主窗口"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('图表预设接口测试')
        self.resize(1200, 800)
        
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
    w = Window()
    w.show()
    auto_close_ms = int(os.getenv("QFW_AUTO_CLOSE_MS", "0") or 0)
    if auto_close_ms > 0:
        QTimer.singleShot(auto_close_ms, app.quit)
    sys.exit(app.exec())
