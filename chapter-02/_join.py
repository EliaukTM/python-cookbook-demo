#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
字符串合并
"""

if __name__ == '__main__':
    parts = ['Is', 'Chicago', 'Not', 'Chicago?']
    print(' '.join(parts))
    print(','.join(parts))
    print(''.join(parts))

    a = 'Is Chicago'
    b = 'Not Chicago?'
    print(a + ' ' + b)
    print('{} {}'.format(a, b))

    # 下面的代码有性能问题
    s = ''
    for p in parts:
        s += p

    # 考虑用join 优化性能
    data = ['ACME', 50, 91.1]
    print(','.join(str(d) for d in data))


    # 你准备编写构建大量小字符串的输出代码，你最好考虑下使用生
    # 成器函数，利用 yield 语句产生输出片段。
    def sample():
        yield 'Is'
        yield 'Chicago'
        yield 'Not'
        yield 'Chicago?'


    print(''.join(sample()))
