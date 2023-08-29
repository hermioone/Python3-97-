import types


class User:
    def __init__(self, name) -> None:
        self.name = name


user = User("hermione")
# 想给 user 动态添加一个方法


def say(self):
    print(f"{self.name}: leihou")


# user.say_hello = say
# 这种添加方法的方式是错的，调用时会报下面的错，因为调用时并没有传入 self
# TypeError: say() missing 1 required positional argument: 'self
# user.say_hello()

# 正确的添加方式
user.say_hello = types.MethodType(say, user)
user.say_hello()
