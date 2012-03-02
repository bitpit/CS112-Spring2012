#!/usr/bin/env python
"""
rects.py

Pygame Rectangles
=========================================================
The following section will test your knowledge of how to 
use pygame Rect, arguably pygame's best feature. Define
the following functions and test to make sure they 
work with `python run_tests.py`

Make sure to use the documentation 
http://www.pygame.org/docs/ref/rect.html


Terms:
---------------------------------------------------------
  Point:     an x,y value
               ex:  pt = 3,4

  Polygon:   a shape defined by a list of points
               ex:  poly = [ (1,2), (4,8), (0,3) ]

  Rectangle:  pygame.Rect
"""

from pygame import Rect
import math


def poly_in_rect(poly, rect):
    count = 0
    for i in range(len(poly)):
        x,y = poly[i]
        if rect.collidepoint(x,y):
            count += 1
    if count == len(poly):
        return True
    else:
        return False


def surround_poly(poly):
    #make x & y list
    xes = []
    yes = []
    for x in range (0,len(poly)):
        xes.append(poly[x][0])
        yes.append(poly[x][1])
    #sort em
    for x in range(0, len(xes)):
        min=x
        for i in range(x+1, len(xes)):
            if xes[i]<xes[min]:
                min = i
        xes[x],xes[min]=xes[min],xes[x]
    for x in range(0, len(yes)):
        min=x
        for i in range(x+1, len(yes)):
            if yes[i]<yes[min]:
                min = i
        yes[x],yes[min]=yes[min],yes[x]
    #return a rect based on the sorted lists
    w = math.fabs(xes[0]) + xes[len(xes)-1] - 1
    h = math.fabs(yes[0]) + yes[len(yes)-1] + 1
    return Rect((xes[0],yes[0]), (w,h))




