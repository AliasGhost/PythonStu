#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : SYG
@Email     : shenyg2412@gmail.com
@File      : day-3.py
@Created   : 2025-03-28 14:04
@Desc      : 
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
