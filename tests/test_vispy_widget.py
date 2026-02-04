# coding:utf-8
"""
Vispy Widget 测试程序

使用 FluentWindow 构建包含 2D 和 3D 场景的测试界面。

## 功能说明

### 1. 云母特效（Mica Effect）
- 本测试程序启用了 Windows 11 云母特效
- **最大化窗口支持**：重写了 resizeEvent，在窗口大小改变后自动重新应用云母特效
- **问题修复**：test_navigation.py 也已修复，使用相同的 resizeEvent 方案
- **原理说明**：Windows 在窗口大小调整时（包括最大化）会清除视觉特效，需要在 resizeEvent 中检测 _isMicaEnabled/_isAcrylicEnabled 并重新应用特效


### 2. 可见性控制组
- **作用**：动态控制场景中各个图形元素的显示/隐藏
- **使用方法**：勾选/取消勾选复选框即可显示/隐藏对应的图形元素
- **实现原理**：通过 `VispyWidget.set_visible(visual_id, visible)` 控制元素可见性
- **动态更新**：添加新图形时会自动在可见性控制组中添加对应的复选框

### 3. 2D 场景操作说明

#### 3.1 XY 平面翻转
通过翻转 X/Y 轴模拟旋转 180 度效果：
- **翻转 X 轴**：左右镜像（相当于绕 Y 轴旋转 180°）
- **翻转 Y 轴**：上下镜像（相当于绕 X 轴旋转 180°）
- **同时翻转 X 和 Y**：等效于绕 Z 轴旋转 180°

#### 3.2 自由旋转（新功能 ✨）
**操作方法**：按住 **Shift + 鼠标左键拖动** 自由旋转画布（绕 Z 轴）

**快捷旋转**：
- 点击 "90°" 按钮：旋转到 90 度
- 点击 "180°" 按钮：旋转到 180 度
- 点击 "270°" 按钮：旋转到 270 度
- 点击 "重置旋转" 按钮：恢复到 0 度

**实时显示**：旋转角度会实时显示在 "旋转: X.X°" 标签中

**API 接口**：
```python
widget2d.set_rotation(angle)    # 设置绝对角度
widget2d.rotate_by(delta)       # 增量旋转
widget2d.reset_rotation()       # 重置旋转
widget2d.get_rotation()         # 获取当前角度
```

#### 3.3 基本操作
- **鼠标左键拖动**：平移视图（不按 Shift 时）
- **鼠标滚轮**：缩放视图
- **重置视图**：点击"重置视图"按钮


### 4. 3D 场景操作
- **鼠标左键拖动**：旋转视图（TurntableCamera，支持完整的 3D 旋转）
- **鼠标右键拖动**：缩放视图
- **鼠标滚轮**：缩放视图
- **视角切换**：通过右侧控制面板的视角按钮快速切换预设视角
"""
import sys
import os
import numpy as np

# 添加父目录到路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGroupBox, QCheckBox
from qfluentwidgets import (FluentWindow, NavigationItemPosition, FluentIcon as FIF, AntDesignIcon as AIF,
                             PrimaryPushButton, PushButton, ToggleButton, Theme, setTheme, isDarkTheme)


