from typing import Iterator


# 自定义迭代器
class MyIterator(Iterator):
    def __init__(self, employee) -> None:
        self.__employee = employee
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__employee):
            raise StopIteration
        value = self.__employee[self.__index]
        self.__index += 1
        return value


class Company:
    def __init__(self, employee) -> None:
        self.employee = employee

    # 此时 Company 就变成了一个可迭代对象
    def __iter__(self):
        return MyIterator(self.employee)


if __name__ == "__main__":
    employee = ["harry", "hermione", "ron"]
    company = Company(employee)
    for e in company:
        print(e)
