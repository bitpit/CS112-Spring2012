#!/usr/bin/env python




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
    return image, image.get_rect()



class PlayerShip(Sprite):
    def __init__(self, x=260, y=500):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('player_ship.png')
        self.rect.x = x
        self.rect.y = y
        #self.rect.clamp(surf)
        self.add(pship_group)

    def update(self, dx, dy):
        if dx > 0 and self.rect.x+dx < 600-self.rect.w:
            self.rect.x += dx
        if dx < 0 and self.rect.x+dx > 0:
            self.rect.x += dx
        if dy > 0 and self.rect.y+dy<600-self.rect.h:
            self.rect.y += dy 
        if dy < 0 and self.rect.y+dy>0:
            self.rect.y += dy 
        pygame.sprite.groupcollide(pship_group, wasp_baddies, True, False)



class Wasp(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('wasp_baddie.png')
        self.rect.x = x
        self.rect.y = y
        self.add(wasp_baddies)
        self.direction = 1
        self.newy = y+90
        self.health = 4

    def update(self):
        if 50 < self.rect.x + 10*self.direction < 540:
            self.rect.x += 10*self.direction
        elif self.rect.y < self.newy:
            self.rect.y += 25
        else:
            self.direction *= -1
            self.newy += 90

    def hurt(self, amount):
        if self.health - amount <= 0:
            self.kill()
        else:
            self.health -= amount
       


class BulletShoot(Sprite):
    def __init__(self, ship):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('bullet.png')
        self.rect.x = ship.rect.x+30
        self.rect.y = ship.rect.y
        self.add(bullets)
    def fire(self):
        if self.rect.y - 16 <= 0:
            self.kill()
        self.rect.y -= 18



##########
#Settings#
##########
BLACK = 0,0,0
WHITE = 255,255,255

SCREEN_SIZE = 800,600
FPS = 30


############
#initialize#
############
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
game = True
won = False
screen.fill(BLACK)
pygame.display.set_caption('Gaylaxitives')

screen_rect = pygame.Rect((0,0),(600,600))
info_rect = pygame.Rect((600,0),(200,600))

bounds = screen_rect

pygame.draw.rect(screen, (210,210,210), info_rect)
pygame.draw.line(screen, WHITE, (600,0),(600,600), 3)


pship_group = Group()
ship = PlayerShip()

wasp_baddies = Group()

bullets = Group()

bx = 490
by = 50
for i in range(5):
    p = Wasp(bx,by)
    bx -= 66


pygame.key.set_repeat(45, 1)

move = 0

######
#game#
######

while game:
    pygame.draw.rect(screen,BLACK,screen_rect)
    
    #input for exit
    for evt in pygame.event.get():
        if evt.type == QUIT:
            game = False
        elif evt.type == KEYDOWN: 
            if evt.key == K_ESCAPE:
                game = False
            if evt.key == K_SPACE:
                missle = BulletShoot(ship)
            if evt.key == K_p:
                print len(bullets)
            

    #input for game
    pressed = pygame.key.get_pressed()
    if pressed[K_LEFT]:
        ship.update(-6,0)
    if pressed[K_RIGHT]:
        ship.update(6,0)
    if pressed[K_UP]:
        ship.update(0,-6)
    if pressed[K_DOWN]:
        ship.update(0,6)
 

    #update wasp baddies
    if move < 2:
        move += 1
    else:
        wasp_baddies.update()
        move = 0
    

    for i in bullets:
        i.fire()
        bullets.draw(screen)

    for enemy in pygame.sprite.groupcollide(wasp_baddies, bullets, False, True):
        enemy.hurt(1)
            


    #draw   
    pship_group.draw(screen)
    wasp_baddies.draw(screen)




    #update
    pygame.display.flip()
    clock.tick(FPS)