class Scene2DInterface(QWidget):
    """2D 场景测试界面"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # 导入 VispyWidget2D（延迟导入，避免在未安装时报错）
        try:
            from qfluentwidgets import VispyWidget2D
            self.has_vispy = True
        except ImportError:
            self.has_vispy = False
            VispyWidget2D = QWidget
        
        self.setObjectName('Scene2DInterface')
        
        # 主布局
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.setContentsMargins(20, 20, 20, 20)
        self.hBoxLayout.setSpacing(20)
        
        # 左侧：Vispy 控件
        self.vispyWidget = VispyWidget2D(self) if self.has_vispy else self._create_fallback_widget()
        self.hBoxLayout.addWidget(self.vispyWidget, stretch=3)
        
        # 右侧：控制面板
        self.controlPanel = self._create_control_panel()
        self.hBoxLayout.addWidget(self.controlPanel, stretch=1)
        
        # 存储 visual IDs
        self.visual_ids = {}
        
        if self.has_vispy:
            # 初始化一些测试图形
            self._init_test_graphics()
    
    def _create_fallback_widget(self):
        """Vispy 不可用时的降级界面"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        label = QLabel("Vispy 未安装\n请运行: pip install 'PySide6-Fluent-Widgets[full]'")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 16px; color: #666;")
        layout.addWidget(label)
        return widget
    
    def _create_control_panel(self):
        """创建控制面板"""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.setAlignment(Qt.AlignTop)
        
        # 标题
        title = QLabel("2D 场景控制")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)
        
        # 操作按钮组
        btn_group = QGroupBox("操作")
        btn_layout = QVBoxLayout(btn_group)
        
        self.clearBtn = PushButton("清除所有")
        self.clearBtn.clicked.connect(self._on_clear_clicked)
        btn_layout.addWidget(self.clearBtn)
        
        self.removeLastBtn = PushButton("移除最后一个")
        self.removeLastBtn.clicked.connect(self._on_remove_last_clicked)
        btn_layout.addWidget(self.removeLastBtn)
        
        self.resetBtn = PushButton("重置视图")
        self.resetBtn.clicked.connect(self._on_reset_clicked)
        btn_layout.addWidget(self.resetBtn)
        
        self.themeBtn = ToggleButton("切换主题")
        self.themeBtn.clicked.connect(self._on_theme_clicked)
        btn_layout.addWidget(self.themeBtn)
        
        layout.addWidget(btn_group)
        
        # 添加图形组
        add_group = QGroupBox("添加图形")
        add_layout = QVBoxLayout(add_group)
        
        self.addLineBtn = PushButton("添加折线")
        self.addLineBtn.clicked.connect(self._add_sine_wave)
        add_layout.addWidget(self.addLineBtn)
        
        self.addMarkersBtn = PushButton("添加散点")
        self.addMarkersBtn.clicked.connect(self._add_random_markers)
        add_layout.addWidget(self.addMarkersBtn)
        
        self.addRectBtn = PushButton("添加矩形")
        self.addRectBtn.clicked.connect(self._add_rectangle)
        add_layout.addWidget(self.addRectBtn)
        
        self.addEllipseBtn = PushButton("添加椭圆")
        self.addEllipseBtn.clicked.connect(self._add_ellipse)
        add_layout.addWidget(self.addEllipseBtn)
        
        self.addTextBtn = PushButton("添加文本")
        self.addTextBtn.clicked.connect(self._add_text)
        add_layout.addWidget(self.addTextBtn)
        
        layout.addWidget(add_group)
        
        # 可见性控制组
        vis_group = QGroupBox("可见性")
        self.vis_layout = QVBoxLayout(vis_group)
        
        self.visCheckboxes = {}
        
        # 为初始图形添加复选框
        self._add_visibility_checkbox('sine', '正弦曲线', True)
        self._add_visibility_checkbox('cosine', '余弦曲线', True)
        self._add_visibility_checkbox('markers', '散点', True)
        self._add_visibility_checkbox('rectangle', '矩形', True)
        self._add_visibility_checkbox('text', '文本', True)
        
        layout.addWidget(vis_group)
        layout.addStretch()
        
        return panel
    
    def _add_visibility_checkbox(self, visual_id: str, label: str, checked: bool = True):
        """添加可见性控制复选框
        
        Args:
            visual_id: Visual 元素 ID
            label: 复选框标签
            checked: 初始选中状态
        """
        checkbox = QCheckBox(label)
        checkbox.setChecked(checked)
        checkbox.stateChanged.connect(lambda state: self._on_visibility_changed(visual_id, state))
        self.visCheckboxes[visual_id] = checkbox
        self.vis_layout.addWidget(checkbox)
    
    def _on_visibility_changed(self, visual_id: str, state: int):
        """可见性复选框状态改变
        
        Args:
            visual_id: Visual 元素 ID
            state: Qt.CheckState (2=选中, 0=未选中)
        """
        if self.has_vispy and visual_id in self.visual_ids:
            is_visible = (state == 2)  # Qt.Checked = 2
            self.vispyWidget.set_visible(self.visual_ids[visual_id], is_visible)
    
    def _init_test_graphics(self):
        """初始化测试图形"""
        # 添加正弦曲线
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        pos = np.column_stack([x, y])
        vid = self.vispyWidget.add_line(pos, color='red', width=2)
        self.visual_ids['sine'] = vid
        
        # 添加余弦曲线
        y2 = np.cos(x)
        pos2 = np.column_stack([x, y2])
        vid2 = self.vispyWidget.add_line(pos2, color='blue', width=2)
        self.visual_ids['cosine'] = vid2
        
        # 添加一些随机散点
        random_x = np.random.rand(50) * 10
        random_y = np.random.rand(50) * 2 - 1
        pos3 = np.column_stack([random_x, random_y])
        vid3 = self.vispyWidget.add_markers(pos3, colors='green', sizes=8, symbol='o')
        self.visual_ids['markers'] = vid3
        
        # 添加矩形
        vid4 = self.vispyWidget.add_rectangle((1, 0.5), (2, 0.5), color=(1, 1, 0, 0.3), border_color='yellow')
        self.visual_ids['rectangle'] = vid4
        
        # 添加文本
        vid5 = self.vispyWidget.add_text("2D Scene", (5, 1.5), font_size=24, color='white')
        self.visual_ids['text'] = vid5
        
        # 自动调整视图
        self.vispyWidget.auto_range()
    
    def _add_sine_wave(self):
        """添加正弦波"""
        if not self.has_vispy:
            return
        x = np.linspace(0, 10, 100)
        y = np.sin(x + np.random.rand() * 2 * np.pi)
        pos = np.column_stack([x, y])
        colors = (np.random.rand(), np.random.rand(), np.random.rand(), 1)
        vid = self.vispyWidget.add_line(pos, color=colors, width=2)
        self.vispyWidget.auto_range()
    
    def _add_random_markers(self):
        """添加随机散点"""
        if not self.has_vispy:
            return
        x = np.random.rand(30) * 10
        y = np.random.rand(30) * 2 - 1
        pos = np.column_stack([x, y])
        colors = (np.random.rand(), np.random.rand(), np.random.rand(), 1)
        vid = self.vispyWidget.add_markers(pos, colors=colors, sizes=10, symbol='s')
        self.vispyWidget.auto_range()
    
    def _add_rectangle(self):
        """添加矩形"""
        if not self.has_vispy:
            return
        pos = (np.random.rand() * 8, np.random.rand() * 1.5)
        size = (np.random.rand() * 2 + 0.5, np.random.rand() * 1 + 0.3)
        color = (np.random.rand(), np.random.rand(), np.random.rand(), 0.5)
        vid = self.vispyWidget.add_rectangle(pos, size, color=color)
        self.vispyWidget.auto_range()
    
    def _add_ellipse(self):
        """添加椭圆"""
        if not self.has_vispy:
            return
        center = (np.random.rand() * 8 + 1, np.random.rand() * 1.5)
        radius = (np.random.rand() * 0.5 + 0.2, np.random.rand() * 0.3 + 0.1)
        color = (np.random.rand(), np.random.rand(), np.random.rand(), 0.6)
        vid = self.vispyWidget.add_ellipse(center, radius, color=color)
        self.vispyWidget.auto_range()
    
    def _add_text(self):
        """添加文本"""
        if not self.has_vispy:
            return
        pos = (np.random.rand() * 8 + 1, np.random.rand() * 1.5)
        text = f"Label {np.random.randint(1, 100)}"
        vid = self.vispyWidget.add_text(text, pos, font_size=16, color='white')
        self.vispyWidget.auto_range()
    
    def _on_remove_last_clicked(self):
        """移除最后一个添加的图形"""
        if not self.has_vispy or not self.visual_ids:
            return
            
        # 获取最后一个添加的键
        last_key = list(self.visual_ids.keys())[-1]
        vid = self.visual_ids[last_key]
        
        # 从 VispyWidget 中移除
        # 使用 remove_visual(visual_id) 移除指定图形
        if self.vispyWidget.remove_visual(vid):
            # 从追踪字典中移除
            del self.visual_ids[last_key]
            
            # 如果有对应的复选框，也移除
            if last_key in self.visCheckboxes:
                checkbox = self.visCheckboxes.pop(last_key)
                self.vis_layout.removeWidget(checkbox)
                checkbox.deleteLater()

    def _on_clear_clicked(self):
        """清除所有图形"""
        if self.has_vispy:
            self.vispyWidget.clear_all()
            self.visual_ids.clear()
    
    def _on_reset_clicked(self):
        """重置视图"""
        if self.has_vispy:
            self.vispyWidget.auto_range()

    
    def _on_theme_clicked(self):
        """切换主题（同时切换全局主题和Vispy主题）"""
        is_dark = self.themeBtn.isChecked()
        
        # 切换全局主题
        setTheme(Theme.DARK if is_dark else Theme.LIGHT, save=False)
        
        # 切换Vispy控件主题
        if self.has_vispy:
            self.vispyWidget.set_theme(is_dark)
        
        # 刷新云母特效
        if hasattr(self.parent(), 'setMicaEffectEnabled'):
            self.parent().setMicaEffectEnabled(True)


