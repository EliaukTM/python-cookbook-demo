#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai


import requests

resp = requests.head('http://www.python.org/index.html')
status = resp.status_code
last_modified = resp.headers['last-modified']
content_type = resp.headers['content-type']
content_length = resp.headers['content-length']
# Here is a requests example that executes a login into the Python Package index using
# basic authentication:
resp = requests.get('http://pypi.python.org/pypi?:action=login',
                    auth=('user', 'password'))
# Here is an example of using requests to pass HTTP cookies from one request to the
# next:
# First request
resp1 = requests.get(url)
...
# Second requests with cookies received on first requests
resp2 = requests.get(url, cookies=resp1.cookies)
# Last, but not least, here is an example of using requests to upload content:


url = 'http://httpbin.org/post'
files = {'file': ('data.csv', open('data.csv', 'rb'))}
r = requests.post(url, files=files)
