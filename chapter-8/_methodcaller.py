#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你有一个字符串形式的方法名称，想通过它调用某个对象的对应方法。
"""

import math
import operator


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


if __name__ == '__main__':
    # 最简单的情况，可以使用getattr() ：
    p = Point(2, 3)
    d = getattr(p, 'distance')(0, 0)  # Calls p.distance(0, 0)

    # 另外一种方法是使用operator.methodcaller()
    operator.methodcaller('distance', 0, 0)(p)
