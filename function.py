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

print '\nDefault parameter:'
def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print '5^2 is: ', power(5)
print '5^18 is: ', power(5, 18)

print '\nOne special case of default parameter:'
def append_end(L = []):
    L.append('END')
    return L
print '1st time called: ', append_end()
print '2nd time called: ', append_end()
print '3rd time aclled: ', append_end()
print 'Fixing the issue: '
def append_end_2(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
print '1st time called: ', append_end_2()
print '2nd time called: ', append_end_2()
print '3rd time aclled: ', append_end_2()

print '\nMutable parameter 可变参数'
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print 'Calling calc(1, 2, 3, 4): ', calc(1, 2, 3, 4)
print 'Calling calc(): ', calc()
nums = [1, 2, 3, 4]
print 'Calling calc(*nums): ', calc(*nums)

print '\nUsing keyword parameter 关键字参数'
def person(name, age, **kw):    # pay attention to **kw
    print 'name:', name, 'age:', age, 'other:', kw 
kw = {'city': 'NYC', 'job': 'Police'}
print "Calling person: "
person('Glen', 35, city = 'Detroit')
person('Beckett', 36, **kw)     # pay attention to **kw

print '\nCombination of parameters 参数组合'
print 'Order: 必选参数，默认参数，可变参数，关键字参数'
def func(a, b, c = 0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
print 'func(1, 2): '
func(1, 2)
print 'func(1, 2, 3)'
func(1, 2, 3)
print 'func(1, 2, 3, \'Terminator\')'
func(1, 2, 3, 'Terminator')
print 'func(1, 2, 3, \'Terminator\', \'Jack Bauer\')'
func(1, 2, 3, 'Terminator', 'Jack Bauer')   # args is interpreted as a tuple
print 'func(1, 2, 3, \'Terminator\', \'Jack Bauer\', city = \'Ann Arbor\', age = 99)'
func(1, 2, 3, 'Terminator', 'Jack Bauer', city = 'Ann Arbor', age = 99)
hello = (10, 11, 12, 13)
kww = {'x': 123}
print 'func(*hello, **kww)'
func(*hello, **kww)

print '\nRecursive function call'
print 'Factorial:'
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print '20! is', fact(20)
# fact(1000) will cause stack overflow
print 'Factorial (TAIL RECURSIVE): '
def fact_tail(num, product):
    if num is 1:    # 'is' = '=='
        return product
    else:
        return fact_tail(num - 1, num * product)
def fact_new(n):
    return fact_tail(n, 1)
print '20! is', fact_new(20) 
# fact_new(1000) will, unfortunately, still cause stack overflow