# 交互逻辑重构设计文档

## 1. 概述
本文档描述了 Vispy 绘图组件交互逻辑的重构方案。目标是理清默认交互、选择/移动模式、以及各种绘制模式的逻辑，并实现基于控制点（Handle）的图元编辑功能。

## 2. 交互模式定义

系统支持以下交互模式（InteractionMode）：

### 2.1 默认模式 (DEFAULT)
*   **行为**：
    *   **左键按住拖动**：平移画布（Pan）。
    *   **滚轮**：以鼠标为中心缩放画布（Zoom）。
    *   **右键按住拖动**：缩放（Vispy 默认行为，可选保留）。
*   **实现**：此模式下，自定义交互管理器（InteractionManager）主要返回 `handled=False`，将事件交给底层的 Vispy `PanZoomCamera` 处理。

### 2.2 移动模式 (MOVE)
*   **行为**：
    *   **左键点击**：拾取图元。
        *   如果点击了未选中图元：选中该图元（高亮显示）。
        *   如果点击了空白处：取消所有选择。
    *   **左键按住拖动**：
        *   如果点击在已选中图元上：移动所有选中图元。
        *   移动过程中需实时更新图元位置预览。
*   **实现**：
    *   `MousePress`: 执行拾取检测（Pick）。
    *   `MouseMove`: 计算偏移量（Delta），更新选中图元位置。
    *   `MouseRelease`: 提交移动操作（Finalize）。

### 2.3 绘制模式 (DRAW_*)

#### 2.3.1 直线 (DRAW_LINE) / 多段线
*   **逻辑**：点击-移动-点击（Click-Move-Click）。
*   **流程**：
    1.  `Click 1`: 确定起点。
    2.  `Move`: 显示从上一点到当前鼠标位置的动态预览线。
    3.  `Click 2+`: 确定下一个点，线段固定，继续预览下一段。
    4.  `DoubleClick`: 结束绘制。
*   **数据**：生成 `LineData` (or `PolylineData`)。

#### 2.3.2 矩形 (DRAW_RECTANGLE)
*   **逻辑**：按住拖动（Drag-to-Draw）。
*   **流程**：
    1.  `Press`: 确定矩形的一个角点（Start Point）。
    2.  `Drag`: 实时预览矩形（Start Point 到 Current Point）。
    3.  `Release`: 确定对角点，结束绘制。
*   **数据**：生成 `RectangleData`。

#### 2.3.3 圆形 (DRAW_CIRCLE)
*   **逻辑**：按住拖动（Drag-to-Draw）。
*   **流程**：
    1.  `Press`: 确定圆心（Center）。
    2.  `Drag`: 实时预览圆形，半径为 Center 到 Current Point 的距离。
    3.  `Release`: 结束绘制。
*   **数据**：生成 `CircleData`。

#### 2.3.4 贝塞尔曲线 (DRAW_BEZIER)
*   **逻辑**：点击-移动-点击（Click-Move-Click）。
*   **流程**：
    1.  `Click 1`: 起点。
    2.  `Move`: 预览。
    3.  `Click 2...N`: 添加控制点。
    4.  `DoubleClick`: 结束绘制。
*   **特性**：曲线阶数由点数决定（N-1阶）。
*   **数据**：生成 `BezierData`。

#### 2.3.5 多边形 (DRAW_POLYGON)
*   **逻辑**：点击-移动-点击-闭合（Click-Move-Click-Close）。
*   **流程**：
    1.  `Click 1`: 起点。
    2.  `Move`: 预览边。
    3.  `Click 2...N`: 添加顶点。
    4.  `Click on Start Point` (with tolerance): 闭合多边形并结束绘制。
*   **数据**：生成 `PolygonData`。

#### 2.3.6 点 (DRAW_POINT)
*   **逻辑**：点击即生成。
*   **流程**：
    1.  `Click`: 在鼠标位置生成点图元。
*   **数据**：生成 `PointData` (or `MarkersData`)。

## 3. 图元端点控制 (Control Points / Handles)

### 3.1 需求
图元绘制接口支持传入参数（如 `with_handles=True`），控制是否生成用于编辑的端点/控制点。

### 3.2 定义
*   **直线**：2个端点 handle。
*   **矩形**：4个角点 handle。
*   **圆形**：圆心 + 边缘点（或半径控制点） handle。
*   **椭圆**：4个极点 handle (或包围盒角点)。
*   **贝塞尔/多边形**：所有顶点/控制点均为 handle。

### 3.3 实现方案
*   在 `DrawingCanvas` 的 `addPrimitive` 方法中增加 `with_handles` 参数。
*   如果 `with_handles=True`，除了创建主图元 Visual 外，还创建一组 `MarkersVisual` (点) 作为子图元或独立图元，但逻辑上关联。
*   **交互**：在移动模式或专门的编辑模式下，拖动这些 Handle 可以修改主图元的几何属性。
    *   *注：本次重构暂主要实现 Handle 的生成和显示，Handle 的交互逻辑（拖动改变形状）可作为移动模式的扩展或后续迭代。*

## 4. 架构调整

### 4.1 InteractionManager
*   **状态机清理**：移除旧的复杂状态标志，使用统一的 `State` 枚举或清晰的变量（`_drawing_step`, `_active_points`）。
*   **事件分发**：根据 `current_mode` 将事件分发到具体的 `_handle_MODE_Event` 方法。

### 4.2 DrawingCanvas
*   **Visual 管理**：增强 `addPrimitive`，支持组合图元（主 Visual + Handle Visuals）。
*   **预览更新**：提供统一的 `updatePreview(data)` 接口。

## 5. 代码生成计划
1.  重构 `InteractionManager`：实现上述所有模式的事件处理逻辑。
2.  更新 `DrawingCanvas`：适配新的信号和预览逻辑，实现 `with_handles` 的图元创建。
3.  更新 `data_models.py`（如有必要）：增加对 Handle 信息的支持（可选）。
