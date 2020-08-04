#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 7:58 下午
# @Author  : liujiatian
# @File    : 二叉树层次遍历.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []

        result = []
        queue = [root]
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(tmp)
        return result
