# 图表预设综合指南

## 概述

本文档提供了图表预设功能的完整使用指南，包括所有图表类型、管理功能和最佳实践。

## 目录结构

```
qfluentwidgets/components/charts/
├── __init__.py                    # 导出核心组件
├── echarts_widget.py              # ECharts组件
├── chart_manager.py               # 图表管理器
└── presets/
    ├── __init__.py                # 预设导出
    ├── enhanced_presets.py        # 管理版预设
    ├── line_charts.py             # 折线图预设
    ├── bar_charts.py              # 柱状图预设
    ├── pie_charts.py               # 环形图预设
    ├── scatter_charts.py           # 散点图预设
    ├── gauge_charts.py             # 仪表盘预设
    ├── radar_charts.py             # 雷达图预设
    └── ...                        # 其他预设
```

## 核心概念

### 1. 图表组件 (EChartsWidget)

基于 PySide6-WebEngine 的 ECharts 图表组件，提供：
- 高性能图表渲染
- 右键菜单支持
- 页面重载处理
- 信号通信机制

### 2. 图表管理器 (ChartManager)

提供通用的图表管理功能：
- 图表注册和管理
- 配置自动恢复
- 页面重载处理
- 全局操作支持

### 3. 预设函数

快速创建常见图表类型的函数：
- **普通预设**：基础图表配置
- **管理版预设**：自动集成管理器

## 图表类型

### 折线图

#### 基础折线图
```python
from qfluentwidgets.components.charts.presets import basic_line_chart

config = basic_line_chart(
    x_data=['1月', '2月', '3月', '4月', '5月', '6月'],
    y_data=[120, 200, 150, 80, 70, 110],
    title="月度销售数据",
    color="#5470c6"
)
```

#### 平滑折线图
```python
from qfluentwidgets.components.charts.presets import smooth_line_chart

config = smooth_line_chart(
    x_data=['周一', '周二', '周三', '周四', '周五', '周六', '周日'],
    y_data=[820, 932, 901, 934, 1290, 1330, 1320],
    title="网站访问量趋势"
)
```

#### 面积图
```python
from qfluentwidgets.components.charts.presets import area_chart

config = area_chart(
    x_data=['2010', '2011', '2012', '2013', '2014', '2015'],
    y_data=[56, 58, 62, 69, 73, 78],
    title="市场份额变化"
)
```

#### 堆叠折线图
```python
from qfluentwidgets.components.charts.presets import stacked_line_chart

x_data = ['1月', '2月', '3月', '4月', '5月', '6月']
series_data = [
    {'name': '产品A', 'data': [120, 132, 101, 134, 90, 230]},
    {'name': '产品B', 'data': [220, 182, 191, 234, 290, 330]}
]

config = stacked_line_chart(x_data, series_data, "堆叠折线图")
```

### 柱状图

#### 基础柱状图
```python
from qfluentwidgets.components.charts.presets import basic_bar_chart

config = basic_bar_chart(
    x_data=['产品A', '产品B', '产品C', '产品D', '产品E'],
    y_data=[120, 200, 150, 80, 70],
    title="产品销量对比"
)
```

#### 对齐柱状图
```python
from qfluentwidgets.components.charts.presets import aligned_bar_chart

config = aligned_bar_chart(
    x_data=['周一', '周二', '周三', '周四', '周五'],
    y_data=[120, 200, 150, 80, 70],
    title="对齐柱状图"
)
```

#### 自定义颜色柱状图
```python
from qfluentwidgets.components.charts.presets import custom_color_bar_chart

x_data = ['Q1', 'Q2', 'Q3', 'Q4']
y_data = [120, 200, 150, 80]
colors = ['#5470c6', '#91cc75', '#fac858', '#ee6666']

config = custom_color_bar_chart(x_data, y_data, colors, "自定义颜色柱状图")
```

### 环形图

#### 圆角环形图
```python
from qfluentwidgets.components.charts.presets import rounded_pie_chart

data = [
    {'name': '直接访问', 'value': 335},
    {'name': '邮件营销', 'value': 310},
    {'name': '联盟广告', 'value': 234},
    {'name': '视频广告', 'value': 135},
    {'name': '搜索引擎', 'value': 1548}
]

config = rounded_pie_chart(data, "圆角环形图")
```

#### 环形图
```python
from qfluentwidgets.components.charts.presets import donut_chart

config = donut_chart(data, "环形图")
```

