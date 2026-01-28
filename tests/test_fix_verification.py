# coding:utf-8
"""
测试脚本：验证FluentWindow最大化后云母效果修复
"""

import sys
import os

# Add parent directory to sys.path to import qfluentwidgets
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_change_event_import():
    """测试QEvent是否正确导入"""
    try:
        from PySide6.QtCore import QEvent
        print("✓ QEvent导入成功")
        return True
    except ImportError as e:
        print(f"✗ QEvent导入失败: {e}")
        return False

def test_fluent_widget_change_event():
    """测试FluentWidget是否有changeEvent方法"""
    try:
        from qfluentwidgets import FluentWidget
        import inspect
        
        # 检查FluentWidget类是否有changeEvent方法
        if hasattr(FluentWidget, 'changeEvent'):
            # 获取方法源码
            source = inspect.getsource(FluentWidget.changeEvent)
            if 'WindowStateChange' in source:
                print("✓ FluentWidget.changeEvent方法包含WindowStateChange处理")
                print(f"方法源码:\n{source}")
                return True
            else:
                print("✗ FluentWidget.changeEvent方法存在但不包含WindowStateChange处理")
                return False
        else:
            print("✗ FluentWidget类没有changeEvent方法")
            return False
            
    except Exception as e:
        print(f"✗ 测试FluentWidget.changeEvent失败: {e}")
        return False

def test_window_effect_methods():
    """测试窗口效果相关方法"""
    try:
        from qfluentwidgets import FluentWidget
        import inspect
        
        methods = ['setMicaEffectEnabled', 'isMicaEffectEnabled', 'setAcrylicEffectEnabled', 'isAcrylicEffectEnabled']
        
        for method in methods:
            if hasattr(FluentWidget, method):
                print(f"✓ FluentWidget.{method}方法存在")
            else:
                print(f"✗ FluentWidget.{method}方法不存在")
                return False
                
        return True
        
    except Exception as e:
        print(f"✗ 测试窗口效果方法失败: {e}")
        return False

def main():
    """主测试函数"""
    print("=" * 60)
    print("FluentWindow最大化云母效果修复验证")
    print("=" * 60)
    
    tests = [
        ("QEvent导入测试", test_change_event_import),
        ("FluentWidget.changeEvent测试", test_fluent_widget_change_event),
        ("窗口效果方法测试", test_window_effect_methods),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        print("-" * 40)
        try:
            result = test_func()
            results.append(result)
        except Exception as e:
            print(f"✗ 测试异常: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    print("测试结果总结:")
    print("=" * 60)
    
    passed = sum(results)
    total = len(results)
    
    for i, (test_name, _) in enumerate(tests):
        status = "✓ 通过" if results[i] else "✗ 失败"
        print(f"{test_name}: {status}")
    
    print(f"\n总计: {passed}/{total} 测试通过")
    
    if passed == total:
        print("\n🎉 所有测试通过！修复应该正常工作。")
        print("\n修复说明:")
        print("- 在FluentWidget中添加了changeEvent方法")
        print("- 监听QEvent.WindowStateChange事件")
        print("- 在窗口状态变化时自动重新应用云母/亚克力效果")
        print("- 这应该解决最大化后云母效果失效的问题")
    else:
        print("\n❌ 部分测试失败，修复可能不完整。")
    
    print("=" * 60)

if __name__ == '__main__':
    main()
