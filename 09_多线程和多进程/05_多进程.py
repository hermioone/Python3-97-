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