#### 半环形图
```python
from qfluentwidgets.components.charts.presets import semi_donut_chart

data = [
    {'name': '已完成', 'value': 75},
    {'name': '进行中', 'value': 20},
    {'name': '待开始', 'value': 5}
]

config = semi_donut_chart(data, "半环形图")
```

### 其他图表

#### 散点图
```python
from qfluentwidgets.components.charts.presets import basic_scatter_chart

data = [
    [10.0, 8.04], [8.0, 6.95], [13.0, 7.58], [9.0, 8.81],
    [11.0, 8.33], [14.0, 9.96], [6.0, 7.24], [4.0, 4.26]
]

config = basic_scatter_chart(data, "散点图")
```

#### 雷达图
```python
from qfluentwidgets.components.charts.presets import basic_radar_chart

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
    }
]

config = basic_radar_chart(data, indicators, "雷达图")
```

#### 仪表盘
```python
from qfluentwidgets.components.charts.presets import (
    basic_gauge_chart,
    animated_gauge_chart,
    speed_gauge_chart,
    level_gauge_chart
)

# 基础仪表盘
config = basic_gauge_chart(75.5, "CPU使用率")

# 动画仪表盘
config = animated_gauge_chart(85.2, "动画仪表盘")

# 速度仪表盘
config = speed_gauge_chart(120, "速度仪表盘")

# 等级仪表盘
config = level_gauge_chart(3, "等级仪表盘")
```

## 管理版预设

管理版预设提供了与图表管理器的自动集成，支持通用reload功能。

### 特点

- ✅ 自动配置存储到管理器
- ✅ 支持页面重载后自动恢复
- ✅ 提供统一的reload接口
- ✅ 支持全局操作

### 使用方式

#### 1. 创建图表组件
```python
from qfluentwidgets.components.charts import EChartsWidget

chart = EChartsWidget()
```

#### 2. 使用管理版预设
```python
from qfluentwidgets.components.charts.presets import managed_basic_line_chart

config = managed_basic_line_chart(
    chart_id="sales_chart",
    x_data=['1月', '2月', '3月', '4月', '5月', '6月'],
    y_data=[120, 200, 150, 80, 70, 110],
    title="月度销售数据"
)
```

#### 3. 设置配置
```python
chart.setOption(config)
```

#### 4. 注册到管理器
```python
from qfluentwidgets.components.charts import get_chart_manager

manager = get_chart_manager()
manager.register_chart(
    chart_id="sales_chart",
    chart_widget=chart,
    config=config
)
```

#### 5. 使用管理功能
```python
from qfluentwidgets.components.charts import reload_chart, update_chart

# 重新加载图表
reload_chart("sales_chart")

# 更新图表数据
new_config = managed_basic_line_chart("sales_chart", new_x_data, new_y_data, "更新数据")
update_chart("sales_chart", new_config)
```

## 图表管理器

### 核心功能

#### 1. 图表注册
```python
from qfluentwidgets.components.charts import get_chart_manager

manager = get_chart_manager()
manager.register_chart(
    chart_id="my_chart",
    chart_widget=chart,
    config=config,
    update_callback=callback_function
)
```

#### 2. 配置更新
```python
manager.update_chart("my_chart", new_config)
```

#### 3. 重新加载
```python
# 单个图表
manager.reload_chart("my_chart")

# 所有图表
manager.reload_all_charts()
```

#### 4. 配置查询
```python
config = manager.get_chart_config("my_chart")
charts = manager.get_registered_charts()
```

### 信号机制

#### 1. 图表重载信号
```python
manager.chartReloaded.connect(on_chart_reloaded)

def on_chart_reloaded():
    print("图表已重新加载")
```

#### 2. 数据更新信号
```python
manager.dataUpdated.connect(on_data_updated)

def on_data_updated(updated_configs):
    for chart_id, config in updated_configs.items():
        print(f"图表 {chart_id} 数据已更新")
```

## 最佳实践

### 1. 导入方式

```python
# 核心组件
from qfluentwidgets.components.charts import EChartsWidget

# 图表管理器
from qfluentwidgets.components.charts import (
    get_chart_manager,
    reload_chart,
    update_chart
)

# 普通预设
from qfluentwidgets.components.charts.presets import (
    basic_line_chart,
    basic_bar_chart,
    donut_chart
)

# 管理版预设
from qfluentwidgets.components.charts.presets import (
    managed_basic_line_chart,
    managed_basic_bar_chart,
    managed_donut_chart
)
```

