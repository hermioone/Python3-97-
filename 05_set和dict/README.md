## 第五章：set 和 dict

python 中的 `dict` 继承自 `abc.MutableMapping`。

### 1. dict 的常用方法

```python
import copy


a = {"a": {"compayn": "imooc"}, "b": {"company": "imooc2"}}

b = a.copy()                        # 浅拷贝
bb = copy.deepcopy(a)               # 深拷贝
a["b"]["company"] = "imooc3"
# {'a': {'compayn': 'imooc'}, 'b': {'company': 'imooc3'}}
print(b)
# {'a': {'compayn': 'imooc'}, 'b': {'company': 'imooc2'}}
print(bb)

new_list = ["tom", "mike"]
new_dict = dict.fromkeys(new_list, {"company": "im"})
# {'tom': {'company': 'im'}, 'mike': {'company': 'im'}}
print(new_dict)


# print(a["leihou"])                # 这样会报错：KeyError: 'leihou'
print(a.get("hello", "leihou"))     # leihou

a.clear()
print(a)

a.update(c="cc")
a.update([("d", "dd")])
a.update((("e", "ee"),))            # 必须要加上 ","，否则在这种情况下不是元组
print(a)                            # {'c': 'cc', 'd': 'dd', 'e': 'ee'}
```

### 2. set 的常用方法

```python
s1 = {"a", "b", "c"}
s2 = set("cef")
b = s1.difference(s2)
print(b)                                    # {'a', 'b'}
print(s1 & s2)                              # {'c'}
print(s1 - s2)                              # {'a', 'b'}
print(s1 | s2)                              # {'a', 'b', 'f', 'e', 'c'}
```

### 3. dict 和 set 的原理

