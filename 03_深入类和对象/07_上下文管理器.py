import contextlib


class Sample:

    def __enter__(self):
        # 获取资源
        print("enter")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print("exit")

    def do_something(self):
        print("do something")

with Sample() as sample:
    sample.do_something()


print("---------------------------------------------------------------------")

@contextlib.contextmanager
# contextlib.contextmanager 把修饰的函数包装成一个上下文管理器
# contextlib.contextmanager 修饰的函数必须是个生成器
def file_open(file_name):
    # yield 之前为 __enter__
    print("file open")
    yield
    # yield 之后为 __exit__
    print("file closed")

with file_open("a.txt") as f:
    print("file processiong")