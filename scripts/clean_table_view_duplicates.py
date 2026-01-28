#!/usr/bin/env python3
# coding: utf-8

"""
专门清理 table_view 图标重复项的脚本
"""

import os
from xml.etree import ElementTree as ET

def clean_table_view_duplicates(qrc_path):
    """清理 table_view 图标的重复项"""
    print(f"🔍 处理文件: {qrc_path}")
    
    # 备份原文件
    backup_path = qrc_path + '.backup2'
    with open(qrc_path, 'r', encoding='utf-8') as src:
        with open(backup_path, 'w', encoding='utf-8') as dst:
            dst.write(src.read())
    print(f"✅ 已备份到: {backup_path}")
    
    # 解析XML
    tree = ET.parse(qrc_path)
    root = tree.getroot()
    
    # 查找 icon prefix 的 qresource 块
    icon_qresource = None
    for qresource in root.findall('qresource'):
        if qresource.get('prefix') == 'icon':
            icon_qresource = qresource
            break
    
    if icon_qresource is None:
        print("❌ 没有找到 icon prefix 的 qresource 块")
        return False
    
    # 找到所有 table_view 文件
    table_view_files = []
    for file_elem in icon_qresource.findall('file'):
        if file_elem.text and 'table_view' in file_elem.text:
            table_view_files.append(file_elem)
    
    print(f"📊 找到 {len(table_view_files)} 个 table_view 文件")
    
    # 统计重复项
    file_counts = {}
    for file_elem in table_view_files:
        file_path = file_elem.text.strip()
        if file_path not in file_counts:
            file_counts[file_path] = []
        file_counts[file_path].append(file_elem)
    
    # 找出重复的文件
    duplicates = {path: elems for path, elems in file_counts.items() if len(elems) > 1}
    
    print(f"🔍 发现 {len(duplicates)} 个重复文件:")
    
    removed_count = 0
    for file_path, elems in duplicates.items():
        print(f"  - {file_path} (重复 {len(elems)} 次)")
        
        # 保留第一个，移除其余的
        for elem in elems[1:]:
            icon_qresource.remove(elem)
            removed_count += 1
            print(f"    ✅ 移除重复项")
    
    # 保存修改后的文件
    ET.indent(tree, space="  ", level=0)
    tree.write(qrc_path, encoding='utf-8', xml_declaration=True)
    
    print(f"✅ 清理完成，移除了 {removed_count} 个重复项")
    return True

def verify_cleanup(qrc_path):
    """验证清理结果"""
    print("\n🔍 验证清理结果:")
    
    tree = ET.parse(qrc_path)
    root = tree.getroot()
    
    # 查找 icon prefix 的 qresource 块
    icon_qresource = None
    for qresource in root.findall('qresource'):
        if qresource.get('prefix') == 'icon':
            icon_qresource = qresource
            break
    
    if icon_qresource is None:
        print("❌ 没有找到 icon prefix 的 qresource 块")
        return
    
    # 统计 table_view 文件
    table_view_files = []
    for file_elem in icon_qresource.findall('file'):
        if file_elem.text and 'table_view' in file_elem.text:
            table_view_files.append(file_elem.text.strip())
    
    print(f"📊 当前 table_view 文件数量: {len(table_view_files)}")
    
    # 检查重复
    file_counts = {}
    for file_path in table_view_files:
        file_counts[file_path] = file_counts.get(file_path, 0) + 1
    
    duplicates = {path: count for path, count in file_counts.items() if count > 1}
    
    if duplicates:
        print(f"⚠️ 仍有 {len(duplicates)} 个重复文件:")
        for file_path, count in duplicates.items():
            print(f"  - {file_path} (重复 {count} 次)")
    else:
        print("✅ 没有重复文件")
    
    # 列出所有 table_view 文件
    print("\n📋 所有 table_view 文件:")
    for file_path in sorted(set(table_view_files)):
        print(f"  - {file_path}")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    qrc_path = os.path.join(project_root, 'qfluentwidgets', '_rc', 'resource.qrc')
    
    print("🧹 清理 table_view 图标重复项")
    print("=" * 60)
    
    if clean_table_view_duplicates(qrc_path):
        verify_cleanup(qrc_path)
    else:
        print("❌ 清理失败")

if __name__ == "__main__":
    main()
