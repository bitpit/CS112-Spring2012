#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?

total=0
for x in nums:
    total+=x
print "1.", str(total)


# 2. Print every even number in nums
evens=[]
for x in nums:
    if (x%2==0):
        evens.append(x)
print "2. The even numbers you entered are "+str(evens)
#print "2. even numbers"

#CODE GOES HERE


# 3. Does nums only contain even numbers? 
only_even = False
for x in nums:
    if (x%2!=0):
        only_even = True

print "3.",      #this bit is part of the fun!
if only_even:    #shoulda forced us 2 do it
    print "only even"
else:
    print "some odd"


# 4. Generate a list every odd number less than 100. Hint: use range()
numeros=range(100)
total=[]
for x in numeros:
    if (x%2!=0):
        total.append(x) 
print "4.", total

