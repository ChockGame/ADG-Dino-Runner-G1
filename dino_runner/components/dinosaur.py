from email import message
import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING, DUCKING_SHIELD, JUMPING, JUMPING_SHIELD, RUNNING, RUNNING_SHIELD, SHIELD_TYPE

DINO_RUNNING = "running"
DINO_JUMPING = "jumping"
DINO_DUCKING = "duck"

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}

class Dinosaur(Sprite):
    POTITION_X = 80
    POTITION_Y = 310
    POTITION_Y_DINO_DUCK = 330      #POSICION EN EL CUALES LOS PIXELES CAMBIAN AL AGACHARSE *( ( - ) = +   /  ( + ) = - )*
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.power_up_time_up = 0
        self.update_image(RUN_IMG[self.type][0])

        self.action = DINO_RUNNING
        self.jump_velocity = self.JUMP_VELOCITY
        self.step = 0

#        if self.dino_duck:
#            self.duck()
#        if self.dino_run:
#            self.run()
#        if self.dino_jump:
#            self.jump()

#        if self.step >= 10:
#            self.step = 0

#        if user_input[pygame.K_UP] and not self.dino_jump:
#           self.dino_duck = False
#           self.dino_run = False 
#           self.dino_jump = True
#        if user_input[pygame.K_DOWN] and not self.dino_jump:
#            self.dino_duck = True
#            self.dino_run = False 
#            self.dino_jump = False
#        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
#            self.dino_duck = False
#            self.dino_run = True
#            self.dino_jump = False
        
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
        self.update_image(DUCK_IMG[self.type][self.step // 5], pos_y=self.POTITION_Y_DINO_DUCK) 
        self.step += 1

    def jump(self):
       pos_y = self.rect.y - self.jump_velocity * 4
       self.update_image(JUMP_IMG[self.type], pos_y=pos_y)
       self.jump_velocity -= 0.8
       if self.jump_velocity < -self.JUMP_VELOCITY:
           self.jump_velocity = self.JUMP_VELOCITY
           self.action = DINO_RUNNING
           self.rect.y = self.POTITION_Y

    def run(self):
        self.update_image(RUN_IMG[self.type][self.step // 5]) 
        self.step += 1

    def update_image(self, image: pygame.surface, pos_x=None, pos_y=None):
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = pos_x or self.POTITION_X
        self.rect.y = pos_y or self.POTITION_Y

    def draw(self, screen):
        screen.blit(self.image, (self.POTITION_X, self.POTITION_Y))

    def one_pick_power_up(self, power_up):
        self.type = power_up.type
        self.power_up_time_up = power_up.start_time + (power_up.duration * 1000) 

    def check_power_up(self, screen):
        if self.type == SHIELD_TYPE:
            time_to_show = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                message(f"{self.type.capitalize()} anable for {time_to_show} seconds", screen, font_size=18, pos_y_center=50)
            else:
                self.type = DEFAULT_TYPE
                self.power_up_time_up = 0
                