### 2. 图表ID命名

```python
# ✅ 推荐：有意义的唯一ID
chart_id = "sales_trend_2024_q1"

# ❌ 不推荐：通用ID
chart_id = "chart1"
```

### 3. 错误处理

```python
try:
    reload_chart(chart_id)
except Exception as e:
    print(f"重新加载图表失败: {e}")
```

### 4. 内存管理

```python
# 长期运行的应用建议定期清理
def cleanup_charts():
    manager = get_chart_manager()
    charts = manager.get_registered_charts()
    
    # 清理不需要的图表
    for chart_id in charts:
        if not is_chart_needed(chart_id):
            manager.unregister_chart(chart_id)
```

## 右键菜单

EChartsWidget 支持自定义右键菜单，包含以下功能：

- **Reload**：重新加载图表页面
- **Save page**：保存页面为HTML
- **Save image**：保存图表为图片
- **Copy image**：复制图表到剪贴板

## 页面重载处理

### 自动恢复机制

1. **页面重载检测**：自动监听 `pageReloaded` 信号
2. **配置恢复**：页面重载后自动恢复图表配置
3. **信号通知**：发出重载和数据更新信号

### 手动处理

```python
class MyChartWidget(QWidget):
    def __init__(self, chart_id, parent=None):
        super().__init__(parent)
        self.chart = EChartsWidget(self)
        
        # 连接重载信号
        self.chart.pageReloaded.connect(self.on_page_reloaded)
    
    def on_page_reloaded(self):
        """页面重新加载后重新初始化图表"""
        print("页面已重新加载，重新初始化图表")
        self.init_chart()
```

## 测试和验证

### 运行综合测试

```bash
# 激活环境
conda activate pyside6dev

# 运行综合测试
python tests/comprehensive_chart_presets_test.py
```

### 测试内容

综合测试包含：
- ✅ 所有图表类型的完整演示
- ✅ 数据刷新和随机数据生成
- ✅ 管理版图表的reload功能
- ✅ 右键菜单功能
- ✅ 页面重载自动恢复
- ✅ 全局操作支持

### 验证清单

- [ ] 图表正常显示
- [ ] 数据刷新功能正常
- [ ] 随机数据生成正常
- [ ] 右键菜单正常工作
- [ ] 管理版图表reload正常
- [ ] 页面重载后配置恢复
- [ ] 全局reload功能正常

## 故障排除

### 常见问题

#### 1. 图表不显示
- 检查是否正确激活了conda环境
- 确认pyside6-fluent-widgets路径正确
- 查看控制台是否有错误信息

#### 2. 右键菜单不工作
- 确认使用的是最新版本的EChartsWidget
- 检查事件过滤器是否正确安装

#### 3. Reload导致JavaScript错误
- 使用管理版预设或手动注册到管理器
- 确保图表ID唯一性

#### 4. 配置不恢复
- 确认图表已正确注册到管理器
- 检查pageReloaded信号连接

### 调试技巧

```python
# 启用详细日志
import logging
logging.basicConfig(level=logging.DEBUG)

# 检查图表注册状态
manager = get_chart_manager()
print(f"已注册图表: {manager.get_registered_charts()}")

# 检查配置存储
print(f"存储的配置: {list(manager._configs.keys())}")
```

## 扩展开发

### 添加新的预设函数

1. 在对应的预设文件中添加新函数
2. 在 `__init__.py` 中导出新函数
3. 在综合测试中添加测试用例

### 创建自定义图表

```python
class CustomChartWidget(QWidget):
    def __init__(self, chart_id, parent=None):
        super().__init__(parent)
        self.chart = EChartsWidget(self)
        
        # 使用管理器
        manager = get_chart_manager()
        config = self.create_config()
        
        manager.register_chart(chart_id, self.chart, config)
        self.chart.setOption(config)
```

## 总结

图表预设系统提供了完整的图表解决方案：

### 核心优势

1. **易用性**：预设函数快速创建常见图表
2. **可扩展性**：支持自定义图表和管理功能
3. **可靠性**：自动处理页面重载和配置恢复
4. **完整性**：涵盖所有主要图表类型

### 使用建议

- **新项目**：直接使用管理版预设
- **现有项目**：可以逐步迁移到管理版
- **简单应用**：使用普通预设即可
- **复杂应用**：使用管理器和自定义功能

---

**文档版本**：1.0  
**最后更新**：2026年3月2日  
**测试状态**：✅ 全部通过
