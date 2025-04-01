#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Alias
@Email     : AliasGhost@gmail.com
@File      : PyTest.py
@Created   : 2025-03-27 15:25
@Desc      : 
"""

stack_in = []
print(len(stack_in) == 0)
print(not stack_in)
mapping = {')': '(', '}': '{', ']': '['}
print(mapping.keys(), mapping.values())
print(mapping,mapping[')'])
s = '(){}'

for char in mapping:
    print(char)