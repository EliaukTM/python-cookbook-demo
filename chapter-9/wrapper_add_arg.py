#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想在装饰器中给被包装函数增加额外的参数，但是不能影响这个函数现有的调用规则。
"""

from functools import wraps


def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    return wrapper


@optional_debug
def spam(a, b, c):
    print(a, b, c)


if __name__ == '__main__':
    spam(1, 2, 3)
    spam(1, 2, 3, debug=True)
