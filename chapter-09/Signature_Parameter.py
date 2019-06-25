#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你有一个函数或方法，它使用 *args 和 **kwargs 作为参数，这样使得它比较通用，
但有时候你想检查传递进来的参数是不是某个你想要的类型。
"""
import inspect
from inspect import Signature, Parameter

if __name__ == '__main__':
    # Make a signature for a func(x, y=42, *, z=None)
    parms = [Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
             Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
             Parameter('z', Parameter.KEYWORD_ONLY, default=None)]
    sig = Signature(parms)
    print(sig)

    """
    一旦你有了一个签名对象，你就可以使用它的 bind() 方法很容易的将它绑定到
    *args 和 **kwargs 上去。下面是一个简单的演示：
    """


    def func(*args, **kwargs):
        bound_values = sig.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            print(name, value)


    func(1, 2, z=3)
    func(1)
    func(1, z=3)
    func(y=2, x=1)
    func(1, 2, 3, 4)

    """
    可以看出来，通过将签名和传递的参数绑定起来，可以强制函数调用遵循特定的规
    则，比如必填、默认、重复等等。
    """

"""
下面是一个强制函数签名更具体的例子。在代码中，我们在基类中先定义了一个非
常通用的 init () 方法，然后我们强制所有的子类必须提供一个特定的参数签名。
"""

from inspect import Signature, Parameter


def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
             for name in names]
    return Signature(parms)


class Structure:
    __signature__ = make_sig()

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)
    # Example use


class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')


class Point(Structure):
    __signature__ = make_sig('x', 'y')


if __name__ == '__main__':
    print(inspect.signature(Stock))
    s1 = Stock('ACME', 100, 490.1)
    # s2 = Stock('ACME', 100)
    # s3 = Stock('ACME', 100, 490.1, shares=50)
