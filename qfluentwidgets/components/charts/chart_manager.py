# coding:utf-8
"""
图表管理器
提供通用的reload功能和图表管理
"""

from typing import List, Optional, Callable
from PySide6.QtCore import QObject, Signal


class ChartManager(QObject):
    """图表管理器，提供通用的reload功能"""
    
    # 信号定义
    chartReloaded = Signal()
    dataUpdated = Signal(dict)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._charts = {}  # 存储图表实例
        self._configs = {}  # 存储图表配置
        self._update_callbacks = {}  # 存储更新回调函数
    
    def register_chart(self, chart_id: str, chart_widget, config: dict, 
                   update_callback: Optional[Callable] = None):
        """
        注册图表
        
        Args:
            chart_id: 图表唯一标识
            chart_widget: 图表组件实例
            config: 图表配置
            update_callback: 数据更新回调函数
        """
        self._charts[chart_id] = chart_widget
        self._configs[chart_id] = config
        self._update_callbacks[chart_id] = update_callback
        
        # 连接页面重新加载信号
        if hasattr(chart_widget, 'pageReloaded'):
            chart_widget.pageReloaded.connect(
                lambda: self._on_chart_reloaded(chart_id)
            )
    
    def _on_chart_reloaded(self, chart_id: str):
        """处理图表页面重新加载事件"""
        print(f"[ChartManager] Chart {chart_id} reloaded, restoring configuration")
        
        if chart_id in self._configs:
            config = self._configs[chart_id]
            chart_widget = self._charts[chart_id]
            
            # 重新设置配置
            chart_widget.setOption(config)
            
            # 发出信号
            self.chartReloaded.emit()
            self.dataUpdated.emit({chart_id: config})
    
    def update_chart(self, chart_id: str, new_config: dict):
        """
        更新图表配置
        
        Args:
            chart_id: 图表唯一标识
            new_config: 新的图表配置
        """
        if chart_id in self._charts:
            self._configs[chart_id] = new_config
            chart_widget = self._charts[chart_id]
            chart_widget.setOption(new_config)
            
            # 调用更新回调
            if chart_id in self._update_callbacks and self._update_callbacks[chart_id]:
                self._update_callbacks[chart_id](new_config)
            
            # 发出信号
            self.dataUpdated.emit({chart_id: new_config})
    
    def reload_chart(self, chart_id: str):
        """
        重新加载指定图表
        
        Args:
            chart_id: 图表唯一标识
        """
        if chart_id in self._charts:
            chart_widget = self._charts[chart_id]
            # 调用图表的reload方法
            if hasattr(chart_widget, '_reload'):
                chart_widget._reload()
            else:
                # 如果没有reload方法，使用setUrl重新加载
                from ..common.chart_resource import ChartResource
                from PySide6.QtCore import QUrl
                chart_widget.setUrl(QUrl(ChartResource.ECHARTS_HTML.path()))
    
    def reload_all_charts(self):
        """重新加载所有注册的图表"""
        for chart_id in self._charts:
            self.reload_chart(chart_id)
    
    def get_chart_config(self, chart_id: str) -> Optional[dict]:
        """获取图表配置"""
        return self._configs.get(chart_id)
    
    def get_chart_widget(self, chart_id: str):
        """获取图表组件"""
        return self._charts.get(chart_id)
    
    def unregister_chart(self, chart_id: str):
        """注销图表"""
        if chart_id in self._charts:
            del self._charts[chart_id]
        if chart_id in self._configs:
            del self._configs[chart_id]
        if chart_id in self._update_callbacks:
            del self._update_callbacks[chart_id]
    
    def get_registered_charts(self) -> List[str]:
        """获取所有已注册的图表ID"""
        return list(self._charts.keys())
    
    def clear_all(self):
        """清除所有注册的图表"""
        self._charts.clear()
        self._configs.clear()
        self._update_callbacks.clear()


# 全局图表管理器实例
_global_chart_manager = ChartManager()


def get_chart_manager() -> ChartManager:
    """获取全局图表管理器实例"""
    return _global_chart_manager


# 便捷函数
def register_chart(chart_id: str, chart_widget, config: dict, 
                   update_callback: Optional[Callable] = None):
    """注册图表到全局管理器"""
    _global_chart_manager.register_chart(chart_id, chart_widget, config, update_callback)


def update_chart(chart_id: str, new_config: dict):
    """更新指定图表配置"""
    _global_chart_manager.update_chart(chart_id, new_config)


def reload_chart(chart_id: str):
    """重新加载指定图表"""
    _global_chart_manager.reload_chart(chart_id)


def reload_all_charts():
    """重新加载所有图表"""
    _global_chart_manager.reload_all_charts()


def get_chart_config(chart_id: str) -> Optional[dict]:
    """获取图表配置"""
    return _global_chart_manager.get_chart_config(chart_id)


def unregister_chart(chart_id: str):
    """注销图表"""
    _global_chart_manager.unregister_chart(chart_id)


def get_registered_charts() -> List[str]:
    """获取所有已注册的图表ID"""
    return _global_chart_manager.get_registered_charts()
