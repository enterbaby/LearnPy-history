#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def div(n):#筛选
    s = str(n)
    if str(n)[::-1] == str(n):#daozhi
        return 1
def ispal(n):
        g = filter(div,n)
        return g
h = ispal(range(1,1000))
h = list(h)
print(h)