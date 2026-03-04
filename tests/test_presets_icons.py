# coding:utf-8
"""
测试预设图表图标引用
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from qfluentwidgets import FluentIcon as FIF, AntDesignIcon as ADI
    
    # 测试图标是否存在
    icons_to_test = [
        ('FIF.SPEED_HIGH', FIF.SPEED_HIGH),
        ('ADI.BARCHART', ADI.BARCHART), 
        ('ADI.PIECHART', ADI.PIECHART),
        ('FIF.SPEED_OFF', FIF.SPEED_OFF),
        ('ADI.LINECHART', ADI.LINECHART),
        ('FIF.SETTING', FIF.SETTING)
    ]
    
    print("测试图表相关图标:")
    for name, icon in icons_to_test:
        try:
            print(f"✓ {name}: {icon}")
        except AttributeError as e:
            print(f"✗ {name}: 不存在 - {e}")
    
    print("\n图标测试完成！")
        
except ImportError as e:
    print(f"导入错误: {e}")
    print("请确保在正确的环境中运行此脚本")
except Exception as e:
    print(f"其他错误: {e}")
