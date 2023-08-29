s1 = {"a", "b", "c"}
s2 = set("cef")
b = s1.difference(s2)
print(b)                                    # {'a', 'b'}
print(s1 & s2)                              # {'c'}
print(s1 - s2)                              # {'a', 'b'}
print(s1 | s2)                              # {'a', 'b', 'f', 'e', 'c'}
