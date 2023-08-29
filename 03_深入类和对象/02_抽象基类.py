# 2种场景：

## 1. 检查某个类是否有某种方法

from typing import Sized


class Company:
    def __init__(self, employee_list) -> None:
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


com = Company(["harry", "hermione", "ron"])
print(hasattr(com, "__len__"))  # True
# 这种情况下更倾向于使用 isinstance 来判断某个对象是不是某种类型

# Sized 中定义了 __len__ 抽象方法
# 实际上 isinstance 不需要继承
print(isinstance(com, Sized))  # True



## 2. 我们需要强制某个子类必须实现某些方法
### 比如实现了一个 web 框架，提供一些扩展功能，比如集成 cache，需要提供 redis 实现、memorycache 实现等等
### 这种情况下就可以约定一个抽象基类，约定一些抽象方法

import abc


class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCache(CacheBase):
    def get(self, key):
        pass

    def set(self, key, value):
        pass


cache = RedisCache()
