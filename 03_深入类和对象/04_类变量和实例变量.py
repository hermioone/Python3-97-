class X:
    aa = 1

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


a = X(1, 2)
print(a.aa, a.x, a.y)                       # 1 1 2
a.aa = 100                                  # 在 a 这个对象上新建了一个实例变量 aa
print(a.aa)                                 # 100
print(X.aa)                                 # 1

b = X(2, 3)
print(b.aa)                                 # 1


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
# 注意：并不是深度优先搜索，如下例

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
# (<class '__main__.AA'>, <class '__main__.BB'>, <class '__main__.CC'>, <class '__main__.DD'>, <class 'object'>)
print(AA.__mro__)
