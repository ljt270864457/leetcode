#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 7:56 下午
# @Author  : liujiatian
# @File    : 二叉树的最大深度.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''
        通过递归计算最大深度
        叶子节点的深度为0，每次递归一层+1
        '''
        if not root:
            return 0
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
