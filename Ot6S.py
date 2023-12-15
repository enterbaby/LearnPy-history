#!/usr/bin/env python3
# -*- coding: utf-8 -*-
d = {'M':89,'D':67,'F':55}
d['H'] = 88
print(d['H'])
name = input('please input your name:')
score = input('please input your score:')
d[name] = score
sear = input('whose do you want:')
if sear in d:
    print(d[sear])
else:
    print('滚!')