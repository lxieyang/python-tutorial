#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '\nUsing dict'
d = {'Michael': 100, 'Sara': 87, 'Tracy': 93}
print 'Sara\'s score:', d['Sara']
print 'Inserting {\'Jack Bauer\': 101} into dict'
d['Jack Bauer'] = 101
print d
print 'Is \'Terminator\' in dict?', 'Terminator' in d
print 'Is there any \'Terminator\' in d?', d.get('Terminator')
print 'Popping \'Sara\''
d.pop('Sara')
print d

print '\nUsing set:'
s = set([1, 2, 3])
print 'Initial set: ', s
print 'Building set using ([1, 2, 3, 2, 1, 4, 6, 4, 5, 7, 3, 7])'
ss = set([1, 2, 3, 2, 1, 4, 6, 4, 5, 7, 3, 7])
print 'The resulting set is: ', ss
print 'Adding 4: '
ss.add(4)
print ss
print 'Adding 8:'
ss.add(8)
print ss
print 'Removing 5:'
ss.remove(5)
print ss
print 'Comparing s1 and s2:'
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s3 = set([3, 4, 5])
print 's1 is ', s1
print 's2 is ', s2
print 's3 is ', s3
print 'INTERSECTION: s1 & s2 is ', s1 & s2
print 'INTERSECTION: s1 & s2 & s3', s1 & s2 & s3
print 'UNION: s2 | s3 is ', s2 | s3

