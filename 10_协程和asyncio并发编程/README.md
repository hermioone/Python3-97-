## 第十章：协程和 asyncio 并发编程


协程：可以暂停的函数（可以向暂停的地方传入值），并且可以在适当的时候回复该函数的继续执行。

> 可以使用生成器实现协程。

### 1. 生成器进阶

生成器的高级用法：
```python
def gen_func():
    html = yield "http://projectsedu.com/1"
    print(html)
    try:
        yield 2
    except Exception as e:
        pass
    yield 3
    return "hermione"


if __name__ == "__main__":
    gen = gen_func()

    # 第1种启动生成器的方式，但是这种方式不能向生成器传入值
    # url = next(gen)
    # print(url)
    # url = next(gen)
    # print(url)

    # 第2种启动生成器的方式
    # 在调用 send 发送非 None 值之前，必须启动一次生成器，方式有2种：
    #   1. url = gen.send(None)
    #   2. url = next(gen)
    url = gen.send(None)
    html = f"<html><body>{url}</body></html>"
    # send 可以传递值进入生成器内部，同步还可以重启生成器直行道下一个 yield
    url = gen.send(html)

    # gen.close()
    # 调用 gen.close() 后再执行生成器就会报错

    print(url)
    # 可以向 yield 中传入异常
    gen.throw(Exception, "download error")
```


### 2. yield from

`yield from` 语法是在 python3.3 中新加入的。

#### 1）yield from my_iterable

`yield from` 可以用来展开可迭代对象。

```python
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
```

#### 2）yield from generator

因为生成器也实现了迭代器协议，所以生成器也是可迭代对象，所以 yield from 也可以作用于生成器。

```python
def g1(gen):
    # gen 是生成器，因为生成器也是可迭代对象，所以可以使用 yield from
    yield from gen


def main():
    # main() 是调用方，g1 是委托生成器，gen 是子生成器
    g = g1()
    g.send(None)
```

此时 `yield from`` 会在调用方（main）与子生成器（gen）之间建立一个双向通道。如下案例所示：

```python
final_result = {}


# 子生
def sales_sum(pro_name):
    total = 0
    while True:
        x = yield
        if not x:
            break
        print(pro_name + " 销量：", x)
        total += x
    return total


# 委托生成器
def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)
        print(key + " 销量统计完成")


def main():
    data_sets = {
        "面膜": [1200, 1500, 3000],
        "手机": [28, 55, 98, 108],
        "大衣": [280, 560, 778, 70]
    }
    for key, data_set in data_sets.items():
        print("start key: ", key)
        m = middle(key)
        m.send(None)
        for value in data_set:
            m.send(value)               # 这里 send 的值直接传递给子生成器
        m.send(None)
    print("final reuslt: ", final_result)


if __name__ == "__main__":
    main()

    """
    start key:  面膜
    面膜 销量： 1200
    面膜 销量： 1500
    面膜 销量： 3000
    面膜 销量统计完成
    start key:  手机
    手机 销量： 28
    手机 销量： 55
    手机 销量： 98
    手机 销量： 108
    手机 销量统计完成
    start key:  大衣
    大衣 销量： 280
    大衣 销量： 560
    大衣 销量： 778
    大衣 销量： 70
    大衣 销量统计完成
    final reuslt:  {'面膜': 5700, '手机': 289, '大衣': 1688}
    """
```

### 3. 协程

在 python3.5 之前，协程都是通过生成器实现的；在 python3.5 后，python 为了将语义变得更加明确，就引入了 `async` 和 `await` 关键词用于定义原生的协程。

