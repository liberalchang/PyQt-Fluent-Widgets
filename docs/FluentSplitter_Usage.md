# FluentSplitter 使用文档

## 概述

`FluentSplitter` 是一个符合 Windows 11 Fluent Design 规范的分割器组件,提供优雅的界面分割和调整功能。

## 特性

- ✅ **主题色手柄**: 手柄使用主题色,与 Slider 保持一致的视觉风格
- ✅ **悬停交互**: 鼠标悬停时手柄高亮并增加宽度,提供清晰的视觉反馈
- ✅ **面板折叠**: 集成折叠按钮,支持快速折叠/展开面板
- ✅ **主题支持**: 完美支持浅色和深色主题自动切换
- ✅ **流畅动画**: 悬停和尺寸调整均带有平滑动画过渡

## 快速开始

### 基本用法

```python
from PySide6.QtCore import Qt
from qfluentwidgets import FluentSplitter

# 创建水平分割器
splitter = FluentSplitter(Qt.Horizontal)

# 添加子部件
splitter.addWidget(leftWidget)
splitter.addWidget(rightWidget)

# 设置初始尺寸比例
splitter.setSizes([300, 700])
```

### 垂直分割器

```python
# 创建垂直分割器
splitter = FluentSplitter(Qt.Vertical)

splitter.addWidget(topWidget)
splitter.addWidget(bottomWidget)
splitter.setSizes([200, 400])
```

## 详细功能

### 1. 手柄样式

手柄默认使用系统主题色:
- **默认状态**: 半透明灰色,宽度 8px
- **悬停状态**: 主题色高亮,宽度增加至 12px
- **按下状态**: 主题色加深

手柄样式会自动响应主题切换(浅色/深色模式)。

### 2. 面板折叠

每个手柄上都有一个折叠按钮:
- **水平分割器**: 显示左右箭头,折叠左侧面板
- **垂直分割器**: 显示上下箭头,折叠上侧面板

点击折叠按钮可快速折叠/展开面板,组件会自动记住折叠前的尺寸。

### 3. 自定义配置

```python
# 设置手柄宽度
splitter.setHandleWidth(10)

# 设置是否允许子部件折叠
splitter.setChildrenCollapsible(True)

# 设置方向
splitter.setOrientation(Qt.Horizontal)
```

## API 参考

### FluentSplitter

**构造函数**
```python
FluentSplitter(orientation: Qt.Orientation = Qt.Horizontal, parent: QWidget = None)
```

**参数**
- `orientation`: 分割器方向 (`Qt.Horizontal` 或 `Qt.Vertical`)
- `parent`: 父部件

**方法**

| 方法 | 说明 |
|------|------|
| `addWidget(widget)` | 添加子部件 |
| `setSizes(sizes: List[int])` | 设置各面板的尺寸 |
| `sizes() -> List[int]` | 获取各面板当前尺寸 |
| `setHandleWidth(width: int)` | 设置手柄宽度 |
| `setOrientation(orientation)` | 设置分割器方向 |
| `setChildrenCollapsible(bool)` | 设置子部件是否可折叠 |

## 样式定制

### QSS 样式

可以通过 QSS 自定义分割器样式:

```qss
FluentSplitter::handle:horizontal {
    width: 10px;
    background: rgba(0, 0, 0, 0.1);
    border-radius: 2px;
}

FluentSplitter::handle:hover {
    background: --ThemeColorPrimary;
}
```

### 主题变量

- `--ThemeColorPrimary`: 主题主色调
- `--ThemeColorLight1`: 主题色浅色变体
- `--ThemeColorDark1`: 主题色深色变体

## 完整示例

```python
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit
from qfluentwidgets import FluentSplitter

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000, 600)
        
        layout = QVBoxLayout(self)
        
        # 创建分割器
        splitter = FluentSplitter(Qt.Horizontal)
        
        # 添加三个面板
        splitter.addWidget(QTextEdit("面板 1"))
        splitter.addWidget(QTextEdit("面板 2"))
        splitter.addWidget(QTextEdit("面板 3"))
        
        # 设置初始比例 (1:2:1)
        splitter.setSizes([250, 500, 250])
        
        layout.addWidget(splitter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())
```

## 设计规范

FluentSplitter 遵循以下 Fluent Design 准则:

1. **圆角几何**: 手柄使用 2px 圆角,符合 Windows 11 设计语言
2. **主题色系统**: 使用系统主题色作为强调色
3. **交互反馈**: 悬停和按下状态提供清晰的视觉反馈
4. **动画过渡**: 100ms 缓动动画,流畅自然
5. **无障碍设计**: 手柄宽度适中(8-12px),易于操作

## 注意事项

1. 折叠功能会自动保存折叠前的尺寸,展开时恢复
2. 手柄索引从 1 开始(第一个手柄位于第一个和第二个子部件之间)
3. 主题切换时样式会自动更新,无需手动刷新
4. 建议为每个子部件设置合理的最小尺寸,避免折叠后无法展开

## 兼容性

- **PySide6**: >= 6.4.2
- **Python**: >= 3.7
- **操作系统**: Windows, macOS, Linux

## 更多信息

- 完整示例: `examples/splitter_example.py`
- 测试代码: `tests/test_splitter.py`
- 源代码: `qfluentwidgets/components/layout/splitter.py`
