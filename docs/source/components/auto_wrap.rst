Auto Wrap 文本自动换行模块
=============================

Auto Wrap 模块提供智能的文本自动换行功能，特别适用于中英文混合文本的处理。
该模块能够正确处理东亚字符的宽度计算，确保文本在指定宽度内合理换行。

主要功能
--------

- **字符宽度计算** - 正确识别东亚字符（宽度为2）和拉丁字符（宽度为1）
- **智能分词** - 根据字符类型进行合理的分词处理
- **自动换行** - 在指定宽度内自动换行，保持文本完整性
- **空白处理** - 智能处理多余的空白字符
- **缓存优化** - 使用 LRU 缓存提升性能

核心组件
--------

CharType
~~~~~~~~

字符类型枚举，定义字符的分类。

.. code-block:: python

   from qfluentwidgets.common.auto_wrap import CharType
   
   # 字符类型
   char_type = CharType.SPACE    # 空格字符
   char_type = CharType.ASIAN    # 东亚字符（中文、日文、韩文等）
   char_type = CharType.LATIN    # 拉丁字符（英文、数字等）

**类型说明：**
- ``SPACE`` - 空格和空白字符
- ``ASIAN`` - 东亚字符，宽度为2
- ``LATIN`` - 拉丁字符，宽度为1

TextWrap
~~~~~~~~

文本换行处理的核心类，提供静态方法进行文本处理。

.. code-block:: python

   from qfluentwidgets.common.auto_wrap import TextWrap
   
   # 基本换行
   text = "这是一个很长的中文文本，需要自动换行处理"
   wrapped_text, is_wrapped = TextWrap.wrap(text, width=20)
   
   print(f"换行结果: {wrapped_text}")
   print(f"是否换行: {is_wrapped}")

主要方法
--------

get_width()
~~~~~~~~~~

获取单个字符的显示宽度。

.. code-block:: python

   width = TextWrap.get_width('A')     # 返回 1
   width = TextWrap.get_width('中')    # 返回 2
   width = TextWrap.get_width(' ')     # 返回 1

**特点：**
- 基于 Unicode East Asian Width 属性
- 使用 LRU 缓存提升性能
- 自动处理特殊字符

get_text_width()
~~~~~~~~~~~~~~~

计算整段文本的显示宽度。

.. code-block:: python

   width = TextWrap.get_text_width("Hello 世界")  # 返回 11
   # H(1) + e(1) + l(1) + l(1) + o(1) + (1) + 世(2) + 界(2) = 11

**用途：**
- 预计算文本宽度
- 判断是否需要换行
- 布局计算

get_char_type()
~~~~~~~~~~~~~~~

获取字符的类型。

.. code-block:: python

   from qfluentwidgets.common.auto_wrap import CharType
   
   char_type = TextWrap.get_char_type('A')     # CharType.LATIN
   char_type = TextWrap.get_char_type('中')    # CharType.ASIAN
   char_type = TextWrap.get_char_type(' ')     # CharType.SPACE

wrap()
~~~~~

主要的文本换行方法。

.. code-block:: python

   text = "This is a long English text mixed with 中文 characters"
   wrapped_text, is_wrapped = TextWrap.wrap(text, width=20)
   
   # 参数说明
   # text: 要换行的文本
   # width: 最大行宽（东亚字符宽度为2）
   # once: 是否只换行一次，默认为True

**返回值：**
- ``wrapped_text`` - 换行后的文本
- ``is_wrapped`` - 是否发生了换行

**使用示例：**

.. code-block:: python

   # 示例1：基本换行
   text = "PySide6-Fluent-Widgets是一个现代化的UI组件库"
   result, wrapped = TextWrap.wrap(text, width=20)
   print(result)
   # 输出: PySide6-Fluent-Widgets是\n一个现代化的UI组件库
   
   # 示例2：只换行一次
   text = "这是一个非常长的文本，需要换行处理"
   result, wrapped = TextWrap.wrap(text, width=15, once=True)
   print(result)
   # 输出: 这是一个非常长的文本，\n需要换行处理

高级用法
--------

自定义换行逻辑
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.auto_wrap import TextWrap, CharType
   
   class CustomTextWrapper:
       def __init__(self, width=20):
           self.width = width
           
       def wrap_paragraph(self, text):
           """处理段落文本"""
           lines = []
           remaining_text = text
           
           while remaining_text:
               wrapped_line, is_wrapped = TextWrap.wrap(remaining_text, self.width)
               lines.append(wrapped_line.split('\n')[0])
               
               if is_wrapped:
                   # 移除已处理的部分
                   processed_length = len(wrapped_line.split('\n')[0])
                   remaining_text = remaining_text[processed_length:].strip()
               else:
                   break
                   
           return '\n'.join(lines)

性能优化
~~~~~~~~

TextWrap 使用了多种优化策略：

.. code-block:: python

   # 1. LRU缓存 - 自动缓存计算结果
   width = TextWrap.get_width('中')  # 第一次计算
   width = TextWrap.get_width('中')  # 从缓存获取
   
   # 2. 批量处理 - 一次处理多行文本
   multi_line_text = """第一行文本
   第二行文本
   第三行文本"""
   
   for line in multi_line_text.split('\n'):
       wrapped, _ = TextWrap.wrap(line, width=20)

实际应用
--------

UI组件中的文本换行
~~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets import Label, QVBoxLayout, QWidget
   from qfluentwidgets.common.auto_wrap import TextWrap
   
   class AutoWrapLabel(Label):
       def __init__(self, text, max_width=200):
           super().__init__()
           self.max_width = max_width
           self.setText(text)
           
       def setText(self, text):
           # 计算字符宽度（假设字符宽度为8像素）
           max_char_width = self.max_width // 8
           wrapped_text, _ = TextWrap.wrap(text, max_char_width)
           super().setText(wrapped_text)
   
   # 使用示例
   label = AutoWrapLabel("这是一个很长的标签文本，需要自动换行显示", max_width=150)

文本编辑器集成
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets import TextEdit
   from qfluentwidgets.common.auto_wrap import TextWrap
   
   class SmartTextEdit(TextEdit):
       def __init__(self):
           super().__init__()
           self.textChanged.connect(self._handle_text_change)
           
       def _handle_text_change(self):
           # 获取当前光标位置的行
           cursor = self.textCursor()
           line_number = cursor.blockNumber()
           
           # 获取该行文本
           document = self.document()
           block = document.findBlockByNumber(line_number)
           line_text = block.text()
           
           # 如果行太长，自动换行
           if TextWrap.get_text_width(line_text) > 80:
               wrapped_text, _ = TextWrap.wrap(line_text, width=80)
               # 这里可以实现自动换行逻辑

注意事项
--------

1. **宽度计算** - 东亚字符宽度为2，拉丁字符宽度为1
2. **缓存限制** - LRU缓存有大小限制，适合重复计算
3. **性能考虑** - 大量文本处理时建议分批处理
4. **空白处理** - 自动合并多余空格，保持文本整洁

相关模块
--------

- :doc:`common.font` - 字体管理
- :doc:`components.widgets` - UI组件
- :doc:`common.config` - 配置管理
