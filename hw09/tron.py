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

def draw_players():
    return

def crash():
    return

def win_message():
    return

def scorekeeper():
    return

def game():
    screen.fill(BLACK)
    print "now in the game loop"
    print "finished"
    return

def textrenderer(text,x,y,color,fontsize):
   font = pygame.font.SysFont("Arial",fontsize)
   ren = font.render(text,1,color)
   screen.blit(ren, (x,y))

BLACK = (0,0,0)

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
done = False
screen_bounds = screen.get_rect()

screen.fill((BLACK))

p1lightbike = []
p2lightbike = []

while not done:
   
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == KEYDOWN and event.key == K_SPACE:
            game()
    
    textrenderer("TRON",50,55,(0,0,255),170)
    textrenderer("a clone",87,220,(238,0,15),50)
    textrenderer("press the spacebar to begin",171,420,(249,255,250),20)

            
    pygame.display.flip()
