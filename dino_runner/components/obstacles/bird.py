from dino_runner.components.obstacles.obstacles import obstacles
from dino_runner.utils.constants import BIRD
import random

class bird(obstacles):
    def __init__(self):
        self.step = 0
        image = BIRD[0]
        super().__init__(image)
        self.rect.y = random.randint(220, 300)               #**** ( ( - )--- ( - )*( - ) =  +   /   ( + )---- ( + )*( - ) =  - )**** AL PONER MAS ES HACIA LO NEGATIVO  SI PONEMOS MENOS ES HACIA ARRIBA (CUADRO DE CORDENADAS)
        self.step = 0
    
    def update(self, game_speed, obstacle):
        super().update(game_speed, obstacle)
        self.image =BIRD[self.step // 5]
        self.step += 1
        if self.step >= 10:
            self.step = 0