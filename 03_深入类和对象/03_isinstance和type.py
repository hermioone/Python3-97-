
class A:
    pass

class B(A):
    pass

b = B()

print(isinstance(b, B))                                 # True
print(isinstance(b, A))                                 # True

# is 是比较的 id，== 比较的是值
print(type(b) is B)                                     # True
print(type(b) is A)                                     # False