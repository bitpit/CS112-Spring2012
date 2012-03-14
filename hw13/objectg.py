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


class Person(Sprite):
    image = None
    def __init__(self, x, y, status, group, sprite):
        Sprite.__init__(self)
        if self.image is None:
            self.image = load_graphics(str(sprite))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.group = group
        self.status = status
        self.add(group)
    def hurt(self, loss, update_health=False):
        if self.health - loss <= 0:
            self.kill()
        else:
            self.health -= loss


class Wasp(Person):
    def __init__(self, x, y, status, group, sprite="wasp_baddie.png"):
        Person.__init__(self, x, y, status, group, sprite)
        self.direction = 1
        self.newy = self.rect.y+90
        self.health = 3
        self.should_update = 0
         
    def update(self):
        if self.should_update == 1: #gives it that nice old arcade slowness
            self.speed = self.get_speed()
            new_space = self.get_space()
        
            if self.status == 0:
                self.get_status()
                
            self.newrect = self.rect.move(new_space)
            self.rect = self.newrect
            self.should_update = 0
        else:
            self.should_update += 1
    
    def get_speed(self):
        if self.rect.y > 318:
            return 12
        elif self.rect.y > 402:
            return 16
        else:
            return 9

    def get_space(self):
        if self.status == 0:
            return (10,0)
        elif 50 < (self.rect.x+(self.speed*self.direction)) < 540:
            return ((self.speed*self.direction),0)
        elif self.rect.y < self.newy:
            return (0,25)
        else:
            if self.rect.y < 190:
                Wasp(-15,50,0,self.group)
            self.direction *= -1
            self.newy += 90
            return ((0,0))

    def get_status(self):
        if self.status == 0 and self.rect.x >= 60:
            self.status = 1
        
        
        

class Aliens(Person):
    def __init__(self, x, y, status, group, sprite="ws_baddie.png"):
        Person.__init__(self, x, y, status, group, sprite)
        self.health = 10
        self.xdirection = 1
        self.ydirection = 1


class PlayerShip(Person):
    def __init__(self, x, y, status, group, sprite="player_ship.png"):
        Person.__init__(self, x, y, status, group, sprite)
        self.health = 50

    def update(self, dx, dy):
        if dx > 0 and self.rect.x+dx < 600-self.rect.w:
            self.rect.x += dx
        if dx < 0 and self.rect.x+dx > 0:
            self.rect.x += dx
        if dy > 0 and self.rect.y+dy<600-self.rect.h:
            self.rect.y += dy 
        if dy < 0 and self.rect.y+dy>0:
            self.rect.y += dy 


class Bullet(Sprite):
    image = None
    def __init__(self, shooter, group, direction, sprite='bullet.png'):
        Sprite.__init__(self)
        if self.image is None:
            self.image = load_graphics(sprite)
        self.rect = self.image.get_rect()
        self.rect.x = shooter.rect.x+30
        self.rect.y = shooter.rect.y
        self.group = group
        self.direction = direction
        self.add(group)
    def update(self):
        if self.rect.y -22*self.direction <= 0 or self.rect.y - 16*self.direction >= 599:
            self.kill()
        self.rect.y -= 22*self.direction

                                    

class Make(object):
    def __init__(self, screen, white, black, sbs):
        self.screen = screen
        self.white = white
        self.black = black
        self.sidebar_stuff = sbs

        self.screen_rect = pygame.Rect((0,0),(600,600))
        self.info_rect = pygame.Rect((600,0),(200,600))

        self.make_start = True


    def start_screen(self):
        if self.make_start:
            white = self.white
            screen = self.screen
            text_render("Use arrows to move, space to fire,",230,225,white,30,screen)
            text_render("and  esc  to  pause  during  gameplay.",244,248,white,24,screen)
            text_render("Press space to begin.",180,285,white,60,screen)
            

    def game_screen(self):
        pygame.draw.rect(self.screen, (210,210,210), self.info_rect)
        pygame.draw.line(self.screen, self.white, (600,0),(600,600), 3)
        Wasp(635,160,1,self.sidebar_stuff)
        text_render(" = 300 pts", 690,182,(90,90,90),27,self.screen)
        Aliens(638,280,1,self.sidebar_stuff)
        text_render(" = 600 pts", 693,302,(90,90,90),27,self.screen)
        text_render("Ship Power",649,545,(80,80,80),24,self.screen)

    def start_enemies(self, bx, by, status, enemies):
        if self.make_start:
            for i in range(5):
                Wasp(bx,by,1,enemies)
                bx -= 66
            self.make_start = False


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
        self.sidebar = True
        self.start_screen = True
        self.start_render = True
        self.fps = 30

        group = pygame.sprite.Group()
        self.screen_rect = pygame.Rect((0,0),(600,600))
       
        self.player = pygame.sprite.Group()
        self.ship = PlayerShip(260, 500, 0, self.player)
        self.enemies = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.sidebar_stuff = pygame.sprite.Group()

        self.black = ((0,0,0))

        self.make = Make(self.screen, (255,255,255),self.black, self.sidebar_stuff)

      
    def pause(self, boolean):
        if boolean:
            self.paused = True
        else:
            self.paused = False
            pygame.key.set_repeat(45,1)
                                

    def quit(self):
        self.done = True

    def update(self):
        pass

    def start_step(self):
        self.clock.tick(self.fps)

        if self.start_render:
            self.make.start_screen()
            self.make.start_enemies(490, 50, 1, self.enemies)
            self.start_render = False


        for evt in pygame.event.get():
            if evt.type == QUIT:
                self.quit()
            elif evt.type == KEYDOWN:
                if evt.key == K_ESCAPE:
                    self.quit()
                if evt.key == K_SPACE:
                    self.start_screen = False
                    self.game = True

        pygame.display.flip()
        
        
    
    def game_step(self):
        self.clock.tick(self.fps)

        if self.sidebar:
            self.make.game_screen()
            self.sidebar_stuff.draw(self.screen)
            self.sidebar = False
        
        for evt in pygame.event.get():
            if evt.type == QUIT:
                self.quit()
            elif evt.type == KEYDOWN:
                if evt.key == K_ESCAPE:
                    pygame.key.set_repeat()
                    if self.paused:
                        self.pause(False)
                    elif not self.paused:
                        self.pause(True)
                if evt.key == K_SPACE:
                    pygame.key.set_repeat()
                    Bullet(self.ship, self.player_bullets, 1,str('bullet.png'))
            elif evt.type == KEYUP:
                if evt.key == K_SPACE:
                    pygame.key.set_repeat(45,1)

        
        if not self.paused:
            pressed = pygame.key.get_pressed()
            if pressed[K_LEFT]:
                self.ship.update(-8,0)
            if pressed[K_RIGHT]:
                self.ship.update(8,0)
            if pressed[K_UP]:
                self.ship.update(0,-8)
            if pressed[K_DOWN]:
                self.ship.update(0,8)

            pygame.draw.rect(self.screen,self.black,self.screen_rect)
  
            self.enemies.update()
            if len(self.player_bullets) > 0:
                for enemy in pygame.sprite.groupcollide(self.enemies, self.player_bullets, False, True):
                    enemy.hurt(1)
                self.player_bullets.update()
                self.player_bullets.draw(self.screen)
                                    
            self.player.draw(self.screen)
            self.enemies.draw(self.screen)
                        
        pygame.display.flip()


    def game_over(self):
        self.clock.tick (self.fps)

        for evt in pygame.event.get():
            if evt.type == QUIT:
                self.quit()
            elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
                self.start_screen = True

        pygame.display.flip()

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


groupo = Group()
Game().run()


groupo = Group()
