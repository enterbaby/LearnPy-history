#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def oddit():#无限序列+生成器
    n = 1
    while True:
        n = n + 2
        yield n
def notdiv(n):#筛选函数
    return lambda x:x%n>0
def prime():#无限循环
    yield 2
    it = oddit()# 初始序列
    while True:
        n = next(it)#返回序列第一个数
        yield n
        it = filter(notdiv(n),it)#构造新序列
s = prime()
for n in s:
    if n < 1000:
        print(n)
    else:
        break