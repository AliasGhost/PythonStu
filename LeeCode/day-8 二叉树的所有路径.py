#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Alias
@Email     : AliasGhost@gmail.com
@File      : day-8 二叉树的所有路径.py
@Created   : 2025-04-03 16:51
@Desc      :
难度：简单
标签：树、DFS、回溯、字符串
题目描述：
给定一个二叉树的根节点 root，返回所有从根节点到叶子节点的路径（以 "->" 连接节点值）。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths(root: TreeNode) -> list[str]:
    def dfs(node, path):
        if not node:
            return
        path.append(str(node.val))
        # 如果是叶子节点，保存路径
        if not node.left and not node.right:
            res.append("->".join(path))
        # 递归处理左右子树
        dfs(node.left, path)
        dfs(node.right, path)
        path.pop()  # 回溯：移除当前节点

    res = []
    dfs(root, [])
    return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(binaryTreePaths(root))
"""
         1
      2     3               1->2            1->3
   4    5  6   7            1->2->4 1->2->5 1->3->6 1->3->7
"""
