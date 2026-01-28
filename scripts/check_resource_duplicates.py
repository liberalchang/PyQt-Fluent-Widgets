#!/usr/bin/env python3
# coding: utf-8

"""
检查和清除 resource.qrc 中的重复文件

此脚本会：
1. 读取 resource.qrc 文件
2. 检查是否有重复的文件路径
3. 列出重复项
4. 可选择性地清理重复项
"""

import os
import sys
from collections import defaultdict
from xml.etree import ElementTree as ET

def find_duplicate_files(qrc_path):
    """查找 resource.qrc 中的重复文件"""
    if not os.path.exists(qrc_path):
        print(f"❌ 文件不存在: {qrc_path}")
        return {}
    
    try:
        tree = ET.parse(qrc_path)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"❌ 解析 XML 失败: {e}")
        return {}
    
    file_counts = defaultdict(list)
    
    # 遍历所有 <file> 标签，并记录其父元素
    for qresource_elem in root.findall('qresource'):
        prefix = qresource_elem.get('prefix', '')
        for file_elem in qresource_elem.findall('file'):
            file_path = file_elem.text.strip() if file_elem.text else ""
            if file_path:
                # 存储文件元素和其父元素信息
                file_counts[file_path].append({
                    'element': file_elem,
                    'parent': qresource_elem,
                    'prefix': prefix
                })
    
    # 找出重复的文件
    duplicates = {path: items for path, items in file_counts.items() if len(items) > 1}
    
    return duplicates

def print_duplicates(duplicates):
    """打印重复文件信息"""
    if not duplicates:
        print("✅ 没有发现重复的文件")
        return
    
    print(f"🔍 发现 {len(duplicates)} 个重复的文件:")
    print("=" * 60)
    
    for i, (file_path, items) in enumerate(duplicates.items(), 1):
        print(f"{i}. {file_path}")
        print(f"   重复次数: {len(items)}")
        
        # 显示每个重复项的位置信息
        for j, item in enumerate(items, 1):
            prefix = item['prefix']
            print(f"   位置 {j}: <qresource prefix=\"{prefix}\">")
        
        print()

def remove_duplicates(qrc_path, duplicates, dry_run=True):
    """移除重复文件"""
    if not duplicates:
        print("✅ 没有重复文件需要移除")
        return True
    
    if dry_run:
        print("🔍 模拟运行 - 以下重复项将被移除:")
    else:
        print("🗑️ 开始移除重复文件...")
    
    try:
        tree = ET.parse(qrc_path)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"❌ 解析 XML 失败: {e}")
        return False
    
    removed_count = 0
    
    for file_path, items in duplicates.items():
        # 保留第一个，移除其余的
        for item in items[1:]:
            elem = item['element']
            parent = item['parent']
            if parent is not None:
                if dry_run:
                    print(f"   将移除: {file_path}")
                else:
                    parent.remove(elem)
                    print(f"   ✅ 已移除: {file_path}")
                    removed_count += 1
    
    if not dry_run:
        # 保存修改后的文件
        try:
            # 格式化输出
            ET.indent(tree, space="  ", level=0)
            tree.write(qrc_path, encoding='utf-8', xml_declaration=True)
            print(f"✅ 已保存修改后的文件，移除了 {removed_count} 个重复项")
        except Exception as e:
            print(f"❌ 保存文件失败: {e}")
            return False
    else:
        print(f"   总计将移除 {sum(len(items) - 1 for items in duplicates.values())} 个重复项")
    
    return True

def backup_file(qrc_path):
    """备份原始文件"""
    backup_path = qrc_path + '.backup'
    try:
        with open(qrc_path, 'r', encoding='utf-8') as src:
            with open(backup_path, 'w', encoding='utf-8') as dst:
                dst.write(src.read())
        print(f"✅ 已备份文件到: {backup_path}")
        return True
    except Exception as e:
        print(f"❌ 备份文件失败: {e}")
        return False

def main():
    """主函数"""
    # 获取项目根目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    qrc_path = os.path.join(project_root, 'qfluentwidgets', '_rc', 'resource.qrc')
    
    print("🔍 检查 resource.qrc 重复文件")
    print(f"📁 文件路径: {qrc_path}")
    print("=" * 60)
    
    # 检查重复文件
    duplicates = find_duplicate_files(qrc_path)
    print_duplicates(duplicates)
    
    if not duplicates:
        print("✅ resource.qrc 文件没有重复项")
        return
    
    # 询问用户是否要清理
    print("=" * 60)
    print("🤔 请选择操作:")
    print("1. 仅显示重复项 (不修改文件)")
    print("2. 备份并清理重复项")
    print("3. 退出")
    
    try:
        choice = input("请输入选择 (1/2/3): ").strip()
    except KeyboardInterrupt:
        print("\n👋 用户取消操作")
        return
    
    if choice == '1':
        print("✅ 仅显示模式，文件未被修改")
    elif choice == '2':
        # 备份文件
        if not backup_file(qrc_path):
            print("❌ 备份失败，操作取消")
            return
        
        # 清理重复项
        if remove_duplicates(qrc_path, duplicates, dry_run=False):
            print("✅ 重复文件清理完成")
            
            # 再次检查确认清理结果
            print("\n🔍 验证清理结果:")
            remaining_duplicates = find_duplicate_files(qrc_path)
            if not remaining_duplicates:
                print("✅ 确认：所有重复项已清理")
            else:
                print("⚠️ 警告：仍有重复项未清理")
                print_duplicates(remaining_duplicates)
        else:
            print("❌ 清理失败")
    elif choice == '3':
        print("👋 退出程序")
    else:
        print("❌ 无效选择")

if __name__ == "__main__":
    main()
