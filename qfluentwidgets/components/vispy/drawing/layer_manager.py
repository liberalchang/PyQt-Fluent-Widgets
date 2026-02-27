# coding:utf-8
"""
层级管理器模块

实现三级层级结构：图层 -> 类型分组 -> 图元
- Primitive: 图元对象，包含 visual、data、选中状态
- PrimitiveGroup: 类型分组，管理同类型图元
- Layer: 图层对象，包含多个 PrimitiveGroup
- LayerManager: 管理所有图层的顶层管理器
"""
from typing import Dict, List, Optional
from dataclasses import dataclass
import uuid

from .data_models import PrimitiveData
from ..vispy_visuals import VisualEntry


@dataclass
class Primitive:
    """图元对象
    
    封装单个图元的所有信息。
    """
    id: str                                 # 唯一标识符
    data: PrimitiveData                     # 图元数据
    visual: VisualEntry                     # Visual 渲染对象
    selected: bool = False                  # 是否选中
    type_name: str = ""                     # 类型名称
    layer_id: str = ""                      # 所属图层ID
    
    def __post_init__(self):
        """初始化后同步类型和图层信息"""
        if not self.type_name:
            self.type_name = self.data.type_name
        if not self.layer_id:
            self.layer_id = self.data.layer_id


class PrimitiveGroup:
    """类型分组类
    
    管理同一类型的图元集合。
    """
    
    def __init__(self, type_name: str, layer_id: str):
        """初始化类型分组
        
        Args:
            type_name: 类型名称（如 "line", "circle" 等）
            layer_id: 所属图层ID
        """
        self.type_name = type_name
        self.layer_id = layer_id
        self.primitives: Dict[str, Primitive] = {}  # id -> Primitive
        self._order: List[str] = []                 # 绘制顺序（ID列表）
        
    def addPrimitive(self, primitive: Primitive) -> None:
        """添加图元
        
        Args:
            primitive: 图元对象
        """
        if primitive.id in self.primitives:
            raise ValueError(f"图元ID已存在: {primitive.id}")
            
        primitive.type_name = self.type_name
        primitive.layer_id = self.layer_id
        
        self.primitives[primitive.id] = primitive
        self._order.append(primitive.id)
        
    def removePrimitive(self, primitive_id: str) -> Optional[Primitive]:
        """移除图元
        
        Args:
            primitive_id: 图元ID
            
        Returns:
            被移除的图元，如果不存在返回 None
        """
        if primitive_id not in self.primitives:
            return None
            
        primitive = self.primitives.pop(primitive_id)
        if primitive_id in self._order:
            self._order.remove(primitive_id)
            
        # 防御性措施：确保剩余图元的样式数据独立
        # 解决可能存在的样式引用共享问题
        for pid in self._order:
            if pid in self.primitives:
                p = self.primitives[pid]
                if hasattr(p.data, 'style'):
                    # 重新赋值样式以打破引用（如果是共享的）
                    # 注意：StyleData.copy() 创建新对象
                    p.data.style = p.data.style.copy()
                    
        return primitive
        
    def getPrimitive(self, primitive_id: str) -> Optional[Primitive]:
        """获取图元
        
        Args:
            primitive_id: 图元ID
            
        Returns:
            图元对象，如果不存在返回 None
        """
        return self.primitives.get(primitive_id)
        
    def getAllPrimitives(self) -> List[Primitive]:
        """获取所有图元（按绘制顺序）
        
        Returns:
            图元列表
        """
        return [self.primitives[pid] for pid in self._order if pid in self.primitives]
        
    def movePrimitive(self, primitive_id: str, new_index: int) -> bool:
        """移动图元到新位置
        
        Args:
            primitive_id: 图元ID
            new_index: 新位置索引
            
        Returns:
            是否成功移动
        """
        if primitive_id not in self._order:
            return False
            
        self._order.remove(primitive_id)
        new_index = max(0, min(new_index, len(self._order)))
        self._order.insert(new_index, primitive_id)
        return True
        
    def clear(self) -> None:
        """清空所有图元"""
        self.primitives.clear()
        self._order.clear()
        
    def __len__(self) -> int:
        return len(self.primitives)


