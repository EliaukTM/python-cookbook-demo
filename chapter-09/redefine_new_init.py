#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你的程序包含一个很大的类继承体系，你希望强制执行某些编程规约（或者代码诊
断）来帮助程序员保持清醒。
"""


# 如果你想监控类的定义，通常可以通过定义一个元类。一个基本元类通常是继承自
# type 并重定义它的 new () 方法或者是 init () 方法。

class MyMeta(type):
    def __new__(self, clsname, bases, clsdict):
        # clsname is name of class being defined
        # bases is tuple of base classes
        # clsdict is class dictionary
        return super().__new__(cls, clsname, bases, clsdict)


# 另一种是，定义 init () 方法：
class MyMeta(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        # clsname is name of class being defined
        # bases is tuple of base classes
        # clsdict is class dictionary


# 为了使用这个元类，你通常要将它放到到一个顶级父类定义中，然后其他的类继承这个顶级父类。
class Root(metaclass=MyMeta):
    pass


class A(Root):
    pass


class B(Root):
    pass


# 作为一个具体的应用例子，下面定义了一个元类，它会拒绝任何有混合大小写名字
# 作为方法的类定义

class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('Bad attribute name: ' + name)
        return super().__new__(cls, clsname, bases, clsdict)


class Root(metaclass=NoMixedCaseMeta):
    pass


class A(Root):
    def foo_bar(self):  # Ok
        pass


class B(Root):
    def fooBar(self):  # TypeError
        pass


# 作为更高级和实用的例子，下面有一个元类，它用来检测重载方法，确保它的调用
# 参数跟父类中原始方法有着相同的参数签名。

import logging
from inspect import signature


class MatchSignaturesMeta(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        sup = super(self, self)
        for name, value in clsdict.items():
            if name.startswith('_') or not callable(value):
                continue
            # Get the previous definition (if any) and compare the signatures
            prev_dfn = getattr(sup, name, None)
            if prev_dfn:
                prev_sig = signature(prev_dfn)
                val_sig = signature(value)
                if prev_sig != val_sig:
                    logging.warning('Signature mismatch in %s. %s != %s',
                                    value.__qualname__, prev_sig, val_sig)


# Example
class Root(metaclass=MatchSignaturesMeta):
    pass


class A(Root):
    def foo(self, x, y):
        pass

    def spam(self, x, *, z):
        pass


# Class with redefined methods, but slightly different signatures
class B(A):
    def foo(self, a, b):
        pass

    def spam(self, x, z):
        pass
