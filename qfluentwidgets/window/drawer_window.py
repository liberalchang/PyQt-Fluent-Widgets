# coding:utf-8
from PySide6.QtCore import Qt, QRect, QPropertyAnimation, QEasingCurve, Signal, QEvent
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget, QFrame, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QGraphicsOpacityEffect

from ..common.style_sheet import isDarkTheme
from ..common.icon import FluentIconBase, toQIcon


class Drawer(QFrame):
    """ 抽屉组件
    
    支持从四个方向（左、右、顶、底）滑出的抽屉
    """
    
    def __init__(self, parent_container: QWidget, direction: str):
        super().__init__(parent_container)
        self.parent_container = parent_container
        self.direction = direction  # left, right, top, bottom
        self.is_visible = False
        
        # 公共内容布局
        self.content_layout = QVBoxLayout()
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        
        # 初始化 UI
        self._init_ui()
        
    def _init_ui(self):
        # 基础样式
        self.setStyleSheet("Drawer { background: white; border: 1px solid #e5e5e5; border-radius: 0px; }")
        if isDarkTheme():
            self.setStyleSheet("Drawer { background: #2c2c2c; border: 1px solid #333333; border-radius: 0px; }")
            
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        # 标题栏（可选，可隐藏或自定义）
        self.title_bar = QFrame(self)
        self.title_bar_layout = QHBoxLayout(self.title_bar)
        self.title_bar_layout.setContentsMargins(16, 8, 16, 8)
        
        self.title_label = QLabel(self.title_bar)
        self.title_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        
        self.close_btn = QPushButton("×", self.title_bar)
        self.close_btn.setFixedSize(32, 32)
        self.close_btn.setCursor(Qt.PointingHandCursor)
        self.close_btn.setStyleSheet("""
            QPushButton { border: none; font-size: 20px; border-radius: 4px; }
            QPushButton:hover { background: #e5e5e5; }
            QPushButton:pressed { background: #cccccc; }
        """)
        if isDarkTheme():
            self.close_btn.setStyleSheet("""
                QPushButton { border: none; font-size: 20px; border-radius: 4px; color: white; }
                QPushButton:hover { background: #3e3e3e; }
                QPushButton:pressed { background: #4e4e4e; }
            """)
            
        self.close_btn.clicked.connect(self.hide_drawer)
        
        self.title_bar_layout.addWidget(self.title_label)
        self.title_bar_layout.addStretch(1)
        self.title_bar_layout.addWidget(self.close_btn)
        
        # 添加到主布局
        self.main_layout.addWidget(self.title_bar)
        
        # 内容容器
        self.content_widget = QWidget(self)
        self.content_widget.setLayout(self.content_layout)
        self.main_layout.addWidget(self.content_widget)
        
        # 初始隐藏状态
        self.hide()

    def set_title(self, title: str):
        self.title_label.setText(title)

    def _get_initial_rect(self):
        """ 根据方向获取初始隐藏位置 """
        container_rect = self.parent_container.rect()
        w, h = self.width(), self.height()
        
        if self.direction == "left":
            return QRect(-w, 0, w, container_rect.height())
        elif self.direction == "right":
            return QRect(container_rect.width(), 0, w, container_rect.height())
        elif self.direction == "top":
            return QRect(0, -h, container_rect.width(), h)
        elif self.direction == "bottom":
            return QRect(0, container_rect.height(), container_rect.width(), h)
        return QRect()

    def _get_target_rect(self):
        """ 根据方向获取显示位置 """
        container_rect = self.parent_container.rect()
        w, h = self.width(), self.height()
        
        if self.direction == "left":
            return QRect(0, 0, w, container_rect.height())
        elif self.direction == "right":
            return QRect(container_rect.width() - w, 0, w, container_rect.height())
        elif self.direction == "top":
            return QRect(0, 0, container_rect.width(), h)
        elif self.direction == "bottom":
            return QRect(0, container_rect.height() - h, container_rect.width(), h)
        return QRect()

    def show_drawer(self, size: int = 300):
        """ 显示抽屉
        
        :param size: 宽度（左右抽屉）或高度（顶底抽屉）
        """
        if self.is_visible:
            return
            
        self.is_visible = True
        self.raise_()
        
        # 根据方向设置大小
        if self.direction in ["left", "right"]:
            self.setFixedWidth(size)
            self.setFixedHeight(self.parent_container.height())
        else:
            self.setFixedWidth(self.parent_container.width())
            self.setFixedHeight(size)
            
        # 设置初始位置并显示
        self.setGeometry(self._get_initial_rect())
        self.show()
        
        # 动画
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(250)
        self.anim.setEasingCurve(QEasingCurve.OutQuart)
        self.anim.setEndValue(self._get_target_rect())
        self.anim.start()

    def hide_drawer(self):
        """ 隐藏抽屉 """
        if not self.is_visible:
            return
            
        self.is_visible = False
        
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(250)
        self.anim.setEasingCurve(QEasingCurve.InQuart)
        self.anim.setEndValue(self._get_initial_rect())
        self.anim.finished.connect(self._on_hide_finished)
        self.anim.start()
        
        # 通知父容器隐藏遮罩
        if isinstance(self.parent_container, DrawerWindow):
            self.parent_container._on_drawer_closed(self)

    def _on_hide_finished(self):
        self.hide()
        
    def update_geometry(self):
        """ 父容器调整大小时更新几何形状 """
        if self.is_visible:
            self.setGeometry(self._get_target_rect())


class DrawerWindow(QWidget):
    """ 带抽屉的窗口组件
    
    包含左、右、顶、底四个方向的抽屉容器
    """
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # 中心内容布局
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        # 初始化抽屉
        self.left_drawer = Drawer(self, "left")
        self.right_drawer = Drawer(self, "right")
        self.top_drawer = Drawer(self, "top")
        self.bottom_drawer = Drawer(self, "bottom")
        
        # 遮罩层
        self.mask = QFrame(self)
        self.mask.setStyleSheet("background: rgba(0, 0, 0, 0.3);")
        self.mask.hide()
        self.mask.installEventFilter(self)
        
        # 记录当前激活的抽屉
        self.active_drawer = None

    def eventFilter(self, obj, event):
        if obj == self.mask and event.type() == QEvent.MouseButtonPress:
            self.hide_all_drawers()
            return True
        return super().eventFilter(obj, event)
        
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.mask.setGeometry(self.rect())
        
        # 更新激活抽屉的几何形状
        if self.active_drawer and self.active_drawer.is_visible:
            self.active_drawer.update_geometry()

    def show_drawer(self, direction: str, size: int = 300, title: str = None):
        """ 显示指定方向的抽屉
        
        :param direction: 'left', 'right', 'top', 'bottom'
        :param size: 抽屉尺寸（宽或高）
        :param title: 抽屉标题
        """
        # 如果方向不同，关闭当前激活的抽屉
        if self.active_drawer and self.active_drawer.direction != direction:
            self.active_drawer.hide_drawer()
            
        drawer = None
        if direction == "left":
            drawer = self.left_drawer
        elif direction == "right":
            drawer = self.right_drawer
        elif direction == "top":
            drawer = self.top_drawer
        elif direction == "bottom":
            drawer = self.bottom_drawer
            
        if drawer:
            self.active_drawer = drawer
            if title:
                drawer.set_title(title)
                
            self.mask.raise_()
            self.mask.show()
            drawer.show_drawer(size)

    def hide_all_drawers(self):
        if self.active_drawer:
            self.active_drawer.hide_drawer()

    def _on_drawer_closed(self, drawer):
        # 抽屉关闭时隐藏遮罩
        self.mask.hide()
        self.active_drawer = None

    def set_central_widget(self, widget: QWidget):
        """ 设置中心内容组件 """
        # 清除现有布局项
        while self.layout.count():
            item = self.layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        self.layout.addWidget(widget)
        # 确保抽屉和遮罩在最上层
        self.mask.raise_()
        self.left_drawer.raise_()
        self.right_drawer.raise_()
        self.top_drawer.raise_()
        self.bottom_drawer.raise_()
