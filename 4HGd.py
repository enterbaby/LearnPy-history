#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def triang(max):
    L = []
    x = 1
    while x < max:
        if x == 1:
            L =[1]
            x = x+1
        else:
            n = 2
            while n<(x+2):
                s = 1
                s = s*((x-1)/(n-1))
                L.append(s)
                n = n + 1
        yield(L)
        x = x + 1


