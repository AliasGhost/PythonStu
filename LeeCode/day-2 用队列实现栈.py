#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Alias
@Email     : AliasGhost@gmail.com
@File      : day-2 用队列实现栈.py
@Created   : 2025-03-28 09:10
@Desc      : 

栈：后进先出（LIFO）→ 需要让最后入队的元素最先出队。
队列：先进先出（FIFO）→ 直接使用队列无法满足栈的特性。

请你仅使用两个队列实现一个后入先出（LIFO）的栈。支持栈的所有操作（push、pop、top、empty）：

实现 MyStack 类：

void push(int x) 将元素 x 压入栈顶

int pop() 移除并返回栈顶元素

int top() 返回栈顶元素（不移除）

boolean empty() 判断栈是否为空
"""

from collections import deque


class MyQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)  # [1, 2, 3]
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())  # [2, 3, 1][3, 1, 2]

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.top())
    print(q.pop())
    print(q.empty())
