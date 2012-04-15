#!/usr/bin/env python

import pygame
from pygame.locals import *

## Settings
BACKGROUND = 150,150,150
RED = 255,0,0
WHITE = 255,255,255
GREEN = 0,255,0
TEAL = 0,255,150

SCREEN_SIZE = 800,600
RECT_SIZE = 120,80
FPS = 30

## initialize
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

## setup game objects
bounds = screen.get_rect()

rect = pygame.Rect((0,0), RECT_SIZE)
rect.center = bounds.center

rects = [pygame.Rect((0,0), RECT_SIZE),
         pygame.Rect((0,0), RECT_SIZE),
         pygame.Rect((0,0), RECT_SIZE),
         pygame.Rect((0,0), RECT_SIZE),]

rects[0].topleft = bounds.topleft
rects[1].topright = bounds.topright
rects[2].bottomleft = bounds.bottomleft
rects[3].bottomright = bounds.bottomright

bigfont = pygame.font.Font(None, 80)

## Game loop
clock = pygame.time.Clock()
done = False
grabbed = False

while not done:

    #input
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
        elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
            done = True
        elif evt.type == MOUSEBUTTONDOWN:
            for rect in rects:
                if rect.collidepoint(pygame.mouse.get_pos()):
            #collide point checks to see if a point collides w/ a rectangle
                    grabbed = rect
                if grabbed:
                    rects.remove(grabbed)
                    rects.append(grabbed)
        elif evt.type == MOUSEBUTTONUP:
            grabbed = False
        

    #update
    if grabbed:
        grabbed.center = pygame.mouse.get_pos()
        grabbed.clamp_ip(bounds) #will not allow rect outside of bounds

    #draw
    screen.fill(BACKGROUND)
    text = bigfont.render("Drag the rectangles!", True, (0,0,0),BACKGROUND)
    loc = text.get_rect()
    loc.center = bounds.center
    screen.blit(text, loc)

    for rect in rects:
        others = rects[:]
        others.remove(rect)

        color = RED
        mulder = (0,0,0)

        if grabbed == rect:
            color = WHITE
            mulder = TEAL
        elif rect.collidelist(others) != -1:
            color = GREEN
        
        pygame.draw.rect(screen, (color), rect)
        pygame.draw.rect(screen, (mulder), rect, 5)

    #refresh
    pygame.display.flip()
    clock.tick(FPS)
