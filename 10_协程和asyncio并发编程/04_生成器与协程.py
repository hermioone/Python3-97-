def gen_func():
    yield 1
    return "hermione"


if __name__ == "__main__":
    gen = gen_func()
    next(gen)
    try:
        next(gen)
    except StopIteration:
        pass
