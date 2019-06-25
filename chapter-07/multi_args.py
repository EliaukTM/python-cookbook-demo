#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想构造一个可接受任意数量参数的函数。
"""

# 一个函数接受任意数量的位置参数
import html


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


# 为了接受任意数量的关键字参数，使用一个以 ** 开头的参数
def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))
    return element


def anyargs(*args, **kwargs):
    print(args)  # A tuple
    print(kwargs)  # A dict


if __name__ == '__main__':
    print(avg(1, 2))
    print(avg(1, 2, 3, 4))

    make_element('item', 'Albatross', size='large', quantity=6)
    make_element('p', '<spam>')
