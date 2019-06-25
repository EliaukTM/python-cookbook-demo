#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai


from itertools import dropwhile, islice, permutations, combinations

if __name__ == '__main__':

    """
    你想遍历一个可迭代对象，但是它开始的某些元素你并不感兴趣，想跳过它们。
    """

    # 你给它传递一个函数对象和一个可迭代对象。它会返回一个迭代器对象，丢弃原有序列中直到函数返回 True 之前的所有元素，然后返回后面所有元素。
    with open('/etc/passwd') as f:
        for line in dropwhile(lambda line: line.startswith('#'), f):
            print(line, end='')

    items = ['a', 'b', 'c', 1, 4, 10, 15]
    for x in islice(items, 3, None):
        print(x)

    # 你想迭代遍历一个集合中元素的所有可能的排列或组合
    items = ['a', 'b', 'c']
    for p in permutations(items):
        print(p)

    for p in permutations(items, 2):
        print(p)

    # 组合
    for c in combinations(items, 3):
        print(c)

    for c in combinations(items, 2):
        print(c)

    for c in combinations(items, 1):
        print(c)
