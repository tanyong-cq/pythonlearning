#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
mutiplication table
'''
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%dX%d=%-2d' % (j, i, i * j), end=('\n'if i == j else ' '))
