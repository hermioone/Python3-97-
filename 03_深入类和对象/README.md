## 第三章：深入理解类和对象

### 1. 鸭子类型和多态

> 鸭子类型：当看到一只鸟走起来像鸭子，游泳起来像鸭子，叫起来也像鸭子，那么这只鸟就可以被称为鸭子

不同于 java，python 中只要具有相同的方法就可以被视为相同的类型，比如 list 和 tuple 和 set 都属于序列类型。

```python
a = ["harry", "hermione", "ron"]
name_tuple = {"zhangsan", "lisi"}
a.extend(name_tuple)
print(a)                    # ['harry', 'hermione', 'ron', 'lisi', 'zhangsan']

# 事实上，任何类型只要实现了 __getitem__ 方法都可以被视为序列类型
class Company:
    def __init__(self, employee_list) -> None:
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]
 
company = Company(['tom', 'bob', 'jack'])
a.extend(company)
print(a)                    # ['harry', 'hermione', 'ron', 'lisi', 'zhangsan', 'tom', 'bob', 'jack']
```

### 2. 抽象基类

在 python 中不推荐使用抽象基类

### 3. 变量的查找顺序

因为 python 中支持多继承，所以 python 中变量的查找顺序就很关键。

在 python 2.3 之后，使用的是一种 C3 算法：
```python
class D:
    name = "D"

class B(D):
    age = "10B"

class E:
    name = "E"

class C(E):
    name = "C"
    age = "10C"

class A(B, C):

    def say(self):
        print(self.name, self.age)

# python 2.3 之后的属性搜索算法：C3算法
a = A()
a.say()                                     # D 10B

## c3 算法的查找顺序
print(A.__mro__)    # (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>, <class 'object'>)
```

> 注意：**C3 算法并不是深度优先搜索**，如下面的菱形继承案例所示

```python
class DD:
    name = "DD"

class BB(DD):
    age = "10B"

class CC(DD):
    name = "CC"

class AA(BB, CC):
    def say(self):
        print(self.name, self.age)

aa = AA()
aa.say()                                    # CC 10B

## c3 算法的查找顺序
# (<class '__main__.AA'>, <class '__main__.BB'>, <class '__main__.CC'>, <class '__main__.DD'>, <class 'object'>)
print(AA.__mro__)
```

### 4. super 的调用顺序

C3 算法也决定了调用 `super().__init__(*args, **kargs)` 时的调用顺序：

```python
class D:
    def __init__(self) -> None:
        print("D")

class B(D):
    def __init__(self) -> None:
        print("B")

        # 还是根据 C3 算法来依次调用
        super(B, self).__init__()

class C(D):
    def __init__(self) -> None:
        print("C")

        # python3 中也可以这么调用
        super().__init__()

class A(B, C):
    def __init__(self) -> None:
        print("A")
        super().__init__()

if __name__ == "__main__":
    a = A()
    """
    打印的顺序为：A -> B -> C -D
    """
```

> 所以 super 的调用顺序其实就是 __mro__ 的查找顺序


### 5. 给对象动态添加方法

```python
import types


class User:
    def __init__(self, name) -> None:
        self.name = name


user = User("hermione")
# 想给 user 动态添加一个方法


def say(self):
    print(f"{self.name}: leihou")


# user.say_hello = say
# 这种添加方法的方式是错的，调用时会报下面的错，因为调用时并没有传入 self
# TypeError: say() missing 1 required positional argument: 'self
# user.say_hello()

# 正确的添加方式
user.say_hello = types.MethodType(say, user)
user.say_hello()

```

### 6. 限制动态添加属性

因为在定义一个类时，可以在运行的时候动态给其添加属性，这样虽然灵活，但是容易没有节制，所以我们有时需要在定义类时，明确的说明这个类的实例对象只能有哪些属性，这样可以控制不被任意添加。

```python
class Person:
    __slots__ = {"name", "age"}

p = Person()
p.name = "hermione"
p.age = 16

# 因为在 Person 类中的类属性 __slots__ 中没有 address，所以下面的语句会报错，从而起到了限制的作用
# p.address = "Hogwarts"
```

> `__slots__` 只在定义的类中生效，而在子类中没有作用

```python
class Student(Person):
    pass

s = Student()
s.name = "ron"
s.age = 16
s.phone_num = "10086"
```