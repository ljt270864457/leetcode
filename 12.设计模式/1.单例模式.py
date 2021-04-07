#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 4:27 下午
# @Author  : liujiatian
# @File    : 1.单例模式.py


'''
单例模式将类的实例化限制为一个对象。 它是一种创建模式，只涉及创建方法和指定对象的一个类。
它提供了创建实例的全局访问点。
'''

class Singleton(object):
    def __new__(cls, name, age):
        if not hasattr(Singleton, '_instance'):
            # 调用父类的__new__函数
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def echo(self):
        print(self.name, self.age)


if __name__ == '__main__':
    s1 = Singleton('Tom', 18)
    s1.echo()
    print(id(s1))
    s2 = Singleton('Jerry', 16)
    s2.echo()
    print(id(s2))
