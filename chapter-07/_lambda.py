#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想为 sort() 操作创建一个很短的回调函数，但又不想用 def 去写一个单行函
数，而是希望通过某个快捷方式以内联方式来创建这个函数
"""

if __name__ == '__main__':
    add = lambda x, y: x + y
    print(add(2, 3))

    add('hello', 'world')

    names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
    print(sorted(names, key=lambda name: name.split()[-1].lower()))

    # 在运行时绑定值
    x = 10
    a = lambda y: x + y
    x = 20
    b = lambda y: x + y

    print(a(10))
    print(b(10))
