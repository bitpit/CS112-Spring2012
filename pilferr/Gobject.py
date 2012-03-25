#!/usr/bin/env python

import random
import pygame
from pygame.locals import *
from pygame.sprite import Sprite, Group, RenderUpdates
import os, sys
from random import randrange, choice



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

class Title(Sprite):
    image = None
    def __init__(self,x,y,surf):
        Sprite.__init__(self)
        if self.image is None:
            self.image = load_graphics('logo.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.surface = surf
    def draw(self):
        self.surface.blit(self.image, (self.rect.x,self.rect.y))

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
    def hurt(self, loss):
        if self.health - loss <= 0:
            self.kill()
            return True
        else:
            self.health -= loss
            return False


class Wasp(Person):
    image1 = None
    image2 = None
    image_hurt = None
    def __init__(self, x, y, status, group, sprite="wasp_baddie.png"):
        Person.__init__(self, x, y, status, group, sprite)
        self.direction = 1
        self.newy = self.rect.y+90
        self.health = 5
        self.health_compare = self.health
        self.frame_update = 0
        self.frame = 0
        if self.image1 is None:
            self.image1 = self.image
        if self.image2 is None:
            self.image2 = load_graphics('wasp_baddie_2.png')
        if self.image_hurt is None:
            self.image_hurt = load_graphics('wasp_shoot.png')
    
    def update(self):
        if self.should_update == 2: #gives it that nice old arcade slowness
            self.animate()
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
        elif 20 < (self.rect.x+(self.speed*self.direction)) < 540:
            return ((self.speed*self.direction),0)
        elif self.rect.y < self.newy:
            return (0,25)
        elif self.rect.y == 600:
            self.kill()
            return ((0,0))
        else:
            if self.rect.y < 190:
                Wasp(-15,50,0,self.group)
            self.direction *= -1
            self.newy += 90
            return ((0,0))
    
    def get_status(self):
        if self.status == 0 and self.rect.x >= 60:
            self.status = 1
    
    def animate(self):
        if self.frame_update < 2:
            self.frame_update += 1
        elif self.frame_update == 3:
            self.frame = 1
            self.frame_update += 1
        elif self.frame_update < 6:
            self.frame_update += 1
        else:
            self.frame = 0
            self.frame_update = 0
        if self.health_compare > self.health:
            self.image = self.image_hurt
            #while self.health_compare > self.health:
            self.health_compare -= 1
        elif self.frame == 0:
            self.image = self.image1
        elif self.frame == 1:
            self.image = self.image2


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
    hurting = None
    def __init__(self, x, y, status, group, sprite="player_ship.png"):
        Person.__init__(self, x, y, status, group, sprite)
        self.health = 50
        self.health_update = self.health*4
        self.healthy = self.image
        if self.hurting is None:
            self.hurting = load_graphics('player_shoot.png')
    
    def update(self, dx, dy):
        self.animate()
        if dx > 0 and self.rect.x+dx < 600-self.rect.w:
            self.rect.x += dx
        if dx < 0 and self.rect.x+dx > 0:
            self.rect.x += dx
        if dy > 0 and self.rect.y+dy<600-self.rect.h:
            self.rect.y += dy 
        if dy < 0 and self.rect.y+dy>0:
            self.rect.y += dy 
    
    def animate(self):
        if self.health_update > self.health*4:
            self.image = self.hurting
            self.health_update -= 1
        else:
            self.image = self.healthy


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
    if ayn == 1:
        rare = 6
    else:
        rare = 2
    if length > 5 or length == 5:
        ayn *= 16
    elif length == 4:
        ayn *= 16
    elif length == 3:
        ayn *= 13
    elif length == 2:
        ayn *= 2*rare
    else:
        ayn *= rare
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




class Star(object):
    #uses ideas from method found at http://tinyurl.com/6snf424
    def __init__(self,screen,screenw,screenh,max_stars):
        self.stars = []
        self.screen = screen
        self.height = screenh
        self.width = screenw
        self.max_stars = max_stars
        for i in range(self.max_stars):
            star = [randrange(0,self.width-1),randrange(0,self.height-1),choice([1,2,3])]
            if star[2] == 1:
                star.append((170,170,170))
            elif star[2] == 2:
                star.append((210,210,210))
            else:
                star.append((255,255,255))
            self.stars.append(star)
    
    def update(self):
        for star in self.stars:
            star[1] += star[2]
            if star[1] >= self.height:
                star[1] = 0
                star[0] = randrange(0,self.width)
                star[2] = choice([1,2,3])
    
    def draw(self):
        for star in self.stars:
            self.screen.fill(star[3],(star[0],star[1],star[2],star[2]))            





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
        self.game1 = False
        self.game2 = False
        self.gameover = True
        self.sidebar = True
        self.start_screen = True
        self.start_render = True
        self.fps = 30

        group = pygame.sprite.Group()
        self.screen_rect = pygame.Rect((0,0),(600,600))
       
        self.score = ScoreKeeper(self.screen)
        self.player = pygame.sprite.Group()
        self.ship = PlayerShip(260, 500, 0, self.player)
        self.player_health = HealthKeeper(self.screen)
        self.enemies = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.sidebar_stuff = pygame.sprite.Group()

        self.stars = Star(self.screen,600,600,200)
        self.unlimited_ammo = 0

        self.black = ((0,0,0))

        self.make = Make(self.screen, (255,255,255),self.black, self.sidebar_stuff,self.score)
      
    def pause(self, boolean):
        if boolean:
            self.paused = True
        else:
            self.paused = False
            pygame.key.set_repeat(45,1)
                                

    def quit(self):
        self.done = True


    def start_step(self):
        self.clock.tick(self.fps)

        if self.start_render:
            self.tittle = Title(100,50,self.screen)
            self.tittle.draw()
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
                    self.game1 = True

        pygame.display.flip()
        
        
    
    def game_step_1(self):
        self.clock.tick(self.fps)

        #checks to see if all enemies are dead and if so advances player to
        #stage 2
        if len(self.enemies) == 0:
            self.game2 = True
            self.game1 = False

        if self.sidebar:
            self.make.game_screen()
            self.sidebar_stuff.draw(self.screen)
            self.sidebar = False

        #bombs
        if len(self.enemies) < 5:
            for sprite in self.enemies:
                shouldbomb = complex_bullet_algorithm(self.enemies, 10)
                if shouldbomb:
                    EnemyBullets(sprite, self.enemy_bullets, 16, ('baddie_missile.png'))
                
            
        
        #get events
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

            #fill screen with blackness
            pygame.draw.rect(self.screen,self.black,self.screen_rect)

            #do starz
            self.stars.update()    
            self.stars.draw()
  
            self.enemies.update()

            #check collosion of self and enemies
            for player in pygame.sprite.groupcollide(self.player, self.enemies, False, False):
                over = player.hurt(17)
                self.player_health.update(17)
                if over:
                    self.game1 = False

            #check collosion of player bullets/update/draw player bullets 
            if len(self.player_bullets) > 0:
                for enemy in pygame.sprite.groupcollide(self.enemies, self.player_bullets, False, True):
                    explode = enemy.hurt(1)
                    if explode:
                        self.score.update(300)
                        self.score.draw()
                        EnemyExplosion((enemy.rect.x+3,enemy.rect.y+15),self.explosions, 5)
                self.player_bullets.update()
                self.player_bullets.draw(self.screen)

            #update/draw explosions if they exist
            if len(self.explosions) > 0:
                self.explosions.update()
                for i in self.explosions:
                    i.draw(self.screen)

            #update/draw enemy bombs/check for collision if they exist
            if len(self.enemy_bullets) > 0:
                for bullets in pygame.sprite.groupcollide(self.enemy_bullets, self.player, True, False):
                    over = self.ship.hurt(2)
                    self.player_health.update(2)
                    if over:
                        self.game1 = False
                self.enemy_bullets.update(9)
                self.enemy_bullets.draw(self.screen)
                            
                                    
            #draw the rest of the stuff
            self.player.draw(self.screen)
            self.enemies.draw(self.screen)
            self.player_health.draw()
                        
        pygame.display.flip()

    def game_step_2(self):
        self.clock.tick(self.fps)

        #keep givin em enemies
        if len(self.enemies) == 0:
            x = 0
            y = -30
            for i in range(6):
                Aliens(x, y, 0, self.enemies)
                x += 90
                
        #get events
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
                if evt.key == K_p:
                    print self.enemy_bullets.sprites()

        
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
            if pressed[K_SPACE]:
                Bullet(self.ship, self.player_bullets, 1)

            #fill screen with blackness
            pygame.draw.rect(self.screen,self.black,self.screen_rect)
            
            #do starz
            self.stars.update()    
            self.stars.draw()
  
            #show text maybe?
            if self.unlimited_ammo < 130:
                text_render("Unlimited Ammo: Just Hold Space!",15,570,(255,255,255),19,self.screen)
                self.unlimited_ammo += 1

            #update enemies/generate bullets
            for sprite in self.enemies:
                if complex_bullet_algorithm(self.enemies, 1):
                    EnemyBullets(sprite, self.enemy_bullets, 16)
            self.enemies.update()
            
            #update/draw/do collosions for enemy bullets if there are any
            if len(self.enemy_bullets) > 0:
                self.enemy_bullets.update(9)#speed
                self.enemy_bullets.draw(self.screen)
                for player in pygame.sprite.groupcollide(self.player,self.enemy_bullets, False, True):
                    over = player.hurt(2)
                    self.player_health.update(2)
                    if over:
                        self.game2 = False
            
            #update/draw explosions if they exist
            if len(self.explosions) > 0:
                self.explosions.update()
                for i in self.explosions:
                    i.draw(self.screen)

            #update/draw/check collision for player bullets if they exist
            if len(self.player_bullets) > 0:
                for enemy in pygame.sprite.groupcollide(self.enemies, self.player_bullets, False, True):
                    explode = enemy.hurt(1)
                    if explode:
                        self.score.update(600)
                        self.score.draw()
                        EnemyExplosion((enemy.rect.x+3,enemy.rect.y+15),self.explosions, 5)
                self.player_bullets.update()
                self.player_bullets.draw(self.screen)


            #check collisions for enemies and player
            for player in pygame.sprite.groupcollide(self.player, self.enemies, False, False):
                over = player.hurt(17)
                self.player_health.update(17)
                if over:
                    self.game2 = False
      

            #draw the rest of the stuff
            self.player.draw(self.screen)
            self.enemies.draw(self.screen)
            self.player_health.draw()

        pygame.display.flip()


    def game_over(self):
        self.clock.tick (self.fps)
        if self.gameover:
            pygame.draw.rect(self.screen,(255,255,255),((70,170),(660,230)))
            text_render('High Score!',110,230,self.black,150,self.screen)
            text_render('Press r to return to title or q to quit', 126,340,self.black,40,self.screen)
            self.gameover = False

        for evt in pygame.event.get():
            if evt.type == QUIT:
                self.quit()
            if evt.type == KEYDOWN:
                if evt.key == K_ESCAPE:
                    self.start_screen = True
                elif evt.key == K_q:
                    self.quit()
                elif evt.key == K_r:
                    self.__init__()
            

        pygame.display.flip()

    def run(self):
        self.done = False
        self.clock = pygame.time.Clock()
        while not self.done:
            if self.game1:
                self.game_step_1()
            elif self.game2:
                self.game_step_2()
            elif self.start_screen:
                self.start_step()
            else:
                self.game_over()


Game().run()

