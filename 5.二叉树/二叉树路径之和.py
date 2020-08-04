#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 3:21 下午
# @Author  : liujiatian
# @File    : 二叉树路径之和.py


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        '''
        LeetCode112
        给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

        说明: 叶子节点是指没有子节点的节点。

        示例: 
        给定如下二叉树，以及目标和 sum = 22，

                      5
                     / \
                    4   8
                   /   / \
                  11  13  4
                 /  \      \
                7    2      1
        返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

        使用减法的方式去处理
        '''
        # 如果root节点什么都没有 直接判断为False
        if not root:
            return False
        # 如果是叶子节点，判断当前的sum是否等于叶子节点 递归终止条件
        if not root.left and not root.right:
            return sum == root.val
        # 递归公式
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
