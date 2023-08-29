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
