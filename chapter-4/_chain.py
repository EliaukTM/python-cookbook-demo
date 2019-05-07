#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想在多个对象执行相同的操作，但是这些对象在不同的容器中，你希望代码在不
失可读性的情况下避免写重复的循环。
"""
from itertools import chain

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = ['x', 'y', 'z']
    for x in chain(a, b):
        print(x)