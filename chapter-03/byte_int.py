#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你有一个字节字符串并想将它解压成一个整数。或者，你需要将一个大整数转换为一个字节字符串。
"""

if __name__ == '__main__':
    data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
    print(len(data))
    print(int.from_bytes(data, 'little'))
    print(int.from_bytes(data, 'big'))

    # 为了将一个大整数转换为一个字节字符串，使用
    # int.to_bytes()方法，并像下面这样指定字节数和字节顺序
    x = 94522842520747284487117727783387188
    print(x.to_bytes(16, 'big'))

    # 字节顺序规则 (little 或 big) 仅仅指定了构建整数时的字节的低位高位排列方式。
    x = 0x01020304
    print(x.to_bytes(4, 'big'))
    print(x.to_bytes(4, 'little'))
