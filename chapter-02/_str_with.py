#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

if __name__ == '__main__':
    filename = 'spam.txt'
    endswith = filename.endswith('.txt')
    print(endswith)
    startswith = filename.startswith('file:')
    print(startswith)

    file_names = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
    _endswith = [name for name in file_names if name.endswith(('.c', '.h'))]
    print(_endswith)
    _any = any(name.endswith('.py') for name in file_names)
    print(_any)

    choices = ['http:', 'ftp:']
    url = 'http://www.python.org'
    """
    这个方法中必须要输入一个元组作为参数。如果你恰巧有一个 list 或者 set 类型的选择项，要确保传递参数前先调用 tuple() 将其转换为元组类型。
    """
    # url.startswith(choices)
    url.startswith(tuple(choices))