class Layer:
    """图层类
    
    管理多个类型分组。
    """
    
    def __init__(self, layer_id: str = None, name: str = "", zorder: int = 0):
        """初始化图层
        
        Args:
            layer_id: 图层ID，如果为None则自动生成
            name: 图层名称
            zorder: 图层顺序（数值越大越靠上）
        """
        self.id = layer_id if layer_id else str(uuid.uuid4())
        self.name = name if name else f"Layer_{self.id[:8]}"
        self.zorder = zorder
        self.visible = True                     # 图层可见性
        self.locked = False                     # 图层锁定状态
        self.groups: Dict[str, PrimitiveGroup] = {}  # type_name -> PrimitiveGroup
        
    def addPrimitive(self, primitive: Primitive) -> None:
        """添加图元到对应的类型分组
        
        Args:
            primitive: 图元对象
        """
        type_name = primitive.data.type_name
        
        # 确保类型分组存在
        if type_name not in self.groups:
            self.groups[type_name] = PrimitiveGroup(type_name, self.id)
            
        self.groups[type_name].addPrimitive(primitive)
        
    def removePrimitive(self, primitive_id: str, type_name: str = None) -> Optional[Primitive]:
        """移除图元
        
        Args:
            primitive_id: 图元ID
            type_name: 类型名称（如果已知可提供以提高效率）
            
        Returns:
            被移除的图元，如果不存在返回 None
        """
        # 如果已知类型名称，直接从对应分组移除
        if type_name and type_name in self.groups:
            return self.groups[type_name].removePrimitive(primitive_id)
            
        # 否则遍历所有分组查找
        for group in self.groups.values():
            primitive = group.removePrimitive(primitive_id)
            if primitive:
                return primitive
                
        return None
        
    def getPrimitive(self, primitive_id: str, type_name: str = None) -> Optional[Primitive]:
        """获取图元
        
        Args:
            primitive_id: 图元ID
            type_name: 类型名称（如果已知可提供以提高效率）
            
        Returns:
            图元对象，如果不存在返回 None
        """
        if type_name and type_name in self.groups:
            return self.groups[type_name].getPrimitive(primitive_id)
            
        for group in self.groups.values():
            primitive = group.getPrimitive(primitive_id)
            if primitive:
                return primitive
                
        return None
        
    def getAllPrimitives(self) -> List[Primitive]:
        """获取图层中所有图元
        
        Returns:
            图元列表
        """
        primitives = []
        for group in self.groups.values():
            primitives.extend(group.getAllPrimitives())
        return primitives
        
    def getPrimitivesByType(self, type_name: str) -> List[Primitive]:
        """获取指定类型的所有图元
        
        Args:
            type_name: 类型名称
            
        Returns:
            图元列表
        """
        if type_name not in self.groups:
            return []
        return self.groups[type_name].getAllPrimitives()
        
    def clear(self) -> None:
        """清空图层中所有图元"""
        self.groups.clear()
        
    def setVisible(self, visible: bool) -> None:
        """设置图层可见性
        
        Args:
            visible: 是否可见
        """
        self.visible = visible
        # 更新所有图元的可见性
        for primitive in self.getAllPrimitives():
            if primitive.visual:
                primitive.visual.set_visible(visible and primitive.data.visible)
                
    def __len__(self) -> int:
        return sum(len(group) for group in self.groups.values())


