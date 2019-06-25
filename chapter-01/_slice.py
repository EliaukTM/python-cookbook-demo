#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你的程序已经出现一大堆已无法直视的硬编码切片下标，然后你想清理下代码
"""

"""
内置的 slice() 函数创建了一个切片对象，可以被用在任何切片允许使用的地方。
"""

if __name__ == '__main__':
    ###### 0123456789012345678901234567890123456789012345678901234567890'
    record = '....................100 .......513.25 ..........'
    cost = int(record[20:23]) * float(record[31:37])
    print(cost)
    # now , you can ...
    SHARES = slice(20, 23)
    PRICE = slice(31, 37)
    cost = int(record[SHARES]) * float(record[PRICE])
    print(cost)
