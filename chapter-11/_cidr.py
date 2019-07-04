#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你有一个 CIDR 网络地址比如“123.45.67.89/27”，你想将其转换成它所代表的所
有 IP （比如，“123.45.67.64”, “123.45.67.65”, …, “123.45.67.95”)）
"""
import ipaddress

# 可以使用 ipaddress 模块很容易的实现这样的计算。例如：
if __name__ == '__main__':
    net = ipaddress.ip_network('123.45.67.64/27')
    print(net)

    for a in net:
        print(a)

    net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
    print(net6)

    for a in net6:
        print(a)

    print(net.num_addresses)

    print(net[0])

    a = ipaddress.ip_address('123.45.67.69')
    print(a in net)

    b = ipaddress.ip_address('123.45.67.123')
    print(b in net)

    inet = ipaddress.ip_interface('123.45.67.73/27')
    print(inet.network)
    print(inet.ip)
