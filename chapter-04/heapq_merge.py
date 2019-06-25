#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你有一系列排序序列，想将它们合并后得到一个排序序列并在上面迭代遍历。
"""

import heapq

if __name__ == '__main__':
    a = [1, 4, 7, 10]
    b = [2, 5, 6, 11]
    for c in heapq.merge(a, b):
        print(c)
