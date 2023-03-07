import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import DUCKING, JUMPING, RUNNING

DINO_RUNNING = "running"
DINO_JUMPING = "jumping"
DINO_DUCKING = "duck"

class Dinosaur(Sprite):
    POTITION_X = 80
    POTITION_Y = 310
    POTITION_Y_DINO_DUCK = 340      #POSICION EN EL CUALES LOS PIXELES CAMBIAN AL AGACHARSE *( ( - ) = +   /  ( + ) = - )*
    JUMP_VELOCITY = 8.5

    def _init_(self):
        self.update_image(DINO_RUNNING[0])
        self.action = DINO_RUNNING
        self.jump_velocity = self.JUMP_VELOCITY
        self.step = 0

        
        """if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step >= 10:
            self.step = 0
        
         if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False 
            self.dino_jump = True
        if user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False 
            self.dino_jump = False
        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False"""
        
    def update(self,user_input):
        if self.action == DINO_RUNNING:
            self.run()
        elif self.action == DINO_JUMPING:
            self.jump()
        elif  self.action == DINO_DUCKING:
            self.duck()
        
        if self.action != DINO_JUMPING:
            if user_input[pygame.K_UP]:
                self.action = DINO_JUMPING
            elif user_input[pygame.K_DOWN]:
                self.action = DINO_DUCKING
            else:
                self.action = DINO_RUNNING

        if self.step >= 10:
            self.step = 0
            pass

    def duck(self):
        self.image(DUCKING[self.step // 5], pos_y=self.POTITION_Y_DINO_DUCK) 
        self.step += 1

    def jump(self):
       pos_y = self.rect.y - self.jump_velocity * 4
       self.update_image(JUMPING, pos_y=pos_y)
       self.jump_velocity -= 0.8
       if self.jump_velocity < -self.JUMP_VELOCITY:
           self.jump_velocity = self.JUMP_VELOCITY
           self.action = DINO_RUNNING
           self.rect.y = self.POTITION_Y

    def run(self):
        self.image = RUNNING[self.step // 5] 
        self.step += 1

    def update_image(self, image: pygame.surface, pos_x=None, pos_y=None):
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = pos_x or self.POTITION_X
        self.rect.y = pos_y or self.POTITION_Y


    def draw(self, screen):
        screen.blit(self.image, (self.POTITION_X, self.POTITION_Y))
