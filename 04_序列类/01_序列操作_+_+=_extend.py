a = [1, 2]
c = a + [3, 4]
print(a)                                # [1, 2]
print(c)                                # [1, 2, 3, 4]

c += [5, 6]
print(c)                                # [1, 2, 3, 4, 5, 6]

c.extend([7, 8])
print(c)                                # [1, 2, 3, 4, 5, 6, 7, 8]

# b = a + (7, 8)                        # 会报错：can only concatenate list (not "tuple") to list
a += (7, 8)
print(a)                                # [1, 2, 7, 8]
a.extend((5, 6))
print(a)                                # [1, 2, 7, 8, 5, 6]


## += 其实是调用了 __iadd__ 这个魔法函数，
# 在 list 的 __iadd__ 实现中，调用了 extend 方法