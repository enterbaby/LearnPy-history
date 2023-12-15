#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = (85-72)/72*100
print('{0:.2f}%'.format(s))
#列表
fy = [21,21,32,54]
print(fy)
print(len(fy))
print(fy[-1])
fy.append(43)
print(fy)
fy.insert(1,'fuck')
print(fy)
fy.pop(4)
print(fy)
fy.insert(1,True)
fm = (True,'ref',324.78,32)
print(fm[2])
