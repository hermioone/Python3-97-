## 第四章：序列类

序列类型的分类包括：
- 容器序列：list、tuple、deque
- 扁平序列：str、bytes、bytearray、array.array
- 可变序列：list、deque、bytearray、array
- 不可变序列：str、tuple、bytes


### 1. +、+=、extend 的区别

对于 list，可以使用 +、+=、extend 等方法来扩充 list：
```python
a = [1, 2]
c = a + [3, 4]
print(a)                                # [1, 2]
print(c)                                # [1, 2, 3, 4]

c += [5, 6]
print(c)                                # [1, 2, 3, 4, 5, 6]

c.extend([7, 8])
print(c)                                # [1, 2, 3, 4, 5, 6, 7, 8]
```

看上去似乎没有区别，但是它们的区别体现在下面的代码中：
```python
# b = a + (7, 8)       # 会报错：can only concatenate list (not "tuple") to list
a += (7, 8)
print(a)               # [1, 2, 7, 8]
a.extend((5, 6))
print(a)               # [1, 2, 7, 8, 5, 6]
```

对于 `+` 这种运算符，左右两边必须是同种类型，如果是不同类型（比如 `list + tuple`）则会报错。而 `+=` 和 `extend` 则没有这种限制。

这是因为 `+=` 其实是调用了 `__iadd__` 这个魔法函数，在 list 的 `__iadd__` 实现中，调用了 `extend` 方法。

### 2. array 和 list

`array` 和 `list` 最大的区别就是 `array` 只能存放指定的数据类型

```python
import array

# 只能存放 int 类型的数据
my_array = array.array("i")
my_array.append(1)
my_array.append(2)
```

### 3. 列表推导式、生成器表达式、字典推导式

```python
# 列表生成式（列表推导式）
# 1. 提取 1 - 20 之间的奇数
odd_list = [i for i in range(21) if i % 2 == 1]
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(odd_list)


def handle_item(item):
    return item * item


odd_list = [handle_item(i) for i in range(10)]

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(odd_list)

print("------------------------------------------------------------------------------------------")

# 生成器表达式
odd_list_gen = (i for i in range(10))
print(type(odd_list_gen))                           # <class 'generator'>
odd_list = list(odd_list_gen)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(odd_list)

print("------------------------------------------------------------------------------------------")

# 字典推导式
my_dict = {"harry": 22, "hermione": 23, "ron": 24}
reversed_dict = {value: key for key, value in my_dict.items()}
# {22: 'harry', 23: 'hermione', 24: 'ron'}
print(reversed_dict)

print("------------------------------------------------------------------------------------------")

# 集合推导式
my_set = {key for key, value in my_dict.items()}
print(type(my_set))                                 # <class 'set'>
# {'hermione', 'harry', 'ron'}
print(my_set)

```