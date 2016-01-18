#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '\n-------------'
print 'Building list'
print '-------------'
L = [a * a for a in range(1, 11)]
print 'Using list comprehension to create list: ', L
LL = [a * a for a in range(1, 11) if a % 2 == 0]
print 'Condition: a is even: ', LL
LLL = [m + n for m in 'ABC' for n in 'XYZ']     # permutation
print 'Double loop to permutate: ', LLL

print '\n---------------------'
print 'List files in folders'
print '---------------------'
import os
print [d for d in os.listdir('..')]

print '\n----------------'
print 'Double variables'
print '----------------'
d = {'Michael': 100, 'Sara': 98, 'Jack': 101, 'Kim': 59}
print [key + ' = ' + str(value) for key, value in d.iteritems()]

print '\n---------------------'
print 'Convert to lower case'
print '---------------------'
l = ['HelLo', 'WoRlD', 'IS', 'THe', 'firST', 'ProGrAM', 'that', 'U', 'WriTE']
print 'Original:', l
print 'To lower:', [s.lower() for s in l]
ll = ['HelLo', 'WoRlD', 18, 'heihei', 'Taylor']
print 'Original:', ll
print 'To lower:', [s.lower() for s in ll if isinstance(s, str)]    # isinstance
