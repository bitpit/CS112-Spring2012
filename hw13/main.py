#!/usr/bin/env python

import random
import pygame
from pygame.locals import *
from pygame.sprite import Sprite, Group, RenderUpdates
import os, sys
from objectg import *



class Game(object):
    title = 'Gobject'
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
                if self.paused and evt.key == K_q:
                    self.quit()
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
        
        else:
            pygame.draw.rect(self.screen,(255,255,255),((10,170),(580,230)))
            text_render('Paused',80,230,self.black,90,self.screen)
            text_render('press esc to resume or q to quit', 126,310,self.black,40,self.screen)
                        
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
                if self.paused and evt.key == K_q:
                    self.quit()
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

        else:
            pygame.draw.rect(self.screen,(255,255,255),((10,170),(580,230)))
            text_render('Paused',80,230,self.black,90,self.screen)
            text_render('press esc to resume or q to quit', 126,310,self.black,40,self.screen)

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

