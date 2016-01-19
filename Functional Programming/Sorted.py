#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '------------'
print 'Using sorted'
print '------------'
L = [36, 5, 12, 9, 21]
print 'Original:', L
print 'Sorted:', sorted(L)

print '\n------------'
print 'Reverse sort'
print '------------'
def reverse_cmp(x, y):
    if x > y:
        return -1
    elif x == y:
        return 0
    else:
        return 1
LL = [36, 5, 12, 9, 21]
print 'Original:', LL
print 'Sorted:', sorted(LL, reverse_cmp)

print '\n----------------------------'
print 'Sort characters without case'
print '----------------------------'
def cmp_ignore_case(ch1, ch2):
    u1 = ch1.upper()
    u2 = ch2.upper()
    if u1 < u2:
        return -1
    elif u1 == u2:
        return 0
    else:
        return 1
LLL = ['Jack', 'Zoo', 'ZOo', 'ariB', 'aRiC', 'hias']
print 'Original:', LLL
print 'Sorted:', sorted(LLL, cmp_ignore_case)
