#!/usr/bin/env python
#rewrite of hw13

import random
import pygame
from pygame.locals import *
from pygame.sprite import Sprite, Group, RenderUpdates
import os, sys


def load_graphics(filename):
    fullfname = os.path.join('graphics', filename)
    try:
        image = pygame.image.load(fullfname)
    except pygame.error, message:
        print 'Cannot load', fullfname
        raise SystemExit, message
    return image


def text_render(text,x,y,color,size, surface):
    font = pygame.font.Font(None, size)
    rend = font.render(text, True, color)
    surface.blit(rend, (x,y))


class Make(object):
    def __init__(self, screen, white, black):
        self.screen = screen
        self.white = white
        self.black = black

        self.make_start = True

    def start_screen(self):
        if self.make_start:
            white = self.white
            screen = self.screen
            text_render("Use arrows to move, space to fire,",230,225,white,30,screen)
            text_render("and  esc  to  pause  during  gameplay.",244,248,white,24,screen)
            text_render("Press space to begin.",180,285,white,60,screen)
            self.make_start = False

    def game_screen(self):
        pass



class Game(object):
    title = 'objectg'
    screen_size = 800, 600
    fps = 30

    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(45,1)
        self.screen = pygame.display.set_mode(self.screen_size)
        if self.title:
            pygame.display.set_caption(self.title)

        self.paused = False
        self.game = False
        self.start_screen = True
        self.fps = 30

        group = pygame.sprite.Group()
       
        self.player = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.sidebar_stuff = pygame.sprite.Group()

        #self.game.health = HealthKeeper(self.screen)
        #self.game.score = ScoreKeeper(self.screen)
        self.screen_rect = pygame.Rect((0,0),(600,600))
        self.info_rect = pygame.Rect((600,0),(200,600))

        self.make = Make(self.screen, (255,255,255),(0,0,0))
        

    def pause(self, boolean):
        if boolean:
            self.paused = True
        else:
            self.paused = False

    def quit(self):
        self.done = True

    def update(self):
        pass

    def start_step(self):
        self.clock.tick(self.fps)

        self.make.start_screen()

        for evt in pygame.event.get():
            if evt.type == QUIT:
                self.quit()
            elif evt.type == KEYDOWN:
                if evt.key == K_ESCAPE:
                    self.quit()
                if evt.key == K_SPACE:
                    self.game = True

        pygame.display.flip()
        

        
    def game_step(self):
        self.clock.tick(self.fps)

    def game_over(self):
        pass

    def run(self):
        self.done = False
        self.clock = pygame.time.Clock()
        while not self.done:
            if self.game:
                self.game_step()
            elif self.start_screen:
                self.start_step()
            else:
                self.game_over()


Game().run()


