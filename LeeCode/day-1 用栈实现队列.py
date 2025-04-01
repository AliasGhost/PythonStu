#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Alias
@Email     : AliasGhost@gmail.com
@File      : day-1 用栈实现队列.py
@Created   : 2025-03-27 15:07
@Desc      :
栈：后进先出（LIFO）→ 需要让最后入队的元素最先出队。
队列：先进先出（FIFO）→ 直接使用队列无法满足栈的特性。
请你仅使用两个栈实现先入先出（FIFO）的队列。队列应当支持一般队列的所有操作
"""

class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        if self.empty():
            return None
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-2]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out


if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)
    print(q.peek())
    print(q.pop())
    print(q.empty())
