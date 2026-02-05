Multimedia 模块 API
===================

Multimedia 模块提供媒体播放和处理功能，支持音频和视频的播放控制。
这些组件基于 Qt 的多媒体框架，提供了现代化的媒体播放界面。

主要功能：
- 媒体播放器核心
- 媒体播放控制栏
- 视频显示组件
- 音频可视化支持

使用方法：
.. code-block:: python

   from qfluentwidgets import MediaPlayer, MediaPlayBar, VideoWidget
   
   # 创建媒体播放器
   player = MediaPlayer()
   
   # 创建播放控制栏
   control_bar = MediaPlayBar()
   control_bar.setMediaPlayer(player)
   
   # 创建视频组件
   video_widget = VideoWidget()
   video_widget.setMediaPlayer(player)
   
   # 播放媒体文件
   player.setSource('path/to/media.mp4')
   player.play()

.. automodule:: qfluentwidgets.multimedia
   :members:
   :undoc-members:
   :show-inheritance:

MediaPlayer
----------

媒体播放器核心，提供媒体文件的播放和控制功能。

主要功能：
- 支持多种媒体格式
- 播放状态管理
- 音量和进度控制
- 播放列表支持

基于 Qt MediaPlayer，提供稳定的媒体播放功能。

.. automodule:: qfluentwidgets.multimedia.media_player
   :members:
   :undoc-members:
   :show-inheritance:

MediaPlayBar
-------------

媒体播放控制栏，提供用户友好的播放控制界面。

主要功能：
- 播放/暂停/停止控制
- 进度条和时间显示
- 音量控制
- 全屏切换

采用 Fluent Design 风格的控制界面。

.. automodule:: qfluentwidgets.multimedia.media_play_bar
   :members:
   :undoc-members:
   :show-inheritance:

VideoWidget
-----------

视频显示组件，用于显示视频内容。

主要功能：
- 高质量视频渲染
- 自适应尺寸调整
- 全屏播放支持
- 视频效果控制

支持各种视频格式和分辨率。

.. automodule:: qfluentwidgets.multimedia.video_widget
   :members:
   :undoc-members:
   :show-inheritance:
