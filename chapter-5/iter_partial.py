#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想在一个固定长度记录或者数据块的集合上迭代，而不是在一个文件中一行一行
的迭代。
"""

if __name__ == '__main__':
    from functools import partial

    RECORD_SIZE = 32
    with open('somefile.data', 'rb') as f:
        records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        ...
