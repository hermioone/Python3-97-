# 列表生成式（列表推导式）
# 1. 提取 1 - 20 之间的奇数
odd_list = [i for i in range(21) if i % 2 == 1]
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(odd_list)


def handle_item(item):
    return item * item


odd_list = [handle_item(i) for i in range(10)]

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(odd_list)

print("------------------------------------------------------------------------------------------")

# 生成器表达式
odd_list_gen = (i for i in range(10))
print(type(odd_list_gen))                           # <class 'generator'>
odd_list = list(odd_list_gen)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(odd_list)

print("------------------------------------------------------------------------------------------")

# 字典推导式
my_dict = {"harry": 22, "hermione": 23, "ron": 24}
reversed_dict = {value: key for key, value in my_dict.items()}
# {22: 'harry', 23: 'hermione', 24: 'ron'}
print(reversed_dict)

print("------------------------------------------------------------------------------------------")

# 集合推导式
my_set = {key for key, value in my_dict.items()}
print(type(my_set))                                 # <class 'set'>
# {'hermione', 'harry', 'ron'}
print(my_set)
