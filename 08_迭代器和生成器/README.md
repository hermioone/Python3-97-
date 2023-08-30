## 第八章：迭代器和生成器

### 1. 迭代器协议

python 中的迭代协议分为两种：
- 迭代器对象
- 可迭代对象
  
```python
# 可迭代对象
class Iterable(Protocol[_T_co]):
    @abstractmethod
    def __iter__(self) -> Iterator[_T_co]: ...

# 迭代器对象
class Iterator(Iterable[_T_co], Protocol[_T_co]):
    @abstractmethod
    def __next__(self) -> _T_co: ...
    def __iter__(self) -> Iterator[_T_co]: ...
```

python 中的迭代器必须要实现两个方法：`__next__`（因为 `__iter__` 在 `Iterator` 中已经实现了），相反可迭代类型（比如 `list`，`tuple` 等序列）则只需要实现 `__iter__` 即可。

```python
from collections.abc import Iterable            # 可迭代类型
from collections.abc import Iterator            # 迭代器

a = [1, 2]
print(isinstance(a, Iterable))              # True
print(isinstance(a, Iterator))              # False

# iter() 方法首先会尝试调用 __iter__ 方法创建迭代器，如果没有实现 __iter__，
# 那么会创建一个默认的迭代器，这个默认的迭代器每次调用时会调用 __getitem__ 方法
iter_a = iter(a)
print(isinstance(iter_a, Iterator))         # True
```

迭代器和可迭代对象的应用：
```python
from typing import Iterator


# 自定义迭代器
class MyIterator(Iterator):
    def __init__(self, employee) -> None:
        self.__employee = employee
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__employee):
            raise StopIteration
        value = self.__employee[self.__index]
        self.__index += 1
        return value


class Company:
    def __init__(self, employee) -> None:
        self.employee = employee

    # 此时 Company 就变成了一个可迭代对象
    def __iter__(self):
        return MyIterator(self.employee)


if __name__ == "__main__":
    employee = ["harry", "hermione", "ron"]
    company = Company(employee)
    for e in company:
        print(e)
```

### 2. 生成器

```python
# 生成器函数：函数中只要有 yield 关键字，那这个函数就是生成器函数
def gen_func():
    yield 1
    yield 2


if __name__ == "__main__":
    # 返回的是一个生成器对象，python 编译字节码的时候就产生了
    gen = gen_func()

    # 生成器对象也是实现了迭代协议
    for i in gen:
        print(i)
```

### 3. 生成器原理

python 中的函数也是对象，所以 python 解释器在进入函数的时候，会创建一个栈帧，这个栈帧也是在堆内存中的，这就决定了栈帧可以独立与调用者存在。所以函数执行结束并不会导致栈帧的释放。
