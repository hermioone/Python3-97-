class Foo:
    bar = True


Foo2 = type("Foo2", (object,), {"bar": True})

a = Foo()
b = Foo2()

print(a.bar)
print(b.bar)

print("--------------------------------------------------------------")


class FooChild(Foo):
    def echo(self):
        print(self.bar)

# 等价于


def echo_bar(self):
    print(self.bar)


FooChild2 = type("FooChild2", (Foo,), {"echo": echo_bar})

a = FooChild2()
a.echo()
