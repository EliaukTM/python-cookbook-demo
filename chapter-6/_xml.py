#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想从一个简单的 XML 文档中提取数据。
"""

from urllib.request import urlopen
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import iterparse
from xml.etree.ElementTree import parse

if __name__ == '__main__':
    u = urlopen('http://planet.python.org/rss20.xml')
    doc = parse(u)

    for item in doc.iterfind('channel/item'):
        title = item.findtext('title')
        date = item.findtext('pubDate')
        link = item.findtext('link')
        print(title)
        print(date)
        print(link)
        print()

"""
你想使用尽可能少的内存从一个超大的 XML 文档中提取数据。
"""


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
            elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


"""
你想使用一个 Python 字典存储数据，并将它转换成 XML 格式。
"""


def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
        return elem


"""
你想读取一个 XML 文档，对它最一些修改，然后将结果写回 XML 文档。
"""


def modify():
    doc = parse('pred.xml')
    root = doc.getroot()
    print(root)

    root.remove(root.find('sri'))
    root.remove(root.find('cr'))
    root.getchildren().index(root.find('nm'))

    e = Element('spam')
    e.text = 'This is a test'
    root.insert(2, e)
    doc.write('newpred.xml', xml_declaration=True)


"""
你想解析某个 XML 文档，文档中使用了 XML 命名空间。
"""


class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)

    def register(self, name, uri):
        self.namespaces[name] = '{' + uri + '}'

    def __call__(self, path):
        return path.format_map(self.namespaces)


def deal_namespace():
    ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
    doc.find(ns('content/{html}html'))
    doc.findtext(ns('content/{html}html/{html}head/{html}title'))
