#!/usr/bin/env python3
# -*- coding: utf-8 -*-
weight = input('please input your weight(kg):')
height = input('please input your height(m):')
weight = float(weight)
height = float(height)
BMI = weight/(height**2)
if BMI < 18.5:
    print('您的BMI指数为%.f,过轻'%BMI)
elif BMI < 25:
    print('正常')
elif BMI < 28:
    print('您的BMI指数为%.f,过重'%BMI)
elif BMI < 32:
    print('肥胖')
else:
    print('严重肥胖')