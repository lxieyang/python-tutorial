#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '---------------------------'
print 'Assigning functions to var:'
print '---------------------------'
print 'Assigning abs to func:'
func = abs
print 'func(-15) is', func(-15)

print '\n-----------------'
print 'Pass in functions'
print '-----------------'
def add_length(x, y, f):    # higher order functions, functions that accept other functions as its own parameters
    return f(x) + f(y)
print 'Calling add_length(-12, 34, abs)...... Return value is', add_length(-12, 34, abs)
