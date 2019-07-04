#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你需要通过 HTTP 协议以客户端的方式访问多种服务。例如，下载数据或者与基
于 REST 的 API 进行交互。
"""

# 对于简单的事情来说，通常使用 urllib.request 模块就够了。

from urllib import request, parse

# Base URL being accessed
url = 'http://httpbin.org/get'
# Dictionary of query parameters (if any)
parms = {
    'name1': 'value1',
    'name2': 'value2'
}
# Encode the query string
querystring = parse.urlencode(parms)
# Make a GET request and read the response
u = request.urlopen(url + '?' + querystring)
resp = u.read()

# 如果你需要使用 POST 方法在请求主体中发送查询参数，可以将参数编码后作为
# 可选参数提供给 urlopen() 函数，就像这样

from urllib import request, parse

# Base URL being accessed
url = 'http://httpbin.org/post'
# Dictionary of query parameters (if any)
parms = {
    'name1': 'value1',
    'name2': 'value2'
}
# Encode the query string
querystring = parse.urlencode(parms)
# Make a POST request and read the response
u = request.urlopen(url, querystring.encode('ascii'))
resp = u.read()

# 如果你需要在发出的请求中提供一些自定义的 HTTP 头，例如修改 user-agent
# 字段, 可以创建一个包含字段值的字典，并创建一个 Request 实例然后将其传给
# urlopen() ，如下：

from urllib import request

...
# Extra headers
headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}
req = request.Request(url, querystring.encode('ascii'), headers=headers)
# Make a request and read the response
u = request.urlopen(req)
resp = u.read()


