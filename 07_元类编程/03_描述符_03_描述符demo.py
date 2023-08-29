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
