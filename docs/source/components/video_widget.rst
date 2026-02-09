VideoWidget 视频控件模块
========================

VideoWidget 模块提供视频显示控件，用于视频内容的显示。支持多种视频格式和显示模式。

主要功能
--------

- **视频显示** - 支持视频内容的显示
- **格式支持** - 支持多种视频格式
- **显示控制** - 提供视频显示控制功能
- **缩放适配** - 支持视频的缩放和适配
- **性能优化** - 针对视频渲染优化

核心组件
--------

VideoWidget
~~~~~~~~~~~

视频控件，提供基础的视频显示功能。

GraphicsVideoItem
~~~~~~~~~~~~~~~~~

图形视频项控件，用于图形界面中的视频显示。

使用示例
--------

基础视频控件使用：

.. code-block:: python

   from qfluentwidgets.multimedia.video_widget import VideoWidget
   
   # 创建视频控件
   video_widget = VideoWidget()
   
   # 设置视频源
   video_widget.setSource("video.mp4")

注意事项
--------

1. **视频格式** - 确保视频格式受支持
2. **性能考虑** - 注意视频播放的性能影响
3. **显示模式** - 选择合适的视频显示模式

相关组件
--------

- :doc:`media_player` - 媒体播放器
- :doc:`media_play_bar` - 媒体播放栏
