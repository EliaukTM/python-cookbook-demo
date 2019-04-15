#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

from collections import namedtuple

"""
你有一段通过下标访问列表或者元组中元素的代码，但是这样有时候会使得你的代
码难以阅读，于是你想通过名称来访问元素。
"""

if __name__ == '__main__':
    Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
    sub = Subscriber('jonesy@example.com', '2012-10-19')
    print(sub)
    print(sub.addr)
    print(sub.joined)
