#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想将一个十六进制字符串解码成一个字节字符串或者将一个字节字符串编码成一
个十六进制字符串。
"""
import base64
import binascii

if __name__ == '__main__':
    s = b'hello'
    h = binascii.b2a_hex(s)
    print(h)
    print(binascii.a2b_hex(h))

    # 类似的功能同样可以在base64模块中找到。
    h = base64.b16encode(s)
    print(h)
    print(base64.b16decode(h))
