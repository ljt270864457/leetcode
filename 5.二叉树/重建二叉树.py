#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 3:40 下午
# @Author  : liujiatian
# @File    : 重建二叉树.py

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder) -> TreeNode:
        if not preorder:
            return TreeNode(None)
        root = TreeNode(preorder.pop(0))
        new_root = root
        for number in preorder:
            if not new_root.left:
                new_root.left = TreeNode(number)
            elif not new_root.right:
                new_root.right = TreeNode(number)
            else:
                new_root = new_root.right
                new_root.left = TreeNode(number)
        return root


if __name__ == '__main__':
    a = [3, 9, 20, 15, 7]
    Solution().buildTree(a)
