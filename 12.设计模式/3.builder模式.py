#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 5:23 下午
# @Author  : liujiatian
# @File    : 3.builder模式.py

import abc

'''
我们想要创建一个有多个部分构成的对象， 而且它的构成需要一步步地完成，只有各个部分都创建好了，这个对象才算完成，因此就诞生了建造者模式。建造者模式将一个复杂的构造过程与其表现分离，这样， 同一个构建过程（使用同一个指挥者）可用于创建多个不同的表现。

建造者模式一般包括：一个指挥者（director）, 多个建造者（builder），比如你去Kfc点餐，你要了个鳕鱼堡，你同事要了个鸡腿堡。你们的订单都是从同一个waiter下的单，waiter把订单交给了后台的工作者（建造者）,经过加工后返回了一个构造好的汉堡。下面举例炒菜的过程，一共炒了两个菜，具体如下代码：
'''


class Dish(object):
    def __init__(self):
        self.meat = None  # 肉
        self.vegetables = None  # 菜
        self.seasoning = None  # 调料

    def __str__(self):
        return f'dish include {self.meat}_{self.vegetables}_{self.seasoning}'


class AbstractBuilder(object, metaclass=abc.ABCMeta):
    dish = Dish()

    @abc.abstractmethod
    def add_meat(self):
        pass

    @abc.abstractmethod
    def add_vegetables(self):
        pass

    @abc.abstractmethod
    def add_seasoning(self):
        pass


class CeleryPorkBuilder(AbstractBuilder):
    # 芹菜炒肉
    def add_meat(self):
        self.dish.meat = '猪肉'

    def add_vegetables(self):
        self.dish.vegetables = '芹菜'

    def add_seasoning(self):
        self.dish.seasoning = '盐'


class RadishBeefBuilder(AbstractBuilder):
    # 萝卜牛肉
    def add_meat(self):
        self.dish.meat = '牛肉'

    def add_vegetables(self):
        self.dish.vegetables = '萝卜'

    def add_seasoning(self):
        self.dish.seasoning = '胡椒'


class Director(object):
    '''
    director 相当于是服务员，他负责串联食客和后厨，将不同的需求转发给不同的builder进行加工
    '''

    def build(self, builder):
        builder.add_meat()
        builder.add_vegetables()
        builder.add_seasoning()
        print(builder.dish)


if __name__ == '__main__':
    celery_pork_builder = CeleryPorkBuilder()
    radish_beef_builder = RadishBeefBuilder()
    director = Director()
    director.build(celery_pork_builder)
    director.build(radish_beef_builder)
