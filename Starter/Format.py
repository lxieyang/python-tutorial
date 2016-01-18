#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = 100
if a >= 0:
    print a
else:
    print -a
    
print '\n'
print '\\\t\\'
print r'\\\t\\'
print '''lines
... line2
... line2'''
print '\n'
print 'T | F is ', True or False
print 'F & T is ', False and True
print '~T is ', not True

a = 'ABC'
b = a
a = 'XYZ'
print b

print '\n'
# myInt = int(raw_input('请输入: '))
myInt = 101010
if myInt > 0:
    print myInt, ' is bigger than 0'
else:
    print myInt, ' is smaller than 0'

print '\nUsing Unicode:'
print 'Hi, %s and %s' % ('Michael', '斯科菲尔德')
