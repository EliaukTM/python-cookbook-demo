#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想给类或静态方法提供装饰器。
"""

"""
给类或静态方法提供装饰器是很简单的，不过要确保装饰器在 @classmethod 或 @staticmethod 之前。
"""

import time
from functools import wraps


# A simple decorator
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return r

    return wrapper
    # Class illustrating application of the decorator to different kinds of methods


class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1


"""
装饰后的类和静态方法可正常工作，只不过增加了额外的计时功能
"""

if __name__ == '__main__':
    s = Spam()
    s.instance_method(1000000)
    Spam.class_method(1000000)
    Spam.static_method(1000000)
