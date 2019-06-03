#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
在创建一个类的对象时，如果之前使用同样参数创建过这个对象，你想返回它的缓
存引用。
"""


# The class in question
class Spam:
    def __init__(self, name):
        self.name = name


# Caching support
import weakref

_spam_cache = weakref.WeakValueDictionary()


def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s


if __name__ == '__main__':
    a = get_spam('foo')
    b = get_spam('bar')
    print(a is b)
    c = get_spam('foo')
    print(a is c)
