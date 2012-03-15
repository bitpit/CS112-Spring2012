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

class Keeper(Sprite):
    def __init__(self, surf):
        Sprite.__init__(self)
        self.surface = surf
    def update(self):
        pass
    def draw(self):
        pass

class ScoreKeeper(Keeper):
    def __init__(self, surf):
        Keeper.__init__(self, surf)
        self.score = int(0000000000)
        self.black = (0,0,0)
    def update(self, amount):
        self.score += amount
    def draw(self):
        pygame.draw.rect(self.surface, self.black, ((610,55),(180,50)))
        pygame.draw.rect(self.surface, (180,180,180), ((612,57),(176,46)))
        if self.score == 0:
            text_render('0000000000',614,68,self.black,40,self.surface)
        elif self.score < 1000:
            text_render('0000000',614,68,self.black,40,self.surface)
            text_render(str(self.score),733,68,self.black,40,self.surface)
        elif self.score < 10000:
            text_render('000000',614,68,self.black,40,self.surface)
            text_render(str(self.score),718,68,self.black,40,self.surface)
        elif self.score < 100000:
            text_render('00000',614,68,self.black,40,self.surface)
            text_render(str(self.score),703,68,self.black,40,self.surface)
        elif self.score < 1000000:
            text_render('0000',614,68,self.black,40,self.surface)
            text_render(str(self.score),688,68,self.black,40,self.surface)

class HealthKeeper(Keeper):
    def __init__(self, surf):
        Keeper.__init__(self, surf)
        self.length = 150
        self.black = ((0,0,0))
    def update(self, loss=1):
        loss *= 3
        if self.length - loss >= 0:
            self.length -= loss
        else:
            self.length = 0
    def draw(self):
        pygame.draw.rect(self.surface, self.black, ((620, 570),(160,11)))
        pygame.draw.line(self.surface,(150,150,150),(625,575),(775,575),3)
        if self.length > 0:
            pygame.draw.line(self.surface,(255,0,0),(625,575),(625+self.length,575),3)


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
        self.should_update = 0
        self.add(group)
    def hurt(self, loss, update_health=False):
        if self.health - loss <= 0:
            self.kill()
            return True
        else:
            self.health -= loss
            return False


class Wasp(Person):
    image1 = None
    image2 = None
    def __init__(self, x, y, status, group, sprite="wasp_baddie.png"):
        Person.__init__(self, x, y, status, group, sprite)
        self.direction = 1
        self.newy = self.rect.y+90
        self.health = 5
        self.frame_update = 0
        self.frame = 0
        if self.image1 is None:
            self.image1 = self.image
        if self.image2 is None:
            self.image2 = load_graphics('wasp_baddie_2.png')
                 
    def update(self):
        if self.frame_update < 5:
            self.frame_update += 1
        elif self.frame_update == 5:
            self.frame = 1
            self.frame_update += 1
        elif self.frame_update < 10:
            self.frame_update += 1
        else:
            self.frame = 0
            self.frame_update = 0
        if self.frame == 0:
            self.image = self.image1
        elif self.frame == 1:
            self.image = self.image2
        if self.should_update == 2: #gives it that nice old arcade slowness
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
        self.health = 18
        self.xdirection = -1
        self.ydirection = 1
        self.health = 20
    def update(self):
        if self.should_update == 2:
            dx = random.randrange(-30,30)
            dy = random.randrange(-30,30)
            dy = random.randrange(-30,30)
            if self.status == 0 and self.rect.y < 25:
                self.rect.y += 10
            elif self.status == 0:
                self.status = 1
            if self.rect.y < 0:
                self.rect.y = 3
            if self.rect.x < 0:
                self.rect.x = 3
            if self.rect.x + dx*self.xdirection > 540 or self.rect.x + dx*self.xdirection < 20:
                self.xdirection *= -1
            if self.rect.y + dy*self.ydirection > 480 or self.rect.y + dy*self.ydirection < 15:
                self.ydirection *= -1
            self.rect.x += dx*self.xdirection
            self.rect.y += dy*self.ydirection
            self.should_update = 0
        else:
            self.should_update += 1



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
    def __init__(self, shooter, group, direction=1, sprite='bullet.png'):
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

class EnemyBullets(Bullet):
    def __init__(self, shooter, group, direction, sprite='evilbullet.png'):
        Bullet.__init__(self, shooter, group, direction, sprite)
        self.direction = direction
    def update(self, speed):
        if self.rect.y - speed*self.direction <= 0 or self.rect.y-speed*self.direction >= 599:
            self.kill()
        self.rect.y -= speed+2*self.direction*-1
    
def complex_bullet_algorithm(enemy_group, seed):
        ayn = seed
        length = len(enemy_group)
        if length > 5 or length == 5:
            ayn *= 16
        elif length == 4:
            ayn *= 16
        elif length == 3:
            ayn *= 8
        elif length == 2:
            ayn *= 4
        else:
            ayn *= 1
        i = random.randrange(ayn)
        if i == 0:
            return True


class EnemyExplosion(Sprite):
    def __init__(self, position, group, radius=5):
        Sprite.__init__(self)
        self.position = position
        self.duration = 10
        self.expandto = 14
        self.radius = radius
        self.group = group
        self.add(group)
    def update(self):
        if self.expandto > self.radius:
            self.radius += 3
        else:
            self.kill()
    def random_color(self):
        return ((random.randrange(120,256),255,random.randrange(120,256)))
    def draw(self, surf):
        pygame.draw.circle(surf, self.random_color(), self.position, self.radius)
                                                
class Make(object):
    def __init__(self, screen, white, black, sbs, score):
        self.screen = screen
        self.white = white
        self.black = black
        self.sidebar_stuff = sbs

        self.screen_rect = pygame.Rect((0,0),(600,600))
        self.info_rect = pygame.Rect((600,0),(200,600))

        self.score = score

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
        self.score.draw()

    def start_enemies(self, bx, by, status, enemies):
        if self.make_start:
            for i in range(5):
                Wasp(bx,by,1,enemies)
                bx -= 66
            self.make_start = False

