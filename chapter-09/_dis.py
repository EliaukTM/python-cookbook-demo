#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想通过将你的代码反编译成低级的字节码来查看它底层的工作机制。
"""


# dis 模块可以被用来输出任何 Python 函数的反编译结果
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        print('Blastoff!')


import dis

dis.dis(countdown)
