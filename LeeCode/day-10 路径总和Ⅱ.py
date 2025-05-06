#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Alias
@Email     : AliasGhost@gmail.com
@File      : day-10 路径总和Ⅱ.py
@Created   : 2025-04-23 16:16
@Desc      :
难度：中等
标签：树、DFS、回溯
题目描述：
给定一棵二叉树的根节点 root 和一个整数 targetSum，返回所有从根节点到叶子节点的路径，这些路径上节点值之和等于 targetSum。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root: TreeNode, targetSum: int) -> list[list[int]]:
    def dfs(node, remain, path):
        if not node:
            return
        path.append(node.val)
        # 如果是叶子节点且满足条件
        if not node.left and not node.right and remain == node.val:
            res.append(path.copy())  # 注意深拷贝
        # 递归左右子树
        dfs(node.left, remain - node.val, path)
        dfs(node.right, remain - node.val, path)
        path.pop()  # 回溯：移除当前节点

    res = []
    dfs(root, targetSum, [])
    return res


if __name__ == '__main__':
    # 构建示例树
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    # 查找路径
    print(pathSum(root, 22))  # 输出：[[5,4,11,2], [5,8,4,5]]