#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
