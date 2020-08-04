#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 3:59 PM
# @Author  : liujiatian
# @File    : 1.循环队列.py

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = [-1] * k
        self.size = k
        self.head = -1
        self.tail = -1

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            print('queue is full')
            return False

        if self.isEmpty():
            self.head = 0

        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            print('queue is empty')
            self.head = self.tail = -1
            return False
        else:
            self.queue[self.head] = -1
            self.head = (self.head + 1) % self.size
            return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1

        return self.queue[self.head % self.size]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1

        return self.queue[self.tail]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """

        return True if self.head == self.tail else False

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return True if (self.tail + 1) % self.size == self.head else False

    def getSize(self):
        '''
        get queue size
        :return:
        '''
        if self.isEmpty():
            return 0
        if self.isFull():
            return self.size
        return (self.tail - self.head + 1 + self.size) % self.size

    def __getitem__(self, key):
        if abs(key) >= self.size or not isinstance(key, int):
            raise KeyError('key index error')
        return self.queue[(self.head + key) % self.size]

if __name__ == '__main__':
    obj = MyCircularQueue(15)
    for i in range(10):
        obj.enQueue(i)
    print(obj.queue)
    print(obj.getSize())

    for i in range(5):
        obj.deQueue()
    print(obj.queue)
    print(obj.getSize())

    for i in range(10, 16):
        obj.enQueue(i)

    print(obj.queue)
    print(obj.Front())
    print(obj.Rear())
    print(obj.getSize())
    print(obj[3])
