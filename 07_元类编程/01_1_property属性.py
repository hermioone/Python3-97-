from datetime import date, datetime


class User:
    def __init__(self, name) -> None:
        self.__name = name
        self.age = 2

    @property
    def age(self):
        return self.__age

    # python2 中不能使用
    @age.setter
    def age(self, value):
        print(f"set age: {value}")
        self.__age = value


if __name__ == "__main__":
    # set age: 2
    user = User("hermione")
    print(user.age)                                         # 0

    # set age: 16
    user.age = 16
    print(user.age)                                         # 16
