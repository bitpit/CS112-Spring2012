#!/usr/bin/env python
import math

class Shape(object):
    def __init__(self):
        pass
    def area(self):
        pass
    def perimeter(self):
        pass
            

class Rect(Shape):
    def __init__(self, w, h):
        Shape.__init__(self)
        self.width = w
        self.height = h
    def area(self):
        orea = self.width*self.height
        return orea
    def perimeter(self):
        perimeter = (self.width*2) + (self.height*2)
        return perimeter
    def __str__ (self):
        pw = str(self.width)
        ph = str(self.height)
        return "A rectangle with a height of "+pw+" and a width of "+ph+"."


class Square(Rect):
    def __init__(self, w):
        Rect.__init__(self, w, h=w)
    def __str__(self):
        ps = str(self.width)
        return "A square with 4 sides measuring "+ps+" units in length."


class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        orea = math.pi*(self.r*self.r)
        return orea
    def perimeter(self): # should be circumference
        perm = math.pi*(self.r*2) 
        return perm
    def __str__(self):
        ps = str(self.r)
        return "A circle with a radius of "+ps+"."
        
        
