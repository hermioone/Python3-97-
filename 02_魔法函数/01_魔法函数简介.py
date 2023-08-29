
class Company:
    def __init__(self, employee_list) -> None:
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]
    
    

company = Company(['tom', 'bob', 'jack'])


for em in company:
    print(em)


company1 = company[:2]
print(company1)                                 # ['tom', 'bob']
print(len(company1))                            # 2


class MyList:
    
    def __init__(self, items) -> None:
        self.items = items

    def __len__(self):
        return len(self.items)


my_list = MyList([1, 2, 3, 4, 5, 6])
# 调用 __len__ 魔法函数
print(len(my_list))                             # 6
