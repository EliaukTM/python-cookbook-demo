#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai
import re
import unicodedata

if __name__ == '__main__':
    s1 = 'Spicy Jalape\u00f1o'
    s2 = 'Spicy Jalapen\u0303o'
    print(s1)
    print(s2)

    print(s1 == s2)
    print(len(s1))
    print(len(s2))

    """
    ”Spicy Jalapeño” 使用了两种形式来表示。第一种使用整体字符”ñ”(U+00F1)，第二种使用拉丁字母”n” 后面跟一个”˜” 的组合字符 (U+0303)
    """

    """
    NFC 表示字符应该是整体组成 (比如可能的话就使用单一编码)，而 NFD 表示字符应该分解为多个组合字符表示。
    """
    t1 = unicodedata.normalize('NFC', s1)
    t2 = unicodedata.normalize('NFC', s2)
    print(ascii(t1))

    t3 = unicodedata.normalize('NFD', s1)
    t4 = unicodedata.normalize('NFD', s2)
    print(t3 == t4)
    print(ascii(t3))

    """
    Python 同样支持扩展的标准化形式 NFKC 和 NFKD，它们在处理某些字符的时候增加了额外的兼容特性。比如
    """
    s = '\ufb01'
    print(s)
    print(unicodedata.normalize('NFD', s))
    print(unicodedata.normalize('NFKD', s))
    print(unicodedata.normalize('NFKC', s))

    """
     \\d 已经匹配任意的 unicode 数字字符了
    """
    num = re.compile('\d+')
    num.match('123')
    num.match('\u0661\u0662\u0663')

    pat = re.compile('stra\u00dfe', re.IGNORECASE)
    s = 'straße'
    print(pat.match(s))
    print(pat.match(s.upper()))
