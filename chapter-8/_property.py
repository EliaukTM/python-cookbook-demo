#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想给某个实例 attribute 增加除访问与修改之外的其他处理逻辑，比如类型检查
或合法性验证。
"""


class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

    """
    上述代码中有三个相关联的方法，这三个方法的名字都必须一样。第一个方法是一
    个 getter 函数，它使得 first name 成为一个属性。其他两个方法给 first name 属
    性添加了 setter 和 deleter 函数。需要强调的是只有在 first name 属性被创建后，
    后面的两个装饰器 @first name.setter 和 @first name.deleter 才能被定义。
    """

if __name__ == '__main__':
    a = Person('Guido')

    # 调用 getter 方法
    print(a.first_name)
    # 调用 setter 方法
    a.first_name = 42
    # 调用 deleter 方法
    del a.first_name