class Scene3DInterface(QWidget):
    """3D 场景测试界面"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # 导入 VispyWidget3D
        try:
            from qfluentwidgets import VispyWidget3D
            self.has_vispy = True
        except ImportError:
            self.has_vispy = False
            VispyWidget3D = QWidget
        
        self.setObjectName('Scene3DInterface')
        
        # 主布局
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.setContentsMargins(20, 20, 20, 20)
        self.hBoxLayout.setSpacing(20)
        
        # 左侧：Vispy 控件
        self.vispyWidget = VispyWidget3D(self) if self.has_vispy else self._create_fallback_widget()
        self.hBoxLayout.addWidget(self.vispyWidget, stretch=3)
        
        # 右侧：控制面板
        self.controlPanel = self._create_control_panel()
        self.hBoxLayout.addWidget(self.controlPanel, stretch=1)
        
        # 存储 visual IDs
        self.visual_ids = {}
        
        if self.has_vispy:
            # 初始化一些测试图形
            self._init_test_graphics()
    
    def _create_fallback_widget(self):
        """Vispy 不可用时的降级界面"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        label = QLabel("Vispy 未安装\n请运行: pip install 'PySide6-Fluent-Widgets[full]'")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 16px; color: #666;")
        layout.addWidget(label)
        return widget
    
    def _create_control_panel(self):
        """创建控制面板"""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.setAlignment(Qt.AlignTop)
        
        # 标题
        title = QLabel("3D 场景控制")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)
        
        # 操作按钮组
        btn_group = QGroupBox("操作")
        btn_layout = QVBoxLayout(btn_group)
        
        self.clearBtn = PushButton("清除所有")
        self.clearBtn.clicked.connect(self._on_clear_clicked)
        btn_layout.addWidget(self.clearBtn)
        
        self.removeLastBtn = PushButton("移除最后一个")
        self.removeLastBtn.clicked.connect(self._on_remove_last_clicked)
        btn_layout.addWidget(self.removeLastBtn)
        
        self.resetBtn = PushButton("重置视图")
        self.resetBtn.clicked.connect(self._on_reset_clicked)
        btn_layout.addWidget(self.resetBtn)
        
        self.themeBtn = ToggleButton("切换主题")
        self.themeBtn.clicked.connect(self._on_theme_clicked)
        btn_layout.addWidget(self.themeBtn)
        
        layout.addWidget(btn_group)
        
        # 视角控制组
        view_group = QGroupBox("视角")
        view_layout = QVBoxLayout(view_group)
        
        self.viewFreeBtn = PushButton("自由视角")
        self.viewFreeBtn.clicked.connect(lambda: self._set_view('free'))
        view_layout.addWidget(self.viewFreeBtn)
        
        self.viewTopBtn = PushButton("顶视图")
        self.viewTopBtn.clicked.connect(lambda: self._set_view('top'))
        view_layout.addWidget(self.viewTopBtn)
        
        self.viewFrontBtn = PushButton("前视图")
        self.viewFrontBtn.clicked.connect(lambda: self._set_view('front'))
        view_layout.addWidget(self.viewFrontBtn)
        
        self.viewSideBtn = PushButton("侧视图")
        self.viewSideBtn.clicked.connect(lambda: self._set_view('side'))
        view_layout.addWidget(self.viewSideBtn)
        
        layout.addWidget(view_group)
        
        # 添加图形组
        add_group = QGroupBox("添加图形")
        add_layout = QVBoxLayout(add_group)
        
        self.addPointsBtn = PushButton("添加点云")
        self.addPointsBtn.clicked.connect(self._add_random_points)
        add_layout.addWidget(self.addPointsBtn)
        
        self.addLineBtn = PushButton("添加3D轨迹")
        self.addLineBtn.clicked.connect(self._add_spiral)
        add_layout.addWidget(self.addLineBtn)
        
        self.addSurfaceBtn = PushButton("添加曲面")
        self.addSurfaceBtn.clicked.connect(self._add_surface)
        add_layout.addWidget(self.addSurfaceBtn)
        
        self.addAxesBtn = PushButton("添加坐标轴")
        self.addAxesBtn.clicked.connect(self._add_axes)
        add_layout.addWidget(self.addAxesBtn)
        
        layout.addWidget(add_group)
        layout.addStretch()
        
        return panel
    
    def _init_test_graphics(self):
        """初始化测试图形"""
        # 添加随机点云
        n = 1000
        xyz = np.random.randn(n, 3) * 5
        colors = np.random.rand(n, 4)
        colors[:, 3] = 1  # alpha
        vid = self.vispyWidget.add_points(xyz, colors=colors, sizes=3)
        self.visual_ids['points'] = vid
        
        # 添加螺旋线
        t = np.linspace(0, 4 * np.pi, 200)
        x = np.cos(t) * 10
        y = np.sin(t) * 10
        z = t
        pos = np.column_stack([x, y, z])
        vid2 = self.vispyWidget.add_line3d(pos, color='red', width=3)
        self.visual_ids['spiral'] = vid2
        
        # 添加坐标轴
        vid3 = self.vispyWidget.add_axes(size=15)
        self.visual_ids['axes'] = vid3
        
        # 自动调整视图
        self.vispyWidget.auto_range()
    
    def _add_random_points(self):
        """添加随机点云"""
        if not self.has_vispy:
            return
        n = np.random.randint(500, 2000)
        xyz = np.random.randn(n, 3) * 10
        color = (np.random.rand(), np.random.rand(), np.random.rand(), 1)
        vid = self.vispyWidget.add_points(xyz, colors=color, sizes=5)
        self.vispyWidget.auto_range()
    
    def _add_spiral(self):
        """添加螺旋线"""
        if not self.has_vispy:
            return
        t = np.linspace(0, 4 * np.pi, 200)
        radius = np.random.rand() * 5 + 5
        x = np.cos(t) * radius
        y = np.sin(t) * radius
        z = t * (np.random.rand() * 2 + 1)
        pos = np.column_stack([x, y, z])
        color = (np.random.rand(), np.random.rand(), np.random.rand(), 1)
        vid = self.vispyWidget.add_line3d(pos, color=color, width=2)
        self.vispyWidget.auto_range()
    
    def _add_surface(self):
        """添加函数曲面"""
        if not self.has_vispy:
            return
        x = np.linspace(-5, 5, 50)
        y = np.linspace(-5, 5, 50)
        x, y = np.meshgrid(x, y)
        z = np.sin(np.sqrt(x**2 + y**2)) * 3
        color = (np.random.rand(), np.random.rand(), np.random.rand(), 1)
        vid = self.vispyWidget.add_surface(x, y, z, color=color, shading='smooth')
        self.vispyWidget.auto_range()
    
    def _add_axes(self):
        """添加坐标轴"""
        if not self.has_vispy:
            return
        size = np.random.rand() * 10 + 10
        vid = self.vispyWidget.add_axes(size=size)
        self.vispyWidget.auto_range()
    
    def _on_remove_last_clicked(self):
        """移除最后一个添加的图形"""
        if not self.has_vispy or not self.visual_ids:
            return
            
        # 获取最后一个添加的键
        last_key = list(self.visual_ids.keys())[-1]
        vid = self.visual_ids[last_key]
        
        # 从 VispyWidget 中移除
        if self.vispyWidget.remove_visual(vid):
            # 从追踪字典中移除
            del self.visual_ids[last_key]

    def _on_clear_clicked(self):
        """清除所有图形"""
        if self.has_vispy:
            self.vispyWidget.clear_all()
            self.visual_ids.clear()
    
    def _on_reset_clicked(self):
        """重置视图"""
        if self.has_vispy:
            self.vispyWidget.auto_range()
    
    def _on_theme_clicked(self):
        """切换主题（同时切换全局主题和Vispy主题）"""
        is_dark = self.themeBtn.isChecked()
        
        # 切换全局主题
        setTheme(Theme.DARK if is_dark else Theme.LIGHT, save=False)
        
        # 切换Vispy控件主题
        if self.has_vispy:
            self.vispyWidget.set_theme(is_dark)
        
        # 刷新云母特效
        if hasattr(self.parent(), 'setMicaEffectEnabled'):
            self.parent().setMicaEffectEnabled(True)
    
    def _set_view(self, mode: str):
        """设置视角"""
        if self.has_vispy:
            self.vispyWidget.set_view(mode)


