class NonNegative:

    def __init__(self, default):
        self.default = default
        self.data = dict()

    def __get__(self, instance, owner):
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Invalid value.")
        self.data[instance] = value

    def __delete__(self, instance):
        pass


class Movie:

    rating = NonNegative(0)
    budget = NonNegative(0)
    gross = NonNegative(0)

    def __init__(self, title, rating, budget, gross):
        # 在实例对象中添加了一个 title 属性
        self.title = title
        # 把 rating 赋值给描述符对象
        self.rating = rating
        # 把 rating 赋值给描述符对象
        self.budget = budget
        # 把 rating 赋值给描述符对象
        self.gross = gross


m = Movie("Harry Potter", 97, 964000, 1300000)
print(f"电脑评分：{m.rating}")
try:
    m.gross = -1
except ValueError as e:
    print(e)

"""
电脑评分：97
Invalid value.
"""

print(m.__dict__)                   # {'title': 'Harry Potter'}
# 从 m.__dict__ 结果中可知，只有 title 是实例属性
