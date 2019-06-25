#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai
import html
from html.parser import HTMLParser
from xml.sax.saxutils import unescape

if __name__ == '__main__':
    s = 'Elements are written as "<tag>text</tag>".'
    print(s)

    print(html.escape(s))

    print(html.escape(s, quote=False))

    s = 'Spicy Jalapeño'
    print(s.encode('ascii', errors='xmlcharrefreplace'))

    s = 'Spicy &quot;Jalape&#241;o&quot.'
    p = HTMLParser()
    print(p.unescape(s))

    t = 'The prompt is &gt;&gt;&gt;'
    print(unescape(t))
