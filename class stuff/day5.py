#!/usr/bin/env python

'''
what is a list?
a list is a mutable array -> storing lots of pieces of data that are related in
     some way
you cant change the length of arrays, but you can change the length of lists
     hence the immutability of a list as compared to an array
first element in the list is a 0

'''

#names = ['bob' , 'fred']
#print names[0]   #first element on the list starts at ZERO
#print names[1]
#print len(names)#counts and displays the length of the list; number of elements

letters = ['a','d','f']
letters += ['b','c']  #inserts the list into 1:1 (first and last place we
                      #want to insert) into list 'letters'
print letters     #-1 selects last thing on the list, -2 is the second last
letters2 = letters[:]
letters[0] = 'huh'
print letters2

