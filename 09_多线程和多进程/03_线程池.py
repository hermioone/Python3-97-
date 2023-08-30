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
print(task1.result())
print(task2.result())
"""
False
False
3
2
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
