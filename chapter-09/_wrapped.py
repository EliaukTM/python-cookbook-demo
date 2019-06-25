#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
一个装饰器已经作用在一个函数上，你想撤销它，直接访问原始的未包装的那个函数。
"""
import time
from functools import wraps


def timethis(func):
    """
    Decorator that reports the execution time.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def add(x, y):
    return x + y


if __name__ == '__main__':
    # 可以通过访问wrapped属性来访问原始函数
    orig_add = add.__wrapped__
    print(orig_add(3, 4))
