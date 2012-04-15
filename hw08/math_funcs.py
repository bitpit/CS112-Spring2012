#!/usr/bin/env python

import math

# Distance formula
def distance((a, b), (x,y)):
    d1 = math.fabs(b-y)
    d2 = math.fabs(a-x)
    distance = math.sqrt((d1*d1)+(d2*d2))
    return distance


# ADVANCED
# Normalizing Vectors
#   normalize a vector of length N.  If given all zeros, just spit back the same vector
#   http://www.fundza.com/vectors/normalize/index.html

#   ex:
#     >>> normalize((1,1))
#     [0.70710678118654746, 0.70710678118654746]
#     >>> normalize([0,0,0])
#     [0,0,0]
#     >>> normalize([1,1,1,1])
#     [0.25, 0.25, 0.25, 0.25]

# def normalize(vec):
