#!/usr/bin/env python

import pygame
from pygame.locals import *
import math
from math import *
import random

def render_font(text,x,y,color,size):
    font = pygame.font.Font(None, size)
    rend = font.render(text, True, color)
    screen.blit(rend, (x,y))

def print_grid(grid):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            print val,
        print ""


##############
## Settings ##
##############
LIGHTLIGHT_GRAY = 235,235,235
BLACK = 0,0,0
LIGHT_GRAY = 215,215,215
GRAY = 183,183,183
DARK_GRAY = 149,149,149
NICE_BLUE = 0,118,189
NICE_RED = 237,28,36
TEAL = 0,255,150

SCREEN_SIZE = 800,600
FPS = 30


################
## initialize ##
################
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

#make play grid
grid = []

for i in range(10):   
    row = []
    for j in range(10):
        row.append(0)
    grid.append(row)

count = 0   
while count < 10:  #while loop inserts bombs
    x = random.randrange(10)
    y = random.randrange(10)
    if grid[x][y] == 0:
        grid[x][y] = 'B'
        count += 1

#places numbers
test_cords = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,0),(1,1),(1,-1))
for y in range(10):
    for x in range(10):
        if grid[y][x] == 'B':
            for d in test_cords:
                test = (x+d[0], y+d[1])
                if test[0]<10 and test[0]>=0 and test[1] < 10 and test[1] >= 0:
                    if grid[test[1]][test[0]] != 'B':
                        grid[test[1]][test[0]] += 1

#four should be max numbers of bombs usually - build in exception for 5? max!

           
print_grid(grid)


    
