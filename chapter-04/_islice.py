#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想得到一个由迭代器生成的切片对象，但是标准切片操作并不能做到。
"""

import itertools


def count(n):
    while True:
        yield n
        n += 1


if __name__ == '__main__':

    c = count(0)
    # print(c[10:20])

    for x in itertools.islice(c, 10, 20):
        print(x)
