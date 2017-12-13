#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
class
'''
class C1(object):
    '''
    class c1
    '''
    def __init__(self):
        self.__x = 2
        self.__y = 3
        print('init')
    def __del__(self):
        print('del')
    def __repr__(self):
        return 'this is repr'
    def test1(self, arg1, arg2):
        '''
        test
        '''
        arg1, arg2 = arg2, arg1
        return arg1*self.__x+arg2*self.__y

c = C1()
print(c)
print(c.test1(1, 2))
del c

class C2(C1):
    '''
    class C2
    '''
    def __repr__(self):
        return 'this is c2 repr'
    def test2(self, arg1, arg2):
        '''
        test2
        '''
        return self.test1(arg2, arg1)

c = C2()
print(c)
print(c.test1(1, 2))
print(c.test2(1, 2))
del c
