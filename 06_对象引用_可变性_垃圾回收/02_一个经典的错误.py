class Company:

    def __init__(self, name, staffs=[]) -> None:
        self.name = name
        self.staffs = staffs

    def add(self, staff):
        self.staffs.append(staff)


com1 = Company("com1")
com2 = Company("com2")

com1.add("tom")

print(com1.staffs)                          # ['tom']
print(com2.staffs)                          # ['tom']

# 因为 com1 和 com2 都没有传递 staffs，所以都使用默认的 list，这个默认的 list 是在所有 Company 的对象间共享的

# 事实上，我们可以直接通过 Company 来获取这个默认的 list
print(Company.__init__.__defaults__)        # (['tom'],)
