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

print '\nUsing list:'
cast = ['Michael Scofield', 'Lincoln Burrows', 'Sara Tancredi']
print cast
print 'cast length is: ', len(cast)
print 'The leading role is: ', cast[0]
print 'The leading role\'s wife is: ', cast[2]
print 'appending cast'
cast.append('Alex Mahone')
print cast
print 'The last role is: ', cast[-1] , '(Accessed using cast[-1])'
print 'Inserting role T-Bag to the 4th place'
cast.insert(3, 'T-Bag')
print cast
print 'Popping Alex out'
cast.pop()
print cast
print 'Appending nonsense'
cast.append('LJ'); cast.append('Brad belick'); cast.append('Paul Kellerman') 
print cast
print 'Removing the third last role'
cast.pop(-3)
print cast 
print 'Replacing Kellerman with Sucre'
cast[-1] = 'Sucre'
print cast
print 'Form a Show list'
show = [1, 'Prison Break', True, 2, '24', True, 3, 'Lost', False, 4, 'Castle', True]
print show
print 'Form a media'
film = [1, 'Apollo 13', 2, 'Terminator', 3, 'Star Wars']
media = ['TV', show, 'Movie', film]
print 'The length of media is: ', len(media)
print media
print 'Trying to sort list'
l = ['Michael', 'Sara', 'Jack', 'Kim', 'terminator', '123']
print 'Initial list: ', l
l.sort()
print 'Sorted list: ', l

print '\nUsing tuple'
t = (1, 2, 3)
print t
# one element tuple
tt = (1, )
print tt

print '\nConditional Statement'
age = 5
if age >= 18:
    print 'Your age is', age
    print 'adult'
elif age >= 6:
    print 'Your age is', age
    print 'teenager'
else: 
    print 'Your age is', age
    print 'kid'

print '\nFor Loop'
print 'Roles in Prison Break:'
for name in cast:
    print name # , to make sure do not change line
print 'Calculating sum:'
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print sum
print 'Using range: '
print 'The first 10 positive integers are: '
print range(1, 11)
sum = 0
for x in range(101):
    sum = sum + x
print sum

print '\nWhile loop'
print 'Calculating the sum of all odd numbers from 0 to 100'
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum
print 'Testing \'break\''
i = 12
for k in range(3, 15):
    print k, ' ',
    if k >= 12:
        break;

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

