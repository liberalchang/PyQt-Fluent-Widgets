Overload 方法重载模块
=======================

Overload 模块提供单分派通用方法描述符，支持基于参数类型的方法重载功能。
该模块扩展了Python的functools.singledispatch，使其能够用于类方法，实现类型安全的方法重载。

主要功能
--------

- **方法重载** - 基于参数类型的方法重载
- **类型分发** - 自动根据参数类型选择合适的实现
- **描述符支持** - 支持包装现有描述符
- **实例方法** - 处理非描述符可调用对象作为实例方法
- **抽象方法** - 支持抽象方法的分派

核心组件
--------

singledispatchmethod
~~~~~~~~~~~~~~~~~~~

单分派通用方法描述符，提供基于类型的方法重载。

.. code-block:: python

   from qfluentwidgets.common.overload import singledispatchmethod
   
   class DataProcessor:
       @singledispatchmethod
       def process(self, data):
           """默认处理方法"""
           raise TypeError(f"Unsupported type: {type(data)}")
       
       @process.register
       def _(self, data: int):
           """处理整数数据"""
           return f"Processing integer: {data * 2}"
       
       @process.register
       def _(self, data: str):
           """处理字符串数据"""
           return f"Processing string: {data.upper()}"
       
       @process.register
       def _(self, data: list):
           """处理列表数据"""
           return f"Processing list: {len(data)} items"
   
   # 使用
   processor = DataProcessor()
   print(processor.process(42))        # 调用int版本
   print(processor.process("hello"))   # 调用str版本
   print(processor.process([1, 2, 3]))  # 调用list版本

方法注册
--------

register()
~~~~~~~~~~

为特定类型注册新的实现方法。

.. code-block:: python

   from qfluentwidgets.common.overload import singledispatchmethod
   
   class Calculator:
       @singledispatchmethod
       def calculate(self, value):
           """默认计算方法"""
           return value
       
       # 注册int类型的实现
       @calculate.register
       def _(self, value: int):
           return value * 2
       
       # 注册float类型的实现
       @calculate.register
       def _(self, value: float):
           return value * 1.5
       
       # 注册str类型的实现
       @calculate.register
       def _(self, value: str):
           return len(value)
   
   # 使用
   calc = Calculator()
   print(calc.calculate(10))      # 20
   print(calc.calculate(10.5))    # 15.75
   print(calc.calculate("hello"))  # 5

实际应用
--------

数据转换器
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.overload import singledispatchmethod
   from PySide6.QtGui import QColor, QPixmap
   from PySide6.QtCore import QSize
   
   class DataConverter:
       @singledispatchmethod
       def to_string(self, value):
           """默认转换为字符串"""
           return str(value)
       
       @to_string.register
       def _(self, value: QColor):
           """QColor转换为字符串"""
           return value.name(QColor.HexArgb)
       
       @to_string.register
       def _(self, value: QSize):
           """QSize转换为字符串"""
           return f"{value.width()}x{value.height()}"
       
       @to_string.register
       def _(self, value: dict):
           """字典转换为JSON字符串"""
           import json
           return json.dumps(value, ensure_ascii=False)
   
   # 使用
   converter = DataConverter()
   print(converter.to_string(QColor(255, 0, 0)))  # #FFFF0000
   print(converter.to_string(QSize(800, 600)))     # 800x600
   print(converter.to_string({"key": "value"}))   # {"key": "value"}

UI组件工厂
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.overload import singledispatchmethod
   from qfluentwidgets import PushButton, Label, CardWidget
   from PySide6.QtWidgets import QWidget
   
   class WidgetFactory:
       @singledispatchmethod
       def create_widget(self, config):
           """默认创建方法"""
           raise TypeError(f"Unsupported config type: {type(config)}")
       
       @create_widget.register
       def _(self, config: dict):
           """根据字典配置创建控件"""
           widget_type = config.get('type', 'label')
           text = config.get('text', '')
           
           if widget_type == 'button':
               return PushButton(text)
           elif widget_type == 'label':
               return Label(text)
           else:
               return QWidget()
       
       @create_widget.register
       def _(self, config: str):
           """根据字符串创建控件"""
           return Label(config)
       
       @create_widget.register
       def _(self, config: list):
           """根据列表创建容器控件"""
           container = CardWidget()
           # 这里可以添加子控件创建逻辑
           return container
   
   # 使用
   factory = WidgetFactory()
   
   # 字典配置
   button_config = {'type': 'button', 'text': 'Click me'}
   button = factory.create_widget(button_config)
   
   # 字符串配置
   label = factory.create_widget("Hello World")
   
   # 列表配置
   container = factory.create_widget([1, 2, 3])

