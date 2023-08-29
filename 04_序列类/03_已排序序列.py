import bisect

# 用来维护已排序的序列（按照升序排序）

##### 二分查找
a = []
bisect.insort(a, 5)
bisect.insort(a, 2)
bisect.insort(a, 8)
bisect.insort(a, 1)
bisect.insort(a, 9)

print(a)                        # [1, 2, 5, 8, 9]
print(bisect.bisect(a, 3))      # 3 这个元素应该被插入在 a 这个列表 index 为 2 的位置
