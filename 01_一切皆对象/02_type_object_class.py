a = 1
b = "abc"

# type 生成了 int class，int class 生成了 1
print(type(1))                                      # <class 'int'>
print(type(int))                                    # <class 'type'>  
print(type(b))                                      # <class 'str'>
print(type(str))                                    # <class 'type'>


##### class 对象是由 type 生成的，实例对象是由 class 对象生成的
class Student:
    pass

stu = Student()
print(type(stu))                                    # <class '__main__.Student'>
print(type(Student))                                # <class 'type'>

class MyStudent(Student):
    pass

print(MyStudent.__bases__)

# type 类的基类
print(type.__bases__)                               # (<class 'object'>,)

print(type(object))                                 # <class 'type'>
print(object.__bases__)                             # ()

def foo():
    pass

print(type(foo))                                    # <class 'function'>

