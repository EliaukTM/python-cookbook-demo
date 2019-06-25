#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你需要将一个 Python 对象序列化为一个字节流，以便将它保存到一个文件、存储
到数据库或者通过网络传输它。
"""
import pickle

if __name__ == '__main__':
    data = ...  # Some Python object
    f = open('somefile', 'wb')
    pickle.dump(data, f)

    # 为了将一个对象转储为一个字符串，可以使用pickle.dumps()

    s = pickle.dumps(data)

    # 为了从字节流中恢复一个对象，使用picle.load()或pickle.loads()函数。
    f = open('somefile', 'rb')
    data = pickle.load(f)

    data = pickle.loads(s)