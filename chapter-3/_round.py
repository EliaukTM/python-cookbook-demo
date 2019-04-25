#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想对浮点数执行指定精度的舍入运算。
"""

if __name__ == '__main__':
    # 四舍五入
    print(round(1.23, 1))
    print(round(1.27, 1))
    print(round(-1.27, 1))
    print(round(1.25361, 3))

    # 传给round()函数的ndigits参数可以是负数，这种情况下，舍入运算会作用在十位、百位、千位等上面。
    a = 1627731
    print(round(a, -1))
    print(round(a, -2))
    print(round(a, -3))

    # 格式化输出
    x = 1.23456
    print(format(x, '0.2f'))
    print(format(x, '0.3f'))
    print('value is {:0.3f}'.format(x))

    a = 2.1
    b = 4.2
    c = a + b
    print(c)

    # 这个属于浮点数的误差，推荐使用decimal
    c = round(c, 2)  # "Fix" result (???)
