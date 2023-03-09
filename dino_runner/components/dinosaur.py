from dino_runner.components.life.heart import Heart
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING, DUCKING_SHIELD, JUMPING, JUMPING_SHIELD, RUNNING, RUNNING_SHIELD, SHIELD_TYPE,FONT_STYLE,HAMMER_TYPE,DUCKING_HAMMER,JUMPING_HAMMER,RUNNING_HAMMER
from dino_runner.components.score import Score
DINO_RUNNING = "running"
DINO_JUMPING = "jumping"
DINO_DUCKING = "duck"

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD , HAMMER_TYPE:DUCKING_HAMMER }
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}

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
        self.lifes = Heart(3) #TRES CORAZONDES DE VIDA
        self.shield_status = False
        self.hammer_status = False
        self.extra_point = 0
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
        self.POTITION_Y = 340  
        self.update_image(DUCK_IMG[self.type][self.step // 5], pos_y=self.POTITION_Y_DINO_DUCK) 
        self.step += 1

    def jump(self):
       self.POTITION_Y = 310
       pos_y = self.rect.y - self.jump_velocity * 4
       self.POTITION_Y = pos_y
       self.update_image(JUMP_IMG[self.type], pos_y=pos_y)
       self.jump_velocity -= 0.8
       if self.jump_velocity < -self.JUMP_VELOCITY:
           self.jump_velocity = self.JUMP_VELOCITY
           self.action = DINO_RUNNING
           self.rect.y = self.POTITION_Y

    def run(self):
        self.POTITION_Y = 310
        self.update_image(RUN_IMG[self.type][self.step // 5]) 
        self.step += 1

    def update_image(self, image: pygame.surface, pos_x=None, pos_y=None):
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = pos_x or self.POTITION_X
        self.rect.y = pos_y or self.POTITION_Y

    def draw(self, screen):
        self.lifes.draw(screen)
        screen.blit(self.image, (self.POTITION_X, self.POTITION_Y))

    def one_pick_power_up(self, power_up):
        self.type = power_up.type
        self.power_up_time_up = power_up.start_time + (power_up.duration * 1000) 

    def print_message(self, message,screen, width_position, height_position):
        font = pygame.font.Font(FONT_STYLE, 32)
        text = font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (width_position, height_position)
        screen.blit(text, text_rect)

    def check_power_up(self, screen,score):
        #TIPO ESCUDO
        if self.type == SHIELD_TYPE:
            time_to_show = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.print_message(f"{self.type.capitalize()} anable for {time_to_show} seconds",screen, 580, 100)
                if(time_to_show <= 0.5):
                    self.shield_status = False#DESACTIVANDO EL ESCUDO
            else:
                self.type = DEFAULT_TYPE
                self.power_up_time_up = 0
        #TIPO MARTILLO
        elif self.type == HAMMER_TYPE:
            time_to_show = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.print_message(f"{self.type.capitalize()} anable for {time_to_show} seconds",screen, 580, 100)
                self.print_message(f"EXTRA:{self.extra_point}",screen,580,400)
            else:
                self.type = DEFAULT_TYPE
                self.power_up_time_up = 0 
                self.hammer_status = False#DESACTIVANDO EL ESCUDO
                print("AUMENTANDO PUNTOS EXTRA")
                print(score)
                print(self.extra_point)
                score += self.extra_point
                self.extra_point = 0
                 # RESETEAMOS los puntos extra       
    def addPoints(self,score):
        score += self.extra_point
