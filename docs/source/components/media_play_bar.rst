MediaPlayBar 媒体播放栏模块
==============================

MediaPlayBar 模块提供媒体播放栏控件，用于媒体播放的控制界面。支持播放控制和音量调节。

主要功能
--------

- **播放控制** - 提供播放、暂停、停止等控制
- **音量调节** - 支持音量的调节和静音
- **进度显示** - 显示播放进度和时间
- **多种样式** - 支持简洁和标准样式
- **键盘快捷键** - 支持媒体控制快捷键

核心组件
--------

MediaPlayBarBase
~~~~~~~~~~~~~~~~

媒体播放栏基类，提供基础的播放控制功能。

**主要子类：**
- ``SimpleMediaPlayBar`` - 简洁型媒体播放栏
- ``StandardMediaPlayBar`` - 标准媒体播放栏

MediaPlayBarButton
~~~~~~~~~~~~~~~~~~

媒体播放按钮控件，用于播放控制按钮。

PlayButton
~~~~~~~~~~~

播放按钮控件，专门用于播放控制。

VolumeButton
~~~~~~~~~~~~~

音量按钮控件，用于音量调节。

使用示例
--------

基础媒体播放栏使用：

.. code-block:: python

   from qfluentwidgets.multimedia.media_play_bar import StandardMediaPlayBar
   
   # 创建媒体播放栏
   play_bar = StandardMediaPlayBar()
   
   # 连接信号
   play_bar.playButton.clicked.connect(self.on_play)

注意事项
--------

1. **信号连接** - 正确连接播放控制信号
2. **样式选择** - 根据界面选择合适的播放栏样式
3. **键盘支持** - 确保键盘快捷键正常工作

相关组件
--------

- :doc:`media_player` - 媒体播放器
- :doc:`slider` - 滑块控件
