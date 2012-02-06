#!/usr/bin/env python

import pygame                    #accesses pygame library
from pygame.locals import *      #??

screen_size = 640,480            #sets a screen of 640*480
background = 0,255,255           #creates background, R,G,B from 0 to 255
                                 # 0,0,0 is black
pygame.init()                    # initializes pygame : voodoo shit
screen = pygame.display.set_mode(screen_size) #

done=False

while not done:
    event = pygame.event.poll()  # listens to see if a key is hit or something
                                 # is clicked
    if event.type == QUIT:       # QUIT is the RED BUTTON in the GUI
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE: #saying there is a
                                 #key down and this key is ESCAPE
        done = True
    elif event.type == KEYDOWN and event.key == K_w: #changes colour background
        background=255,0,0
    elif event.type == KEYDOWN and event.key == K_e: #depending on the key that
        background=0,255,255
    elif event.type == KEYDOWN and event.key == K_r: #is pressed
        background=0,255,0
        
    elif event.type == MOUSEBUTTONDOWN: #looks for mouse clicks and prints em
        print "Mouse",pygame.mouse.get_pos() #positive y is down for computers
    screen.fill(background)      # fills the screen with the color background
    pygame.display.flip()        # flips between two screens, double buffer

print "Bye bye"                  # aint no lie baby
