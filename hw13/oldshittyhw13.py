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
    return image


def text_render(text,x,y,color,size):
    font = pygame.font.Font(None, size)
    rend = font.render(text, True, color)
    screen.blit(rend, (x,y))
        

class HealthKeeper(Sprite):
    def __init__(self, surf):
        Sprite.__init__(self)
        self.surface = surf
        self.length = 150

    def update(self, loss=1):
        loss *= 3
        if self.length - loss >= 0:
            self.length -= loss
        else:
            self.length = 0

    def draw(self):
        pygame.draw.rect(self.surface, BLACK, ((620, 570),(160,11)))
        pygame.draw.line(self.surface,(150,150,150),(625,575),(775,575),3)
        if self.length > 0:
            pygame.draw.line(self.surface,(255,0,0),(625,575),(625+self.length,575),3)



class ScoreKeeper(Sprite):
    def __init__(self, surf):
        Sprite.__init__(self)
        self.surface = surf
        self.score = int(0000000000)
        
    def increase(self, amount):
        self.score += amount

    def draw(self):
        pygame.draw.rect(screen, BLACK, ((610,55),(180,50)))
        pygame.draw.rect(screen, (180,180,180), ((612,57),(176,46)))
        if self.score == 0:
            text_render('0000000000',614,68,BLACK,40)
        elif self.score < 1000:
            text_render('0000000',614,68,BLACK,40)
            text_render(str(self.score),733,68,BLACK,40)
        elif self.score < 10000:
            text_render('000000',614,68,BLACK,40)
            text_render(str(self.score),718,68,BLACK,40)
        elif self.score < 100000:
            text_render('00000',614,68,BLACK,40)
            text_render(str(self.score),703,68,BLACK,40)
        elif self.score < 1000000:
            text_render('0000',614,68,BLACK,40)
            text_render(str(self.score),688,68,BLACK,40)




class PlayerShip(Sprite):
    image = None
    def __init__(self, x=260, y=500):
        Sprite.__init__(self)
        if PlayerShip.image is None:
            PlayerShip.image = load_graphics('player_ship.png')
        self.image = PlayerShip.image
        self.rect = self.image.get_rect()
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


    def hurt(self,loss):
        if self.health - loss <= 0:
            self.kill()
        else:
            self.health -= loss
            health.update(loss)
            health.draw()



class Wasp(Sprite):
    image = None
    def __init__(self, x, y, status, group):
        Sprite.__init__(self)
        if Wasp.image is None:
            Wasp.image = load_graphics('wasp_baddie.png')
        self.image = Wasp.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1
        self.newy = y+90
        self.health = 3
        self.status = status
        self.add(group)

    def update(self):
        if self.rect.y > 318:
            speed = 13
        elif self.rect.y > 402:
            speed = 16
        else:
            speed = 10
        if self.status == 0:
            self.rect.x += 10
            if self.rect.x >= 60:
                self.status = 1
        elif 50 < self.rect.x + speed*self.direction < 540:
            self.rect.x += speed*self.direction
        elif self.rect.y < self.newy:
            self.rect.y += 25
        else:
            if self.rect.y < 190:
                newwasp = Wasp(-15,50,0,enemies)
            self.direction *= -1
            self.newy += 90

    def hurt(self, amount):
        if self.health - amount <= 0:
            score.increase(300)
            score.draw()
            EnemyExplosion((self.rect.x-4,self.rect.y+25))
            self.kill()
        else:
            self.health -= amount



class Aliens(Sprite):
    image = None
    def __init__(self, x, y, status, group):
        Sprite.__init__(self)
        if Aliens.image is None:
            Aliens.image = load_graphics('ws_baddie.png')
        self.image = Aliens.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 10
        self.status = status
        self.add(group)
        self.group = group
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
        fire = random.randrange(7)
        if fire == 4:
            BulletShoot(self, enemy_bullets,str('evilbullet.png'))

    def hurt(self, amount):
        if self.health - amount <= 0:
            score.increase(600)
            score.draw()
            EnemyExplosion((self.rect.x-4,self.rect.y+25))
            self.kill()
        else:
            self.health -= amount

    def self_intersect(self):
        return pygame.sprite.spritecollideany(self,self.group)


