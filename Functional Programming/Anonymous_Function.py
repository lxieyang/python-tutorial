#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '------------'
print 'Using Lambda'
print '------------'
L = range(1, 10)
print 'Original:', L
print 'Mapped using lambda:', map(lambda x: x * x, L)

print '\n-----------------------------'
print 'Assigning lambda to variables'
print '-----------------------------'
f = lambda x: x * x
print f(5)

print '\n----------------'
print 'Returning lambda'
print '----------------'
def build(x, y):
    return lambda: x * x + y * y
print build(1, 2)()