class VispyTestWindow(FluentWindow):
    """Vispy 测试主窗口"""
    
    def __init__(self):
        super().__init__()
        
        # 启用云母特效（Windows 11）
        self.setMicaEffectEnabled(True)
        
        # 创建子界面
        self.scene2dInterface = Scene2DInterface(self)
        self.scene3dInterface = Scene3DInterface(self)
        
        # 初始化导航
        self.initNavigation()
        
        # 设置窗口属性
        self.resize(1200, 800)
        self.setWindowTitle('Vispy Widget 测试程序 - 云母特效')
    
    def initNavigation(self):
        """初始化导航栏"""
        self.addSubInterface(self.scene2dInterface, AIF.AREACHART, '2D 场景')
        self.addSubInterface(self.scene3dInterface, FIF.IOT, '3D 场景')
    
    def resizeEvent(self, e):
        """重写 resizeEvent 以确保云母特效在最大化后仍然有效"""
        super().resizeEvent(e)
        # 在 Windows 11 上重新应用云母特效（解决最大化后失效的问题）
        if hasattr(self, '_isMicaEnabled') and self._isMicaEnabled:
            # 延迟刷新云母特效，确保窗口大小调整完成
            from PySide6.QtCore import QTimer
            QTimer.singleShot(10, lambda: self.setMicaEffectEnabled(True))


if __name__ == '__main__':
    # 设置主题（可选择 Theme.LIGHT 或 Theme.DARK）
    setTheme(Theme.DARK, save=False)  # 使用暗色主题以更好展示云母特效
    
    app = QApplication(sys.argv)
    window = VispyTestWindow()
    window.show()
    sys.exit(app.exec())
