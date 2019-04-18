#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai
import re

if __name__ == '__main__':

    """
    当写正则式字符串的时候，相对普遍的做法是使用原始字符串比如 r'(\d+)/(\d+)/(\d+)' 。
    这种字符串将不去解析反斜杠，这在正则表达式中是很有用的。如果不这样做的话，你必须使用两个反斜杠，类似 '(\\d+)/(\\d+)/(\\d+)' 。
    """

    text1 = '11/27/2012'
    if re.match(r'\d+/\d+/\d+', text1):
        print('yes')
    else:
        print('no')

    text2 = 'Nov 27, 2012'
    if re.match(r'\d+/\d+/\d+', text2):
        print('yes')
    else:
        print('no')

    # 多次匹配。预编译
    datepat = re.compile(r'\d+/\d+/\d+')
    if datepat.match(text1):
        print('yes')
    else:
        print('no')

    # match() 总是从字符串开始去匹配，如果你想查找字符串任意部分的模式出现位置，使用 findall() 方法去代替
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    findall = datepat.findall(text)
    print(findall)

    # 利用括号去捕获分组
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    m = datepat.match('11/27/2012')
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
    print(m.groups())
    month, day, year = m.groups()

    datepat_findall = datepat.findall(text)
    print(datepat_findall)

    for m in datepat.finditer(text):
        print(m.groups())

    """
    你正在试着用正则表达式匹配某个文本模式，但是它找到的是模式的最长可能匹配。而你想修改它变成查找最短的可能匹配。
    """
    str_pat = re.compile(r'\"(.*)\"')
    text1 = 'Computer says "no."'
    print(str_pat.findall(text1))

    text2 = 'Computer says "no." Phone says "yes."'
    print(str_pat.findall(text2))

    # 为了修正这个问题，可以在模式中的 * 操作符后面加上? 修饰符
    # 这样就使得匹配变成非贪婪模式，从而得到最短的匹配，也就是我们想要的结果。
    str_pat = re.compile(r'\"(.*?)\"')
    print(str_pat.findall(text2))

    """
    你正在试着使用正则表达式去匹配一大块的文本，而你需要跨越多行去匹配。
    """
    # 当你用点 (.) 去匹配任意字符的时候，忘记了点 (.) 不能匹配换行符的事实。
    comment = re.compile(r'/\*(.*?)\*/')
    text1 = '/* this is a comment */'
    print(comment.findall(text1))
    text2 = '/* this is a \n multiline comment */'
    print(comment.findall(text2))

    # 为了修正这个问题，你可以修改模式字符串，增加对换行的支持。
    # (?:.|\n) 指定了一个非捕获组 (也就是它定义了一个仅仅用来做匹配，而不能通过单独捕获或者编号的组)。
    comment = re.compile(r'/\*((?:.|\n)*?)\*/')
    print(comment.findall(text2))

    # re.DOTALL 它可以让正则表达式中的点 (.) 匹配包括换行符在内的任意字符。
    comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
    print(comment.findall(text2))
