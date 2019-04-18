#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai
import re
from calendar import month_abbr


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


if __name__ == '__main__':
    text = 'yeah, but no, but yeah, but no, but yeah'
    text.replace('yeah', 'yep')

    """
    sub() 函数中的第一个参数是被匹配的模式，第二个参数是替换模式。反斜杠数字
    比如 \3 指向前面模式的捕获组号。
    """
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

    """
    对于更加复杂的替换，可以传递一个替换回调函数来代替
    """
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    datepat.sub(change_date, text)

    """
    替换后有多少替换发生了
    """
    newtext, n = datepat.subn(r'\3-\1-\2', text)

    """
    忽略大小写的方式搜索与替换文本字符串
    """
    text = 'UPPER PYTHON, lower python, Mixed Python'
    re.findall('python', text, flags=re.IGNORECASE)
    re.sub('python', 'snake', text, flags=re.IGNORECASE)

    """
    例子揭示了一个小缺陷，替换字符串并不会自动跟被匹配字符串的大小写保持一致。为了修复这个，你可能需要一个辅助函数，就像上面的matchcase
    """
    re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
