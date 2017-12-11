#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
list
'''
l = [1, 2, 3, 'a', 'b', 'c']
print(l)
l.append('A')
print(l)
l.pop()
print(l)
print(l[1])
print(l[1:3])
print(l[1:-2])
print(len(l))
for i in l:
    print(i)
l.insert(3, 'A')
print(l)
print(l+['A', 'B', 'C'])
print(l*2)
print(1 in l)
print(max(['a', 'c', 'b']))
print(min(['a', 'c', 'b']))
l.reverse()
print(l)
l = ['a', 'c', 'b']
l.sort()
print(l)
