#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你在类中需要重复的定义一些执行相同逻辑的属性方法，比如进行类型检查，怎样
去简化这些重复代码呢？
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name must be a string')
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('age must be an int')
        self._age = value


# 可以看到，为了实现属性值的类型检查我们写了很多的重复代码。只要你以后看到
# 类似这样的代码，你都应该想办法去简化它。一个可行的方法是创建一个函数用来定
# 义属性并返回它。例如：

def typed_property(name, expected_type):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('{} must be a {}'.format(name, expected_type))
        setattr(self, storage_name, value)

    return prop


# Example use
class Person:
    name = typed_property('name', str)
    age = typed_property('age', int)
    def __init__(self, name, age):
        self.name = name
        self.age = age
