#!/usr/bin/env python3
# -*- coding: utf-8 -*-
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    #s = t[0]
    s = t[1]
    return s
L2 = sorted(L, key=by_name)
print(L2)