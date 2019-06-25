#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

from collections import Iterable

"""
你想将一个多层嵌套的序列展开成一个单层列表
"""


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


if __name__ == '__main__':
    items = [1, 2, [3, 4, [5, 6], 7], 8]
    # Produces 1 2 3 4 5 6 7 8
    for x in flatten(items):
        print(x)

    items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
    for x in flatten(items):
        print(x)
