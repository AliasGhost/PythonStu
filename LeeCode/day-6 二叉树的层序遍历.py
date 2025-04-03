#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Alias
@Email     : AliasGhost@gmail.com
@File      : day-6 二叉树的层序遍历.py
@Created   : 2025-04-03 10:54
@Desc      :
难度：中等
标签：树、BFS、队列
题目描述：
给定一个二叉树的根节点 root，返回其节点值的 层序遍历 结果（即逐层从左到右访问所有节点）。
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: TreeNode) -> list[list[int]]:
    if not root:
        return []

    queue = deque([root])  # 队列初始化，存入根节点
    res = []

    while queue:
        level_size = len(queue)  # 当前层的节点数
        current_level = []  # 存储当前层的节点值

        for _ in range(level_size):
            node = queue.popleft()  # 弹出队首节点
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)  # 左子节点入队
            if node.right:
                queue.append(node.right)  # 右子节点入队

        res.append(current_level)  # 将当前层加入结果

    return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    print(levelOrder(root))