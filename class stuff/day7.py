#!/usr/bin/env python

import pygame
from random import randint
from pygame import draw
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800,600))

screen.fill((0,0,0))
done = False

def draw_tie(surf, color, pos, size=40):
    x, y = pos
    width = size/8
    draw.rect(surf, color, (x,y,width,size))
    draw.rect(surf, color, (x+size-width,y,width,size))
    draw.rect(surf, color, (x,y+(size-width*5),size,width))
    draw.circle(surf, color, (x+size/2,y+size/2),size/4)

col = 0
dir = 1
color=[]
pos=[]
size=[]

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            color.append((col,0,col))
            pos.append((pygame.mouse.get_pos()))
            size.append((randint(80,220)))
    col += dir
    if col>255 or col < 0:
        dir *= -1
        col += dir

    screen.fill((0,0,0))
    for i in range(len(color)):
        size[i] -= 3
        if size[i]>0:
            draw_tie(screen, color[i], pos[i], size[i])
    
    

    #draw tie fighter

    #draw_tie(screen, (col,0,98), (20,30))
    #draw_tie(screen, (col,0,98), (115,58))
    #draw_tie(screen, (col,0,98), (87,310))
    #draw_tie(screen, (col,0,98), (220,90))

    pygame.display.flip()
    
    #size
    #random place
