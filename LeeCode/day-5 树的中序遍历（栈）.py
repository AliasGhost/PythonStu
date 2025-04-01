#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Alias
@Email     : AliasGhost@gmail.com
@File      : day-5 树的中序遍历（栈）.py
@Created   : 2025-04-01 11:36
@Desc      :

难度：中等
标签：栈、树、DFS
题目描述：
给定一个二叉树的根节点 root，返回它的 中序遍历（左 → 根 → 右）。要求使用 迭代算法（即非递归）实现。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 栈
def inorderTraversal(root: TreeNode) -> list[int]:
    stack, res, curr = [], [], root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res

# 递归
def inorderRecursive(root: TreeNode) -> list[int]:
    if not root:
        return []
    return inorderRecursive(root.left) + [root.val] + inorderRecursive(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    print(root.val)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print("中序遍历结果:", inorderTraversal(root))  # 应输出 [1, 3, 2]
    print("中序遍历结果:", inorderRecursive(root))  # 应输出 [1, 3, 2]
