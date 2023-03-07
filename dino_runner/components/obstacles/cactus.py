import random
from dino_runner.components import obstacles

from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS


class Cactus(obstacles):
    def __init__(self):
        cactus_type = random.randint(0, 2)
        image = SMALL_CACTUS[cactus_type]
        super().__init__(image)
        self.rect.y = 325
    
    def ___init__(self):
        cactus_type = random.randint(0, 2)
        image = LARGE_CACTUS[cactus_type]
        super().__init__(image)
        self.rect.y = 300               #**** ( ( - )--- ( - )*( - ) =  +   /   ( + )---- ( + )*( - ) =  - )**** AL PONER MAS ES HACIA LO NEGATIVO  SI PONEMOS MENOS ES HACIA ARRIBA (CUADRO DE CORDENADAS)

class bird(obstacles):
    def __init__(self):
        bird_type = 0
        image = BIRD(bird_type)
        super().__init__(image)
        self.rect.y = 250               #**** ( ( - )--- ( - )*( - ) =  +   /   ( + )---- ( + )*( - ) =  - )**** AL PONER MAS ES HACIA LO NEGATIVO  SI PONEMOS MENOS ES HACIA ARRIBA (CUADRO DE CORDENADAS)
        self.step = 0
    
    def draw(self, screen):
        if self.step >= 9:      #**** 4 pixeles por segundo es decir ( 0 - 4 ) una accion "bird/.imag1" de ( 5 - 9 ) otra accion "bird/.imag2" ( 10 ) reinicio del bluqe para bird
            self.step = 0        #**** rinicion del blue bird
        screen.blit(self.image, [self.step // 5], self.rect)
        self.step += 1

       