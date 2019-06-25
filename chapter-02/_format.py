#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想创建一个内嵌变量的字符串，变量被它的值所表示的字符串替换掉。
"""
import string
import sys

if __name__ == '__main__':
    s = '{name} has {n} messages.'
    print(s.format(name='Guido', n=37))

    # 如果要被替换的变量能在变量域中找到，那么你可以结合使用 format map()
    # 和 vars()
    name = 'Guido'
    n = 37
    print(s.format_map(vars()))


    class Info:
        def __init__(self, name, n):
            self.name = name
            self.n = n


    # vars() 还有一个有意思的特性就是它也适用于对象实例。
    a = Info('Guido', 37)
    s.format_map(vars(a))

    # format 和 format map() 的一个缺陷就是它们并不能很好的处理变量缺失的情况

    # s.format(name='Guido')

    """
     Traceback(most recent call last):
     File "<stdin>", line 1, in < module > 
     KeyError: 'n'
    """


    # 一种避免这种错误的方法是另外定义一个含有 missing () 方法的字典对象

    class safesub(dict):
        """ 防止 key 找不到 """

        #  missing () 方法可以让你定义如何处理缺失的值
        def __missing__(self, key):
            return '{' + key + '}'


    del n
    print(s.format_map(safesub(vars())))

    """
    如果你发现自己在代码中频繁的执行这些步骤，你可以将变量替换步骤用一个工具函数封装起来。
    """


    def sub(text):
        # sub() 函数使用 sys._getframe(1) 返回调用者的栈帧。可以从中访问属性
        # f_locals 来获得局部变量
        return text.format_map(safesub(sys._getframe(1).f_locals))


    name = 'Guido'
    n = 37
    print(sub('Hello {name}'))

    # format()和format_map()相比较下面面这些方案而已更加先进，因此应该
    # 被优先选择。使用format()方法还有一个好处就是你可以获得对字符串格式化的所有
    # 支持(对齐，填充，数字格式化等待)，而这些特性是使用像模板字符串之类的方案不
    # 可能获得的。
    s = string.Template('$name has $n messages.')
    s.substitute(vars())
