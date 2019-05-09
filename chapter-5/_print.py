# !/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

if __name__ == '__main__':
    """
    你想将 print() 函数的输出重定向到一个文件中去
    """
    with open('d:/work/test.txt', 'wt') as f:
        print('Hello World!', file=f)

    print('ACME', 50, 91.5)
    print('ACME', 50, 91.5, sep=',')
    print('ACME', 50, 91.5, sep=',', end='!!\n')

    for i in range(5):
        print(i)

    for i in range(5):
        print(i, end=' ')

    print(','.join('ACME', '50', '91.5'))
