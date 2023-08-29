# 模式：[start:end:step]

"""
start 表示切片开始位置，默认为0
end 表示切片截止位置，默认为列表长度
step 表示切片的补偿，默认为1

当 start、end、step 为默认值时可以省略，省略步长时可以同时省略最后一个冒号

当 step 为负数时，表示反向切片，此时 start 应该大于 end
"""



import numbers


a = [3, 4, 5, 6, 7, 9, 11, 12, 15, 17]
print(a[::])                # [3, 4, 5, 6, 7, 9, 11, 12, 15, 17]
print(a[::-1])              # [17, 15, 12, 11, 9, 7, 6, 5, 4, 3]
print(a[::2])               # [3, 5, 7, 11, 15]
print(a[3:6])               # [6, 7, 9]
print(a[0:100])             # [3, 4, 5, 6, 7, 9, 11, 12, 15, 17]
print(a[100:])              # []

a[:0] = [1, 2]              # a = [1, 2] + a
print(a)                    # [1, 2, 3, 4, 5, 6, 7, 9, 11, 12, 15, 17]

a[:3] = []
print(a)                    # [4, 5, 6, 7, 9, 11, 12, 15, 17]


# Group 支持切片操作
class Group:

    """
    如果要实现可变的序列（MutableSequence），还需实现 __setitem__, __delitem__, insert 方法
    """

    def __init__(self, group_name, company_name, staffs) -> None:
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        pass

    # 实现可切片的关键
    def __getitem__(self, item):
        return self.staffs[item]

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def __contains__(self):
        pass


group = Group("user", "imooc", ["harry", "hermione", "ron"])
print(group[:2])                    # ['harry', 'hermione']



class Group2:
    def __init__(self, group_name, company_name, staffs) -> None:
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        pass

    # 实现可切片的关键
    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            # 如果 item 是切片对象
            return cls(self.group_name, self.company_name, self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(self.group_name, self.company_name, [self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        return item in self.staffs

    def __str__(self) -> str:
        return f"group->{self.group_name}, company->{self.company_name}, staffs->{self.staffs}"

group = Group2("user", "imooc", ["harry", "hermione", "ron"])
print(group[:2])            # group->user, company->imooc, staffs->['harry', 'hermione']
print(group[1])             # group->user, company->imooc, staffs->['hermione']

# 调用了 __contains__
print("hermione" in group)  # True