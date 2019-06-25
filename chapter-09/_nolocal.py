#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai
import logging
from functools import wraps, partial

"""
你想写一个装饰器来包装一个函数，并且允许用户提供参数在运行时控制装饰器行为。
"""

"""
解决：
引入一个访问函数，使用 nolocal 来修改内部变量。然后这个访问函数被作为一
个属性赋值给包装函数。
"""


# Utility decorator to attach a function as an attribute of obj
def attach_wrapper(obj, func=None):
    if func is None:
        # partial函数的功能就是：把一个函数的某些参数给固定住，返回一个新的函数。
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    '''
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    '''

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        # Attach setter functions
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper

    return decorate


# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    add(2, 3)
    add.set_message('Add called')
    add(2, 3)
    add.set_level(logging.WARNING)
    add(2, 3)
