#!/usr/bin/env python
from hwtools import *

print "Section 3:  Lists"
print "-----------------------------"

nums = input_nums()

# 1. "nums" is a list of numbers entered from the command line.  How many
#    numbers were entered?

total=str(len(nums))
print "You entered "+total+" numbers."

print "1.", __

# 2.  Append 3 and 5 to nums

nums.append(3)
nums.append(5)

print "2.", nums

# 3.  Remove the last element from nums

total=0
for x in nums:
    total+=1
total-=1
del nums[total]
print "3.", nums


# 4.  Set the 3rd element to 7

nums[2]=7
print "4.", nums


# 5. [ADVANCED] Grab a new list of numbers and add it to the existing one

# print "5.", nums


# 6. [ADVANCED] Make a copy of this new giant list and delete the 2nd 
#    through 4th values

# nums_copy = __
# print "6.", nums, nums_copy
