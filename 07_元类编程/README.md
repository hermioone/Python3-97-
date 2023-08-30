## 第七章：元类编程

### 1. property 属性

#### 1）什么是 property 属性

在 python 中数据的属性 和处理数据的方法 都可以叫做属性（attribute）。简单来说，在一个类中, 方法是属性, 数据也是属性。

而 “property 属性” 指的是不改变类接口的前提下使用存取方法 (即 setter 和 getter) 来修改数据的属性。

```python
from datetime import date, datetime


class User:
    def __init__(self, name, birthday) -> None:
        # 属性
        self.name = name
        self.birthday = birthday
        self._age = 0

    # property 属性
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


if __name__ == "__main__":
    user = User("hermione", date(year=1993, month=4, day=15))
    print(user.age)                                         # 0
    user.age = 16
    print(user.age)                                         # 16

```

#### 2）为什么使用 property

为什么要使用 `property` 呢？因为如果我们只使用属性时，无法对属性的赋值进行限制，比如把 age 赋值为 "abc"，这样在程序运行时没有问题，但这样的赋值毫无意义。

因此我们可以使用 `property` 来对属性赋值进行限制，甚至设置只读特性。

#### 3）属性的查找顺序

假设有一个类 `User` 的实例对象 `user`，那么 `user.name` 的查找顺序为：
1. 首先查找 `User` 类中是否有名为 `name` 的 property 属性，如果有，则直接返回
2. 如果没有，那么才从 `user` 实例中开始查找

```python
class User:

    @property
    def prop(self):
        return 10


obj = User()

print(vars(obj))                        # {}

# {'__module__': '__main__', 'prop': <property object at 0x00000252696C3790>, '__dict__': <attribute '__dict__' of 'User' objects>, '__weakref__': <attribute '__weakref__' of 'User' objects>, '__doc__': None}
print(User.__dict__)

print(User.prop)                        # <property object at 0x0000022D4F5E3790>
print(obj.prop)                         # 10
# obj.prop = 100                        # 会报错，因为没有 setter
obj.__dict__["prop"] = 100
print(vars(obj))                        # {'prop': 100}
print(obj.prop)                         # 10

## 把 prop 从特性改为属性
User.prop = 1000
print(obj.prop)                         # 100
```

从上面的代码中可以发现：
1. **property 属性是存储在在类中的 `__dict__` 中**
2. 对象会优先使用特性的值，当类中的特性变为属性后，才调用到了实例属性

#### 4）property 属性总结

