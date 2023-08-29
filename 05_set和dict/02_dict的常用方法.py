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
