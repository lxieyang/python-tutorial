#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '---------'
print 'Using map'
print '---------'
def f(x):
    return x * x
L = range(1, 11)
print 'Original:', L
print 'Mapped:', map(f, L)
print 'Convert to string using map:', map(str, L)
def char2num(ch):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[ch]
print 'Converting \'12345\' to int list', map(char2num, '12345')

print '\n------------'
print 'Using reduce'
print '------------'
def add(x, y):
    return x + y
LL = range(1, 11)
print 'Original:', LL
print 'Using reduce to calculate sum:', reduce(add, L)
LLL = range(1,10,2)
def toInt(x, y):
    return x * 10 + y
print 'Original:', LLL
print 'Using reduce to convert into a integer:', reduce(toInt, LLL)

print '\n----------'
print 'Str to Int'
print '----------'
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(ch):
        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[ch]
    return reduce(fn, map(char2num, s))
print 'Converting \'12345\' to a number:', str2int('12345')
print 'Using lambda function:'
def char2num(ch):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[ch]
def str2int_new(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print 'Converting \'12345\' to a number:', str2int_new('12345')
