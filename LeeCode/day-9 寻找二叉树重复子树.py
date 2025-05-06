#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Alias
@Email     : AliasGhost@gmail.com
@File      : day-9 寻找二叉树重复子树.py
@Created   : 2025-04-08 13:44
@Desc      :
难度：中等
标签：树、哈希表、DFS
题目描述：
给定一棵二叉树的根节点 root，返回所有重复的子树。对于同一类的重复子树，只需返回其中任意一棵的根节点即可。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findDuplicateSubtrees(root: TreeNode) -> list[TreeNode]:
    from collections import defaultdict

    subtree_count = defaultdict(int)  # 记录子树序列化字符串的出现次数
    result = []

    def serialize(node):
        if not node:
            return "None"
        # 序列化当前子树（后序遍历）
        left_str = serialize(node.left)
        right_str = serialize(node.right)
        subtree_str = f"{node.val},{left_str},{right_str}"  # 拼接唯一标识

        # 检查是否重复
        subtree_count[subtree_str] += 1
        if subtree_count[subtree_str] == 2:  # 避免重复添加
            result.append(node)
        return subtree_str

    serialize(root)
    return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.left.left = TreeNode(4)
    duplicates = findDuplicateSubtrees(root)
    for node in duplicates:
        print(node.val)
