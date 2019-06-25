#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想读写一个二进制数组的结构化数据到 Python 元组中。
"""
from struct import Struct


def write_records(records, format, f):
    '''
    Write a sequence of tuples to a binary file of structures.
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)


def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset) for offset in range(0, len(data), record_struct.size))


if __name__ == '__main__':
    records = [(1, 2.3, 4.5),
               (6, 7.8, 9.0),
               (12, 13.4, 56.7)]
    with open('data.b', 'wb') as f:
        write_records(records, '<idd', f)

    '''
       有很多种方法来读取这个文件并返回一个元组列表。首先，如果你打算以块的形式
       增量读取文件，你可以这样做
       '''
    with open('data.b', 'rb') as f:
        for rec in read_records('<idd', f):
            # Process rec
            pass

    '''
    如果你想将整个文件一次性读取到一个字节字符串中，然后在分片解析。那么你可以这样做：
    '''
    with open('data.b', 'rb') as f:
        data = f.read()
    for rec in unpack_records('<idd', data):
        # Process rec
        pass
