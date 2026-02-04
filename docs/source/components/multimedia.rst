多媒体组件 (Multimedia)
=======================

本节介绍 PySide6-Fluent-Widgets 中的多媒体相关组件。

MediaPlayer
----------

媒体播放器组件，支持音频和视频播放。

.. code-block:: python

   from qfluentwidgets import MediaPlayer
   from PySide6.QtCore import QUrl

   # 创建媒体播放器
   player = MediaPlayer()
   player.setFixedSize(600, 400)
   
   # 加载媒体文件
   player.setMedia(QUrl.fromLocalFile('path/to/video.mp4'))
   
   # 播放控制
   player.play()
   player.pause()
   player.stop()

MediaPlayBar
------------

媒体播放控制栏，提供播放控制界面。

.. code-block:: python

   from qfluentwidgets import MediaPlayBar

   # 创建播放控制栏
   play_bar = MediaPlayBar()
   play_bar.setFixedSize(600, 60)
   
   # 连接信号
   play_bar.playClicked.connect(lambda: print('播放'))
   play_bar.pauseClicked.connect(lambda: print('暂停'))
   play_bar.stopClicked.connect(lambda: print('停止'))
   play_bar.volumeChanged.connect(lambda volume: print(f'音量: {volume}'))

VideoWidget
-----------

视频显示组件，用于显示视频内容。

.. code-block:: python

   from qfluentwidgets import VideoWidget

   # 创建视频组件
   video_widget = VideoWidget()
   video_widget.setFixedSize(800, 450)
   
   # 设置视频源
   video_widget.setVideoSource('path/to/video.mp4')

完整示例
--------

