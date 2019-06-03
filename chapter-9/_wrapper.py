#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想在函数上添加一个包装器，增加额外的操作处理 (比如日志、计时等)。
"""

# 如果你想使用额外的代码包装一个函数，可以定义一个装饰器函数

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
def countdown(n):
    """
    Counts down
    """
    while n > 0:
        n -= 1


if __name__ == '__main__':
    countdown(100000)
    countdown(10000000)
