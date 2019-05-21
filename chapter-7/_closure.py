#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想要扩展函数中的某个闭包，允许它能访问和修改函数的内部变量。
"""


def sample():
    n = 0

    # Closure function
    def func():
        print('n=', n)

    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func


if __name__ == '__main__':
    f = sample()
    f.set_n(10)

    f()
    f.get_n()
