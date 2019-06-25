#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你写好了一个函数，然后想为这个函数的参数增加一些额外的信息，这样的话其他
使用者就能清楚的知道这个函数应该怎么使用。
"""


def add(x: int, y: int) -> int:
    # 123123
    return x + y


if __name__ == '__main__':
    print(help(add))

    print(add.__annotations__)
