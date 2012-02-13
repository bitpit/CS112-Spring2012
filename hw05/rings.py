#!/usr/bin/env python

import pygame
from pygame.locals import *

## COLORS
BLUE = 0, 133, 199
RED = 223, 0, 36
YELLOW = 244, 195, 0
GREEN = 0, 159, 61
BLACK = 0, 0, 0
WHITE = 255, 255, 255

THICKNESS = 20


## MAIN
pygame.init()
screen = pygame.display.set_mode((800, 388))
pygame.display.set_caption("Olympic Rings   [press ESC to quit]")

## Draw
screen.fill(WHITE)
#tops
pygame.draw.ellipse(screen,BLUE,(51,26,219,219),20)
pygame.draw.ellipse(screen,BLACK,(289,26,219,219),20)
pygame.draw.ellipse(screen,RED,(527,26,219,219),20)
#bottoms
pygame.draw.ellipse(screen,YELLOW,(170,136,219,219),20)
pygame.draw.ellipse(screen,GREEN,(408,136,219,219),20)


## Loop
clock = pygame.time.Clock()
done = False
while not done:
    event = pygame.event.poll()
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True

    pygame.display.flip()
    clock.tick(30)

print "ByeBye"
