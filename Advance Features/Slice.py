#!/usr/bin/env python
# -*- coding: utf-8 -*-
L = ['michael', 'sara', 'jack', 'kim', 'kate', 'steve']
print 'Original: ', L
print L[0:3]    # slicing
print L[:3]     # omit 0
print L[-2:]
LL = range(16)
print 'Original: ', LL
print LL[:10:2] # step size = 2
print LL[::5]
print LL[:]     # original list
T = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print 'Original: ', T
print T[:3]     # result is still a tuple
string = 'Jack Bauer is a hero!'
print 'Original: ', string
print string[:4]    # string can also be sliced 
print string[::2]   # string can also be sliced
