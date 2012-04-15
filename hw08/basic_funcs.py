#!/usr/bin/env python
import sys

# Make a greeter
def greeter(name):
    name = str(name)
    print_name = name.lower()
    print "hello, "+print_name


# Draw a box
def box(w,h):
    wholder = w
    h2 = h
    if not isinstance(h,int) or not isinstance(w,int) or w < 1 or h < 1:
        print "Error: Invalid Dimensions"
    else:
        while h > 0:
            if h == 1 or h == h2:
                sys.stdout.write('+')
                w -= 1
                h -= 1
                while w > 1:
                    sys.stdout.write('-')
                    w -= 1
                if h > 1 or w > 0:
                    sys.stdout.write('+')
                    print
                elif h == 1:
                    print
                    sys.stdout.write('+')
                    return
                w = wholder
                while h > 1:    
                    sys.stdout.write('|')
                    w -= 1
                    while w > 1:
                        sys.stdout.write(' ')
                        w -= 1
                    sys.stdout.write('|')
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

