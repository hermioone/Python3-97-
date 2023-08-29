class User:
    def __new__(cls, *args, **kwargs):
        print("in new")
        return super().__new__(cls)

    def __init__(self, name) -> None:
        print("in init")
        self.name = name
