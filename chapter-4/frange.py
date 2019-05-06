#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不
一样。
"""


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


if __name__ == '__main__':
    for n in frange(0, 4, 0.5):
        print(n)

    print(list(frange(0, 1, 0.125)))

