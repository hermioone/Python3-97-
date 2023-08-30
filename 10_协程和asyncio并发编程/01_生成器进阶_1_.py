def gen_func():
    html = yield "http://projectsedu.com/1"
    print(html)
    try:
        yield 2
    except Exception as e:
        pass
    yield 3
    return "hermione"


if __name__ == "__main__":
    gen = gen_func()

    # 第1种启动生成器的方式，但是这种方式不能向生成器传入值
    # url = next(gen)
    # print(url)
    # url = next(gen)
    # print(url)

    # 第2种启动生成器的方式
    # 在调用 send 发送非 None 值之前，必须启动一次生成器，方式有2种：
    #   1. url = gen.send(None)
    #   2. url = next(gen)
    url = gen.send(None)
    html = f"<html><body>{url}</body></html>"
    # send 可以传递值进入生成器内部，同步还可以重启生成器直行道下一个 yield
    url = gen.send(html)

    # gen.close()
    # 调用 gen.close() 后再执行生成器就会报错

    print(url)
    # 可以向 yield 中传入异常
    gen.throw(Exception, "download error")
