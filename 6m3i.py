#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
def prod(L):
    def f(x,y):
        y = x*y
        return y
    r = reduce(f,L)
    return r
s = prod([3,5,7,9])
print (s)