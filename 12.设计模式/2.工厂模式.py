#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 5:09 下午
# @Author  : liujiatian
# @File    : 2.工厂模式.py

'''
工厂模式属于创建模式列表类别。它提供了创建对象的最佳方法。 在工厂模式中，创建对象时不会将逻辑公开给客户端，并使用通用接口引用新创建的对象。
工厂模式使用工厂方法在Python中实现。 当用户调用一个方法时，传入一个字符串，并通过工厂方法实现创建一个新对象，并将此对象作为返回值。 工厂方法中使用的对象类型由通过方法传递的字符串确定。
在下面的例子中，每个方法都包含对象作为参数，这是通过工厂方法实现的。
'''


class Resource(object):
    def get_content(self):
        print('this is content')


class Image(Resource):
    def get_content(self):
        print('this is image content')


class Video(Resource):
    def get_content(self):
        print('this is video content')


class Text(Resource):
    def get_content(self):
        print('this is text content')


def resource_factory(resource_type: str):
    if resource_type.capitalize() in globals().keys():
        instance = globals()[resource_type.capitalize()]()
    else:
        instance = Resource()
    instance.get_content()


if __name__ == '__main__':
    resource_factory('image')
    resource_factory('video')
    resource_factory('text')
    resource_factory('unk')
