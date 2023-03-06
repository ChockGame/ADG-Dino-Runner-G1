import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import JUMPING, RUNNING


DINO_RUNNING = "running"
DINO_JUMPING = "jumping"
DINO_DUCKING = "duck"


class Dinosaur(Sprite):
    POTITION_X = 80
    POTITION_Y = 310
    JUMP_VELOCITY = 8.5
    DUCK_VELOCITY = 8.5

    def _init_(self):
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POTITION_X
        self.rect.y = self.POTITION_Y
        self.action = DINO_RUNNING
        self.jump_velocity = self.JUMP_VELOCITY
        self.duck_velocity = self.DUCK_VELOCITY
        self.step = 0
        
    def update(self, user_input):
        if self.action == DINO_RUNNING:
            self.run()
        elif self.action == DINO_JUMPING:
            self.jump()

        if self.action == DINO_RUNNING:
            self.run()
        elif  self.action == DINO_DUCKING:
            self.duck()
        
        if self.action != DINO_JUMPING:
            if user_input[pygame.K_UP]:
                self.action = DINO_JUMPING
            else:
                self.action = DINO_RUNNING

        if self.action != DINO_DUCKING:
            if user_input[pygame.K_DOWN]:
                self.action = DINO_DUCKING
            else:
                self.action = DINO_RUNNING

        if self.step >= 10:
            self.step = 0
            pass

    def jump(self):
        self.image = JUMPING
        self.rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        print("VELOCITY", self.jump_velocity)
        print("Y ::", self.rect.y)
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.jump_velocity = self.JUMP_VELOCITY
            self.action = DINO_RUNNING
            self.rect.y = self.POTITION_Y

    def duck(self):
        self.image = DUCKING
        self.rect.y += self.duck_velocity * 4
        self.duck_velocity -= 0.8
        print("VELOCITY", self.duck_velocity)
        print("Y ::", self.rect.y)
        if self.duck_velocity < +self.DUCK_VELOCITY:
            self.duck_velocity = self.DUCK_VELOCITY
            self.action = DINO_RUNNING
            self.rect.y = self.POTITION_Y

    def run(self):
        self.image = RUNNING[self.step // 5] 
        self.rect =  self.image.get_rect()
        self.rect.x = self.POTITION_X
        self.rect.y = self.POTITION_Y
        self.step += 1

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


        

