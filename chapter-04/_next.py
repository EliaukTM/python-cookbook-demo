#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""你想遍历一个可迭代对象中的所有元素，但是却不想使用 for 循环。"""


# 使用 next() 函数并在代码中捕获 StopIteration 异常
def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass


with open('/etc/passwd') as f:
    while True:
        line = next(f)
        if line is None:
            break
        print(line, end='')
