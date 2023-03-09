import random
import pygame
from dino_runner.components.obstacles.cactus import cactus
from dino_runner.components.obstacles.bird import bird
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager():
    def __init__(self):
        self.obstacles = []
        self.extra_point = 0
    def update(self, game_speed, player, on_death,screen):
        if not len(self.obstacles):
            cac = random.randint(0, 2)
            if cac == 0:
                self.obstacles.append(cactus())
            elif cac == 1:
                self.obstacles.append(cactus())
            elif cac == 2:
                self.obstacles.append(bird())
        for obstacle in self.obstacles:
                obstacle.update(game_speed, self.obstacles)
                if player.rect.colliderect(obstacle.rect):#CUANDO TE CHOCAS
               
                    if player.hammer_status == True:
                        if(obstacle == bird()):
                            print("bird")
                            self.obstacles.remove(obstacle)
                            player.lifes.heart_list.pop()
                        else:
                            player.extra_point += 100                            
                            self.obstacles.remove(obstacle)
                    if player.shield_status == False and player.hammer_status == False:
                        self.obstacles.remove(obstacle)
                        player.lifes.heart_list.pop()#LISTA DE VIDAS LE QUITAS UNA VIDA EL POP ELIMINA DE LA LISTA UNA VALOR LA ULTIMA
                        #QUE PASA SI TIENES LONGITUD 0
                        #   not        0 = false = true
                        if(not len(player.lifes.heart_list)):
                            on_death()                




    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset(self):
        self.obstacles = []