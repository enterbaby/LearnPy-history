#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
L = ['skjy','shKO','HkjIi','GJHGK']
def normal(L):
    def f(x):
        K = list(x)
        K[0] = K[0].upper()
        D = ''.join(K)
        return D
    def g(x):
            x = x.lower()
            return x
    L = map(g,L)
    L = map(f,L)
    S = list(L)
    print(S)
normal(L)