#!/usr/bin/env python
from hwtools import *

print "Section 2:  Loops"
print "-----------------------------"

# 1. Keep getting a number from the input (num) until it is a multiple of 3.
num = int(raw_input("Please enter a multiple of 3: "))     
 
while (num%3!=0):
    print "That's not a multiple of 3! Try again!"
    num = int(raw_input("Please enter a multiple of 3: "))
    


#print "1.", num

while (num!=0):
    print num
    num = num-3
print "0"
#print "we have liftoff"

#print "2. Countdown from", num


# 3. [ADVANCED] Get another num.  If num is a multiple of 3, countdown 
#    by threes.  If it is not a multiple of 3 but is even, countdown by 
#    twos.  Otherwise, just countdown by ones.

# num = int(raw_input("3. Countdown from: "))

