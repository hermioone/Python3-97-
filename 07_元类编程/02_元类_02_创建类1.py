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
