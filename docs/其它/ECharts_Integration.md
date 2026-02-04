# ECharts 图表组件集成文档

## 1. 架构设计

本模块通过集成 `QWebEngineView` 与 `ECharts` 图表库，为 PySide6 应用提供高性能、交互式的图表显示功能。

### 1.1 核心组件

*   **EChartsWidget**: 继承自 `QWebEngineView`，是主要的图表显示控件。负责加载 HTML 页面、管理 WebChannel 通信以及提供 Python 端的操作接口。
*   **ChartBridge**: 一个 `QObject` 子类，充当 Python 与 JavaScript 之间的通信桥梁。通过 `QWebChannel` 暴露给前端，实现双向交互。
*   **资源管理 (ChartResource)**: 统一管理 ECharts 相关的 HTML、JS 文件路径，确保资源在打包和开发环境中均能正确加载。
*   **资源文件**:
    *   `echarts.html`: 承载图表的 HTML 模板，内置了 WebChannel 初始化和图表 resize 逻辑。
    *   `echarts.min.js`: ECharts 核心库。
    *   `qwebchannel.js`: Qt WebChannel 的 JS 客户端库。

### 1.2 通信机制

*   **Python -> JS**: 通过 `QWebEnginePage.runJavaScript()` 执行 JS 代码。主要用于：
    *   `setOption`: 更新图表配置。
    *   `resize`: 触发图表重绘。
*   **JS -> Python**: 通过 `QWebChannel` 将 Python 对象注册为 `window.bridge`。JS 端调用 `bridge` 的方法（如 `onChartClick`）将数据回传给 Python。

### 1.3 目录结构

```
qfluentwidgets/
├── components/
│   └── charts/
│       ├── __init__.py
│       └── echarts_widget.py    # EChartsWidget 实现
├── common/
│   └── chart_resource.py        # 资源路径枚举
└── _rc/
    └── html/
        ├── echarts.html         # 图表容器页面
        ├── echarts.min.js       # ECharts 库
        └── qwebchannel.js       # 通信库
```

## 2. 快速开始

### 2.1 依赖安装

确保安装了包含 WebEngine 的 PySide6 组件（通常在 `full` 模式下安装）：

```bash
pip install PySide6-Fluent-Widgets[full]
```

### 2.2 基础使用

```python
from PySide6.QtWidgets import QApplication
from qfluentwidgets.components.charts import EChartsWidget

app = QApplication([])

# 创建图表控件
chart = EChartsWidget()
chart.show()

# 设置图表选项 (标准的 ECharts Option 字典)
option = {
    'xAxis': {
        'type': 'category',
        'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    'yAxis': {
        'type': 'value'
    },
    'series': [
        {
            'data': [150, 230, 224, 218, 135, 147, 260],
            'type': 'line'
        }
    ]
}

# 应用配置
chart.setOption(option)

app.exec()
```

## 3. API 文档

### EChartsWidget

`qfluentwidgets.components.charts.EChartsWidget`

继承自 `PySide6.QtWebEngineWidgets.QWebEngineView`。

#### 信号 (Signals)

*   **chartClicked(data: dict)**
    *   当用户点击图表中的数据项时触发。
    *   `data`: 包含点击事件详细信息的字典（如 `seriesName`, `name`, `value` 等）。

#### 方法 (Methods)

*   **__init__(parent=None)**
    *   初始化图表控件。自动设置背景透明并加载 ECharts 资源。

*   **setOption(option: dict)**
    *   设置或更新图表的配置项。
    *   参数: `option` - 符合 ECharts 配置项手册的字典。
    *   说明: 支持增量更新。

*   **pushData(data: np.ndarray, seriesIndex: int = 0)**
    *   高性能数据推送方法，专门优化了 NumPy 数组的传输。
    *   参数:
        *   `data`: NumPy 数组或列表。
        *   `seriesIndex`: 要更新的系列索引，默认为 0。

## 4. 高级特性

### 4.1 动态数据更新

可以通过定时器定期调用 `setOption` 来实现动态图表：

```python
def update_chart():
    new_data = get_sensor_data()
    chart.setOption({
        'series': [{'data': new_data}]
    })

timer = QTimer()
timer.timeout.connect(update_chart)
timer.start(1000)
```

### 4.2 交互事件处理

监听图表点击事件：

```python
def on_click(data):
    print(f"Clicked value: {data['value']}")

chart.chartClicked.connect(on_click)
```

## 5. 注意事项

1.  **WebEngine 依赖**: 本组件依赖 `PySide6.QtWebEngineWidgets`。在某些精简版 Python 环境或不支持 WebEngine 的系统上可能无法运行。组件内部已做 `try-except` 处理，若无法导入将显示错误提示。
2.  **异步加载**: 图表 HTML 的加载是异步的。`EChartsWidget` 内部实现了缓存机制 (`_cachedOption`)，因此您可以安全地在 `__init__` 中立即调用 `setOption`，组件会在加载完成后自动应用配置。
3.  **资源打包**: 所有必要的 JS 库均已通过 Qt 资源系统 (`.qrc`) 打包，支持离线运行，无需互联网连接。
