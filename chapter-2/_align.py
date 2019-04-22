#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想通过某种对齐方式来格式化字符串
"""

if __name__ == '__main__':
    text = 'Hello World'

    print(text.ljust(20))
    print(text.rjust(20))
    print(text.center(20))

    print(text.rjust(20, '='))
    text.center(20, '*')

    """
     format() 同样可以用来很容易的对齐字符串。你要做的就是使用 <,> 或者ˆ 字符后面紧跟一个指定的宽度
    """
    print(format(text, '>20'))
    print(format(text, '<20'))
    print(format(text, '^20'))

    print(format(text, '=>20s'))
    print(format(text, '*^20s'))

    print('{:>10s} {:>10s}'.format('Hello', 'World'))

    x = 1.2345
    print(format(x, '>10'))
    print(format(x, '^10.2f'))

    """
    在老的代码中，你经常会看到被用来格式化文本的 % 操作符。
    但是，在新版本代码中，你应该优先选择 format() 函数或者方法。 
    format() 要比 % 操作符的功能更为强大。
    并且 format() 也比使用 ljust() , rjust() 或 center()方法更通用，
    因为它可以用来格式化任意对象，而不仅仅是字符串。
    """
