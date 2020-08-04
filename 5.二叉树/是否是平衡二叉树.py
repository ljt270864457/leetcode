#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 8:37 下午
# @Author  : liujiatian
# @File    : 是否是平衡二叉树.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    '''
    LeetCode 110
    给定一个二叉树，判断它是否是高度平衡的二叉树。

    本题中，一棵高度平衡二叉树定义为：

    一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

    示例 1:

    给定二叉树 [3,9,20,null,null,15,7]

        3
       / \
      9  20
        /  \
       15   7
    返回 true 。

    示例 2:

    给定二叉树 [1,2,2,3,3,null,null,4,4]

           1
          / \
         2   2
        / \
       3   3
      / \
     4   4
    返回 false 。
    '''

    def isBalanced(self, root: TreeNode) -> bool:
        '''
        1.解题思路：
        递归求解
        求解每个节点的左孩子和右孩子的深度
        f(left) and f(right) and abs(height(left)-height(right))<2
        终止条件，如果到叶子节点还是满足每个条件，那么返回True
        :param root:
        :return:
        '''
        if not root:
            return True

        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(
            self.get_depth(root.left) - self.get_depth(root.right)) < 2

    def get_depth(self, node: TreeNode) -> int:
        if not node:
            return 0
        return 1 + max(self.get_depth(node.left), self.get_depth(node.right))
