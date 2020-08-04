#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 9:37 下午
# @Author  : liujiatian
# @File    : 二叉树直径.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    '''
    给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

    示例 :
    给定二叉树

              1
             / \
            2   3
           / \
          4   5
    返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
       
    注意：两结点之间的路径长度是以它们之间边的数目表示。
    '''

    def __init__(self):
        self.result = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        '''
        解题思路：
        1.初始化最大直径为0
        2.遍历每个节点，计算该节点的直径
        3.如果该节点的直径大于最大直径，更新最大直径
        PPT：https://leetcode-cn.com/problems/diameter-of-binary-tree/solution/shi-pin-jie-shi-di-gui-dai-ma-de-yun-xing-guo-chen/
        :param root:
        :return:
        '''

        def height(root):
            if not root:
                return 0
            l = height(root.left)
            r = height(root.right)
            # 当前节点最大的直径，如果是叶子节点的话，直径为1
            self.result = max(l + r, self.result)
            return 1 + max(l, r)

        height(root)
        return self.result
