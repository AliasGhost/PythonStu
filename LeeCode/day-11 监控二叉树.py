#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Alias
@Email     : AliasGhost@gmail.com
@File      : day-11 监控二叉树.py
@Created   : 2025-05-06 09:32
@Desc      :
难度：困难
标签：树、DFS、贪心算法
题目描述：
给定一棵二叉树的根节点 root，要求在树的节点上安装摄像头。每个摄像头可以监控 自身、父节点和直接子节点。求覆盖整棵树所需的最小摄像头数量。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minCameraCover(root: TreeNode) -> int:
    result = 0  # 记录摄像头总数

    def dfs(node):
        nonlocal result
        if not node:
            return 1  # 空节点默认已被监控（避免干扰）

        left = dfs(node.left)
        right = dfs(node.right)

        # 情况1：任一子节点未被监控 → 当前节点必须安装摄像头
        if left == 0 or right == 0:
            result += 1
            return 2

        # 情况2：任一子节点有摄像头 → 当前节点已被监控
        if left == 2 or right == 2:
            return 1

        # 情况3：子节点均被监控但无摄像头 → 当前节点未被监控
        return 0

    # 检查根节点是否未被监控
    if dfs(root) == 0:
        result += 1
    return result

if __name__ == '__main__':
    # 构建示例树
    root = TreeNode(0)
    root.left = TreeNode(0)
    root.left.left = TreeNode(0)
    root.left.left.right = TreeNode(0)

    print(minCameraCover(root))  # 输出：2