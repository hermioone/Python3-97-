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

# 通过协程可以实现多任务，但是这种方案一定是假的任务，又因为只要运行时切换任务足够看，用户看不出区别，所以表面上这就是多任务
