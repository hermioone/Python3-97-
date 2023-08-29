class Foo:
    # property 就是描述符
    @property
    def attr(self):
        print("获取属性attr的值")
        return "attr的值"

    def bar(self):
        pass


print(type(Foo.attr))                   # <class 'property'>
print(type(Foo.bar))                    # <class 'function'>
