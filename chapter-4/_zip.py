#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想同时迭代多个序列，每次分别从一个序列中取一个元素。
"""
from itertools import zip_longest

if __name__ == '__main__':
    xpts = [1, 5, 4, 2, 10, 7]
    ypts = [101, 78, 37, 15, 62, 99]
    for x, y in zip(xpts, ypts):
        print(x, y)

    a = [1, 2, 3]
    b = ['w', 'x', 'y', 'z']
    for i in zip(a, b):
        print(i)

    for i in zip_longest(a, b):
        print(i)

    for i in zip_longest(a, b, fillvalue=0):
        print(i)



