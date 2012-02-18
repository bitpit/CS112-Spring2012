#!/usr/bin/env python
"""
Selection sort
by Evan Ricketts
"""

from hwtools import input_nums

nums = input_nums()

print "Before sort:"
print nums

n = len(nums)
for x in range(0, n):
    min=x
    for i in range(x+1, n):
        if nums[i]<nums[min]:
            min = i
    nums[x],nums[min]=nums[min],nums[x]

print "After sort:"
print nums
