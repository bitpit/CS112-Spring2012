#!/usr/bin/env python

n = 0
while n == 0:
    n = int(raw_input("Enter a number greater than 0:  "))
    if n == 0:
        print "That's zero! Try again."
        
print "20 /", n, "is", 20/(float (n))
