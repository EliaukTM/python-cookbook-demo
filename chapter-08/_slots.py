#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你的程序要创建大量 (可能上百万) 的对象，导致占用很大的内存。
"""


class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    """
    当你定义 slots 后，Python 就会为实例使用一种更加紧凑的内部表示。实例通
    过一个很小的固定大小的数组来构建，而不是为每个实例定义一个字典，这跟元组或列表很类似。
    """