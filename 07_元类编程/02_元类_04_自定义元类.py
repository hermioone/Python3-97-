
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
