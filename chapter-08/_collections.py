#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想实现一个自定义的类来模拟内置的容器类功能，比如列表和字典。但是你不确
定到底要实现哪些方法。
"""
import bisect
import collections


class A(collections.Iterable):
    pass


class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)


if __name__ == '__main__':
    # a = A()

    # Traceback(most recent call last):
    #     File "<stdin>", line 1, in < module >
    # TypeError: Can't instantiate abstract class A with abstract methods __iter__

    # 只要实现iter()方法就不会报错了

    items = SortedItems([5, 1, 3])
    print(list(items))
    print(items[0], items[-1])
    items.add(2)
    print(list(items))
