#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想将某个实例的属性访问代理到内部另一个实例中去，目的可能是作为继承的一
个替代方法或者实现代理模式。
"""


class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B1:
    """ 简单的代理 """

    def __init__(self):
        self._a = A()

    def spam(self, x):
        # Delegate to the internal self._a instance
        return self._a.spam(x)

    def foo(self):
        # Delegate to the internal self._a instance
        return self._a.foo()

    def bar(self):
        pass


"""
***************************************
"""

"""
如果有大量的方法需要代理，那么使用 getattr () 方法或许或更好些
"""


class B2:
    """ 使用 __getattr__ 的代理，代理方法比较多时候 """

    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    # Expose all of the methods defined on class A
    def __getattr__(self, name):
        """ 这个方法在访问的 attribute 不存在的时候被调用
        the __getattr__() method is actually a fallback method
        that only gets called when an attribute is not found"""
        return getattr(self._a, name)


"""
另外一个代理例子是实现代理模式
"""


# A proxy class that wraps around another object, but
# exposes its public attributes
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj

    def __getattr__(self, name):
        print('getattr:', name)
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)

    # Delegate attribute deletion
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)


# 使用这个代理类时，你只需要用它来包装下其他类即可
class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar:', self.x, y)


# Create an instance
s = Spam(2)
# Create a proxy around it
p = Proxy(s)
# Access the proxy
print(p.x) # Outputs 2
p.bar(3) # Outputs "Spam.bar: 2 3"
p.x = 37 # Changes s.x to 37