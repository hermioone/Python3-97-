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
