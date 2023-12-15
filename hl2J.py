#!/usr/bin/env python3
# -*- coding: utf-8 -*-
birth = input('生日：')
birth = int(birth)
if birth <= 1999 & birth > 1989:
    print('90后')
elif birth <=1989:
    print('you are to old!')
else :
    print('00后')