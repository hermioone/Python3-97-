from collections.abc import Iterable            # 可迭代类型
from collections.abc import Iterator            # 迭代器

a = [1, 2]
print(isinstance(a, Iterable))              # True
print(isinstance(a, Iterator))              # False

# iter() 方法首先会尝试调用 __iter__ 方法创建迭代器，如果没有实现 __iter__，
# 那么会创建一个默认的迭代器，这个默认的迭代器每次调用时会调用 __getitem__ 方法
iter_a = iter(a)
print(isinstance(iter_a, Iterator))         # True
