#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
function
'''
def area(width, height=10):
    '''
    area
    '''
    print('width=%s, height=%s' % (width, height))
    return width*height

print(area(10, 20))
print(area(height=10, width=20))
print(area(10))

def sum(a, b, *c):
    '''
    sum
    '''
    d = a+b
    for i in c:
        d = d+i
    return d

print(sum(1, 2))
print(sum(1, 2, 3, 4, 5))

sum1 = lambda a, b: a+b
print(sum1(1, 2))

print(__name__)
