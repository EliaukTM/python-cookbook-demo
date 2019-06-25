#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想通过改变实例创建方式来实现单例、缓存或其他类似的特性
"""


# 如果你定义了一个类，就能像函数一样的调用它来创建实例

class Spam:

    def __init__(self, name):
        self.name = name


a = Spam('Guido')
b = Spam('Diana')


# 如果你想自定义这个步骤，你可以定义一个元类并自己实现 call () 方法

# 假设你不想任何人创建这个类的实例
class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")


# Example
class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam.grok')


# 假如你想实现单例模式（只能创建唯一实例的类），实现起来也很简单
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


# Example
class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')


# 假设你想创建 8.25 小节中那样的缓存实例
import weakref


class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj


# Example
class Spam(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name
