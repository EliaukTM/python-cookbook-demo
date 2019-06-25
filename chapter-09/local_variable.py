#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想在使用范围内执行某个代码片段，并且希望在执行后所有的结果都不可见。
"""

# 为了理解这个问题，先试试一个简单场景。首先，在全局命名空间内执行一个代码片段：

a = 13
exec('b = a + 1')
print(b)


def test():
    a = 13
    exec('b = a + 1')
    print(b)

# test()

# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# File "<stdin>", line 4, in test
# NameError: global name 'b' is not defined

# 可以看出，最后抛出了一个 NameError 异常，就跟在 exec() 语句从没执行过一
# 样。要是你想在后面的计算中使用到 exec() 执行结果的话就会有问题了。


def test():
    a = 13
    loc = locals()
    exec('b = a + 1')
    b = loc['b']
    print(b)


test()
