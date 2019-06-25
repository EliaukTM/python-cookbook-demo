#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
分数计算
"""
from fractions import Fraction

if __name__ == '__main__':
    a = Fraction(5, 4)
    b = Fraction(7, 16)
    print(a + b)
    print(a * b)

    c = a * b
    print(c.numerator)
    print(c.denominator)

    print(float(c))

    # Limiting the denominator of a value
    print(c.limit_denominator(8))

    x = 3.75
    y = Fraction(*x.as_integer_ratio())
    print(y)
