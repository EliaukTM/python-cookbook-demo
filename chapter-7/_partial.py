#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你有一个被其他 python 代码使用的 callable 对象，可能是一个回调函数或者是一
个处理器，但是它的参数太多了，导致调用时出错。
"""
import math
from functools import partial


def spam(a, b, c, d):
    print(a, b, c, d)


if __name__ == '__main__':
    s1 = partial(spam, 1)  # a = 1

    # 现在我们使用partial()函数来固定某些参数值
    s1(2, 3, 4)
    s1(4, 5, 6)

    s2 = partial(spam, d=42)  # d = 42
    s2(1, 2, 3)

    points = [(1, 2), (3, 4), (5, 6), (7, 8)]


    def distance(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return math.hypot(x2 - x1, y2 - y1)


    pt = (4, 3)
    points.sort(key=partial(distance, pt))
    print(points)
