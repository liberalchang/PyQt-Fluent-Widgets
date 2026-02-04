# PySide6-Fluent-Widgets 中文文档

本目录包含了 PySide6-Fluent-Widgets 包的完整中文文档。

## 文档结构

```
docs/
├── source/                 # 文档源文件
│   ├── index.rst          # 主页
│   ├── introduction.rst   # 项目介绍
│   ├── architecture.rst   # 架构概览
│   ├── api/               # API 文档
│   ├── components/        # 组件使用指南
│   ├── code_examples/     # 示例代码
│   └── conf.py            # Sphinx 配置
├── build/                 # 构建输出目录
└── build_docs.py         # 文档构建脚本
```

## 快速开始

### 1. 安装依赖

```bash
# 激活 conda 环境
conda activate pyside6dev

# 安装 Sphinx 和相关扩展
pip install sphinx sphinx-rtd-theme sphinx-markdown-tables recommonmark
```

### 2. 构建文档

#### 方法一：使用构建脚本（推荐）

```bash
# Windows
build_docs.bat

# 或者直接运行 Python 脚本
python build_docs.py
```

#### 方法二：手动构建

```bash
# 生成 API 文档
sphinx-apidoc -o docs/source/api qfluentwidgets --force --module-first

# 构建 HTML 文档
cd docs
sphinx-build -b html source build
```

### 3. 查看文档

构建完成后，在浏览器中打开 `docs/build/index.html` 即可查看文档。

## 文档内容

### 项目介绍
- PySide6-Fluent-Widgets 简介
- 主要特性和优势
- 安装和配置方法
- 快速开始示例

### 架构概览
- 整体架构设计
- 模块组织结构
- 设计原则和理念
- 主题系统说明

### API 参考文档
- **Common 模块**: 通用工具和基础类
- **Components 模块**: UI 组件库
- **Window 模块**: 窗口相关组件
- **Multimedia 模块**: 多媒体组件

### 组件使用指南
- **基础控件**: 按钮、输入框、进度条等
- **导航组件**: 导航栏、标签页、面包屑等
- **对话框**: 消息框、文件对话框、颜色选择器等
- **设置组件**: 设置卡片、配置界面等
- **材质设计**: 亚克力效果、阴影效果等
- **图表组件**: 折线图、柱状图、饼图等
- **日期时间**: 日历、日期选择器、时间选择器等
- **布局组件**: 流式布局、分割器等
- **2D/3D 可视化**: Vispy 集成组件

### 示例代码
- 快速开始示例
- 基础组件使用示例
- 导航界面示例
- 对话框使用示例
- 设置界面示例
- 主题切换示例
- 自定义组件示例

## 自定义和扩展

### 添加新组件文档

1. 在 `docs/source/components/` 目录下创建新的 `.rst` 文件
2. 在 `docs/source/components/index.rst` 中添加到 toctree
3. 重新构建文档

### 修改样式

编辑 `docs/source/conf.py` 文件中的 HTML 主题配置：

```python
html_theme_options = {
    "sidebar_hide_name": False,
    # 其他主题选项
}
```

### 添加自定义 CSS

在 `docs/source/_static/css/` 目录下添加 CSS 文件，并在 `conf.py` 中引用：

```python
html_css_files = [
    'css/custom.css',
]
```

## 常见问题

### Q: 构建时出现编码错误？
A: 确保系统支持 UTF-8 编码，在 Windows 上可以运行 `chcp 65001`。

### Q: API 文档没有生成？
A: 检查 `qfluentwidgets` 包是否在 Python 路径中，确保能正常导入。

### Q: 文档显示异常？
A: 清理构建目录后重新构建：删除 `docs/build` 目录后重新运行构建脚本。

## 贡献指南

欢迎贡献文档改进：

1. 修正错误和改进表述
2. 添加更多示例代码
3. 完善组件使用说明
4. 添加最佳实践建议

## 许可证

文档遵循与项目相同的 LGPLv3 许可证。
