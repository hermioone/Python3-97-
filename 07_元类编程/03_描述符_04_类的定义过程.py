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


"""
leihou
"""

# 当 python 解释器遇到 class Person 的时候，实际上会进行调用
# 其目的是：知道类有哪些属性和方法
# 然后将这些属性、方法传递到元类 type 中，进而创建 Person 这个类对象
