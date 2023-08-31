final_result = {}


# 子生
def sales_sum(pro_name):
    total = 0
    while True:
        x = yield
        if not x:
            break
        print(pro_name + " 销量：", x)
        total += x
    return total


# 委托生成器
def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)
        print(key + " 销量统计完成")


def main():
    data_sets = {
        "面膜": [1200, 1500, 3000],
        "手机": [28, 55, 98, 108],
        "大衣": [280, 560, 778, 70]
    }
    for key, data_set in data_sets.items():
        print("start key: ", key)
        m = middle(key)
        m.send(None)
        for value in data_set:
            m.send(value)               # 这里 send 的值直接传递给子生成器
        m.send(None)
    print("final reuslt: ", final_result)


if __name__ == "__main__":
    main()

    """
    start key:  面膜
    面膜 销量： 1200
    面膜 销量： 1500
    面膜 销量： 3000
    面膜 销量统计完成
    start key:  手机
    手机 销量： 28
    手机 销量： 55
    手机 销量： 98
    手机 销量： 108
    手机 销量统计完成
    start key:  大衣
    大衣 销量： 280
    大衣 销量： 560
    大衣 销量： 778
    大衣 销量： 70
    大衣 销量统计完成
    final reuslt:  {'面膜': 5700, '手机': 289, '大衣': 1688}
    """
