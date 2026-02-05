Exception Handler 异常处理模块
===============================

Exception Handler 模块提供异常处理装饰器，用于优雅地处理函数执行过程中可能出现的异常。
该模块通过装饰器模式提供统一的异常处理机制，确保应用在遇到异常时能够优雅地恢复。

主要功能
--------

- **异常捕获** - 自动捕获函数执行中的所有异常
- **默认值返回** - 异常发生时返回预设的默认值
- **装饰器模式** - 通过装饰器简化异常处理代码
- **深度复制** - 确保默认值的安全性
- **智能返回** - 根据默认值数量智能返回

核心组件
--------

exceptionHandler
~~~~~~~~~~~~~~~

异常处理装饰器，为函数提供异常处理能力。

.. code-block:: python

   from qfluentwidgets.common.exception_handler import exceptionHandler
   
   # 基本用法
   @exceptionHandler("默认值")
   def risky_function():
       # 可能抛出异常的代码
       return 1 / 0
   
   result = risky_function()  # 返回 "默认值"
   
   # 多个默认值
   @exceptionHandler("默认", "值")
   def multi_return_function():
       raise ValueError("出错了")
   
   result = multi_return_function()  # 返回 ("默认", "值")

装饰器参数
----------

default
~~~~~~~

默认值参数，指定异常发生时返回的值。

.. code-block:: python

   # 单个默认值
   @exceptionHandler(None)
   def get_user_data():
       # 可能失败的数据获取
       pass
   
   # 多个默认值
   @exceptionHandler([], {}, "")
   def get_config_data():
       # 返回多个值的配置获取
       pass

返回值处理
----------

智能返回逻辑
~~~~~~~~~~~~

装饰器会根据默认值的数量智能决定返回值：

.. code-block:: python

   from qfluentwidgets.common.exception_handler import exceptionHandler
   
   # 情况1：无默认值
   @exceptionHandler()
   def no_default():
       raise Exception("错误")
   
   result = no_default()  # 返回 None
   
   # 情况2：单个默认值
   @exceptionHandler("默认")
   def single_default():
       raise Exception("错误")
   
   result = single_default()  # 返回 "默认"
   
   # 情况3：多个默认值
   @exceptionHandler("值1", "值2", "值3")
   def multiple_default():
       raise Exception("错误")
   
   result = multiple_default()  # 返回 ("值1", "值2", "值3")

实际应用
--------

数据获取保护
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.exception_handler import exceptionHandler
   import requests
   
   @exceptionHandler({})
   def get_user_info(user_id):
       """获取用户信息，失败时返回空字典"""
       response = requests.get(f"https://api.example.com/users/{user_id}")
       response.raise_for_status()
       return response.json()
   
   @exceptionHandler([])
   def get_user_posts(user_id):
       """获取用户文章，失败时返回空列表"""
       response = requests.get(f"https://api.example.com/users/{user_id}/posts")
       response.raise_for_status()
       return response.json()
   
   # 使用
   user_info = get_user_info(123)  # 失败时返回 {}
   user_posts = get_user_posts(123)  # 失败时返回 []

文件操作保护
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.exception_handler import exceptionHandler
   import json
   
   @exceptionHandler({})
   def load_config(file_path):
       """加载配置文件，失败时返回空配置"""
       with open(file_path, 'r', encoding='utf-8') as f:
           return json.load(f)
   
   @exceptionHandler(False)
   def save_config(config, file_path):
       """保存配置文件，失败时返回False"""
       with open(file_path, 'w', encoding='utf-8') as f:
           json.dump(config, f, indent=2, ensure_ascii=False)
       return True
   
   # 使用
   config = load_config("config.json")  # 文件不存在时返回 {}
   success = save_config(config, "config.json")  # 保存失败时返回False

UI组件保护
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.exception_handler import exceptionHandler
   from qfluentwidgets import InfoBar
   
   @exceptionHandler(None)
   def get_data_from_api():
       """从API获取数据用于UI显示"""
       # 可能失败的网络请求
       pass
   
   def update_ui():
       """更新UI界面"""
       data = get_data_from_api()
       
       if data is None:
           # 数据获取失败，显示错误信息
           InfoBar.error(
               title="数据加载失败",
               content="请检查网络连接",
               duration=3000
           )
       else:
           # 数据获取成功，更新界面
           # 更新UI的代码
           pass

配置处理保护
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.exception_handler import exceptionHandler
   
   @exceptionHandler("默认主题", "蓝色", 12)
   def load_theme_config():
       """加载主题配置"""
       # 从配置文件读取主题设置
       return "深色主题", "#0078D7", 14
   
   @exceptionHandler(False)
   def apply_theme_config(name, color, size):
       """应用主题配置"""
       # 应用主题设置
       return True
   
   # 使用
   theme_name, theme_color, font_size = load_theme_config()
   success = apply_theme_config(theme_name, theme_color, font_size)

高级用法
--------

链式装饰器
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.exception_handler import exceptionHandler
   import time
   import functools
   
   def retry(max_attempts=3, delay=1):
       """重试装饰器"""
       def decorator(func):
           @functools.wraps(func)
           def wrapper(*args, **kwargs):
               for attempt in range(max_attempts):
                   try:
                       return func(*args, **kwargs)
                   except Exception as e:
                       if attempt == max_attempts - 1:
                           raise
                       time.sleep(delay)
           return wrapper
       return decorator
   
   # 组合使用异常处理和重试
   @exceptionHandler(None)
   @retry(max_attempts=3, delay=1)
   def robust_api_call():
       """健壮的API调用"""
       # 可能失败但可以重试的操作
       pass

类方法保护
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.exception_handler import exceptionHandler
   
   class DataManager:
       def __init__(self):
           self.data = {}
       
       @exceptionHandler(None)
       def get_data(self, key):
           """安全获取数据"""
           return self.data[key]
       
       @exceptionHandler(False)
       def set_data(self, key, value):
           """安全设置数据"""
           if not isinstance(key, str):
               raise ValueError("键必须是字符串")
           self.data[key] = value
           return True
       
       @exceptionHandler([])
       def get_all_keys(self):
           """获取所有键"""
           return list(self.data.keys())
   
   # 使用
   manager = DataManager()
   value = manager.get_data("nonexistent")  # 返回 None
   success = manager.set_data(123, "value")  # 返回 False
   keys = manager.get_all_keys()  # 返回 []

异步函数保护
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.exception_handler import exceptionHandler
   import asyncio
   
   @exceptionHandler("默认结果")
   async def async_operation():
       """异步操作保护"""
       # 可能失败的异步操作
       await asyncio.sleep(1)
       raise ValueError("异步操作失败")
   
   async def main():
       result = await async_operation()  # 返回 "默认结果"
       print(f"结果: {result}")
   
   # 运行异步函数
   asyncio.run(main())

最佳实践
--------

1. **合理默认值** - 选择与函数返回类型匹配的默认值
2. **异常日志** - 在关键位置添加异常日志记录
3. **类型一致性** - 确保默认值与正常返回值类型一致
4. **性能考虑** - 避免在频繁调用的函数中使用复杂默认值
5. **测试覆盖** - 为异常情况编写测试用例

注意事项
--------

- 装饰器会捕获所有异常，包括 KeyboardInterrupt
- 默认值使用 deepcopy 避免引用问题
- 空默认值列表会返回 None
- 装饰器不会影响函数的正常执行

相关模块
--------

- :doc:`common.config` - 配置管理
- :doc:`components.widgets` - UI组件
- :doc:`common.animation` - 动画系统
