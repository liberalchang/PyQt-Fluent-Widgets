#!/usr/bin/env python3
# coding: utf-8

import os
from xml.etree import ElementTree as ET

def find_icon_blocks(qrc_path):
    """查找所有icon prefix的qresource块"""
    tree = ET.parse(qrc_path)
    root = tree.getroot()
    
    icon_blocks = []
    for i, qresource in enumerate(root.findall('qresource')):
        prefix = qresource.get('prefix', '')
        if prefix == 'icon':
            files = [f.text.strip() for f in qresource.findall('file') if f.text]
            icon_blocks.append({
                'index': i,
                'prefix': prefix,
                'files': files,
                'element': qresource
            })
    
    return icon_blocks

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    qrc_path = os.path.join(project_root, 'qfluentwidgets', '_rc', 'resource.qrc')
    
    icon_blocks = find_icon_blocks(qrc_path)
    
    print(f"找到 {len(icon_blocks)} 个 icon prefix 的 qresource 块:")
    print("=" * 60)
    
    for i, block in enumerate(icon_blocks):
        print(f"块 {i+1} (位置 {block['index']}):")
        print(f"  文件数量: {len(block['files'])}")
        
        # 查找table_view相关的文件
        table_view_files = [f for f in block['files'] if 'table_view' in f]
        if table_view_files:
            print(f"  table_view 文件:")
            for f in table_view_files:
                print(f"    - {f}")
        
        print()

if __name__ == "__main__":
    main()
