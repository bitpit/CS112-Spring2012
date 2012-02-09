#!/usr/bin/env python

titles = ['Hitchikers Guide to the Galaxy',
          'Restaurant at the End of the Galaxy',
          'Life, the Universe, and Everything']

titles.append('So Long, and Thanks for All the Fish') #adds dat shit to the end

#cept the titles are difficult to read!

#for loops! they are lessy sucky in python
for title in titles[0:2]:
    print title     #in java this would be a for each loop
for i in range(1,11):#range command with single number starts at zero and counts
                     #up to number given by ones:can specify both as seen above
                     #also can count by multiples by specifying third variable
    print i

numbers = range(100)
decimals = numbers[:]
for i,n in enumerate(numbers):
    numbers[i] = n*.2
print numbers