class EnemyExplosion(Sprite):
    def __init__(self, position, radius=5):
        Sprite.__init__(self)
        self.position = position
        self.duration = 10
        self.expandto = 18
        self.radius = radius
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
    image = None
    def __init__(self, ship, group, image=str('bullet.png')):
        Sprite.__init__(self)
        if BulletShoot.image is None:
            BulletShoot.image = load_graphics(image)
        self.image = BulletShoot.image
        self.rect = self.image.get_rect()
        self.rect.x = ship.rect.x+30
        self.rect.y = ship.rect.y
        self.add(group)
    def fire(self, direction):
        if self.rect.y - 16*direction <= 0 or self.rect.y - 16*direction >= 599:
            self.kill()
        self.rect.y -= 18*direction

class MissleShoot(Sprite):
    image = None
    def __init__(self, ship, group, image=str('baddie_missile.png')):
        Sprite.__init__(self)
        if MissleShoot.image is None:
            MissleShoot.image = load_graphics(image)
        self.image = MissleShoot.image
        self.rect = self.image.get_rect()
        self.rect.x = ship.rect.x+20
        self.rect.y = ship.rect.y+30
        self.rect.w += 30 
        self.add(group)
    def collision_detection(self):
        pass
    def update(self,direction):
        if self.rect.y -10*direction <= 0 or self.rect.y -10*direction >=599:
            self.kill()
        self.rect.y -= 13*direction


class RenderText(object):
    def __init__(self):
        self._intro1 = str("Use arrows to move, space to fire,")
        self._intro2 = str("and esc to pause during gameplay.")
        self._intro3 = str("Press space to begin.")
    def intro_text(self):
        text_render(self._intro1,230,225,WHITE,30)
        text_render(self._intro2,259,248,WHITE,24)
        text_render(self._intro3,180,285,WHITE,60)


class GameEvents(object):
    def __init__(self):
        self.clock = clock 
    def make_start_enemies(self):
        bx = 490
        by = 50
        for i in range(5):
            p = Wasp(bx,by,1,enemies)
            bx -= 66
    def draw_sidebar(self):
        pygame.draw.rect(screen, (210,210,210), info_rect)
        pygame.draw.line(screen, WHITE, (600,0),(600,600), 3)
        Wasp(635,160,1,sidebar_stuff)
        text_render(" = 300 pts", 690,182,(90,90,90),27)
        Aliens(638,280,1,sidebar_stuff)
        text_render(" = 600 pts", 693,302,(90,90,90),27)
        text_render("Ship Power",649,545,(80,80,80),24)
    def step(self):
        self.clock.tick(FPS)
        for evt in pygame.event.get():
            if evt.type == QUIT:
                exit()
            elif evt.type == KEYDOWN: 
                if evt.key == K_ESCAPE:
                    exit()
                if evt.key == K_SPACE:
                    game = True
                    begin = False
        

    


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
#pygame magic
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
screen.fill(BLACK)
pygame.display.set_caption('glax')

#booleans for game functions
game = False #game starts game
won = False #won is if you win, which is currently impossible
begin = True  #begin controls loop for start screen
phase2 = False #controls display of loop saying 'unlimited ammo'
unlimit = -1 #also controls display of 'unlimited ammo'
limitless = False #also for unlimited
pause = False #self explanitory

#make some objects
screen_rect = pygame.Rect((0,0),(600,600)) #objects dealing with window stuff
info_rect = pygame.Rect((600,0),(200,600)) 
bounds = screen_rect  
sidebar_stuff = Group()
writetext = RenderText() #and text stuff

pship_group = Group() #objects dealing with game stuff
ship = PlayerShip() 
enemies = Group()
your_bullets = Group()
enemy_bullets = Group()
explosions = Group()
enemy_missiles = Group()
health = HealthKeeper(screen)
score = ScoreKeeper(screen)

doEvent = GameEvents() #used to control game stuff




#set key repeats for movement
pygame.key.set_repeat(45, 1)

move = 0

######
#game#
######
pygame.draw.rect(screen,BLACK,screen_rect)

writetext.intro_text()

doEvent.make_start_enemies()

while begin:   #loop to start game
    for evt in pygame.event.get():
            if evt.type == QUIT:
                exit()
            elif evt.type == KEYDOWN: 
                if evt.key == K_ESCAPE:
                    exit()
                if evt.key == K_SPACE:
                    game = True
                    begin = False
                
    pygame.display.flip()
    clock.tick(FPS)


