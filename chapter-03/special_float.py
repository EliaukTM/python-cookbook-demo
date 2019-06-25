#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想创建或测试正无穷、负无穷或 NaN(非数字) 的浮点数。
"""
import math

if __name__ == '__main__':
    a = float('inf')
    print(a)

    b = float('-inf')
    print(b)

    c = float('nan')
    print(c)

    # 为了测试这些值的存在，使用math.isinf()和math.isnan()函数。
    print(math.isinf(a))
    print(math.isnan(a))

    # 无穷大数在执行数学计算的时候会传播
    print(a + 45)
    print(a * 10)
    print(10 / a)

    # 但是有些操作时未定义的并会返回一个NaN结果。
    a = float('inf')
    print(a / a)

    b = float('-inf')
    print(a + b)

    c = float('nan')
    print(c + 23)
    print(c / 2)
    print(c * 2)
    print(math.sqrt(c))

    # NaN值的一个特别的地方时它们之间的比较操作总是返回False。
    c = float('nan')
    d = float('nan')
    print(c == d)
    print(c is d)

    # 由于这个原因，测试一个NaN值得唯一安全的方法就是使用math.isnan()
