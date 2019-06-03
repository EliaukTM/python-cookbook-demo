#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你写了一个装饰器作用在某个函数上，但是这个函数的重要的元信息比如名字、文
档字符串、注解和参数签名都丢失了。
"""

# 任何时候你定义装饰器的时候，都应该使用 functools 库中的 @wraps 装饰器来注
# 解底层包装函数。


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

    print(countdown.__name__)
    print(countdown.__doc__)
    print(countdown.__annotations__)
