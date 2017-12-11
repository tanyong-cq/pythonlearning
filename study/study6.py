#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
number
'''
import math, random

print(1+2)
print(2-1)
print(2*3)
print(3/2)
print(2/3)
print(5//3)
print(5%3)
print(2**10)
print((1+2j)+(2+4j))
print(1 == 2)
print(1 != 2)
print(1 < 2)
print(1 > 2)
print(1 >= 2)
print(1 <= 2)
a = 60
b = 13
print('a={:08b}'.format(a))
print('b={:08b}'.format(b))
print('c={:08b}'.format(a&b))
print('c={:08b}'.format(a|b))
print('c={:08b}'.format(a^b))
print('c={:08b}'.format(~a))
print('c={:08b}'.format(b<<2))
print('c={:08b}'.format(b>>2))
print(int(1.1))
print(float(1))
print(abs(-10.2))
print(round(10.55, 1))
print()
print(math.ceil(5.1))
print(math.exp(10))
print(math.log(10))
print(math.modf(10.2))
print(math.sqrt(10))
print()
print(math.sin(30))
print(math.cos(30))
print(math.radians(30))
print()
print(random.random())
print(random.randrange(100))
l = [1, 2, 3, 4]
print(random.choice(l))
random.shuffle(l)
print(l)
print(random.uniform(1, 100))
