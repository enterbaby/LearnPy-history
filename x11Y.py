#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 列表生成式
import math
L = ['Hello', 'World', 18, 'Apple', None]
X = [x.lower() if isinstance(x,str) else None for x in L]
print(X)
#结果中None值未去掉