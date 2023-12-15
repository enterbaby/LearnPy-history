#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def triangles():
    L = [0,1,0]
    while True:
        yield L[1:-1]
        L = [0] + [L[x]+L[x+1] for x in range(len(L)-1)] + [0]
