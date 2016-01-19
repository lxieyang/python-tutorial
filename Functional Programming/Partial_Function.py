#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '-----------------------'
print 'Using partial functions'
print '-----------------------'
s = '101100101'
print 'Base = 10:', int(s)
print 'Base = 8:', int(s, base=8)
print 'Base = 2:', int(s, base=2)
print 'Defining partial function'
import functools
int2 = functools.partial(int, base=2)
print 'Using partial functions'
print 'Base = 2:', int2(s)
print 'Base = 10:', int2(s, base=10)

print '\n-------------------------'
print 'One special (faulty case)'
print '-------------------------'
# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
# 当传入：
# int2 = functools.partial(int, base=2)
# 实际上固定了int()函数的关键字参数base，也就是：
# int2('10010')
# 相当于：
# kw = { base: 2 }
# int('10010', **kw)
max2 = functools.partial(max, 10)
print max2(5, 6, 7)
# 相当于：
# args = (10, 5, 6, 7)
# max(*args)


