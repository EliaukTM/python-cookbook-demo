#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你写的最新的网络认证方案代码遇到了一个难题，并且你唯一的解决办法就是使用
复数空间。再或者是你仅仅需要使用复数来执行一些计算操作。
"""
import cmath

if __name__ == '__main__':
    a = complex(2, 4)
    print(a)

    b = 3 - 5j
    print(b)

    # 对应的实部、虚部和共轭复数可以很容易的获取。
    print(a.real)
    print(a.imag)
    print(a.conjugate())

    print(a + b)
    print(a * b)
    print(a / b)
    print(abs(a))

    # 如果要执行其他的复数函数比如正弦、余弦或平方根，使用cmath模块
    print(cmath.sin(a))
    print(cmath.cos(a))
    print(cmath.exp(a))

    """
    Python中大部分与数学相关的模块都能处理复数。比如如果你使用
    numpy ，可以很容易的构造一个复数数组并在这个数组上执行各种操作
    """
    import numpy as np

    a = np.array([2 + 3j, 4 + 5j, 6 - 7j, 8 + 9j])
    print(a + 2)
    print(np.sin(a))

    """
    Python 的标准数学函数确实情况下并不能产生复数值，因此你的代码中不可能会出现复数返回值。
    """

    # 会报错
    # math.sqrt(-1)

    # 如果你想生成一个复数返回结果，你必须显示的使用cmath模块
    cmath.sqrt(-1)
