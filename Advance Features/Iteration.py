#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '------------------'
print 'Iteration of dict'
print '------------------'
d = {'Michael': 100, 'Sara': 98, 'Jack': 101, 'Kim': 59}
print 'Original dict:', d
print 'Iterate through keys: '
for key in d:
    print key
print 'Iterate through values: '
for value in d.itervalues():
    print value
print 'Iterate through keys & values: '
for k, v in d.iteritems():
    print k, v

print '\n-------------------'
print 'Iteration of string'
print '-------------------'
for ch in 'Michael Scofield':
    print ch

print '\n-----------------'
print 'Judge if iterable'
print '-----------------'
from collections import Iterable
print 'Is string \'abc\' iterable?', isinstance('abc', Iterable)
print 'Is list \'[1, 2, 3]\' interable?', isinstance([1, 2, 3], Iterable)
print 'Is int 123 iterable?', isinstance(123, Iterable)

print '\n---------------------'
print 'Iterate through index'
print '---------------------'
ll = ['J', 'A', 'C', 'K']
for i, value in enumerate(ll):      # enumerate()
    print 'Index:', i, 'Value:', value

print '\n-------------'
print 'Element pairs'
print '-------------'
for x, y, z in [(1,2,3), (4,5,6), (7,8,9), (10,11,12)]:
    print x, y, z
for x, y in enumerate([(1,2,3), (4,5,6), (7,8,9), (10,11,12)]):
    print 'Index:', x, 'Values:', '\t',y[0], '\t', y[1], '\t', y[2]
