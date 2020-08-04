#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 10:20 PM
# @Author  : liujiatian
# @File    : 1.单项链表.py

class Node(object):
    def __init__(self, val: int, next_node=None):
        self.val = val
        self.next_node = next_node


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._head = None
        self._length = 0

    def __len__(self):
        return self._length

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        cur_node = self._head
        for _ in range(index):
            if not cur_node or not cur_node.next_node:
                return -1
            cur_node = cur_node.next_node
        return cur_node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val, self._head)
        self._head = node
        self._length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        cur_node = self._head
        if not cur_node:
            self.addAtHead(val)
        else:
            while True:
                if not cur_node.next_node:
                    node = Node(val)
                    cur_node.next_node = node
                    self._length += 1
                    break

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self._length:
            return

        last_node = None
        cur_node = self._head
        for _ in range(index):
            last_node = cur_node
            cur_node = cur_node.next_node
        new_node = Node(val, next_node=cur_node)
        last_node.next_node = new_node
        self._length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index > self._length:
            return

        last_node = None
        cur_node = self._head
        for _ in range(index):
            last_node = cur_node
            cur_node = cur_node.next_node
        next_node = cur_node.next_node
        last_node.next_node = next_node
        self._length -= 1

    def get_items(self):
        result = []
        cur_node = self._head
        while True:
            result.append(cur_node.val)
            if not cur_node.next_node:
                break
            cur_node = cur_node.next_node
        return result


if __name__ == '__main__':
    ll = MyLinkedList()
    ll.addAtHead(1)  # 1
    ll.addAtTail(3)  # 1 3
    print(ll.get_items())
    ll.addAtIndex(1, 2)
    print(ll.get_items())
    ll.deleteAtIndex(2)
    print(ll.get_items())
