import random
from dino_runner.utils.constants import *

class Draw_Cloud:
    def __init__(self):
        self.pos_x = SCREEN_WIDTH
        self.pos_y = 50
        self.image = CLOUD
        self.width = self.image.get_width()
        
     
    def update(self,game_speed):
        self.pos_x -= game_speed - 3
        if self.pos_x < -self.width:
            self.pos_x = SCREEN_WIDTH

    def draw(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))