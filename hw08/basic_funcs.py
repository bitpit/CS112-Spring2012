#!/usr/bin/env python

# Make a greeter
def greeter(name):
    name = str(name)
    print_name = name.lower()
    return "hello, %s" %print_name


# Draw a box
def box(w,h):
    wholder = w
    h2 = h
    if w < 1 or h < 1:
        print "Error: Invalid Dimensions"
    while h > 0:
        if h == 1 or h == h2:
            print "+",
            w -= 1
            h -= 1
            while w > 1:
                print "-",
                w -= 1
            if h > 0 or w > 0:
                print "+",
                print
        w = wholder
        while h > 1:    
            print "|",
            w -= 1
            while w > 1:
                print " ",
                w -= 1
            print "|",
            h -= 1
            print
            w = wholder

# ADVANCED
# Draw a Festive Tree
#    draw a festive tree based on the specifications.  You will need to discover the arguments 
#    and behavior by running the unittests to see where it fails.  Return a string, do not print.
#
#  ex:
#    >>> print tree()
#        *
#        ^
#       ^-^
#      ^-^-^
#     ^-^-^-^
#    ^-^-^-^-^
#       | |
#       | |

# def tree()