数据验证器
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.overload import singledispatchmethod
   
   class Validator:
       @singledispatchmethod
       def validate(self, value):
           """默认验证方法"""
           return True
       
       @validate.register
       def _(self, value: str):
           """字符串验证"""
           return len(value.strip()) > 0
       
       @validate.register
       def _(self, value: int):
           """整数验证"""
           return 0 <= value <= 100
       
       @validate.register
       def _(self, value: list):
           """列表验证"""
           return len(value) > 0 and all(isinstance(x, str) for x in value)
       
       @validate.register
       def _(self, value: type(None)):
           """None值验证"""
           return False
   
   # 使用
   validator = Validator()
   
   print(validator.validate("hello"))     # True
   print(validator.validate(""))          # False
   print(validator.validate(50))          # True
   print(validator.validate(150))         # False
   print(validator.validate(["a", "b"]))  # True
   print(validator.validate(None))        # False

高级用法
--------

复杂类型分发
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.overload import singledispatchmethod
   from typing import Union, List, Dict
   
   class AdvancedProcessor:
       @singledispatchmethod
       def process(self, data):
           """默认处理方法"""
           return f"Unknown type: {type(data)}"
       
       @process.register
       def _(self, data: List[str]):
           """处理字符串列表"""
           return f"String list with {len(data)} items: {', '.join(data)}"
       
       @process.register
       def _(self, data: List[int]):
           """处理整数列表"""
           return f"Integer list sum: {sum(data)}"
       
       @process.register
       def _(self, data: Dict[str, str]):
           """处理字符串字典"""
           return f"String dict: {len(data)} key-value pairs"
       
       @process.register
       def _(self, data: Union[int, float]):
           """处理数字类型"""
           return f"Number: {data} (type: {type(data).__name__})"
   
   # 使用
   processor = AdvancedProcessor()
   
   print(processor.process(["a", "b", "c"]))     # String list with 3 items: a, b, c
   print(processor.process([1, 2, 3, 4]))         # Integer list sum: 10
   print(processor.process({"key1": "val1"}))    # String dict: 1 key-value pairs
   print(processor.process(42))                  # Number: 42 (type: int)
   print(processor.process(3.14))                # Number: 3.14 (type: float)

继承中的重载
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.overload import singledispatchmethod
   
   class BaseProcessor:
       @singledispatchmethod
       def process(self, data):
           """基类处理方法"""
           return f"Base processing: {data}"
       
       @process.register
       def _(self, data: str):
           """基类字符串处理"""
           return f"Base string processing: {data.upper()}"
   
   class ExtendedProcessor(BaseProcessor):
       @BaseProcessor.process.register
       def _(self, data: int):
           """子类整数处理"""
           return f"Extended int processing: {data * 10}"
       
       @BaseProcessor.process.register
       def _(self, data: list):
           """子类列表处理"""
           return f"Extended list processing: {len(data)} items"
   
   # 使用
   processor = ExtendedProcessor()
   
   print(processor.process("hello"))  # Base string processing: HELLO
   print(processor.process(42))       # Extended int processing: 420
   print(processor.process([1, 2, 3])) # Extended list processing: 3 items
   print(processor.process(3.14))     # Base processing: 3.14

动态注册
~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.overload import singledispatchmethod
   
   class DynamicProcessor:
       def __init__(self):
           self.setup_dispatch()
       
       @singledispatchmethod
       def process(self, data):
           """默认处理方法"""
           return f"Default: {data}"
       
       def setup_dispatch(self):
           """动态注册处理方法"""
           
           # 注册自定义类型
           class CustomType:
               def __init__(self, value):
                   self.value = value
           
           @self.process.register
           def _(self, data: CustomType):
               return f"Custom type: {data.value}"
           
           # 注册元组类型
           @self.process.register
           def _(self, data: tuple):
               return f"Tuple with {len(data)} elements"
           
           # 注册集合类型
           @self.process.register
           def _(self, data: set):
               return f"Set with {len(data)} unique elements"
   
   # 使用
   processor = DynamicProcessor()
   
   # 测试自定义类型
   custom = processor.__class__.__module__.CustomType("test")
   print(processor.process(custom))  # Custom type: test
   
   print(processor.process((1, 2, 3)))  # Tuple with 3 elements
   print(processor.process({1, 2, 3}))   # Set with 3 unique elements

最佳实践
--------

1. **类型提示** - 使用类型注解明确支持的参数类型
2. **默认实现** - 提供合理的默认处理方法
3. **错误处理** - 在默认方法中处理不支持的类型
4. **文档字符串** - 为每个重载方法提供清晰的文档
5. **测试覆盖** - 为每个支持的类型编写测试用例

注意事项
--------

- 重载基于第一个参数的类型进行分发
- 注册的方法会覆盖默认实现
- 不支持基于多个参数的重载
- 类型匹配使用isinstance()函数
- 抽象方法也能正确处理分派

相关模块
--------

- :doc:`common.exception_handler` - 异常处理
- :doc:`common.config` - 配置管理
- :doc:`components.widgets` - UI组件
