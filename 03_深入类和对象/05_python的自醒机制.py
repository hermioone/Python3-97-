class Person:
    """
    leihou
    """
    name = "user"

class Student(Person):
    def __init__(self, school) -> None:
        self.school = school


if __name__ == "__main__":
    user = Student("Hogwarts")
    print(user.__dict__)        # {'school': 'Hogwarts'}
    print(Person.__dict__)      # {'__module__': '__main__', '__doc__': '\n    leihou\n    ', 'name': 'user', '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>}
    user.__dict__["age"] = 10
    print(user.age)             # 10

    print(dir(user))
    # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'name', 'school']