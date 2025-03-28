#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : SYG
@Email     : shenyg2412@gmail.com
@File      : temp.py
@Created   : 2025-03-25 14:46
@Desc      : 
"""

def yield_t():
    x = 1
    yield x
    yield x+1
    yield x+2
    yield x+3
    yield x+4
excelp=yield_t()
print(next(excelp))
print(next(excelp))
print(next(excelp))
print(next(excelp))
print(next(excelp))