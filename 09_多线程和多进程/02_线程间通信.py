
from queue import Queue
import threading
import time


detail_url_list = Queue()


def get_detail_html(_total):
    count = 0
    while count < _total:
        item = detail_url_list.get(block=True)
        print(f"item: {item}")
        count += 1


class GetDetailUrl(threading.Thread):

    def __init__(self, name, total):
        super().__init__(name=name)
        self._total = total

    def run(self):
        print(threading.current_thread, " get detail url started")
        for i in range(self._total):
            detail_url_list.put(i, block=True)
            time.sleep(2)
        print(threading.current_thread, " get detail url end")


total = 5
t1 = threading.Thread(target=get_detail_html, args=(total,))
t2 = GetDetailUrl("get_detail_url", total)
start_time = time.time()
t1.start()
t2.start()
t1.join()
t2.join()

print("last time: {}".format(time.time() - start_time))
