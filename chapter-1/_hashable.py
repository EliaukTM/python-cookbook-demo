#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
怎样在一个序列上面保持元素顺序的同时消除重复的值？
"""


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            # 收集器，最后汇成一个集合
            yield item
            seen.add(item)


"""
如果你想消除元素不可哈希 (比如 dict 类型) 的序列中重复元素的话

注：这里的 key 参数指定了一个函数，将序列元素转换成 hashable 类型
"""


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    result = list(dedupe(a))
    print(result)

    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    result = list(dedupe(a, key=lambda d: (d['x'], d['y'])))
    print(result)
