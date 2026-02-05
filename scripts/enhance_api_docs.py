#!/usr/bin/env python3
# coding: utf-8
"""
增强API文档内容，添加详细的模块说明
"""

import re
from pathlib import Path

def enhance_api_docs():
    """增强API文档内容"""
    
    api_dir = Path(__file__).parent.parent / 'docs' / 'source' / 'api'
    
    # 增强主要模块的API文档
    enhancements = {
        'components.rst': {
            'description': '''Components 模块是 PySide6-Fluent-Widgets 的核心，包含所有的 UI 组件。
这些组件按照功能进行了分类，包括基础控件、导航组件、对话框、设置组件等。

主要特点：
- 基于 Fluent Design 设计语言
- 支持亮色/暗色主题自动切换
- 完整的中文本地化支持
- 丰富的自定义选项和信号槽机制

使用方法：
.. code-block:: python

   from qfluentwidgets import PushButton, ComboBox, InfoBar
   
   # 创建基础组件
   button = PushButton('点击我')
   combo = ComboBox()
   
   # 连接信号
   button.clicked.connect(lambda: InfoBar.success(title='成功', content='按钮被点击'))

''',
            'modules': {
                'widgets': '''基础控件模块，包含最常用的 UI 组件。

包含38个组件文件，提供：
- 按钮组件族（23种变体）
- 输入组件族（输入框、下拉框、数值框等）
- 显示组件族（标签、卡片、图标等）
- 进度组件族（进度条、环形进度等）
- 列表和表格组件
- 菜单和工具提示组件

这些组件是构建应用界面的基础，支持完整的主题系统和交互功能。''',
                
                'navigation': '''导航组件模块，提供应用导航和布局相关的功能。

包含11个组件，提供：
- NavigationInterface：完整的导航界面框架
- Pivot：透视导航，类似标签页
- Breadcrumb：面包屑导航
- SegmentedWidget：分段控件
- NavigationPanel：可折叠的导航面板

适用于构建具有复杂导航结构的应用程序。''',
                
                'dialog_box': '''对话框组件模块，提供各种对话框和选择器。

包含11个组件，提供：
- ColorDialog：颜色选择对话框
- MessageBox：消息框
- FolderListDialog：文件夹列表对话框
- ColorPalette：颜色面板
- ScreenColorPicker：屏幕颜色选择器

支持模态和非模态对话框，提供丰富的自定义选项。''',
                
                'settings': '''设置相关组件模块，用于构建设置界面。

包含8个组件，提供：
- SettingCard：设置卡片基类
- SwitchSettingCard：开关设置卡片
- RangeSettingCard：范围设置卡片
- ComboBoxSettingCard：下拉设置卡片
- OptionsSettingCard：选项设置卡片

专门用于构建应用的设置界面，支持分组和展开功能。''',
                
                'material': '''材质设计组件模块，实现 Fluent Design 的材质效果。

包含6个组件，提供：
- AcrylicWidget：亚克力效果组件
- AcrylicMenu：亚克力菜单
- AcrylicLineEdit：亚克力输入框
- AcrylicComboBox：亚克力下拉框
- AcrylicToolTip：亚克力工具提示

实现毛玻璃效果和材质设计语言，提供现代化的视觉体验。''',
                
                'charts': '''图表组件模块，提供数据可视化功能。

包含2个组件，提供：
- EChartsWidget：基于 ECharts 的图表组件
- ChartBridge：图表桥接器

支持多种图表类型：折线图、柱状图、饼图、散点图等。
集成了 Apache ECharts，提供丰富的交互和动画效果。''',
                
                'date_time': '''日期时间组件模块，提供日期和时间选择功能。

包含6个组件，提供：
- CalendarPicker：日历选择器
- DatePicker：日期选择器
- TimePicker：时间选择器
- FastCalendarView：快速日历视图

支持多种日期格式和本地化设置，提供友好的用户界面。''',
                
                'layout': '''布局组件模块，提供自定义布局管理器。

包含5个组件，提供：
- FlowLayout：流式布局
- ExpandLayout：可展开布局
- VBoxLayout：垂直盒子布局
- FluentSplitter：分割器

这些布局管理器补充了 Qt 内置的布局，提供更灵活的界面布局选项。''',
                
                'vispy': '''2D/3D 可视化组件模块，基于 Vispy 库实现。

包含14个组件，提供：
- VispyWidget2D：2D 可视化组件
- VispyWidget3D：3D 可视化组件
- PointCloudViewer：点云查看器
- 交互式绘图工具

适用于科学计算、数据可视化和 3D 图形应用开发。'''
            }
        },
        
        'common.rst': {
            'description': '''Common 模块是 PySide6-Fluent-Widgets 的基础设施，提供整个组件库的基础功能。

主要功能：
- 动画引擎和过渡效果
- 颜色管理和主题系统
- 配置管理和持久化
- 图标管理和资源加载
- 样式表管理和主题切换
- 国际化支持

这些基础功能确保了所有组件的一致性和可扩展性。''',
            
            'modules': {
                'animation': '''动画引擎模块，提供平滑的过渡效果和动画功能。

主要类：
- AnimationBase：动画基类
- FluentAnimation：Fluent 风格动画
- 各种动画效果：平移、缩放、透明度、旋转等

支持缓动函数和动画链，提供流畅的用户体验。''',
                
                'color': '''颜色管理模块，实现主题色彩系统。

主要功能：
- Fluent Design 色彩规范
- 亮色/暗色主题自动切换
- 自定义主题色支持
- 颜色对比度计算

确保应用在不同主题下都有良好的视觉效果。''',
                
                'config': '''配置管理模块，提供应用配置的持久化存储。

主要功能：
- qconfig：全局配置对象
- 多种配置类型：字符串、数字、颜色、文件夹等
- 配置验证和序列化
- 自动保存和加载

支持配置文件的导入导出，便于用户迁移设置。''',
                
                'icon': '''图标管理模块，提供统一的图标加载和管理。

主要功能：
- FluentIcon：内置图标集合
- 多尺寸和主题适配
- 图标缓存和按需加载
- 自定义图标支持

提供完整的 Fluent Design 图标库，支持 SVG 和位图格式。''',
                
                'style_sheet': '''样式表管理模块，实现 QSS 样式的动态管理。

主要功能：
- FluentStyleSheet：样式表管理器
- 动态样式切换
- 主题样式自动应用
- 自定义样式支持

确保所有组件的视觉一致性，支持运行时样式切换。'''
            }
        }
    }
    
    for filename, content in enhancements.items():
        file_path = api_dir / filename
        
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
            
            # 在模块说明前添加详细描述
            if 'modules' in content:
                # 为每个模块添加详细说明
                for module_name, module_desc in content['modules'].items():
                    pattern = rf'({module_name}\n\n-{{10,}}\n\n)'
                    replacement = rf'\1{module_desc}\n\n'
                    file_content = re.sub(pattern, replacement, file_content)
            
            # 在文件开头添加总体描述
            if 'description' in content:
                # 在第一个 automodule 之前插入描述
                pattern = r'(\.\. automodule::)'
                replacement = f'{content["description"]}\n\n\\1'
                file_content = re.sub(pattern, replacement, file_content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(file_content)
            
            print(f"已增强 {filename}")
        else:
            print(f"文件不存在: {file_path}")

def main():
    """主函数"""
    enhance_api_docs()
    print("\nAPI文档增强完成！")

if __name__ == '__main__':
    main()
