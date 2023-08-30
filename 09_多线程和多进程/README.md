## 第九章：多线程和多进程

### 1. GIL

GIL 是得同一时刻只有一个线程可以执行。GIL 的释放时机：
1. GIL 会根据执行的字节码行数以及时间片释放
2. GIL 会在遇到 IO 操作时释放

### 2. 多线程

对于 IO 操作来说，多线程和多进程性能差别不大。

#### 1）多线程的使用方式

方式一：

```python
def get_detail_html(url):
    print(threading.current_thread, " get detail html started")
    time.sleep(2)
    print(threading.current_thread, " get detail html end")


t1 = threading.Thread(target=get_detail_html, args=("",))
start_time = time.time()
t1.start()
t1.join()

print("last time: {}".format(time.time() - start_time))
```

方式二：

```python
class GetDetailUrl(threading.Thread):

    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print(threading.current_thread, " get detail url started")
        time.sleep(2)
        print(threading.current_thread, " get detail url end")


t1 = GetDetailUrl("get_detail_url")
start_time = time.time()
t1.start()
t1.join()

print("last time: {}".format(time.time() - start_time))
```

#### 2）线程间通信

线程间通信可以通过 `Queue` 来实现。

#### 3）线程池

为什么使用线程池（`futures`）：
1. 主线程可以获取某个线程的状态和返回值
2. `futures` 可以让多线程和多进程编码接口一致

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def get_html(duration):
    time.sleep(duration)
    return duration


executor = ThreadPoolExecutor(max_workers=2)
# 通过 submit 提交执行的函数到线程池中，submit 是立即返回
task1 = executor.submit(get_html, (3))
task2 = executor.submit(get_html, (2))

# 非阻塞获取 task 的状态
print(task1.done())
print(task2.done())
# 阻塞并且获取 task 的结果
print(task2.result())
print(task1.result())
"""
False
False
2
3
"""


a = [3, 2, 4]

# 返回以及完成的 task（谁先完成就先返回哪个）
# all_tasks 是 list[Future]
all_tasks = [executor.submit(get_html, (duration)) for duration in a]
# as_completed 是一个生成器，会 yield 已经完成的 task
for future in as_completed(all_tasks):
    data = future.result()
    print(f"get page {data} success")
"""
get page 2 success
get page 3 success
get page 4 success
"""


# 通过 executor 获取已经完成的 task（按照 a 的顺序返回）
for data in executor.map(get_html, a):
    # 也是返回一个生成器
    print(f"get page {data} success")
"""
get page 3 success
get page 2 success
get page 4 success
"""
```

### 3. 多进程

由于 GIL 锁的机制，对于某些耗 CPU 的操作，多线程无法充分利用多核 CPU 的优势，此时用多进程更有优势；对于 IO 操作来说，多线程优于多进程。

#### 1）多进程的使用方式

多进程有2种 API。

第一种（不推荐）：
```python
import multiprocessing
import time

# 这种多进程方式不推荐


def get_html(n):
    time.sleep(n)
    return n


if __name__ == "__main__":
    progress = multiprocessing.Process(target=get_html, args=(2,))
    # start 前 pid：None
    print("start 前 pid：{}".format(progress.pid))
    progress.start()
    # start 后 pid：652
    print("start 后 pid：{}".format(progress.pid))
    progress.join()
    print("main process end")
```

第二种（推荐）：
```python
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor
import time


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# ThreadPoolExecutor 实现了上下文管理协议，所以可以使用 with

if __name__ == "__main__":
    with ThreadPoolExecutor(3) as executor:
        all_task = [executor.submit((fib), (num)) for num in range(30, 40)]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("execute result: {}".format(data))
            # 耗时：9.9738028049469
        print("耗时：{}".format(time.time() - start_time))

    # 注意：多进程必须放在 if __name__ == "__main__" 中
    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit((fib), (num)) for num in range(30, 40)]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("execute result: {}".format(data))
        # 耗时：5.143215179443359
        print("耗时：{}".format(time.time() - start_time))
```

#### 2）多进程的通信

##### a. Queue
多进程编程中不能使用普通的 `Queue`，因为多进程中数据是隔离的。只能使用多进程专用 `Queue`，使用方式和普通 Queue 一样：
```python
from multiprocessing import Queue
```

> 注意：multiprocessing 中的 Queue 不能用于 multiprocessing 中的进程池（`multiprocessing.Pool`，这个进程池只能使用 `multiprocessing.Manager.Queue`）

##### b. Pipe

`Pipe` 的性能高于 `Queue`

```python
def producer(pipe):
    pipe.send("hermione")
    time.sleep(2)


def consumer(pipe):
    time.sleep(2)
    data = pipe.recv()
    print(data)


if __name__ == "__main__":
    receive_pipe, send_pipe = Pipe()
    # pipe 只能适用于2个进程
    p = Process(target=producer, args=(send_pipe,))
    c = Process(target=consumer, args=(receive_pipe,))

    p.start()
    c.start()
    p.join()
    c.join()
```

##### c. Manager

```python
from multiprocessing import Manager, Process

def add_data(p_dict, key, value):
    p_dict[key] = value


if __name__ == "__main__":

    progress_dict = Manager().dict()
    t1 = Process(target=add_data, args=(progress_dict, "hermione", 16))
    t2 = Process(target=add_data, args=(progress_dict, "ron", 16))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(progress_dict)
```

> 注意：使用 Manager 的时候注意同步问题（加锁，`Manager.RLock`）。


