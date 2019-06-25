#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你需要使用 Base64 格式解码或编码二进制数据。
"""
import base64

if __name__ == '__main__':
    s = b'hello'
    a = base64.b64encode(s)
    print(a)

    print(base64.b64decode(a))
