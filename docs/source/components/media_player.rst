MediaPlayer 媒体播放器模块
============================

MediaPlayer 模块提供媒体播放器控件，用于音频和视频的播放。支持多种媒体格式和控制功能。

主要功能
--------

- **媒体播放** - 支持音频和视频播放
- **格式支持** - 支持多种媒体格式
- **播放控制** - 提供完整的播放控制功能
- **音视频同步** - 确保音视频同步播放
- **性能优化** - 针对媒体播放优化

核心组件
--------

MediaPlayer
~~~~~~~~~~~

媒体播放器控件，提供基础的媒体播放功能。

MediaPlayerBase
~~~~~~~~~~~~~~~~

媒体播放器基类，提供基础的播放功能。

使用示例
--------

基础媒体播放器使用：

.. code-block:: python

   from qfluentwidgets.multimedia.media_player import MediaPlayer
   
   # 创建媒体播放器
   player = MediaPlayer()
   
   # 加载媒体文件
   player.setSource("video.mp4")
   
   # 开始播放
   player.play()

注意事项
--------

1. **媒体格式** - 确保媒体格式受支持
2. **资源管理** - 注意媒体资源的内存管理
3. **错误处理** - 妥善处理播放错误

相关组件
--------

- :doc:`media_play_bar` - 媒体播放栏
- :doc:`video_widget` - 视频控件
