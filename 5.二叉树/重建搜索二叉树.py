#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def reconstructRec(arr, cur_index, end_index):
    '''
    构建左子树和右子树
    '''
    if cur_index == -1 or cur_index > end_index:
        return
    root = TreeNode(arr[cur_index])
    left = find_left(arr, cur_index)
    right = find_right(arr, cur_index)
    # 从left_index到第一个大于该元素的区间都是左子树
    root.left = reconstructRec(arr, left, right - 1)
    # 第一个大于该元素以及其右侧的所有元素都在右子树
    root.right = reconstructRec(arr, right, end_index)
    return root


def find_left(arr, cur_index):
    '''
    判断后续元素是否大于当前元素，返回后一个元素的index
    '''
    if cur_index + 1 < len(arr) and arr[cur_index] > arr[cur_index + 1]:
        return cur_index + 1
    else:
        return -1


def find_right(arr, cur_index):
    '''
    找到第一个比当前元素大的元素索引
    '''
    if cur_index + 1 == len(arr):
        return -1

    for i in range(cur_index + 1, len(arr)):
        if arr[i] > arr[cur_index]:
            return i
    return -1


def preOrder(root: TreeNode):
    '''
    前序遍历
    '''
    if not root:
        return []
    return [root.val] + preOrder(root.left) + preOrder(root.right)


if __name__ == '__main__':
    '''
    题目描述：根据二叉搜索树的前序遍历结果，重建搜索二叉树
         5
        / \
       4   6
       /
       2
        \
         3
    
    解题思路：
    1. 前序遍历的根节点是数组中第0个元素
    2. 找到左节点索引：如果下一个元素小于当前节点，那么下一个节点就是左节点，否则左节点为None
    3. 找到右节点索引：当前节点右侧第一个大于该节点元素所在的索引，如果没有比起大的话，右节点为None
    4. 递归：左子树索引范围[start_index,right_index-1]，右子树索引范围[right_index,end_index],递归终止条件为左子树为空或右子树为空
    '''
    arr = [5, 4, 2, 3, 6]
    root = reconstructRec(arr, 0, len(arr) - 1)
    assert preOrder(root) == arr