#create sidebar stuff
doEvent.draw_sidebar()
sidebar_stuff.draw(screen)
health.draw()
score.draw()


while game: #main game loop
    pygame.draw.rect(screen,BLACK,screen_rect)
    
    #input for exit
    for evt in pygame.event.get():
        if evt.type == QUIT:
            exit()
        elif evt.type == KEYDOWN: 
            if evt.key == K_ESCAPE:
                pygame.key.set_repeat()
                pause = True
            if evt.key == K_SPACE:
                if unlimit == -1:
                    pygame.key.set_repeat(30,10)
                    missle = BulletShoot(ship,your_bullets)
                    pygame.key.set_repeat(45, 1)
                else:
                    missle = BulletShoot(ship,your_bullets)
            if evt.key == K_p:
                print score.score


    #loop for paused game
    while pause:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN and evt.key == K_ESCAPE:
                pygame.key.set_repeat(45, 1)
                pause = False
            if evt.type == QUIT:
                exit()
        clock.tick(FPS)

    #input for game
    pressed = pygame.key.get_pressed()
    if pressed[K_LEFT]:
        ship.update(-8,0)
    if pressed[K_RIGHT]:
        ship.update(8,0)
    if pressed[K_UP]:
        ship.update(0,-8)
    if pressed[K_DOWN]:
        ship.update(0,8)
 

    #update wasp baddies
    if move < 2:
        move += 1
    else:
        enemies.update()
        move = 0
    
    #update bullets
    for i in your_bullets:
        i.fire(1)
    your_bullets.draw(screen)

    for enemy in pygame.sprite.groupcollide(enemies, your_bullets, False, True):
        enemy.hurt(1)
            
    for i in enemy_bullets:
        i.fire(-1)
    enemy_bullets.draw(screen)

    if len(enemies) < 5 and unlimit == -1:
        length = len(enemies)
        if length == 4:
            ayn = 158
        elif length == 3:
            ayn = 80
        elif length == 2:
            ayn = 40
        else:
            ayn = 16
        for enemy in enemies:
            i = random.randrange(ayn)
            if i == 0:
                MissleShoot(enemy, enemy_missiles)
                
                
    if len(enemy_missiles) > 0:
        for player in pygame.sprite.groupcollide(pship_group,enemy_missiles, False, True):
            player.hurt(3)
        enemy_missiles.update(-1)
        enemy_missiles.draw(screen)
    

    #collide functions for player, bullets, stuff...
    for player in pygame.sprite.groupcollide(pship_group,enemy_bullets, False, True):
        player.hurt(1)
    for player in pygame.sprite.groupcollide(pship_group,enemies, False, False):
        player.hurt(17)

    
    #update explosions
    for i in explosions:
        i.update()
        i.draw(screen)

      
#spawn new enemies all the first stage ones are killed or all the 2nd stage ones
    if len(enemies) == 0:
        x = 0
        y = -30
        unlimit = 1
        for i in range(6):
            Aliens(x, y, 0, enemies)
            x += 90
            

    if len(pship_group) == 0:
        health.update(150)
        health.draw()
        game = False


    #draw updates
    pship_group.draw(screen)
    enemies.draw(screen)



    #shows the unlimited ammo warning if unlocked
    if unlimit < 100 and unlimit > 0 and limitless == False:
        text_render("Unlimited Ammo: Just Hold Space!",15,570,WHITE,19)
        unlimit += 1
    elif unlimit >= 100 and limitless == False:
        limitless = True
        


    #update the screen
    pygame.display.flip()
    clock.tick(FPS)


#//END OF GAME LOOP
finalbomb = EnemyExplosion((325,325),30)
while finalbomb.expandto > finalbomb.radius:
    finalbomb.update() 
    finalbomb.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
    

pygame.draw.rect(screen,WHITE,((70,170),(660,230)))

if not won:
    text_render('Game Over',110,240,BLACK,150)
else:
    text_render('You Win!',170,240,BLACK,150)

while not game:
    
    for evt in pygame.event.get():
        if evt.type == QUIT:
            exit()
        elif evt.type == KEYDOWN: 
            if evt.key == K_ESCAPE:
                exit()
    


    pygame.display.flip()
    clock.tick(FPS)

