a = 1
print(id(a))                                # 140717222716200
b = 1
print(id(b))                                # 140717222716200

class Student:
    pass
print(id(Student))

a = None
b = None
print(id(a) == id(b))
