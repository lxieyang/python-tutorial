#!/usr/bin/env python
# -*- coding: utf-8 -*-

def now():
    print '2016-01-18'
print now.__name__
f = now
f()
print f.__name__

print '\n------------'
print 'Decorate 1st'
print '------------'
def log(func):
    def wrapper(*args, **kw):
        print 'Calling %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
@log
def now():
    print '2016-01-18'
now()
print 'now()\'s name is', now.__name__

print '\n------------'
print 'Decorate 2nd'
print '------------'
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
@log('Executing the function')
def now():
    print '2016-01-18'
now()
print 'now()\'s name is', now.__name__

print '\n------------'
print 'Decorate 3rd'
print '------------'
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
@log
def now():
    print '2016-01-18'
now()
print 'now()\'s name is', now.__name__

print '\n------------'
print 'Decorate 4th'
print '------------'
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
@log('Executing the function')
def now():
    print '2016-01-18'
now()
print 'now()\'s name is', now.__name__

