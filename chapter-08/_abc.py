#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想定义一个接口或抽象类，并且通过执行类型检查来确保子类实现了某些特定的方法
"""
import io
from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


# 继承
class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


# 抽象基类的一个主要用途是在代码中检查某些类是否为特定类型，实现了特定接口
def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    pass


# 除了继承这种方式外，还可以通过注册方式来让某个类实现抽象基类
# Register the built-in I/O classes as supporting our interface
IStream.register(io.IOBase)
# Open a normal file and type check
f = open('foo.txt')
isinstance(f, IStream)  # Returns True


# @abstractmethod 还能注解静态方法、类方法和 properties 。你只需保证这个注解紧靠在函数定义前即可
class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass
