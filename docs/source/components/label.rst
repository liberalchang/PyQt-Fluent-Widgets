Label 标签控件模块
==================

Label 模块提供多种标签控件，用于显示文本和图像内容。支持多种样式和尺寸的标签显示。

主要功能
--------

- **多种样式** - 支持标题、正文、说明等多种文本样式
- **图像显示** - 支持图像和头像显示
- **超链接** - 支持可点击的超链接标签
- **尺寸适配** - 提供多种预设尺寸
- **主题适配** - 自动适应深色/浅色主题

核心组件
--------

FluentLabelBase
~~~~~~~~~~~~~~

Fluent标签基类，提供基础的标签功能。

**主要子类：**
- ``CaptionLabel`` - 说明标签
- ``BodyLabel`` - 正文标签  
- ``StrongBodyLabel`` - 加粗正文标签
- ``SubtitleLabel`` - 副标题标签
- ``TitleLabel`` - 标题标签
- ``LargeTitleLabel`` - 大标题标签
- ``DisplayLabel`` - 显示标签

ImageLabel
~~~~~~~~~~

图像标签控件，用于显示图像内容。

AvatarWidget
~~~~~~~~~~~~

头像控件，用于显示用户头像。

HyperlinkLabel
~~~~~~~~~~~~~~

超链接标签，支持可点击的链接。

使用示例
--------

基础标签使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.label import (
       TitleLabel, BodyLabel, CaptionLabel, SubtitleLabel
   )
   
   # 创建不同样式的标签
   title = TitleLabel("标题文本")
   body = BodyLabel("正文内容")
   caption = CaptionLabel("说明文字")
   subtitle = SubtitleLabel("副标题")

注意事项
--------

1. **样式选择** - 根据内容重要性选择合适的标签样式
2. **尺寸设置** - 标签会根据内容自动调整大小
3. **主题适配** - 标签会自动适应系统主题

相关组件
--------

- :doc:`button` - 按钮控件
- :doc:`image` - 图像控件
