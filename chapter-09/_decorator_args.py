#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想写一个装饰器，既可以不传参数给它，比如 @decorator ，也可以传递可选参
数给它，比如 @decorator(x,y,z)
"""
import logging
from functools import wraps, partial


def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)
    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper


# Example use
@logged
def add(x, y):
    return x + y


@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')

"""
可以看到，@logged 装饰器可以同时不带参数或带参数。
"""