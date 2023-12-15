#!/usr/bin/env python3
# -*- coding: utf-8 -*-
forward = list(range(101))
sum = 0
n = 0
while n <101:
    sum = sum + forward[n]
    n = n + 1
print(sum)
print(forward[100])
print(forward[0])