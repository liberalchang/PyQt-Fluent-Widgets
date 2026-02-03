import os
import re
import sys
import argparse

def replace_svg_color(svg_content: str, replace_color: str = "white") -> str:
    """
    修正 SVG 颜色：
    1. 替换显式的黑色/深灰色为目标颜色
    2. 给无 fill 属性的 path 标签添加 fill=目标颜色（处理隐式默认黑）
    """
    # 步骤1：替换显式的黑色/深灰色（兼容之前的场景）
    color_patterns = [
        r"black", r"#000000", r"#000", r"rgb\(0,\s*0,\s*0\)", r"rgba\(0,\s*0,\s*0,\s*[0-9.]*\)",
        r"#111111", r"#111", r"#222222", r"#222", r"#333333", r"#333"
    ]
    modified_content = svg_content
    for pattern in color_patterns:
        # 替换显式 fill/stroke 属性
        fill_attr = re.compile(rf'(fill\s*=\s*["\']){pattern}(["\'])', re.IGNORECASE)
        stroke_attr = re.compile(rf'(stroke\s*=\s*["\']){pattern}(["\'])', re.IGNORECASE)
        modified_content = fill_attr.sub(rf'\1{replace_color}\2', modified_content)
        modified_content = stroke_attr.sub(rf'\1{replace_color}\2', modified_content)
        # 替换 style 中的显式颜色
        fill_style = re.compile(rf'(style\s*=\s*["\'].*?fill\s*:\s*){pattern}(;.*?["\'])', re.IGNORECASE)
        stroke_style = re.compile(rf'(style\s*=\s*["\'].*?stroke\s*:\s*){pattern}(;.*?["\'])', re.IGNORECASE)
        modified_content = fill_style.sub(rf'\1{replace_color}\2', modified_content)
        modified_content = stroke_style.sub(rf'\1{replace_color}\2', modified_content)

    # 步骤2：给无 fill 属性的 <path> 标签添加 fill=目标颜色（核心修正）
    # 匹配 <path ...> 但不含 fill= 的标签
    path_no_fill = re.compile(r'(<path\s+)(?!.*fill\s*=)([^>]*>)', re.IGNORECASE)
    modified_content = path_no_fill.sub(rf'\1fill="{replace_color}" \2', modified_content)

    # 步骤3：兜底：给 svg 根标签设置默认 fill（防止漏网之鱼）
    svg_root = re.compile(r'(<svg\s+)([^>]*>)', re.IGNORECASE)
    if 'fill="' not in modified_content.split('<svg')[1].split('>')[0]:
        modified_content = svg_root.sub(rf'\1fill="{replace_color}" \2', modified_content)

    return modified_content

def process_svg_files(target_dir=None):
    """
    1. 重命名原SVG为 xxx_black.svg
    2. 基于 xxx_black.svg 生成 xxx_white.svg（处理隐式/显式黑色）
    """
    # 使用传入的目录路径，如果没有传入则使用当前目录
    current_dir = target_dir if target_dir else os.getcwd()
    rename_success = 0
    rename_skip = 0
    rename_error = 0
    gen_white_success = 0
    gen_white_skip = 0
    gen_white_error = 0

    print(f"开始处理目录：{current_dir}")
    print("-" * 60)

    for filename in os.listdir(current_dir):
        if os.path.isdir(filename):
            continue
        file_base, file_ext = os.path.splitext(filename)
        if file_ext.lower() != ".svg":
            continue

        # ========== 1. 重命名为 xxx_black.svg ==========
        if "_black" in file_base:
            print(f"[重命名] 跳过：{filename}（已含_black）")
            rename_skip += 1
            black_filename = filename
        else:
            black_filename = f"{file_base}_black{file_ext}"
            if os.path.exists(black_filename):
                print(f"[重命名] 跳过：{filename}（{black_filename}已存在）")
                rename_skip += 1
                continue
            try:
                os.rename(os.path.join(current_dir, filename), os.path.join(current_dir, black_filename))
                print(f"[重命名] 成功：{filename} → {black_filename}")
                rename_success += 1
            except OSError as e:
                print(f"[重命名] 失败：{filename} → {str(e)}")
                rename_error += 1
                continue

        # ========== 2. 生成 xxx_white.svg（核心修正） ==========
        white_filename = f"{file_base}_white{file_ext}"
        white_path = os.path.join(current_dir, white_filename)
        if os.path.exists(white_path):
            print(f"[生成白色版] 跳过：{black_filename} → {white_filename}（已存在）")
            gen_white_skip += 1
            continue

        # 读取原SVG
        try:
            with open(os.path.join(current_dir, black_filename), "r", encoding="utf-8") as f:
                svg_content = f.read()
        except Exception as e:
            print(f"[生成白色版] 失败：{black_filename} → 读取错误：{str(e)}")
            gen_white_error += 1
            continue

        # 修正颜色（处理隐式默认黑 + 显式黑）
        modified_svg = replace_svg_color(
            svg_content=svg_content,
            replace_color="white"  # 目标颜色：白色
        )

        # 写入白色版SVG
        try:
            with open(white_path, "w", encoding="utf-8") as f:
                f.write(modified_svg)
            print(f"[生成白色版] 成功：{black_filename} → {white_filename}（隐式/显式黑→白色）")
            gen_white_success += 1
        except Exception as e:
            print(f"[生成白色版] 失败：{black_filename} → 写入错误：{str(e)}")
            gen_white_error += 1

    # 汇总结果
    print("-" * 60)
    print("处理完成！汇总：")
    print(f"【重命名黑色版】✅ 成功：{rename_success} | ⏭️ 跳过：{rename_skip} | ❌ 失败：{rename_error}")
    print(f"【生成白色版】✅ 成功：{gen_white_success} | ⏭️ 跳过：{gen_white_skip} | ❌ 失败：{gen_white_error}")

def main():
    """主函数：解析命令行参数并执行处理"""
    parser = argparse.ArgumentParser(
        description="SVG图标颜色转换工具 - 将SVG文件转换为黑色和白色版本",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  python iconnamechange.py                    # 处理当前目录
  python iconnamechange.py /path/to/icons     # 处理指定目录
  python iconnamechange.py .                  # 处理当前目录（显式指定）
        """
    )
    
    parser.add_argument(
        'directory',
        nargs='?',  # 可选参数
        default=None,
        help='要处理的目录路径（可选，默认为当前目录）'
    )
    
    args = parser.parse_args()
    
    # 验证目录路径
    target_dir = args.directory
    if target_dir:
        if not os.path.exists(target_dir):
            print(f"错误：目录不存在：{target_dir}")
            sys.exit(1)
        if not os.path.isdir(target_dir):
            print(f"错误：不是有效目录：{target_dir}")
            sys.exit(1)
        # 转换为绝对路径
        target_dir = os.path.abspath(target_dir)
    
    # 执行处理
    process_svg_files(target_dir)

if __name__ == "__main__":
    main()
    input("\n按回车键退出...")