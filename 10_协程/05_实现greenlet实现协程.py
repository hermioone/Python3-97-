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
