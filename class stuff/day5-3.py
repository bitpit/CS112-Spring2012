#!/usr/bin/env python

'''
1 draw curve in all 4 corners
2 press up/dn to change width of the lines
'''

import pygame
from pygame.locals import *
# Settings
BLACK = 0,0,0
RED = 255,0,0
size = 400,400
# Intializeation
pygame.init()
screen = pygame.display.set_mode(size)

done = False
sep = 8
pygame.key.set_repeat(100,100) #keeps looking for key input i believe
while not done:
    #Looks for Quit/Escapes
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == KEYDOWN and event.key == K_UP:
            sep += 1
        elif event.type == KEYDOWN and event.key == K_DOWN:
            sep -= 1
        

    #Drawing
    screen.fill(BLACK)
    for i in range (0,400,sep):
        pygame.draw.line(screen,RED,(0,i),(i,399))
        pygame.draw.line(screen,RED,(399,i),(i,0))
        pygame.draw.line(screen,RED,(i,399),(399,399-i))
        pygame.draw.line(screen,RED,(399-i,0),(0,i))
    pygame.display.flip()


'''
for hw - fill in appropriate code, print the # for our answer for readability
'''
