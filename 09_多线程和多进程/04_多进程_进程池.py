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