class LayerManager:
    """图层管理器类
    
    管理所有图层的顶层管理器，提供完整的CRUD操作。
    """
    
    def __init__(self):
        """初始化图层管理器"""
        self.layers: Dict[str, Layer] = {}      # layer_id -> Layer
        self._order: List[str] = []             # 图层顺序（ID列表，顺序影响绘制）
        self._primitive_index: Dict[str, str] = {}  # primitive_id -> layer_id（快速查找）
        
        # 创建默认图层
        self._createDefaultLayer()
        
    def _createDefaultLayer(self) -> Layer:
        """创建默认图层
        
        Returns:
            默认图层对象
        """
        default_layer = Layer(name="默认图层", zorder=0)
        self.layers[default_layer.id] = default_layer
        self._order.append(default_layer.id)
        return default_layer
        
    def addLayer(self, name: str = "", zorder: int = None) -> Layer:
        """添加新图层
        
        Args:
            name: 图层名称
            zorder: 图层顺序
            
        Returns:
            新创建的图层对象
        """
        if zorder is None:
            # 默认在最上层
            zorder = max([layer.zorder for layer in self.layers.values()], default=0) + 1
            
        layer = Layer(name=name, zorder=zorder)
        self.layers[layer.id] = layer
        self._order.append(layer.id)
        self._sortLayers()
        return layer
        
    def removeLayer(self, layer_id: str) -> Optional[Layer]:
        """移除图层
        
        Args:
            layer_id: 图层ID
            
        Returns:
            被移除的图层，如果不存在返回 None
        """
        if layer_id not in self.layers:
            return None
            
        # 不允许删除最后一个图层
        if len(self.layers) <= 1:
            raise ValueError("不能删除最后一个图层")
            
        layer = self.layers.pop(layer_id)
        self._order.remove(layer_id)
        
        # 清理图元索引
        for primitive in layer.getAllPrimitives():
            self._primitive_index.pop(primitive.id, None)
            
        return layer
        
    def getLayer(self, layer_id: str) -> Optional[Layer]:
        """获取图层
        
        Args:
            layer_id: 图层ID
            
        Returns:
            图层对象，如果不存在返回 None
        """
        return self.layers.get(layer_id)
        
    def getAllLayers(self) -> List[Layer]:
        """获取所有图层（按zorder排序）
        
        Returns:
            图层列表
        """
        return [self.layers[lid] for lid in self._order if lid in self.layers]
        
    def _sortLayers(self) -> None:
        """按zorder排序图层"""
        self._order.sort(key=lambda lid: self.layers[lid].zorder if lid in self.layers else 0)
        
    def addPrimitive(self, primitive: Primitive, layer_id: str = None) -> None:
        """添加图元到指定图层
        
        Args:
            primitive: 图元对象
            layer_id: 图层ID，如果为None则添加到第一个图层
        """
        if layer_id is None:
            # 使用第一个图层
            if not self.layers:
                self._createDefaultLayer()
            layer_id = self._order[0]
            
        if layer_id not in self.layers:
            raise ValueError(f"图层不存在: {layer_id}")
            
        layer = self.layers[layer_id]
        layer.addPrimitive(primitive)
        
        # 更新索引
        self._primitive_index[primitive.id] = layer_id
        
    def removePrimitive(self, primitive_id: str) -> Optional[Primitive]:
        """移除图元
        
        Args:
            primitive_id: 图元ID
            
        Returns:
            被移除的图元，如果不存在返回 None
        """
        # 通过索引快速定位图层
        layer_id = self._primitive_index.get(primitive_id)
        if layer_id is None:
            return None
            
        layer = self.layers.get(layer_id)
        if layer is None:
            return None
            
        primitive = layer.removePrimitive(primitive_id)
        if primitive:
            self._primitive_index.pop(primitive_id, None)
            
        return primitive
        
    def getPrimitive(self, primitive_id: str) -> Optional[Primitive]:
        """获取图元
        
        Args:
            primitive_id: 图元ID
            
        Returns:
            图元对象，如果不存在返回 None
        """
        layer_id = self._primitive_index.get(primitive_id)
        if layer_id is None:
            return None
            
        layer = self.layers.get(layer_id)
        if layer is None:
            return None
            
        return layer.getPrimitive(primitive_id)
        
    def getAllPrimitives(self) -> List[Primitive]:
        """获取所有图元（按图层顺序）
        
        Returns:
            图元列表
        """
        primitives = []
        for layer in self.getAllLayers():
            if layer.visible:
                primitives.extend(layer.getAllPrimitives())
        return primitives
        
    def getPrimitivesByLayer(self, layer_id: str) -> List[Primitive]:
        """获取指定图层的所有图元
        
        Args:
            layer_id: 图层ID
            
        Returns:
            图元列表
        """
        layer = self.getLayer(layer_id)
        if layer is None:
            return []
        return layer.getAllPrimitives()
        
    def getPrimitivesByType(self, type_name: str, layer_id: str = None) -> List[Primitive]:
        """获取指定类型的图元
        
        Args:
            type_name: 类型名称
            layer_id: 图层ID，如果为None则搜索所有图层
            
        Returns:
            图元列表
        """
        if layer_id:
            layer = self.getLayer(layer_id)
            if layer is None:
                return []
            return layer.getPrimitivesByType(type_name)
        else:
            primitives = []
            for layer in self.getAllLayers():
                if layer.visible:
                    primitives.extend(layer.getPrimitivesByType(type_name))
            return primitives
            
    def movePrimitiveToLayer(self, primitive_id: str, target_layer_id: str) -> bool:
        """将图元移动到另一个图层
        
        Args:
            primitive_id: 图元ID
            target_layer_id: 目标图层ID
            
        Returns:
            是否成功移动
        """
        primitive = self.removePrimitive(primitive_id)
        if primitive is None:
            return False
            
        try:
            self.addPrimitive(primitive, target_layer_id)
            return True
        except Exception:
            # 移动失败，恢复原位置
            original_layer_id = primitive.layer_id
            self.addPrimitive(primitive, original_layer_id)
            return False
            
    def clear(self) -> None:
        """清空所有图层和图元"""
        self.layers.clear()
        self._order.clear()
        self._primitive_index.clear()
        self._createDefaultLayer()
        
    def exportData(self) -> dict:
        """导出所有图层和图元数据
        
        Returns:
            包含所有数据的字典
        """
        layers_data = []
        for layer in self.getAllLayers():
            layer_data = {
                'id': layer.id,
                'name': layer.name,
                'zorder': layer.zorder,
                'visible': layer.visible,
                'locked': layer.locked,
                'primitives': []
            }
            
            for primitive in layer.getAllPrimitives():
                primitive_data = {
                    'id': primitive.id,
                    'type': primitive.type_name,
                    'data': primitive.data,
                    'selected': primitive.selected
                }
                layer_data['primitives'].append(primitive_data)
                
            layers_data.append(layer_data)
            
        return {'layers': layers_data}
