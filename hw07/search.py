#!/usr/bin/env python
"""
Binary Search
by Evan Ricketts
"""
from hwtools import input_nums


nums=input_nums()

#sort
n = len(nums)
for x in range(0, n):
    min=x
    for i in range(x+1, n):
        if nums[i]<nums[min]:
            min = i
    nums[x],nums[min]=nums[min],nums[x]


print "I have sorted your numbers"

x = int(raw_input("Which number should I find: "))

min = 0
max = len(nums)-1


while min<=max:
    middle = ((min + max) / 2)
    check = nums[middle]
    if check == x:
        break
    elif check < x:
        min = middle + 1
    elif check > x:
        max = middle - 1
    
        

if nums[middle]==x:
    print "Found", x, "at position", middle, "in list 'nums'"
else:
    print "Could not find", x
