## 第六章：对象引用、可变性和垃圾回收

### 1. 对象引用
**python 的变量本质上是一个指针。**

在 python 中 `==` 是判断值是否相等，`is` 是判断 `id` 是否相等。

```python
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
print(a == b)                       # True
print(a is b)                       # False
print(id(a), id(b))                 # 2235218674816 2235218685696
```

下面我们看一个经典的错误：
```python
class Company:

    def __init__(self, name, staffs=[]) -> None:
        self.name = name
        self.staffs = staffs

    def add(self, staff):
        self.staffs.append(staff)


com1 = Company("com1")
com2 = Company("com2")

com1.add("tom")

print(com1.staffs)                          # ['tom']
print(com2.staffs)                          # ['tom']

# 因为 com1 和 com2 都没有传递 staffs，所以都使用默认的 list，这个默认的 list 是在所有 Company 的对象间共享的

# 事实上，我们可以直接通过 Company 来获取这个默认的 list
print(Company.__init__.__defaults__)        # (['tom'],)
```

### 2. 垃圾回收

python 中垃圾回收算法使用的是 `引用计数`。