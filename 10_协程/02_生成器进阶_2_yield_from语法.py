# yield from 是 python3.3 中新加的语法
# yield from iterable

from itertools import chain


my_list = [1, 2, 3]
my_dict = {
    "hermione": 16,
    "ron": 16
}

for value in chain(my_list, my_dict, range(5, 10)):
    """
    1
    2
    3
    hermione
    ron
    5
    6
    7
    8
    9
    """
    print(value)

print("-" * 10 + "自己实现 chain" + "-" * 10)


def my_chain(*args):
    for my_iterable in args:
        # for value in my_iterable:
        #     yield value
        yield from my_iterable                  # 等价于上面2行的内容


for value in my_chain(my_list, my_dict, range(5, 10)):
    print(value)


print("-" * 10 + "yield from" + "-" * 10)


def g1(gen):
    # gen 是生成器，因为生成器也是可迭代对象，所以可以使用 yield from
    yield from gen


def main():
    # main() 是调用方，g1 是委托生成器，gen 是子生成器
    # yield from 会在调用方（main）与子生成器（gen）之间建立一个双向通道
    g = g1()
    g.send(None)
