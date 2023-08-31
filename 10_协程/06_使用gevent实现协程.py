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
