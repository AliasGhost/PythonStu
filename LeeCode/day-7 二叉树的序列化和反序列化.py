#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Alias
@Email     : AliasGhost@gmail.com
@File      : day-7 二叉树的序列化和反序列化.py
@Created   : 2025-04-03 14:29
@Desc      :
难度：困难
标签：树、DFS、字符串、设计
题目描述：
设计一个算法，将二叉树序列化为字符串，并能将字符串反序列化为原始的二叉树结构。你需要保证二叉树可以被唯一地序列化/反序列化。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """将树序列化为字符串"""
        if not root:
            return "None"
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return f"{root.val},{left},{right}"  # 前序遍历格式

    def deserialize(self, data: str) -> TreeNode:
        """从字符串反序列化树"""
        nodes = data.split(',')  # 拆分为列表
        return self._build_tree(nodes)

    def _build_tree(self, nodes: list) -> TreeNode:
        if nodes[0] == "None":
            nodes.pop(0)
            return None
        root = TreeNode(int(nodes.pop(0)))  # 创建当前节点
        root.left = self._build_tree(nodes)  # 递归左子树
        root.right = self._build_tree(nodes)  # 递归右子树
        return root

if __name__ == '__main__':
    # 构建示例树
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    # 序列化 & 反序列化
    codec = Codec()
    print(codec.serialize(root))  # "1,2,None,None,3,4,None,None,5,None,None"
    print(codec.deserialize(codec.serialize(root)))  # 恢复原始结构