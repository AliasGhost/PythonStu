#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Alias
@Email     : AliasGhost@gmail.com
@File      : day-3 有效的括号.py
@Created   : 2025-03-28 14:04
@Desc      :

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s，判断字符串是否有效。有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
"""


# (({{}[]}))
def is_bracket(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else ''
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack


s = '((){)'
print(is_bracket(s))