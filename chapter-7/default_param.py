#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想定义一个函数或者方法，它的一个或多个参数是可选的并且有一个默认值。
"""

if __name__ == '__main__':

    def spam(a, b=42):
        print(a, b)


    spam(1)  # Ok. a=1, b=42
    spam(1, 2)  # Ok. a=1, b=2

    """
    如果默认参数是一个可修改的容器比如一个列表、集合或者字典，可以使用 None
    作为默认值
    """


    def spam(a, b=None):
        if b is None:
            b = []


    """
    如果你并不想提供一个默认值，而是想仅仅测试下某个默认参数是不是有传递进来
    """
    _no_value = object()


    def spam(a, b=_no_value):
        if b is _no_value:
            print('No b value supplied')
