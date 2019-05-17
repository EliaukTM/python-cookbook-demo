#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你希望构造一个可以返回多个值的函数
"""


def myfun():
    return 1, 2, 3


if __name__ == '__main__':
    a, b, c = myfun()
    print(a)
    print(b)
    print(c)

    x = myfun()
    print(x)
