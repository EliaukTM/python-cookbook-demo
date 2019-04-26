#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你需要将数字格式化后输出，并控制数字的位数、对齐、千位分隔符和其他的细节。
"""

if __name__ == '__main__':
    x = 1234.56789
    # 保留两位
    print(format(x, '0.2f'))
    # 10个宽度，保留一位小数右对齐
    print(format(x, '>10.1f'))
    # 10个宽度，保留一位小数左对齐
    print(format(x, '<10.1f'))
    # 10个宽度，保留一位小数居中对齐
    print(format(x, '^10.1f'))
    # 逗号分隔
    print(format(x, ','))
    # 逗号分隔，保留一位小数
    print(format(x, '0,.1f'))

    print(format(x, 'e'))
