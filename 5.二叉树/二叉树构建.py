#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 9:06 PM
# @Author  : liujiatian
# @File    : 二叉树构建.py

class Node(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree(object):
    def __init__(self):
        self.root = Node()

    def add(self, item):
        '''
        向树添加元素
        :param item:
        :return:
        '''
        new_node = Node(item)
        if not self.root.val:
            self.root = new_node
            return

        stack = [self.root]
        while stack:
            cur_node = stack.pop(0)
            if not cur_node.left:
                cur_node.left = new_node
                break
            elif not cur_node.right:
                cur_node.right = new_node
                break
            else:
                stack.append(cur_node.left)
                stack.append(cur_node.right)

    def recursion_front(self, root):
        '''
        递归前序遍历 根-左-右
        :param root:
        :return:
        '''
        if not root:
            return

        print(root.val)
        self.recursion_front(root.left)
        self.recursion_front(root.right)

    def front(self, root):
        '''
        前序遍历非递归
        :return:
        '''
        if not root.val:
            return

        # result = []
        # stack = [root]
        # while stack:
        #     cur_node = stack.pop(0)
        #     result.append(cur_node.val)
        #     if cur_node.left:
        #         stack.append(cur_node.left)
        #         break
        #     if cur_node.right:
        #         stack.append(cur_node.right)
        #         break
        # return result

    def recursion_middle(self, root):
        '''
        中序遍历 左-根-右
        :param root:
        :return:
        '''
        if not root:
            return []

        self.recursion_middle(root.left)
        print(root.val)
        self.recursion_middle(root.right)

    def middle(self, root):
        '''
        中序遍历非递归
        :return:
        '''
        pass

    def recursion_end(self, root):
        '''
        递归后续遍历 左-右-根
        :param root:
        :return:
        '''
        if not root:
            return

        self.recursion_end(root.left)
        self.recursion_end(root.right)
        print(root.val)

    def end(self, root):
        '''
        非递归
        :param root:
        :return:
        '''
        pass


if __name__ == '__main__':
    '''
          1
       2     3
     4  5  6   7
    '''
    t = Tree()
    for i in range(1, 8):
        t.add(i)

    # 递归实现
    t.recursion_front(t.root)
    # t.recursion_middle(t.root)
    # t.recursion_end(t.root)

    # 非递归实现
    print(t.front(t.root))
    # print(t.middle(t.root))
