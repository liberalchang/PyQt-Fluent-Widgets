# Windows 11 Fluent Design: 色彩系统 (Color)

**最后更新**: 2025-12-29
**参考**: [Microsoft Learn - Color](https://learn.microsoft.com/zh-cn/windows/apps/design/signature-experiences/color)

## 1. 概述
色彩在 Fluent Design 中用于提供直观的视觉层级、指示状态并体现个性化。Windows 11 的色彩系统旨在支持**浅色 (Light)** 和 **深色 (Dark)** 模式的无缝切换，同时保证无障碍阅读体验。

## 2. 核心模式 (Modes)

### 2.1 浅色与深色模式
*   **浅色模式 (Light Mode)**: 默认模式，适用于光线充足的环境。背景通常为白色或浅灰色，文本为黑色。
*   **深色模式 (Dark Mode)**: 适用于低光环境或用户偏好。背景为深灰色（非纯黑），文本为白色。
*   **原则**: 应用必须同时支持两种模式，并能跟随系统设置自动切换。

## 3. 颜色角色 (Color Roles)

### 3.1 基础色 (Base Colors)
用于背景和表面，构建应用的层级结构。
*   **Alt**: 用于替代背景，通常比主背景稍深（浅色模式）或稍浅（深色模式），用于区分内容块。
*   **Solid**: 实色背景，用于不支持 Mica/Acrylic 的场景。

### 3.2 强调色 (Accent Color)
用于突出关键交互元素（如主按钮、选中状态、滑块进度条）。
*   **系统强调色**: 默认跟随用户在 Windows 设置中选择的颜色。
*   **品牌强调色**: 应用可定义自己的品牌色，但需确保在亮/暗模式下均有足够对比度。

### 3.3 语义色 (Semantic Colors)
用于传达特定状态，通常不随主题色改变：
*   **错误 (Error)**: 红色，用于警示、错误提示。
*   **成功 (Success)**: 绿色，用于完成、通过。
*   **警告 (Warning)**: 黄色/橙色，用于注意。
*   **信息 (Information)**: 蓝色，用于一般提示。

## 4. 文本颜色 (Text Colors)
文本颜色具有透明度，以适应不同背景：
*   **Primary (主要)**: 100% 不透明度 (Light: #000000, Dark: #FFFFFF)。用于标题、正文。
*   **Secondary (次要)**: ~60% 不透明度。用于副标题、说明文字。
*   **Tertiary (第三级)**: ~40% 不透明度。用于占位符、禁用文本。

## 5. 对比度与无障碍 (Accessibility)
*   **文本对比度**: 普通文本至少 4.5:1，大号文本至少 3:1。
*   **非文本对比度**: 图标和控件边界至少 3:1。

## 6. 实现建议
*   避免硬编码 HEX 值。使用系统提供的 ThemeResources 或 CSS/QSS 变量（如 `SystemControlBackgroundBaseLowBrush`）。
*   在 QSS 中定义调色板变量，通过 `qfluentdesign` 的主题引擎动态替换。