下面是一个完整的多媒体组件使用示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                                QWidget, QLabel, QPushButton, QFileDialog, QSlider)
   from PySide6.QtCore import Qt, QUrl, QTimer
   from qfluentwidgets import *

   class MultimediaDemoWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           self.setWindowTitle('多媒体组件示例')
           self.resize(900, 700)
           
           # 创建界面
           self.setup_ui()

       def setup_ui(self):
           """设置界面"""
           central_widget = QWidget()
           self.setCentralWidget(central_widget)
           
           layout = QVBoxLayout(central_widget)
           
           # 添加标题
           title = SubtitleLabel('多媒体组件示例')
           layout.addWidget(title)
           
           # 创建媒体播放器
           self.setup_media_player(layout)
           
           # 创建播放控制栏
           self.setup_play_bar(layout)

       def setup_media_player(self, layout):
           """设置媒体播放器"""
           # 视频显示区域
           video_group = QGroupBox('视频播放器')
           video_layout = QVBoxLayout(video_group)
           
           # 创建视频组件
           self.video_widget = VideoWidget()
           self.video_widget.setFixedSize(800, 450)
           self.video_widget.setStyleSheet("""
               VideoWidget {
                   background-color: black;
                   border: 2px solid #ddd;
                   border-radius: 8px;
               }
           """)
           video_layout.addWidget(self.video_widget)
           
           # 文件选择按钮
           file_layout = QHBoxLayout()
           
           self.file_label = QLabel('未选择文件')
           self.file_label.setStyleSheet('color: #666;')
           
           select_btn = PrimaryPushButton('选择视频文件')
           select_btn.clicked.connect(self.select_video_file)
           
           file_layout.addWidget(self.file_label)
           file_layout.addWidget(select_btn)
           file_layout.addStretch()
           
           video_layout.addLayout(file_layout)
           
           layout.addWidget(video_group)

       def setup_play_bar(self, layout):
           """设置播放控制栏"""
           control_group = QGroupBox('播放控制')
           control_layout = QVBoxLayout(control_group)
           
           # 创建播放控制栏
           self.play_bar = MediaPlayBar()
           self.play_bar.setFixedHeight(80)
           control_layout.addWidget(self.play_bar)
           
           # 进度条
           progress_layout = QHBoxLayout()
           
           progress_label = QLabel('进度:')
           self.progress_slider = QSlider(Qt.Horizontal)
           self.progress_slider.setRange(0, 100)
           self.progress_slider.setValue(0)
           
           self.time_label = QLabel('00:00 / 00:00')
           self.time_label.setStyleSheet('color: #666;')
           
           progress_layout.addWidget(progress_label)
           progress_layout.addWidget(self.progress_slider)
           progress_layout.addWidget(self.time_label)
           
           control_layout.addLayout(progress_layout)
           
           # 音量控制
           volume_layout = QHBoxLayout()
           
           volume_label = QLabel('音量:')
           self.volume_slider = QSlider(Qt.Horizontal)
           self.volume_slider.setRange(0, 100)
           self.volume_slider.setValue(50)
           self.volume_slider.setFixedWidth(150)
           
           self.volume_value_label = QLabel('50%')
           
           volume_layout.addWidget(volume_label)
           volume_layout.addWidget(self.volume_slider)
           volume_layout.addWidget(self.volume_value_label)
           volume_layout.addStretch()
           
           control_layout.addLayout(volume_layout)
           
           # 连接信号
           self.play_bar.playClicked.connect(self.play_video)
           self.play_bar.pauseClicked.connect(self.pause_video)
           self.play_bar.stopClicked.connect(self.stop_video)
           
           self.progress_slider.valueChanged.connect(self.seek_video)
           self.volume_slider.valueChanged.connect(self.change_volume)
           
           # 创建定时器更新进度
           self.progress_timer = QTimer()
           self.progress_timer.timeout.connect(self.update_progress)
           
           layout.addWidget(control_group)

       def select_video_file(self):
           """选择视频文件"""
           file_path, _ = QFileDialog.getOpenFileName(
               self,
               '选择视频文件',
               '',
               '视频文件 (*.mp4 *.avi *.mkv *.mov);;所有文件 (*.*)'
           )
           
           if file_path:
               self.file_label.setText(f'已选择: {file_path}')
               self.video_widget.setVideoSource(file_path)
               InfoBar.success('视频文件加载成功', parent=self)

       def play_video(self):
           """播放视频"""
           if hasattr(self.video_widget, 'play'):
               self.video_widget.play()
               self.progress_timer.start(1000)  # 每秒更新一次
               InfoBar.info('开始播放', parent=self)

       def pause_video(self):
           """暂停视频"""
           if hasattr(self.video_widget, 'pause'):
               self.video_widget.pause()
               self.progress_timer.stop()
               InfoBar.info('暂停播放', parent=self)

       def stop_video(self):
           """停止视频"""
           if hasattr(self.video_widget, 'stop'):
               self.video_widget.stop()
               self.progress_timer.stop()
               self.progress_slider.setValue(0)
               InfoBar.info('停止播放', parent=self)

       def seek_video(self, position):
           """跳转到指定位置"""
           if hasattr(self.video_widget, 'setPosition'):
               # 假设视频总时长为100秒
               duration = 100
               seek_time = (position / 100) * duration
               self.video_widget.setPosition(seek_time)

       def change_volume(self, volume):
           """改变音量"""
           self.volume_value_label.setText(f'{volume}%')
           if hasattr(self.video_widget, 'setVolume'):
               self.video_widget.setVolume(volume)

       def update_progress(self):
           """更新播放进度"""
           if hasattr(self.video_widget, 'position') and hasattr(self.video_widget, 'duration'):
               current_time = self.video_widget.position()
               total_time = self.video_widget.duration()
               
               if total_time > 0:
                   progress = int((current_time / total_time) * 100)
                   self.progress_slider.setValue(progress)
                   
                   # 更新时间显示
                   current_str = self.format_time(current_time)
                   total_str = self.format_time(total_time)
                   self.time_label.setText(f'{current_str} / {total_str}')

       def format_time(self, seconds):
           """格式化时间显示"""
           minutes = int(seconds // 60)
           seconds = int(seconds % 60)
           return f'{minutes:02d}:{seconds:02d}'

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       window = MultimediaDemoWindow()
       window.show()
       sys.exit(app.exec())

最佳实践
--------

1. **文件格式支持**: 
   - 支持常见的视频格式 (MP4, AVI, MKV, MOV)
   - 支持常见的音频格式 (MP3, WAV, FLAC)
   - 提供格式转换建议

2. **用户体验**: 
   - 提供清晰的播放控制界面
   - 支持键盘快捷键控制
   - 显示播放进度和时间信息

3. **性能优化**: 
   - 合理设置缓冲区大小
   - 处理大文件的加载
   - 优化内存使用

4. **错误处理**: 
   - 处理文件不存在的情况
   - 处理格式不支持的情况
   - 提供友好的错误提示

依赖要求
--------

使用多媒体组件可能需要安装额外的解码器：

.. code-block:: bash

   # Windows 通常自带解码器
   # Linux 可能需要安装
   sudo apt-get install libavcodec-extra
   
   # macOS 通常自带支持
