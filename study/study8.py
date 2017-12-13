#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
dict
'''
d1 = {'a':1, 'b':2, 'c':3}
print(d1)
print(d1.keys())
print(d1.values())
print(str(d1))
print(len(d1))
print(d1['a'])
d1['a'] = 10
print(d1['a'])
del d1['a']
print(d1)
d1.clear()
print(d1)
print(d1.get('a'))
