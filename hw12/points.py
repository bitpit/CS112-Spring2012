#!/usr/bin/env python
import math


class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def move (self, x, y):
        self.x = x
        self.y = y
    
    def translate (self, nx, ny):
        self.x += nx
        self.y += ny
    
    def distance (self, other):
        d1 = math.fabs(self.x-other.x)
        d2 = math.fabs(self.y-other.y)
        distance = math.sqrt((d1*d1)+(d2*d2))
        return distance
    
    def __str__ (self):
        self.px = str(self.x)
        self.py = str(self.y)
        return "("+self.px+","+self.py+")"
    
    def __eq__ (self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


