#!/usr/bin/env python
"""
tron.py
by Evan Ricketts
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
    if ([px,py] in ptail):
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


def textrenderer(text,x,y,color,fontsize):
   font = pygame.font.SysFont("Arial",fontsize)
   rend = font.render(text,1,color)
   screen.blit(rend, (x,y))
   return

def game_over(loser):
    if loser == 3:
        l = "Player 1 Wins!"
        color = (255,0,0)
    elif loser == 4:
        l = "Player 2 Wins!"
        color = (0,0,255)
    screen.fill((240,255,255))
    textrenderer(l,100,235,color,60)
    textrenderer("Game Over",249,195,(0,0,0),20)
    textrenderer("(press space to exit)",240,465,(30,30,30),14)
    pygame.display.flip()
    x = 0
    while x == 0:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_SPACE:
                return
                

def instructions():
    screen.fill((0,0,0))
    textrenderer("TRON",40,40,(0,0,255),30)
    textrenderer("is a game for two players.",134,49,(255,255,255),22)
    textrenderer("Each player must avoid the walls and the paths", 42,110,(255,255,255),22)
    textrenderer("created by their own tail as well as their opponents'",42,135,(255,255,255),22)
    textrenderer("tail.",42,160,(255,255,255),22)

    textrenderer("Player 1",42,225,(255,0,0),22)
    textrenderer("steers their craft with the W, A, S & D keys.",130,225,(255,255,255),22)

    textrenderer("Player 2",42,285,(0,0,255),22)
    textrenderer("steers their craft with the Up, Down, Left &",130,285,(255,255,255),22)
    textrenderer("Right arrow keys.",42,313,(255,255,255),22)
    
    textrenderer("Good luck!!",42,420,(255,255,255),32)
    textrenderer("(press space to exit)",54,465,(255,255,255),14)
    
    pygame.display.flip()
    
    x = 0
    while x == 0:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_SPACE:
                return
            if event.type == KEYDOWN and event.key == K_ESCAPE:
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
    loser = 1

    #game loop control
    game = False
    
    screen.fill(BLACK)
    
    textrenderer("TRON",50,55,(0,0,255),170)
    textrenderer("a clone",87,220,(238,0,15),50)
    
    textrenderer("press the spacebar to begin",171,420,(249,255,250),20)
    textrenderer("or press i for instructions",172,450,(230,230,231),18)

    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == KEYDOWN and event.key == K_SPACE:
            screen.fill(BLACK)
            game = True
        elif event.type == KEYDOWN and event.key == K_i:
            instructions()


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
        p1tail.append([p1x,p1y])
        
        #gameover?
        if loser == 3:
            game_over(loser)
            game = False
            break
        
        #p2movement
        p2x,p2y,p2xdir,p2ydir,loser = move(p2x,p2y,p2xdir,p2ydir,p2tail,2,p1tail)
        p2tail.append([p2x,p2y])

        #is there a gameover?
        if loser == 4:
            game_over(loser)
            game = False
            break
        
        
        #draw players
        for i in range(len(p1tail)):
            pleasedraw(p1tail[i], p1xdir, p1ydir, screen, BLUE)
        for i in range(len(p2tail)):
            pleasedraw(p2tail[i], p2xdir, p2ydir, screen, RED)
        pygame.display.flip()
        

    pygame.display.flip()
