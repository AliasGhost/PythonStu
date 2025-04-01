#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Alias
@Email     : AliasGhost@gmail.com
@File      : day-4 最小栈.py
@Created   : 2025-04-01 10:10
@Desc      :
设计一个支持 push、pop、top 操作，并能在 常数时间 内检索到最小元素的栈。

实现 MinStack 类：

void push(int val) 将元素 val 压入栈。

void pop() 删除栈顶元素。

int top() 获取栈顶元素。

int getMin() 返回栈中的最小元素。

要求：所有操作的时间复杂度为 O(1)。
"""


class min_stack:
    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> int:
        self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == '__main__':
    a = min_stack()
    print(a.push(-2))
    print(a.push(0))
    print(a.push(-3))
    print(a.getMin())
    print(a.pop())
    print(a.top())
    print(a.getMin())
