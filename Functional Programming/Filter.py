#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '--------'
print 'keep odd'
print '--------'
def is_odd(x):
    return x % 2 != 0
L = range(1, 11)
print 'Original:', L
print 'Filtered:', filter(is_odd, L)

print '---------------------'
print 'Removing empty string'
print '---------------------'
def not_empty(s):
    return s and s.strip()
LLL = ['A', '', 'B', None, 'C', '  ']
print 'Removing empty str', filter(not_empty, LLL)
