class User:

    @property
    def prop(self):
        return 10


obj = User()

print(vars(obj))                        # {}

# 特性是在类中的
# {'__module__': '__main__', 'prop': <property object at 0x00000252696C3790>, '__dict__': <attribute '__dict__' of 'User' objects>, '__weakref__': <attribute '__weakref__' of 'User' objects>, '__doc__': None}
print(User.__dict__)


print(User.prop)                    # <property object at 0x0000022D4F5E3790>
print(obj.prop)                     # 10
# obj.prop = 100                    # 会报错，因为没有 setter
obj.__dict__["prop"] = 100
print(vars(obj))                    # {'prop': 100}
print(obj.prop)                     # 10

# 此时 prop 不再是 User 类中的 property 了，而是一个普通的类属性
User.prop = 1000
print(obj.prop)                     # 100
