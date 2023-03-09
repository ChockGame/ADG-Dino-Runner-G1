from dino_runner.utils.constants import HEART

class Heart:
    def __init__(self,number_life):
        self.image = HEART
        self.heart_list = [x for x in range(1,number_life+1)] 
        self.width = self.image.get_width()
    
    def draw(self, screen):
        for heart in self.heart_list:
                                    # X         Y
            screen.blit(self.image, (30+(heart*30),30)) #DIBUJAR LOS CORAZON DE 30 DE SEPARACION
    def reset_heart(self,number_life):
        self.heart_list = [x for x in range(1,number_life+1)] 