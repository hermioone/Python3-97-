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
