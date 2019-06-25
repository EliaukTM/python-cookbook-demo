#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想在子类中调用父类的某个已经被覆盖的方法。
"""


class A:
    def spam(self):
        print('A.spam')


class B(A):
    def spam(self):
        print('B.spam')
        super().spam()  # Call parent spam()


"""
super() 函数的一个常见用法是在 init () 方法中确保父类被正确的初始化了
"""


class A:
    def __init__(self):
        self.x = 0


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1
