#!/usr/bin/env python



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
    return image, image.get_rect()


def text_render(text,x,y,color,size):
    font = pygame.font.Font(None, size)
    rend = font.render(text, True, color)
    screen.blit(rend, (x,y))


class PlayerShip(Sprite):
    def __init__(self, x=260, y=500):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('player_ship.png')
        self.rect.x = x
        self.rect.y = y
        self.add(pship_group)
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
        pygame.sprite.groupcollide(pship_group, wasp_baddies, True, False)



class Wasp(Sprite):
    def __init__(self, x, y, status):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('wasp_baddie.png')
        self.rect.x = x
        self.rect.y = y
        self.add(wasp_baddies)
        self.direction = 1
        self.newy = y+90
        self.health = 7
        self.status = status

    def update(self):
        if self.status == 0:
            self.rect.x += 10
            if self.rect.x >= 60:
                self.status = 1
        elif 50 < self.rect.x + 10*self.direction < 540:
            self.rect.x += 10*self.direction
        elif self.rect.y < self.newy:
            self.rect.y += 25
        else:
            if self.rect.y < 190:
                newwasp = Wasp(-15,50,0)
            self.direction *= -1
            self.newy += 90

    def hurt(self, amount):
        if self.health - amount <= 0:
            EnemyExplosion((self.rect.x-4,self.rect.y+25))
            self.kill()
        else:
            self.health -= amount


class Aliens(Sprite):
    def __init__(self, x, y, status, group):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('ws_baddie.png')
        self.rect.x = x
        self.rect.y = y
        self.health = 10
        self.status = status
        self.add(group)
        self.xdirection = 1
        self.ydirection = 1

    def update(self):
        dx = random.randrange(-30,30)
        dy = random.randrange(-30,30)
        if self.status == 0 and self.rect.y < 25:
            self.rect.y += 10
        elif self.status == 0:
            self.status = 1
        if self.rect.x + dx*self.xdirection > 540 or self.rect.x + dx*self.xdirection < 20:
            self.xdirection *= -1
        if self.rect.y + dy*self.ydirection > 480 or self.rect.y + dy*self.ydirection < 15:
            self.ydirection *= -1
        self.rect.x += dx*self.xdirection
        self.rect.y += dy*self.ydirection
        fire = random.randrange(5)
        if fire == 4:
            BulletShoot(self, enemy_bullets)

    def hurt(self, amount):
        if self.health - amount <= 0:
            EnemyExplosion((self.rect.x-4,self.rect.y+25))
            self.kill()
        else:
            self.health -= amount


class EnemyExplosion(Sprite):
    def __init__(self, position):
        Sprite.__init__(self)
        self.position = position
        self.duration = 10
        self.expandto = 18
        self.radius = 5
        self.add(explosions)
        
    def update(self):
        if self.expandto > self.radius:
            self.radius += 3
        else:
            self.kill()

    def random_color(self):
        return ((random.randrange(120,256), 255, random.randrange(120,256)))

    def draw(self, surf):
        pygame.draw.circle(surf, self.random_color(), self.position, self.radius)



class BulletShoot(Sprite):
    def __init__(self, ship, group):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('bullet.png')
        self.rect.x = ship.rect.x+30
        self.rect.y = ship.rect.y
        self.add(group)
    def fire(self, direction):
        if self.rect.y - 16*direction <= 0 or self.rect.y - 16*direction >= 599:
            self.kill()
        self.rect.y -= 18*direction
'''
class EnemyBullet(BulletShoot):
    def __init__(self, ship):
        BulletShoot.__init__(self, ship)
'''


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
game = False
won = False
begin = True
phase2 = False
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

your_bullets = Group()
enemy_bullets = Group()

explosions = Group()

#creates enemies currently
bx = 490
by = 50
for i in range(5):
    p = Wasp(bx,by,1)
    bx -= 66


pygame.key.set_repeat(45, 1)

move = 0

######
#game#
######
pygame.draw.rect(screen,BLACK,screen_rect)
text_render("Use arrows to move, space to fire.",145,225,WHITE,30)
text_render("Press space to begin.",110,285,WHITE,50)

while begin:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            begin = False
        elif evt.type == KEYDOWN: 
            if evt.key == K_ESCAPE:
                begin = False
            if evt.key == K_SPACE:
                game = True
                begin = False


    pygame.display.flip()
    clock.tick(FPS)


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
                missle = BulletShoot(ship,your_bullets)
            if evt.key == K_p:
                print len(explosions)
            

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
    
    #update bullets
    for i in your_bullets:
        i.fire(1)
    your_bullets.draw(screen)

    for enemy in pygame.sprite.groupcollide(wasp_baddies, your_bullets, False, True):
        enemy.hurt(1)
            
    for i in enemy_bullets:
        i.fire(-1)
    enemy_bullets.draw(screen)



    #update explosions
        
    for i in explosions:
        i.update()
        i.draw(screen)

        
    if len(wasp_baddies) == 0:
        x = 0
        y = -30
        for i in range(6):
            Aliens(x, y, 0, wasp_baddies)
            x += 90
            

    if len(pship_group) == 0:
        game = False


    #draw 
    pship_group.draw(screen)
    wasp_baddies.draw(screen)




    #update
    pygame.display.flip()
    clock.tick(FPS)



if not won:
    pygame.draw.rect(screen,WHITE,((65,170),(660,230)))
    text_render('Game Over',110,240,BLACK,150)

while not won:
    
    for evt in pygame.event.get():
        if evt.type == QUIT:
            exit()
        elif evt.type == KEYDOWN: 
            if evt.key == K_ESCAPE:
                exit()
            if evt.key == K_SPACE:
                exit()


    pygame.display.flip()
    clock.tick(FPS)
