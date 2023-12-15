#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections.abc import Iterable
def findm(L):
    x = 0
    i = 0
    if isinstance(L,Iterable):
        for n in L:
            if n > x:
                x = n
            if n < i:
                i = n
        return (x,i)
    