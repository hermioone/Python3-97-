class D:
    def __init__(self) -> None:
        print("D")

class B(D):
    def __init__(self) -> None:
        print("B")

        # 还是根据 C3 算法来依次调用
        super(B, self).__init__()

class C(D):
    def __init__(self) -> None:
        print("C")

        # python3 中也可以这么调用
        super().__init__()

class A(B, C):
    def __init__(self) -> None:
        print("A")
        super().__init__()

if __name__ == "__main__":
    a = A()
    """
    打印的顺序为：A -> B -> C -D
    """
    # 所以 super 的调用顺序其实就是 __mro__ 的查找顺序