#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
L = ['skjy','shKO','HkjIi','GJHGK']
def normal(L):
    def f(x):
        return x.capitalize()
    L = map(f,L)
    S = list(L)
    print(S)
normal(L)