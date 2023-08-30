# 生成器函数：函数中只要有 yield 关键字，那这个函数就是生成器函数
def gen_func():
    yield 1
    yield 2


if __name__ == "__main__":
    # 返回的是一个生成器对象，python 编译字节码的时候就产生了
    gen = gen_func()

    # 生成器对象也是实现了迭代协议
    for i in gen:
        print(i)
