#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想创建一个新的拥有一些额外功能的实例属性类型，比如类型检查。
"""


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

    """
    一个描述器就是一个实现了三个核心的属性访问操作 (get, set, delete) 的类，分别为 get () 、 set () 和 delete () 这三个特殊的方法。
    这些方法接受一个实例作为输入，之后相应的操作实例底层的字典。
    """


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
