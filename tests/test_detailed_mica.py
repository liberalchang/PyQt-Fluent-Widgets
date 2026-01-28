# coding:utf-8
"""
详细测试：验证云母效果的视觉表现
"""

import sys
import os

# Add parent directory to sys.path to import qfluentwidgets
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtCore import Qt, QEvent, QTimer
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QColor

from qfluentwidgets.window.fluent_window import FluentWidget


class DetailedMicaTest(FluentWidget):
    """详细的云母效果测试窗口"""

    def __init__(self):
        super().__init__()
        
        # 设置窗口属性
        self.resize(700, 500)
        self.setWindowTitle('云母效果详细测试')
        
        # 创建主布局
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        
        # 状态标签
        self.statusLabel = QLabel("云母效果状态检测", self)
        self.statusLabel.setStyleSheet("""
            font-size: 16px; 
            font-weight: bold; 
            color: #0078D4; 
            background: rgba(255,255,255,0.9); 
            padding: 15px; 
            border-radius: 8px;
            border: 2px solid #0078D4;
        """)
        
        # 效果详情标签
        self.detailLabel = QLabel("等待检测...", self)
        self.detailLabel.setStyleSheet("""
            font-size: 14px; 
            color: #333; 
            background: rgba(255,255,255,0.8); 
            padding: 10px; 
            border-radius: 5px;
        """)
        self.detailLabel.setWordWrap(True)
        
        # 手动测试按钮
        self.testBtn = QPushButton("手动重新应用云母效果", self)
        self.testBtn.clicked.connect(self.manual_apply_mica)
        self.testBtn.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                padding: 12px;
                background: #0078D4;
                color: white;
                border: none;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: #106EBE;
            }
            QPushButton:pressed {
                background: #005A9E;
            }
        """)
        
        # 切换主题按钮
        self.themeBtn = QPushButton("切换主题测试", self)
        self.themeBtn.clicked.connect(self.toggle_theme)
        self.themeBtn.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                padding: 12px;
                background: #107C10;
                color: white;
                border: none;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: #0E5F0A;
            }
        """)
        
        # 添加到布局
        layout.addWidget(self.statusLabel)
        layout.addWidget(self.detailLabel)
        layout.addWidget(self.testBtn)
        layout.addWidget(self.themeBtn)
        layout.addStretch()
        
        self.setCentralWidget(central_widget)
        
        # 启用云母效果
        print("正在启用云母效果...")
        self.setMicaEffectEnabled(True)
        
        # 延迟检查初始状态
        QTimer.singleShot(500, self.check_mica_status)
        
        print("窗口初始化完成")

    def manual_apply_mica(self):
        """手动重新应用云母效果"""
        print("\n=== 手动重新应用云母效果 ===")
        self._reapplyWindowEffect()
        QTimer.singleShot(200, self.check_mica_status)

    def toggle_theme(self):
        """切换主题测试"""
        from qfluentwidgets.common.style_sheet import isDarkTheme, setTheme, Theme
        current_theme = Theme.DARK if isDarkTheme() else Theme.LIGHT
        new_theme = Theme.LIGHT if isDarkTheme() else Theme.DARK
        setTheme(new_theme)
        print(f"主题切换: {current_theme} -> {new_theme}")
        
        # 重新应用云母效果
        QTimer.singleShot(100, self._reapplyWindowEffect)
        QTimer.singleShot(300, self.check_mica_status)

    def check_mica_status(self):
        """检查云母效果状态"""
        print("\n=== 云母效果状态检查 ===")
        
        # 检查各种状态
        mica_enabled = self.isMicaEffectEnabled()
        translucent = self.testAttribute(Qt.WA_TranslucentBackground)
        bg_color = self.backgroundColor if hasattr(self, 'backgroundColor') else "未知"
        window_state = self.windowState()
        
        print(f"云母效果启用: {mica_enabled}")
        print(f"透明背景属性: {translucent}")
        print(f"背景颜色: {bg_color}")
        print(f"窗口状态: {window_state}")
        
        # 更新UI
        if mica_enabled and translucent:
            self.statusLabel.setText("✅ 云母效果已启用")
            self.statusLabel.setStyleSheet("""
                font-size: 16px; 
                font-weight: bold; 
                color: #107C10; 
                background: rgba(255,255,255,0.9); 
                padding: 15px; 
                border-radius: 8px;
                border: 2px solid #107C10;
            """)
            
            self.detailLabel.setText(
                f"✅ 云母效果状态良好\n"
                f"• 效果启用: {mica_enabled}\n"
                f"• 透明背景: {translucent}\n"
                f"• 背景颜色: {bg_color}\n"
                f"• 窗口状态: {window_state}\n\n"
                f"如果背景仍然显示为白色，可能是：\n"
                f"1. Windows版本不支持云母效果\n"
                f"2. 需要重启应用才能看到效果\n"
                f"3. 系统主题设置影响"
            )
        else:
            self.statusLabel.setText("❌ 云母效果异常")
            self.statusLabel.setStyleSheet("""
                font-size: 16px; 
                font-weight: bold; 
                color: #D13438; 
                background: rgba(255,255,255,0.9); 
                padding: 15px; 
                border-radius: 8px;
                border: 2px solid #D13438;
            """)
            
            self.detailLabel.setText(
                f"❌ 云母效果状态异常\n"
                f"• 效果启用: {mica_enabled}\n"
                f"• 透明背景: {translucent}\n"
                f"• 背景颜色: {bg_color}\n"
                f"• 窗口状态: {window_state}\n\n"
                f"可能的问题：\n"
                f"1. Windows版本不支持（需要Win11 Build 22000+）\n"
                f"2. 系统设置中禁用了透明效果\n"
                f"3. 显卡驱动不支持"
            )

    def changeEvent(self, event):
        super().changeEvent(event)
        
        if event.type() == QEvent.WindowStateChange:
            print(f"窗口状态变化: {self.windowState()}")
            # 延迟检查状态
            QTimer.singleShot(300, self.check_mica_status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    print("=" * 60)
    print("云母效果详细测试")
    print("=" * 60)
    print("1. 检查云母效果是否正确启用")
    print("2. 测试窗口最大化时的效果保持")
    print("3. 提供手动重新应用和主题切换功能")
    print("=" * 60)
    
    w = DetailedMicaTest()
    w.show()
    
    sys.exit(app.exec())
