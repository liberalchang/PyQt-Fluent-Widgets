# coding:utf-8
import sys
import os

# Add parent directory to sys.path to import qfluentwidgets
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtCore import Qt, QEvent
from PySide6.QtWidgets import QApplication, QLabel

from qfluentwidgets import FluentWidget


class SimpleTestWindow(FluentWidget):
    """简单的测试窗口，专门用于测试云母效果修复"""

    def __init__(self):
        super().__init__()
        
        # 设置窗口属性
        self.resize(800, 600)
        self.setWindowTitle('云母效果最大化修复测试')
        
        # 添加一个标签来显示状态
        self.statusLabel = QLabel("请尝试最大化窗口观察云母效果", self)
        self.statusLabel.setAlignment(Qt.AlignCenter)
        self.statusLabel.setStyleSheet("font-size: 18px; color: white; background: transparent;")
        
        # 启用云母效果
        self.setMicaEffectEnabled(True)
        
        print(f"窗口初始化完成 - 云母效果启用: {self.isMicaEffectEnabled()}")
        print(f"初始窗口状态: {self.windowState()}")

    def resizeEvent(self, event):
        """重写resizeEvent来更新标签位置"""
        super().resizeEvent(event)
        # 将标签居中显示
        self.statusLabel.setGeometry(0, 0, self.width(), self.height())

    def changeEvent(self, event):
        """重写changeEvent来检测窗口状态变化"""
        super().changeEvent(event)
        
        if event.type() == QEvent.WindowStateChange:
            old_state = event.oldState()
            new_state = self.windowState()
            
            print(f"窗口状态变化: {old_state} -> {new_state}")
            print(f"云母效果启用状态: {self.isMicaEffectEnabled()}")
            
            # 更新状态标签
            if self.isMaximized():
                self.statusLabel.setText("窗口已最大化\n云母效果应该保持有效\n(修复后应该重新应用)")
                print("✓ 窗口已最大化，changeEvent已触发，云母效果应该重新应用")
            elif self.isFullScreen():
                self.statusLabel.setText("窗口已全屏")
                print("窗口已全屏")
            else:
                self.statusLabel.setText("窗口已还原\n云母效果应该正常")
                print("窗口已还原")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 创建简单测试窗口
    w = SimpleTestWindow()
    w.show()
    
    print("=" * 50)
    print("云母效果最大化修复测试")
    print("=" * 50)
    print("1. 窗口已创建并启用云母效果")
    print("2. 请尝试最大化窗口")
    print("3. 观察控制台输出和云母效果变化")
    print("4. 修复后，最大化时云母效果应该自动重新应用")
    print("=" * 50)
    
    sys.exit(app.exec())
