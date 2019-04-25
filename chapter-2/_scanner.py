#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你有一个字符串，想从左至右将其解析为一个令牌流。
"""
import re
from collections import namedtuple

if __name__ == '__main__':
    text = 'foo = 23 + 42 * 10'

    NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
    NUM = r'(?P<NUM>\d+)'
    PLUS = r'(?P<PLUS>\+)'
    TIMES = r'(?P<TIMES>\*)'
    EQ = r'(?P<EQ>=)'
    WS = r'(?P<WS>\s+)'
    master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

    print(master_pat.groups)

    """
    为了令牌化，使用模式对象很少被人知道的 scanner() 方法。这个方法会创建一个 scanner 对象，
    在这个对象上不断的调用 match() 方法会一步步的扫描目标文本，每步一个匹配
    """
    scanner = master_pat.scanner('foo = 42')

    match = scanner.match()
    print(match.lastgroup, match.group())

    match = scanner.match()
    print(match.lastgroup, match.group())

    """
    实际使用这种技术的时候，可以很容易的像下面这样将上述代码打包到一个生成器中
    """


    def generate_tokens(pat, text):
        Token = namedtuple('Token', ['type', 'value'])
        scanner = pat.scanner(text)
        for m in iter(scanner.match, None):
            yield Token(m.lastgroup, m.group())


    for tok in generate_tokens(master_pat, 'foo = 42'):
        print(tok)

