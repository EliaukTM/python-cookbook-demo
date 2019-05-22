#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想封装类的实例上面的“私有”数据，但是 Python 语言并没有访问控制。
"""


class A:
    def __init__(self):
        self._internal = 0  # An internal attribute
        self.public = 1  # A public attribute

    def public_method(self):
        '''
        A public method
        '''
        pass

    def _internal_method(self):
        pass

    """
    Python 并不会真的阻止别人访问内部名称。但是如果你这么做肯定是不好的，可能会导致脆弱的代码。
    """

    """
    你还可能会遇到在类定义中使用两个下划线 (__) 开头的命名。
    使用双下划线开始会导致访问名称变成其他形式。比如，在类 B 中，私有
    属性会被分别重命名为_B__private 和_B__private method 。这时候你可能会问这样
    重命名的目的是什么，答案就是继承——这种属性通过继承是无法被覆盖的。
    """

    class B:
        def __init__(self):
            self.__private = 0

        def __private_method(self):
            pass

        def public_method(self):
            pass
            self.__private_method()
