class Bar:
    pass


a = 1
b = Bar()

print(a.__class__)                      # <class 'int'>
print(a.__class__.__class__)            # <class 'type'>
print(b.__class__)                      # <class '__main__.Bar'>
print(b.__class__.__class__)            # <class 'type'>
