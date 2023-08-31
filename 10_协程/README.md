## 第十章：协程


协程是 python 中另外一种实现多任务的方式，只不过比线程更小占用更小执行单元。

在一个线程中的某个函数，可以在任何地方保存当前函数的一些临时变量等信息，然后切换到另外一个函数中执行（注意不是通过调用函数的方式做到的），并且切换的次数以及什么时候再切换到原来的函数都由开发者自己确定。

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

#### 1）使用 yield 实现协程

```python
import time


def work1():
    count = 0
    while count < 10:
        print("------ worker1 ------")
        count += 1
        yield
        time.sleep(0.5)


def work2():
    count = 0
    while count < 10:
        print("------ worker2 ------")
        count += 1
        yield
        time.sleep(0.5)


def main():
    w1 = work1()
    w2 = work2()
    while True:
        next(w1)
        next(w2)


if __name__ == "__main__":
    main()
```

通过协程可以实现多任务，但是这种方案一定是假的任务，又因为只要运行时切换任务足够看，用户看不出区别，所以表面上这就是多任务。

#### 2）使用 greenlet 实现协程

必须先安装 greenlet：
```shell
pip install greenlet
```

使用方式：

```python
import time
from greenlet import greenlet


def work1():
    count = 0
    while count < 10:
        print("------ worker1 ------")
        count += 1
        gr2.switch()
        time.sleep(0.5)


def work2():
    count = 0
    while count < 10:
        print("------ worker2 ------")
        count += 1
        gr1.switch()
        time.sleep(0.5)


gr1 = greenlet(work1)
gr2 = greenlet(work2)


gr1.switch()
```

#### 3）使用 gevent 实现协程
前2种实现协程的方式都不好，推荐使用这种方式。

greenlet 已经实现了协程，但是还需要人工切换，太麻烦了。python 还有一个比 greenlet 更强大的并且能够自动切换任务的模块 gevent。

其原理是当一个 greenlet 遇到 IO 操作时，就自动切换到其他的 greenlet，等到 IO 操作结束，再在适当的时候切换回来继续执行。

由于 IO 操作非常耗时，经常使程序处于等待状态， 有了 gevent 我们就自动切换协程，就保证总有 greenlet 在运行。

> gevent 切换的条件是：遇到延时

使用 gevent 需要先安装：
```shell
pip install gevent
```

使用方式：
```python
import time
import gevent
from gevent import monkey


# time 模块中的延时不具备自动切换任务的功能，而 gevent 中的延时具备
# 因此我们需要将 time 延时全部改为 gevent 延时
# 这句话可以让代码中所有的 time.sleep() 切换成 gevent.sleep()
monkey.patch_all()


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # gevent.sleep(0.1)                 # 这就是一个延时操作，会引发 gevent 切换任务

        # 默认情况下 time.sleep 不会导致 gevent 切换
        # 需要加上 monkey.patch_all() 才可以
        time.sleep(0.1)


# g1 = gevent.spawn(f, 4)
# g2 = gevent.spawn(f, 5)
# g3 = gevent.spawn(f, 6)
# g1.join()       # join 会等待 g1 标识的那个任务执行完毕后，对其进行清理工作，其实这就是一个耗时操作
# g2.join()
# g3.join()

# 等价于上面的
gevent.joinall([
    gevent.spawn(f, 4),
    gevent.spawn(f, 5),
    gevent.spawn(f, 6),
])
```