property 属性算是 python的高级语法，但是实际上大部分情况是用不到这个语法的. 如果代码中,需要对属性进行检查，更好的做法是使用[描述符](#3-属性描述符).

### 2. 元类（type）

#### 1）元类的定义
元类就是一个特殊的类，专门用来创建其他类的类。

> 在 python 中，根据元类创建了其他的类对象，根据类对象创建实例对象，而元类也是由元类创建出来的。

```python
class Bar:
    pass


a = 1
b = Bar()

print(a.__class__)                      # <class 'int'>
print(a.__class__.__class__)            # <class 'type'>
print(b.__class__)                      # <class '__main__.Bar'>
print(b.__class__.__class__)            # <class 'type'>
```

#### 2）元类的应用1：创建类
```python
class A:
    pass


"""
Help on class A in module __main__:

class A(builtins.object)
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

None
"""
print(help(A))


# 尽量使用 B 变量来接收 type 返回值，也可用其他的变量名，为了可读性高，建议使用 B 来当做变量名
B = type("B", (), {})

"""
Help on class B in module __main__:

class B(builtins.object)
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)

None
"""
print(help(B))

print("--------------------------------------------------------------")

class Foo:
    bar = True


Foo2 = type("Foo2", (object,), {"bar": True})

a = Foo()
b = Foo2()

print(a.bar)
print(b.bar)

print("--------------------------------------------------------------")


class FooChild(Foo):
    def echo(self):
        print(self.bar)

# 等价于


def echo_bar(self):
    print(self.bar)


FooChild2 = type("FooChild2", (Foo,), {"echo": echo_bar})

a = FooChild2()
a.echo()
```

#### 3）元类的应用2：自定义元类

```python

# 如果在定义类的时候没有指定 metaclass，那么就用默认的 type 创建
class Foo:
    pass


# 把类中的 public 属性名都改为大写
def upper_attr(class_name, class_parents, class_attr):
    # 遍历属性字典，把 public 的属性的属性名都改为大写
    new_attr = {}
    for key, value in class_attr.items():
        if not key.startswith("__"):
            new_attr[key.upper()] = value

    return type(class_name, class_parents, new_attr)


class Bar(metaclass=upper_attr):
    name = "hermione"
    age = 16


print(hasattr(Bar, "name"))                     # False
print(hasattr(Bar, "NAME"))                     # True
"""
{
    'NAME': 'hermione', 
    'AGE': 16, 
    '__module__': '__main__', 
    '__dict__': <attribute '__dict__' of 'Bar' objects>, 
    '__weakref__': <attribute '__weakref__' of 'Bar' objects>, 
    '__doc__': None
}
"""
print(Bar.__dict__)
```

从上面的代码可知，元类定义的类是什么样的，类真正就是什么样的。

上面的代码还存在变种，即 `metaclass=MyClassName`，此时元类的定义依赖 `MyClassName.__new__()` 方法的放回结果。

```python
class TypeClass:
    def __new__(clas, class_name, class_parents, class_attr):
        new_attr = {}
        # ...
        return type(class_name, class_parents, new_attr)


class Bar(metaclass=TypeClass):
    name = "hermione"
    age = 16
```

#### 4）为什么要使用元类

> 元类就是深度的魔法，99%的用户根本不必为此操心，如果想搞清楚究竟是否需要用到元类，那么你就不需要它。那些实际用到元类的人都非常清楚地知道他们究竟需要做什么，而且根本不需要解释为什么要用元类。

在 MySQL 的 ORM 模型框架中，大量使用了元类。


### 3. 描述符

#### 1）`__getattr__` 和 `__getattribute__`

`__getattr__` 和 `__getattribute__` 都是对访问属性时的特殊操作：
- `__getattr__` 只针对未定义属性的调用
- `__getattribute__` 针对所有的属性运行

```python
class User:
    def __init__(self, name) -> None:
        self.name = name

    # 党统实例对象访问一个不存在的属性时，此方法会自动被调用，可以在这里进一步处理，例如可以产生一个异常等
    def __getattr__(self, item):
        print(f"{item} 属性不存在")
        return None

    # 获取任何属性时都会先进入这个方法，尽量不要重写这个方法
    # def __getattribute__(self, __name: str) -> Any:
    #     pass


if __name__ == "__main__":
    user = User("hermione")
    print(user.name)                                # hermione
    print(user.age)                                 # None
```

如果一个类中没有实现 `__getattr__`，那么当通过实例对象访问一个不存在的属性时，会调用父类的 `__getattr__`，而默认的 `__getattr__`（object 中的）的功能是产生一个异常。

如果 `__getattr__` 和 `__getattribute__` 同时出现，访问一个不存在的属性时会调用 `__getattribute__`。

#### 2）什么是描述符

之前学习过的 `property` 本质上就是一个描述符，只不过我们只是直接使用了它，并没有研究它的实现过程。

严格地说，如果一个类中有如下3个方法中的任意一个，那么用这个类创建的对象就是 “描述符对象”：
- `__get__`
- `__set__`
- `__delete__`

如果有另外一个类，这个类中有一个类属性，这个类属性是一个描述符对象，此时我们称这个类属性为 “描述符”。

```python
import numbers


class IntField:
    def __get__(self, instance, owner):
        # owner 是 instance 的类：<class '__main__.Person'>
        print("__get__")
        return self.__age

    def __set__(self, instance, value):
        # self 是当前描述符对象
        # instance 是 Person 实例对象
        print("__set__")
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value needed")
        if value <= 0:
            raise ValueError("positive value needed")
        self.__age = value


class Person:
    # 此时 age 就是描述符
    age = IntField()


p = Person()

"""
__set__
__get__
10
"""
p.age = 10
print(p.age)
```

小总结：当我们自定义一个类属性，且类属性是一个具有 `__get__`/`__set__`/`__delete` 3个方法中任意实现一个的类创建的实例对象，那么：
- 在获取这个类属性时，会自动调用 `__get__`
- 在设置这个类属性时，会自动调用 `__set__`
- 在删除这个类属性时，会自动调用 `__delete__`

看上去很像 `property`，实际上 `property` 就是如上述的方式实现的

#### 3）有描述符的类的定义过程

```python
class NameDes:
    def __init__(self) -> None:
        self.__name = None

    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass


class Person:
    name = NameDes()
    print("leihou")
```

当 python 解释器遇到 `class Person` 的时候，实际上会进行调用（所以会打印 “leihou”），其目的是：知道类有哪些属性和方法，然后将这些属性、方法传递到元类 type 中，进而创建 Person 这个类对象
  
定义过程：
1. python 解释器执行完 `classNameDes` 后，创建 NameDes 类对象
2. python 解释器执行到 `name = NameDesc()` 时创建描述符对象
3. python 解释器执行 `print("leihou)`
4. python 解释器创建 Person 类对象，让 `name` 类属性指向描述符对象

#### 4）为什么使用描述符

1. 可以做类型检查：比 setter/getter 更简洁
2. 比 `property` 方便

```python
class NonNegative:

    def __init__(self, default):
        self.default = default
        self.data = dict()

    def __get__(self, instance, owner):
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Invalid value.")
        self.data[instance] = value

    def __delete__(self, instance):
        pass


class Movie:

    rating = NonNegative(0)
    budget = NonNegative(0)
    gross = NonNegative(0)

    def __init__(self, title, rating, budget, gross):
        # 在实例对象中添加了一个 title 属性
        self.title = title
        # 把 rating 赋值给描述符对象
        self.rating = rating
        # 把 rating 赋值给描述符对象
        self.budget = budget
        # 把 rating 赋值给描述符对象
        self.gross = gross


m = Movie("Harry Potter", 97, 964000, 1300000)
print(f"电脑评分：{m.rating}")
try:
    m.gross = -1
except ValueError as e:
    print(e)

"""
电脑评分：97
Invalid value.
"""

print(m.__dict__)                   # {'title': 'Harry Potter'}
# 从 m.__dict__ 结果中可知，只有 title 是实例属性
```

从上面的例子可知：
1. 如果在类中定义了描述符，那么类的实例变量中的同名实例属性则不存在，对这个属性的 get/set 都会执行描述符的相关操作
2. 如果使用 property，则需要在类中定义大量的 getter/setter，且每个 setter 中代码冗余度过多。因此这就是使用描述符的原因。

#### 5）描述符的应用：使用描述符实现 classmethod

```python
class ClassMethod:

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        print(self.func, instance, owner)

        def call(*args):
            self.func(owner, *args)
        return call


class A:
    M = 100

    def a(self):
        print("a 是实例方法")

    # 类作为装饰器，等价于 b = ClassMethod(b)，此时 b 也就是一个描述符了
    @ClassMethod
    def b(cls):
        print("b 是类方法1")
        print(cls.M)
        print("b 是类方法2")


A.b()
"""
b 是类方法1
100
b 是类方法2
"""
```

#### 6）描述符的应用：惰性计算

惰性计算就是懒加载，并且计算过一次后不需要再重复计算。

```python
class Lazy:
    def __init__(self, fun):
        self.fun = fun

    def __get__(self, instance, owner):
        print("LazyProperty.__get__")
        if instance is None:
            return self

        value = self.fun(instance)
        # Lazy 必须是非数据描述符，否则 setattr 这一步不会生效
        setattr(instance, self.fun.__name__, value)
        return value


class Circle:
    __PI = 3.14

    def __init__(self, radius) -> None:
        self.radius = radius

    @Lazy
    def area(self):
        print("computing")
        return self.__PI * self.radius ** 2


a = Circle(4)
print("-" * 10 + " 1 " + "-" * 10)
print(a.area)
print("-" * 10 + " 2 " + "-" * 10)
print(a.area)
print("-" * 10 + " 3 " + "-" * 10)


"""
---------- 1 ----------
LazyProperty.__get__
computing
50.24
---------- 2 ----------
50.24
---------- 3 ----------
"""
```

从上面的代码中可知，只有第一次调用 `a.area` 时才触发了计算，后续的调用都不再需要重复计算了。



### 4. 属性查找顺序

```python
class C:
    pass

c = C()
```

对于上面的代码，当我们调用 `c.m` 时的属性查找顺序：
1. 首先查找 `c.__dict__['m']` 是否存在
2. 不存在则再找 `type(c).__dict__['m']` 是否存在
3. 不存在则再继续向上找父类

这个期间找到的如果是普通值就输出，如果找到的是一个描述符，则调用 `__get__` 方法

### 5. 数据描述符和非数据描述符

同时定义了 `__get__` 和 `__set__` 的描述符是数据描述符（资料描述符）；只定义了 `__get__` 的描述符是非数据描述符。


二者的区别是：
> 当属性名和描述符名相同时，在访问这个同名属性时，如果是数据描述符就会先访问描述符；如果是非数据描述符则会先访问属性。

```python
class M:

    def __init__(self):
        self.x = 1

    def __get__(self, instance, owner):
        print("get m here")
        return self.x

    def __set__(self, instance, value):
        print("set m here")
        self.x = value + 1


class N:

    def __init__(self):
        self.x = 1

    def __get__(self, instance, owner):
        print("get n here")
        return self.x


class AA:
    m = M()                     # m 是一个数据描述符
    n = N()                     # n 是一个非数据描述符

    def __init__(self, m, n):
        self.m = m              # 给描述符赋值
        self.n = n              # n 是非数据描述符，所以这里是创建一个名为 n 的实例属性


# set m here
aa = AA(2, 5)

# {'n': 5}
print(aa.__dict__)

# {'__module__': '__main__', 'm': <__main__.M object at 0x000002481AE0C890>, 'n': <__main__.N object at 0x000002481AE0C8D0>, '__init__': <function AA.__init__ at 0x000002481ADFDB20>, '__dict__': <attribute '__dict__' of 'AA' objects>, '__weakref__': <attribute '__weakref__' of 'AA' objects>, '__doc__': None}
print(AA.__dict__)

# 5
print(aa.n)

"""
get n here
1
"""
print(AA.n)

"""
get m here
3
"""
print(aa.m)

"""
get m here
3
"""
print(AA.m)
```

### 6. 描述符的原理

当调用一个属性，而属性指向一个描述符时，为什么就会去调用这个描述符呢？

其实这是由 `obj.__getattribute__` 方法控制的，其中 obj 是新式类的实例对象，因为新式类中集成了 `__getattribute__` 方法，当访问一个属性比如 `b.x` 时，会自动调用这个方法。

`__getattribute__` 的定义如下：

```python
def __getattribute__(self, key):
    "Emulate type_getattro() in Objects/typeobject.c"
    v = object.__getattribute__(self, key)
    if hasattr(v, "__get__"):
        return v.__get__(None, self)
    return v
```

> 所以如果在一个类中重写了 `__getattribute__()`， 将会改变描述符的行为，甚至导致描述符关闭。


### 7. `__new__` 和 `__init__`

`__new__` 是用来控制对象的生成过程；`__init__` 是用来完善对象的。如果 `__new__` 中不返回对象，则不会调用 `__init__`。

### 8. 实现一个 orm

```python
class Field:
    pass


class IntFiled(Field):
    def __init__(self, db_column, min_value: int = None, max_value: int = None):
        if min_value > max_value:
            raise ValueError("min_value must be smaller than max_value")
        self.db_column = db_column
        self.__min_value = min_value
        self.__max_value = max_value
        self.__value = None

    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value: int):
        if value < self.__min_value or value > self.__max_value:
            raise ValueError("value must be between min_value and max_value")
        self.__value = value


class CharFiled(Field):

    def __init__(self, db_column, max_length: int):
        self.db_column = db_column
        self.__max_length = max_length
        self.__value = None

    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        if len(value) > self.__max_length:
            raise ValueError("Too long")
        self.__value = value


# 自定义元类，将 Model 中定义的所有字段和 meta 数据（db，table）都放入类的属性中
# 数据库字段都放入 cls._fields 这个字典中；Meta 放入 cls._meta 这个字典中
class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        _fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                _fields[key] = value
        meta = attrs.get("Meta", None)
        _meta = {}
        db_name = getattr(meta, "db_name")
        table_name = getattr(meta, "table_name")
        _meta["db"] = db_name
        _meta["table"] = table_name
        attrs["_meta"] = _meta
        attrs["_fields"] = _fields
        del attrs["Meta"]
        return super().__new__(cls, name, bases, attrs, **kwargs)


class ModelBase():

    def save(self):
        """
        保存到数据库
        """
        db = self._meta["db"]
        table = self._meta["table"]

        columns = []
        values = []
        for key, value in self._fields.items():
            columns.append(value.db_column)
            values.append(str(getattr(self, key)))
        columns_str = ','.join(columns)
        values_str = ','.join(values)

        sql = f"insert into {db}.{table}({columns_str}) value({values_str})"
        print(sql)


class User(ModelBase, metaclass=ModelMetaClass):

    name = CharFiled(db_column="name", max_length=10)
    age = IntFiled(db_column="age", min_value=0, max_value=100)

    class Meta:
        db_name = "demo"
        table_name = "user"


if __name__ == "__main__":
    user = User()
    user.name = "hermione"
    user.age = 16
    user.save()
```