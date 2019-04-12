#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

from collections import OrderedDict

"""
想要构建一个将来需要序列化或编码成其他格式的映射的时候， OrderedDict
是非常有用的。比如，你想精确控制以 JSON 编码后字段的顺序
"""


def ordered_dict():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    for key in d:
        print(key, d[key])


"""
字典的运算
"""


def calc_dict():
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    # zip() 函数先将键和值反转过来
    min_price = min(zip(prices.values(), prices.keys()))
    max_price = max(zip(prices.values(), prices.keys()))
    prices_sorted = sorted(zip(prices.values(), prices.keys()))
    print(min_price)
    print(max_price)
    print(prices_sorted)

    # zip() 函数创建的是一个只能访问一次的迭代器。
    prices_and_names = zip(prices.values(), prices.keys())
    print(min(prices_and_names))  # OK
    # print(max(prices_and_names))  # ValueError: max() arg is an empty sequence


"""
怎样在两个字典中寻寻找相同点 (比如相同的键、相同的值等等)？
"""


def deal_two_dict():
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }
    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }
    # Find keys in common
    a.keys() & b.keys()  # { 'x', 'y' }
    # Find keys in a that are not in b
    a.keys() - b.keys()  # { 'z' }
    # Find (key,value) pairs in common
    a.items() & b.items()  # { ('y', 2) }

    # 以现有字典构造一个排除几个指定键的新字典
    c = {key: a[key] for key in a.keys() - {'z', 'w'}}
    print(c)


if __name__ == '___main__':
    ordered_dict()
    calc_dict()
    deal_two_dict()
