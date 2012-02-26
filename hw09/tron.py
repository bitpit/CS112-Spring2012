#!/usr/bin/env python
"""
tron.py
"""

import pygame
import math
import random
import time
from pygame import draw
from pygame.locals import *


pygame.init()
pygame.font.init()

#inits for screen stuff
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
done = False
screen_bounds = screen.get_rect()


def pleasedraw(pos, xd, yd, screen, color):
    x,y = pos
    pygame.draw.line(screen,color,(x,y),(x+xd,y+yd), 14)
    
def move(px,py,dx,dy,ptail,l,optail):
    px += dx
    py += dy
    for i in ptail:
        if i == ([px,py]):
            if l == 2:
                l = 4
            elif l == 1:
                l = 3
    for i in optail:
        for q in range(1,13):
            if i == ([px,py]) or i == ([(px-q),(py-q)]) or i == ([(px+q),(py+q)]):
                if l == 2:
                    l = 4
                elif l == 1:
                    l = 3
    
    if px < 1 or px > 599 or py < 1 or py > 599:
        if l == 2:
            l = 4
        elif l == 1:
            l = 3

    return px, py, dx, dy, l

def win_screen(winner):


def textrenderer(text,x,y,color,fontsize):
   font = pygame.font.SysFont("Arial",fontsize)
   rend = font.render(text,1,color)
   screen.blit(rend, (x,y))
   return


#program loop
while not done:

    #player movement inits
    p1xdir = -2
    p1ydir = 0

    p2xdir = 2
    p2ydir = 0

    p1x, p1y = 545,285
    p2x, p2y = 55,285
    
    p1tail = []
    p2tail = []

    #colors & such inits
    BLACK = (0,0,0)
    RED = (255,0,0)
    BLUE = (0,0,255)
    p1point,p2point = 0,0
    loser = 1

    #game loop control
    game = False
    
    screen.fill(BLACK)
    
    textrenderer("TRON",50,55,(0,0,255),170)
    textrenderer("a clone",87,220,(238,0,15),50)
    
    textrenderer("press the spacebar to begin",171,420,(249,255,250),20)
    #textrenderer("or press i for instructions",172,450,(230,230,231),18)

    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == KEYDOWN and event.key == K_SPACE:
            screen.fill(BLACK)
            game = True


    #game loop                    
    while game:
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN 
                                      and event.key == K_ESCAPE):
                game = False
                
            #p1 controls
            elif event.type == KEYUP and event.key == K_UP:
                p1ydir = -2
                p1xdir = 0
            elif event.type == KEYUP and event.key == K_DOWN:
                p1ydir = 2
                p1xdir = 0
            elif event.type == KEYUP and event.key == K_LEFT:
                p1ydir = 0
                p1xdir = -2
            elif event.type == KEYUP and event.key == K_RIGHT:
                p1ydir = 0
                p1xdir = 2
            #p2 controls
            elif event.type == KEYUP and event.key == K_w:
                p2ydir = -2
                p2xdir = 0
            elif event.type == KEYUP and event.key == K_s:
                p2ydir = 2
                p2xdir = 0
            elif event.type == KEYUP and event.key == K_a:
                p2ydir = 0
                p2xdir = -2
            elif event.type == KEYUP and event.key == K_d:
                p2ydir = 0
                p2xdir = 2

        #p1 movement
        p1x,p1y,p1xdir,p1ydir,loser = move(p1x,p1y, p1xdir, p1ydir, p1tail,1,p2tail)
        
        if loser == 3:
            win_screen(3)
            game = False
        
        p1tail.append([p1x,p1y])

        
        #p2movement
        p2x,p2y,p2xdir,p2ydir,loser = move(p2x,p2y,p2xdir,p2ydir,p2tail,2,p1tail)

        if loser == 4:
            win_screen(4)
            game = False

        p2tail.append([p2x,p2y])
        
        
        #draw players
        for i in range(len(p1tail)):
            pleasedraw(p1tail[i], p1xdir, p1ydir, screen, BLUE)
        for i in range(len(p2tail)):
            pleasedraw(p2tail[i], p2xdir, p2ydir, screen, RED)
        
       
        

        pygame.display.flip()
        


    pygame.display.flip()
