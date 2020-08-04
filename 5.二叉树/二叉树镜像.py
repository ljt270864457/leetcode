#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 2:34 下午
# @Author  : liujiatian
# @File    : 二叉树镜像.py

'''
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        '''
        解题思路：
        1. 依次递归处理root节点的左节点和右节点
        2. 每个root节点的左右节点进行交换
        :param root:
        :return:
        '''
        if not root:
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root
