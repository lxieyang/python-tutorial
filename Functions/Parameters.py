#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
