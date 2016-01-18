#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '\nDefining a function'
print 'Defining my own abs() as theAbs'
def theAbs(x):
    if x >= 0:
        return x
    else:
        return -x
print 'The absolute value of -23 is ', theAbs(-23)

print '\nUsing \'pass\''
def noop():
    pass
print 'Calling noop(): ', noop()
print '\nInstance check:'
def newAbs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print 'Calling newAbs(): '
print 'The abs of -123.123 is: ', newAbs(-123.123)

print '\nReturning multiple values'
import math
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
print 'Calling move(100, 100, 60, math.pi / 6):'
first, second = move(100, 100, 60, math.pi / 6)
print first, second
print 'Calling move(5, 5, 3, math.pi / 2):'
retVal = move(5, 5, 3, math.pi / 2)
print retVal
