#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想读写 JSON(JavaScript Object Notation) 编码格式的数据。
"""
import json

if __name__ == '__main__':
    data = {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23
    }
    json_str = json.dumps(data)
    print(json_str)

    data = json.loads(json_str)
    print(data)

    # Writing JSON data
    with open('data.json', 'w') as f:
        json.dump(data, f)

    # Reading JSON data
    with open('data.json', 'r') as f:
        data = json.load(f)
