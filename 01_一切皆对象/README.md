## 第一章：一切皆对象

### 1. type, object 和 class
> 类是由 type 这个类生成的对象，实例对象是由类对象创建出来的。

**`type` 也是一个类，同时 `type` 也是一个对象**。`type` 类的基类是 `object`：
```python
print(type.__bases__)                               # (<class 'object'>,)
```

`object` 的基类为空，同时 object 是由 type 类生成出来的：
```python
print(type(object))                                 # <class 'type'>
print(object.__bases__)                             # ()
```

`type` 和 `object` 和 `class` 的关系总结为：

![20230824123407](https://hermione-pic.oss-cn-beijing.aliyuncs.com/vscode/20230824123407.png)

1. 所有 class 都是继承自 `object`
2. 所以 class （包括 object）都是 `type` 类的实例
3. `type` （对象）也是 `type` （类）的实例

所以 python 中一切皆对象（包括 class，`object`，`type` 都是对象）。

### 2. Python 中的内置类型

- 数值：
  - `int`
  - `float`
  - `complex`
  - `bool`
- 迭代类型
- 序列类型：
  - `list`
  - `bytes`，`bytearray`，`memoryview`（二进制序列）
  - `range`
  - `tuple`
  - `str`
  - `array`
- 映射（dict）
- 集合：
  - `set`
  - `frozenset`
- 上下文管理类型（with）
- 其他：
  - 模块类型
  - class 和实例
  - 函数类型
  - 方法类型
  - 代码类型
  - object类型
  - type类型
  - ellipsis类型
  - notimplemented类型
  
