#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

