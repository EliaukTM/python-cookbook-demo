#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想改变对象实例的打印或显示输出，让它们更具可读性
"""


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # repr()方法返回一个实例的代码表示形式，通常用来重新构造这个实例。内
    # 置的repr()函数返回这个字符串，跟我们使用交互式解释器显示的值是一样的。
    # str()方法将实例转换为一个字符串，使用str()或print()函数会输出这个字符串
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


if __name__ == '__main__':
    # >> > p = Pair(3, 4)
    # >> > p
    # Pair(3, 4)  # __repr__() output
    # >> > print(p)
    # (3, 4)  # __str__() output

    p = Pair(3, 4)
    print(p)

    print('p is {0!r}'.format(p))
    print('p is {0}'.format(p))
