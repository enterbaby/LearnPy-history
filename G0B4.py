#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
'''def person (name,age,**kw):
    if 'city' in kw:
        pass
        print('haha')
    if 'job' in kw:
        pass
        print('bibi')
    print('name:',name,'age:',age,'other:',kw)'''
'''def person(name,age,*,city,job):#命名关键词参数
    print(name,age,city,job)'''
def person(name,age,*args,city,job):
    print(name,age,args,city,job)