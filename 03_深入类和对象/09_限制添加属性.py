
class Person:
    __slots__ = {"name", "age"}


p = Person()
p.name = "hermione"
p.age = 16

# 因为在 Person 类中的类属性 __slots__ 中没有 address，所以下面的语句会报错，从而起到了限制的作用
# p.address = "Hogwarts"


# __slots__ 只在定义的类中生效，而在子类中没有作用
class Student(Person):
    pass


s = Student()
s.name = "ron"
s.age = 16
s.phone_num = "10086"
