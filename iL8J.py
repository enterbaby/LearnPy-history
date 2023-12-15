#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
print('一元二次方程求根')
def quad(a,b,c):
 if not isinstance(a+b+c,(int,float)):
    raise TypeError('Wrong type')
 elif b**2-4*a*c >= 0:
    x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    print(x1)
    return x1,x2
 else:
    print('无解')

print('quadratic(2, 3, 1) =', quad('c', 3, 1))
print('quadratic(1, 3, -4) =', quad(1, 3, -4))

if quad(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quad(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')