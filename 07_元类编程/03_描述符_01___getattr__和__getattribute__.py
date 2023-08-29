

class User:
    def __init__(self, name) -> None:
        self.name = name

    # 党统实例对象访问一个不存在的属性时，此方法会自动被调用，可以在这里进一步处理，例如可以产生一个异常等
    def __getattr__(self, item):
        print(f"{item} 属性不存在")
        return None

    # 获取任何属性时都会先进入这个方法，尽量不要重写这个方法
    # def __getattribute__(self, __name: str) -> Any:
    #     pass


if __name__ == "__main__":
    user = User("hermione")
    print(user.name)                                # hermione
    print(user.age)                                 # None
