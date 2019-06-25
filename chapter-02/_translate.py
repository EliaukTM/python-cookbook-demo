#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai
import sys
import unicodedata

if __name__ == '__main__':
    s = 'pýtĥöñ\fis\tawesome\r\n'
    print(s)

    remap = {
        ord('\t'): ' ',
        ord('\f'): ' ',
        ord('\r'): None  # Deleted
    }
    a = s.translate(remap)
    print(a)

    """
     dict.fromkeys() 方法构造一个字典，每个 Unicode 和音符作为键，对于的值全部为 None
    """
    cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                             if unicodedata.combining(chr(c)))
    b = unicodedata.normalize('NFD', a)
    print(b)
    print(b.translate(cmb_chrs))
