#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

import pygame
import math
import random
import time
from pygame import draw
from pygame.locals import *


pygame.init()
pygame.font.init()


#colors & such
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
WIDTH = 2

p1point,p2point = 0,0
loser = 1

#inits for screen stuff
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
done = False
screen_bounds = screen.get_rect()

screen.fill((BLACK))

#player movement
p1xdir = -1
p1ydir = 0

p2xdir = 1
p2ydir = 0

p1x, p1y = 485,285
p2x, p2y = 245,450

p1tail = []
p2tail = []


def pleasedraw(pos, xd, yd, screen, color):
    x,y = pos
    pygame.draw.line(screen,color,(x,y),(x+xd,y+yd), 5)
    
def move(px,py,dx,dy,ptail,bounds,l):
    px += dx
    py += dy
    for i in ptail:
        print i
        if i == ([px,py]):
            l = 3

    return px, py, dx, dy, l
    



def textrenderer(text,x,y,color,fontsize):
   font = pygame.font.SysFont("Arial",fontsize)
   rend = font.render(text,1,color)
   screen.blit(rend, (x,y))
   return


#control loop
while not done:
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
                game = quit()
                
            #p1 controls
            elif event.type == KEYUP and event.key == K_UP:
                p1ydir = -1
                p1xdir = 0
            elif event.type == KEYUP and event.key == K_DOWN:
                p1ydir = 1
                p1xdir = 0
            elif event.type == KEYUP and event.key == K_LEFT:
                p1ydir = 0
                p1xdir = -1
            elif event.type == KEYUP and event.key == K_RIGHT:
                p1ydir = 0
                p1xdir = 1
            #p2 controls
            elif event.type == KEYUP and event.key == K_w:
                p2ydir = -1
                p2xdir = 0
            elif event.type == KEYUP and event.key == K_s:
                p2ydir = 1
                p2xdir = 0
            elif event.type == KEYUP and event.key == K_a:
                p2ydir = 0
                p2xdir = -1
            elif event.type == KEYUP and event.key == K_d:
                p2ydir = 0
                p2xdir = 1

        #p1 movement
        p1x,p1y,p1xdir,p1ydir,loser = move(p1x,p1y, p1xdir, p1ydir, p1tail, screen_bounds, loser)
        
        if loser == 3:
            game = False
        
        p1tail.append([p1x,p1y])

        #p2movement
        p2x,p2y,p2xdir,p2ydir,loser = move(p2x,p2y,p2xdir,p2ydir,p2tail,screen_bounds,loser)

        if loser == 3:
            game = False

        p2tail.append([p2x,p2y])
        
        
        #draw players
        for i in range(len(p1tail)):
            pleasedraw(p1tail[i], p1xdir, p1ydir, screen, BLUE)
        for i in range(len(p2tail)):
            pleasedraw(p2tail[i], p2xdir, p2ydir, screen, RED)
        
       
        

        pygame.display.flip()
        clock.tick(30000)


    pygame.display.flip()
