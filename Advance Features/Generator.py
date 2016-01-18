#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '\n------------------------------'
print 'Generate \'list\' with generator'
print '------------------------------'
L = [x * x for x in range(10)]
print 'List:', L
g = (x * x for x in range(10))
print 'Generated List:',
for n in g:
    print n,

print '\n\n------------------'
print 'Fibonacci Sequence'
print '------------------'
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b,
        a, b = b, a + b
        n = n + 1

print '\nCalling fib(10）'
fib(10)
def fib_new(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b     # generator
        a, b = b, a + b
        n = n + 1
print '\nCalling fib_new(10)'
for n in fib_new(10):
    print n,
print '\nUsing next()'
func = fib_new(6)
print func.next()
print func.next()
print func.next()
print func.next()
print func.next()
print func.next()
