#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def trim(str):
    n = 0
    s = 0
    while n == 0 or s == 0:
        if str[0:1] == ' ':
            str = str[1:]
        elif str[0] != ' ':
            n = 1
        elif str[-1:] == ' ':
            str = str[:-2]
        else:
            n = 1
    #print(str)
    return str