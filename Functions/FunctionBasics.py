#!/usr/bin/env python
# -*- coding: utf-8 -*-
print 'Using abs()'
print 'The absolute value of -12112 is ', abs(-12112)

print '\ncmp(1, 2)', cmp(1, 2)
print 'cmp(2, 2)', cmp(2, 2)
print 'cmp(4, 2)', cmp(4, 2)

print '\nConversion: '
print '12.345 -> int: ', int(12.345)

print 'Alias'
print 'Setting theAbsoluteValueFunction as an alias of abs()'
theAbsoluteValueFunction = abs
print 'The abs of -12312 is ', theAbsoluteValueFunction(-12312)
