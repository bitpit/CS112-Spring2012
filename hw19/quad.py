#!/usr/bin/env python
from math import ceil, floor

import pygame
from pygame.locals import *

from pygame import Rect

MAX_DEPTH = 10
class QuadTreeNode(object):

    def __init__(self, rect, depth = 0):
        self.rect = rect
        self.data = None
        self.is_split = False

        self.ne = None
        self.nw = None
        self.se = None
        self.sw = None
        self.rects = []
        self.depth = depth

    def add_point(self, point):
        # if we don't have data, just add it
        if self.data is None and not self.is_split:
            self.data = point
            return
        elif self.depth == MAX_DEPTH:
            self.data = point
            return

        # if already haven't split, do that now
        if not self.is_split:
            prev_point = self.data
            self.is_split = True

            r = self.rect
            w = self.rect.width / 2.0
            h = self.rect.height / 2.0
            d = self.depth + 1

            self.nw = QuadTreeNode( Rect(r.left, r.top, floor(w), floor(h) ), d )
            self.ne = QuadTreeNode( Rect(r.centerx, r.top, ceil(w), floor(h) ), d ) 
            self.sw = QuadTreeNode( Rect(r.left, r.centery, floor(w), ceil(h) ), d )
            self.se = QuadTreeNode( Rect(r.centerx, r.centery, ceil(w), ceil(h) ), d )

            # re add the point
            self.add_point(prev_point)

        # add the point to the split
        if self.nw.rect.collidepoint(point):
            self.nw.add_point(point)
        elif self.ne.rect.collidepoint(point):
            self.ne.add_point(point)
        elif self.sw.rect.collidepoint(point):
            self.sw.add_point(point)
        else:
            self.se.add_point(point)
            
    
    def get_points(self):
        points = []
        if self.data is not None:
            points.append(self.data)

        if self.se and self.se.data is not None:
            for p in self.se.get_points():
                if p != self.data:
                    points.append(p)
        if self.sw and self.sw.data is not None:
            for p in self.sw.get_points():
                if p != self.data:
                    points.append(p)
        if self.nw and self.nw.data is not None:
            for p in self.nw.get_points():
                if p != self.data:
                    points.append(p)
        if self.ne and self.ne.data is not None:
            for p in self.ne.get_points():
                if p != self.data:
                    points.append(p)
        return points


    def get_rects(node, rects=None):
       if not node.is_split and node.depth == 0:
           rects.append(node.rect)
           return rects
               
       else:
           node.rects.append(node.rect)
               
       if node.is_split:
           QuadTreeNode.get_rects(node.ne)
           node.rects.extend(node.ne.rects)
           QuadTreeNode.get_rects(node.nw)
           node.rects.extend(node.nw.rects)
           QuadTreeNode.get_rects(node.se)
           node.rects.extend(node.se.rects)
           QuadTreeNode.get_rects(node.sw)
           node.rects.extend(node.sw.rects)
           return node.rects
               
       else:
           return node.rects
       




'''
qtree = QuadTreeNode(Rect(0, 0, 100, 100))

qtree.add_point((25, 25))
qtree.add_point((75, 75))
qtree.add_point((22, 22))

qtree.add_point((45,89))
qtree.add_point((78,34))
qtree.get_points()


print qtree.get_points()

'''
