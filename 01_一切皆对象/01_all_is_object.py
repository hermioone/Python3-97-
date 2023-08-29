
## 函数是对象
def ask(name = "hermione"):
    print(name)

my_func = ask
my_func()


## 类也是对象
class Person:
    def __init__(self) -> None:
        print("leihou")

my_class = Person
my_class()


obj_list = []
obj_list.append(ask)
obj_list.append(Person)

for item in obj_list:
    print(item())


def decorator_func():
    print("dec start")
    return ask

decorator_func()("tom")