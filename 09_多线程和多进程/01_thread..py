
import threading
import time


# 方式一
def get_detail_html(url):
    print(threading.current_thread, " get detail html started")
    time.sleep(2)
    print(threading.current_thread, " get detail html end")


t1 = threading.Thread(target=get_detail_html, args=("",))
start_time = time.time()
t1.start()
t1.join()

print("last time: {}".format(time.time() - start_time))


# 方式二
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
