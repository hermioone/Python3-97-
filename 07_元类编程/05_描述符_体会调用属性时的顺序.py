
class M:

    def __init__(self):
        self.x = 1

    def __get__(self, instance, owner):
        return self.x

    def __set__(self, instance, value):
        self.x = value


class AA:
    m = M()
    n = 2

    def __init__(self, score):
        self.score = score


aa = AA(3)
# {'score': 3}
print(aa.__dict__)
# 3
print(aa.score)
# 3
print(aa.__dict__["score"])

# {'__module__': '__main__', 'm': <__main__.M object at 0x0000028853737790>, 'n': 2, '__init__': <function AA.__init__ at 0x000002885373D9E0>, '__dict__': <attribute '__dict__' of 'AA' objects>, '__weakref__': <attribute '__weakref__' of 'AA' objects>, '__doc__': None}
print(type(aa).__dict__)
# 2
print(aa.n)
# 2
print(type(aa).__dict__['n'])

# 1
print(aa.m)
# 1
print(type(aa).__dict__['m'].__get__(aa, AA))

print("-" * 20)

# 1
print(AA.m)
# <__main__.M object at 0x0000028853737790>
print(AA.__dict__['m'])
