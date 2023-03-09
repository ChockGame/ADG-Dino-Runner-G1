import random
from dino_runner.components.obstacles.obstacles import obstacles

from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class cactus(obstacles):
    def __init__(self):
        CACTUS_IMG = SMALL_CACTUS + LARGE_CACTUS
        cactus_type = random.randint(0, len(CACTUS_IMG)-1)
        image = CACTUS_IMG[cactus_type]
        super().__init__(image)
        if cactus_type > 2:
            self.rect.y = 300                       #**** ( ( - )--- ( - )*( - ) =  +   /   ( + )---- ( + )*( - ) =  - )**** AL PONER MAS ES HACIA LO NEGATIVO  SI PONEMOS MENOS ES HACIA ARRIBA (CUADRO DE CORDENADAS)
        else:
            self.rect.x = 325
