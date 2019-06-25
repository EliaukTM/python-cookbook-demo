#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想在类中定义装饰器，并将其作用在其他函数或方法上。
"""

"""
在类里面定义装饰器很简单，但是你首先要确认它的使用方式。比如到底是作为一
个实例方法还是类方法。下面我们用例子来阐述它们的不同：
"""
from functools import wraps


class A:
    # Decorator as an instance method
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)

        return wrapper

    # Decorator as a class method
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)

        return wrapper


if __name__ == '__main__':
    a = A()


    @a.decorator1
    def spam():
        pass


    # As a class method
    @A.decorator2
    def grok():
        pass

    # 仔细观察可以发现一个是实例调用，一个是类调用。
