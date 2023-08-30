# 多进程编程中不能使用普通的 Queue，只能使用多进程专用 Queue，使用方式和普通 Queue 一样
from multiprocessing import Manager, Pipe, Pool, Process, Queue
import time


def producer(pipe):
    pipe.send("hermione")
    time.sleep(2)


def consumer(pipe):
    time.sleep(2)
    data = pipe.recv()
    print(data)


def add_data(p_dict, key, value):
    p_dict[key] = value


if __name__ == "__main__":
    receive_pipe, send_pipe = Pipe()
    # pipe 只能适用于2个进程
    p = Process(target=producer, args=(send_pipe,))
    c = Process(target=consumer, args=(receive_pipe,))

    p.start()
    c.start()
    p.join()
    c.join()

    # 使用 manager 来进行线程间同步
    progress_dict = Manager().dict()
    t1 = Process(target=add_data, args=(progress_dict, "hermione", 16))
    t2 = Process(target=add_data, args=(progress_dict, "ron", 16))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(progress_dict)
