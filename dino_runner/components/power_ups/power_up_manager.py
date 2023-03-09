import random

import pygame
from dino_runner.utils.constants import HAMMER_TYPE, SHIELD_TYPE
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.utils.helper import message
class PowerUpManager:
    def __init__(self):
        self.power_ups: list(PowerUp) = []
#  en que puntaje vamos a generar un power up
        self.when_appears = 0
        self.round = 1
    def update(self, game_speed, score, player):
        if not self.power_ups and score == self.when_appears:
            self.when_appears += random.randint(100, 350)
            #intercalar los powerupss
            if self.round % 2 == 0:
                print("Shield")
                self.power_ups.append(Shield())
                self.round +=1
            else:
                self.power_ups.append(Hammer())
                self.round +=1

        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if power_up.rect.colliderect(player.rect):
                if power_up.type == HAMMER_TYPE:
                    player.hammer_status = True
                    power_up.start_time = pygame.time.get_ticks()
                    player.one_pick_power_up(power_up)
                    print("QUITAR POWER UP")
                    self.power_ups.remove(power_up)   
                else:
                    player.shield_status = True
                    power_up.start_time = pygame.time.get_ticks()
                    player.one_pick_power_up(power_up)
                    print("QUITAR POWER UP")
                    self.power_ups.remove(power_up)    
    def draw(self, screen):
         for power_up in self.power_ups:
            power_up.draw(screen)
        
    def reset(self):
        self.power_ups = []
        self.when_appears = random.randint(100, 550)

        