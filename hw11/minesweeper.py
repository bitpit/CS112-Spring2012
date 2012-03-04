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

def final_bombs():
    for z in range(10):
        for i in range(10):
            fX, fY, p, pp = tile_rects[z][i]
            if tile_state[z][i] == 0 and grid[z][i] == 'B':
                fX, fY, p, pp = tile_rects[z][i]
                pygame.draw.rect(screen,(193,193,193),tile_rects[z][i])
                d_bomb(fX+13,fY+15)
    return
                                 

def print_grid(grid):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            print val,
        print ""

def d_flag(x,y):
    x += 8
    y += 19
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
        over = False
        i = 0
        x = 18
        y = 150
        pygame.draw.line(screen,WHITE,(x,y-2),(x+300,y-2),2)
        for z in range(10):
            for i in range(10):
                fX, fY, p, pp = tile_rects[z][i]
                pygame.draw.line(screen,WHITE,(x,y),(x,y+28),2)
                if tile_state[z][i] == 0:
                    pygame.draw.rect(screen,BORDER_GRAY,tile_rects[z][i])
                elif tile_state[z][i] == 1:
                    pygame.draw.rect(screen,(193,193,193),tile_rects[z][i])
                    text = str(grid[z][i])
                    TEXT_COLOR = 0,0,0
                    if text == 'B':
                        d_bomb(fX+13,fY+15)
                        over = True
                    elif text == '1':
                        TEXT_COLOR = 0,0,255
                        render_font(text,fX+7,fY+4,TEXT_COLOR,31)
                    elif text == '2':
                        TEXT_COLOR = 0,128,0
                        render_font(text,fX+7,fY+4,TEXT_COLOR,31)
                    elif text == '3':
                        TEXT_COLOR = 230,0,0
                        render_font(text,fX+7,fY+4,TEXT_COLOR,31)
                    elif text == '4':
                        Text_COLOR = 0,0,128
                        render_font(text,fX+7,fY+4,TEXT_COLOR,31)
                    
                elif tile_state[z][i] == 2:
                    pygame.draw.rect(screen,BORDER_GRAY,tile_rects[z][i])
                    d_flag(fX,fY)
                x += 30
            pygame.draw.line(screen,WHITE,(x,y),(x,y+28),2)
            x = 18
            y += 30
            pygame.draw.line(screen,WHITE,(x,y-2),(x+300,y-2),2)
        return over

def adjacent_zeros(test_cords):
    for x in range(10):
        for y in range(10):
            if grid[x][y] == 0 and tile_state[x][y] == 1:
                for d in test_cords:
                    test = (x+d[0], y+d[1])
                    if test[0]<10 and test[0]>=0 and test[1] < 10 and test[1] >= 0:
                        if grid[test[0]][test[1]] == 0:
                            tile_state[test[0]][test[1]] = 1
    

def winner():
    win_count = 0
    for p in range(10):
        for q in range(10):
            if tile_state[p][q] == 1 and grid[p][q] != 'B':
                win_count += 1
    if win_count == 90:
        return True
    else:
        return False

##############
## Settings ##
##############
BLACK = 0,0,0
WHITE = 255,255,255

TILE_GRAY = 192,192,192 #is also outer border gray
BORDER_GRAY = 128,128,128#is also tile border bottom/right gray
BG_GRAY = 90,90,90

SCREEN_SIZE = 340,520
FPS = 30
#test_cords are used to do the adjacent zeros function and the board setup
test_cords = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,0),(1,1),(1,-1))
zeros_cords = ((-1,0),(0,-1),(0,1),(1,0))

################
## initialize ##
################
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)


###############
## game loop ##
###############

clock = pygame.time.Clock()           
clicked = False #to track clicking of menu items
hover = False  #to track if the mouse is hovering over a menu item
done = False
game = False
pygame.display.set_caption('Minesweeper')
screen.fill(BLACK)
quit_rect = pygame.Rect((50,290), (94,40))  #rects for checking collision w/ 
start_rect =  pygame.Rect((50,228), (220,40)) #menu items
won = False


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

    game_OVER = False

#places numbers in logic grid
    for y in range(10):
        for x in range(10):
            if grid[y][x] == 'B':
                for d in test_cords:
                    test = (x+d[0], y+d[1])
                    if test[0]<10 and test[0]>=0 and test[1] < 10 and test[1] >= 0:
                        if grid[test[1]][test[0]] != 'B':
                            grid[test[1]][test[0]] += 1

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
    
       
    #draw 'minesweeper' title thang
    render_font("M",25,77,BORDER_GRAY,105)
    render_font("inesweeper",84,95,TILE_GRAY,57)
    pygame.draw.line(screen,BORDER_GRAY,(0,133),(30,133),3)
    pygame.draw.line(screen,BORDER_GRAY,(80,133),(236,133),3)
    pygame.draw.line(screen,BORDER_GRAY,(253,133),(340,133),3)
    pygame.draw.line(screen,BORDER_GRAY,(0,425),(340,425),3)
   

    #draw menu items
    COLOR1 = 130,130,130
    COLOR2 = COLOR1
    COLOR3 = 255,255,255
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
        screen.fill(BG_GRAY) #background

        exit_rect = pygame.Rect((130,470),(65,25))
           
            
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
                            tile_state[x][y] = 1
            elif evt.type == MOUSEBUTTONDOWN and evt.button == 3: #flag
                for x in range(10):
                    for y in range(10):
                        rect = tile_rects[x][y]
                        if rect.collidepoint(pygame.mouse.get_pos()):
                            tile_state[x][y] = 2
        
        

        #draw
        adjacent_zeros(zeros_cords)
        game_OVER = draw_grid()
        
    
        
        EXIT_COLOR = WHITE
        if exit_rect.collidepoint(pygame.mouse.get_pos()):
            EXIT_COLOR = BORDER_GRAY
        render_font("EXIT",146,474,EXIT_COLOR,27)


        #winning circuit
        won = winner()
        while (won):
            x = 29
            y = 52
            pygame.draw.rect(screen,BLACK,((x,y),(280,60)))
            render_font("YOU WON!!",x+22,y+13,WHITE,60)
            for evt in pygame.event.get():
                if evt.type == MOUSEBUTTONDOWN:
                    if exit_rect.collidepoint(pygame.mouse.get_pos()):
                        won = False
                        game = False
                elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
                    won = False
                    game = False
            EXIT_COLOR = WHITE
            if exit_rect.collidepoint(pygame.mouse.get_pos()):
                EXIT_COLOR = BORDER_GRAY
            render_font("EXIT",146,474,EXIT_COLOR,27)       
            
            pygame.display.flip()
            clock.tick(FPS)
        
        #losing circuit
        while (game_OVER):
            x = 29
            y = 52
            pygame.draw.rect(screen,BLACK,((x,y),(280,60)))
            render_font("GAME  OVER",x+7,y+9,WHITE,60)
            for evt in pygame.event.get():
                if evt.type == MOUSEBUTTONDOWN:
                    if exit_rect.collidepoint(pygame.mouse.get_pos()):
                        game_OVER = False
                        game = False
                        #done = True
                elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
                    game_OVER = False
                    game = False
                    #done = True
            EXIT_COLOR = WHITE
            if exit_rect.collidepoint(pygame.mouse.get_pos()):
                EXIT_COLOR = BORDER_GRAY
            render_font("EXIT",146,474,EXIT_COLOR,27)       
            final_bombs()
            pygame.display.flip()
            clock.tick(FPS)
            

        pygame.display.flip()
        clock.tick(FPS)
        



    #refresh
    pygame.display.flip()
    clock.tick(FPS)
