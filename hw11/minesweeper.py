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

def d_flag(x,y):
   pygame.draw.polygon(screen,(220,0,0),((x+7,y-7),(x,y-8),(x+7,y-14),
                                          (x+7,y-7)))
   pygame.draw.line(screen,(220,0,0),(x+6,y-4),(x+6,y-8),2)
   pygame.draw.line(screen,BLACK,(x+3,y-3),(x+9,y-3),2)
   pygame.draw.line(screen,BLACK,(x,y),(x+12,y),4)

def d_bomb(x,y):
    pygame.draw.circle(screen, BLACK, (x,y), 6)
    pygame.draw.arc(screen,BLACK,(x+3,y-7,7,7),270,273,3)
    pygame.draw.rect(screen,(241,234,62),(x+8,y-2,2,2))
    pygame.draw.rect(screen,(241,234,62),(x+9,y-3,2,2))
    pygame.draw.rect(screen,(230,0,0),(x+9,y-2,2,2))
    pygame.draw.rect(screen,(241,234,62),(x+7,y-3,2,2))

def draw_grid():
    #draw squares
        i = 0
        x = 18
        y = 150
        pygame.draw.line(screen,WHITE,(x,y-2),(x+300,y-2),2)
        for z in range(10):
            for i in range(10):
                pygame.draw.line(screen,WHITE,(x,y),(x,y+28),2)
                pygame.draw.rect(screen,BORDER_GRAY,tile_rects[z][i])
                x += 30
            pygame.draw.line(screen,WHITE,(x,y),(x,y+28),2)
            x = 18
            y += 30
            pygame.draw.line(screen,WHITE,(x,y-2),(x+300,y-2),2)



##############
## Settings ##
##############
BLACK = 0,0,0
WHITE = 255,255,255

TILE_GRAY = 192,192,192 #is also outer border gray
BORDER_GRAY = 128,128,128#is also tile border bottom/right gray

TEAL = 0,255,150

SCREEN_SIZE = 340,520
FPS = 30


################
## initialize ##
################
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

#make play grids
grid = [] #logic grid
tile_state = [] #tile state grid
tile_rects = [] #tile rectaingle grill

#init grid
for i in range(10):   
    row = []
    for j in range(10):
        row.append(0)
    grid.append(row)

#init tile_state (0 for unseen, 1 for uncovered, 2 for flagged)
for i in range(10):
    row = []
    for j in range(10):
        row.append(0)
    tile_state.append(row)

count = 0   
while count < 10:  #while loop inserts bombs in logic grid
    x = random.randrange(10)
    y = random.randrange(10)
    if grid[x][y] == 0:
        grid[x][y] = 'B'
        count += 1

#places numbers in logic grid
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

#makes tile_rects
x = 18
y = 150
for z in range(10):
    row = []
    for i in range(10):
        row.append(pygame.Rect((x+2,y),(28,28)))
        x += 30
    x = 18
    y += 30
    tile_rects.append(row)
    


print_grid(grid)
#x, y, z, p = tile_rects[1][1]
#print x,y,z,p

###############
## game loop ##
###############

clock = pygame.time.Clock()           
clicked = False
hover = False
done = False
game = False
pygame.display.set_caption('Minesweeper')
screen.fill(BLACK)
quit_rect = pygame.Rect((50,290), (94,40))
start_rect =  pygame.Rect((50,228), (220,40))

while not done:
    screen.fill(BLACK)
    
    #input for menu
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
        elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
            done = True
        elif evt.type == MOUSEBUTTONDOWN:
            if hover == start_rect:
                game = True
            elif hover == quit_rect:
                done = True
                break
        
        if start_rect.collidepoint(pygame.mouse.get_pos()):
            hover = start_rect
        elif quit_rect.collidepoint(pygame.mouse.get_pos()):
            hover = quit_rect
        else:
            hover = False
                
    
       
    #draw 'minesweeper' title thang
    render_font("M",25,77,BORDER_GRAY,105)
    render_font("inesweeper",84,95,TILE_GRAY,57)
    pygame.draw.line(screen,BORDER_GRAY,(0,133),(30,133),3)
    pygame.draw.line(screen,BORDER_GRAY,(80,133),(236,133),3)
    pygame.draw.line(screen,BORDER_GRAY,(253,133),(340,133),3)
    pygame.draw.line(screen,BORDER_GRAY,(0,425),(340,425),3)
   

    #draw menu items
    COLOR1 = (65,65,65)
    COLOR2 = COLOR1
    COLOR3 = 181,179,179
    if hover == start_rect:
        COLOR1 = COLOR3
    elif hover == quit_rect:
        COLOR2 = COLOR3
    render_font("Start Game",68,230,COLOR1,48)
    render_font("o",54,239,COLOR1,17)
    render_font("Quit",68,295,COLOR2,48)
    render_font("o",54,304,COLOR2,17)

    ###############
    ## main game ##
    ###############
    while game == True:
        uncover = False
        screen.fill(TILE_GRAY) #background

        exit_rect = pygame.Rect((130,470),(65,25))
        
        #exit bit
        #exit_rect = pygame.Rect   #exit rect
        #pygame.draw.rect(screen,WHITE,((130,470),(55,25)))
                        
            
        #input
        for evt in pygame.event.get():
            if evt.type == QUIT:
                done = True
                game = False
            elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
                done = True
                game = False
            #input for unovering/flagging
            elif evt.type == MOUSEBUTTONDOWN and evt.button == 1: #uncover
                if exit_rect.collidepoint(pygame.mouse.get_pos()):
                    game = False
                    break
                for x in range(10):
                    for y in range(10):
                        rect = tile_rects[x][y]
                        if rect.collidepoint(pygame.mouse.get_pos()):
                            uncover = x,y
                            flag = 0
                print uncover,'uncover'
            elif evt.type == MOUSEBUTTONDOWN and evt.button == 3: #flag
                for x in range(10):
                    for y in range(10):
                        rect = tile_rects[x][y]
                        if rect.collidepoint(pygame.mouse.get_pos()):
                            flag = x,y
                            uncover = 0
                print flag,'flag'
            #elif evt.type == MOUSEBUTTONDOWN:
                
               
                    
        
        #refresh


        #draw
        draw_grid()
        
        EXIT_COLOR = WHITE
        if exit_rect.collidepoint(pygame.mouse.get_pos()):
            EXIT_COLOR = BORDER_GRAY
        render_font("EXIT",146,474,EXIT_COLOR,27)

        pygame.display.flip()
        clock.tick(FPS)
        



    #refresh
    pygame.display.flip()
    clock.tick(FPS)
