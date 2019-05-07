#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想在迭代一个序列的同时跟踪正在被处理的元素索引。
"""

if __name__ == '__main__':
    my_list = ['a', 'b', 'c']
    for idx, val in enumerate(my_list):
        print(idx, val)

    my_list = ['a', 'b', 'c']
    for idx, val in enumerate(my_list, 1):
        print(idx, val)

