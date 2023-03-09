import random
import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.cloud import Draw_Cloud
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.score import Score


from dino_runner.utils.constants import BG, CLOUD, DINO_START, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.cloud = Draw_Cloud()
        self.player = Dinosaur()
        self.obstacle_manage = ObstacleManager()
        self.score = Score()
        self.death_count = 0
        self.power_up_manger = PowerUpManager()
        self.power_up_manger.reset()


    def run(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
            
        pygame.quit()

    def start_game(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manage.reset()
        self.player.lifes.reset_heart(3)
        self.score.score = 0
        self.player.extra_point = 0
        self.game_speed = 20 #REINICIO DE LA VELOCIDAD DEL JUEGO
        #self.score.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.cloud.update(self.game_speed)
        self.obstacle_manage.update(self.game_speed, self.player, self.on_death,self.screen)
        self.score.update(self,self.player.extra_point)
        self.power_up_manger.update(self.game_speed, self.score.score,self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.cloud.draw(self.screen)
        self.obstacle_manage.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_manger.draw(self.screen)
        self.player.check_power_up(self.screen,self.score.score)
        # pygame.display.update()
        pygame.display.flip()
        
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.fill((0, 255, 0))
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def on_death(self):
        is_invincible = self.player.type == SHIELD_TYPE
        if not is_invincible:
            self.playing = False
            self.death_count += 1

    """def Draw_Cloud(self):
       image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_clo, self.y_pos_clo))
        self.screen.blit(CLOUD, (image_width + self.x_pos_clo, self.y_pos_clo))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos_clo, self.y_pos_clo))
            self.x_pos_clo = 0
        self.x_pos_clo -= self.game_speed"""
    


    def show_menu(self):
        # Rellenar de color blanco la pantalla
        self.screen.fill((255, 255, 255))
        #  Poner un mensaje de bienvenida
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        if not self.death_count:
            self.screen.fill((0,0,255))
            font = pygame.font.Font(FONT_STYLE, 32)
            text = font.render("Welcome, press any key to start!", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)
        #   tarea mostrar un mesaje para que se reinicie el juego ---- mostrar cuantas veces se a muerto------ mostrar el mensaje que se ha obtenido en la ejecusion

        else:
            self.screen.fill((255,0,0))
            self.message("RESTAR GAME", half_screen_width, half_screen_height)
            self.message(f"Death: {self.death_count}", half_screen_width, half_screen_height + 50)
            self.message(f"Score: {self.score.score}", half_screen_width, half_screen_height + 100)
            



        # Poner una imagen a modo de icino en el centro
        self.screen.blit(DINO_START, (half_screen_width - 40, half_screen_height - 140))
        # Plasmar los cambios
        pygame.display.update()
        # Manejar eventos
        self.handle_menu_events()

    def message(self, message, width_position, height_position):
        font = pygame.font.Font(FONT_STYLE, 32)
        text = font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (width_position, height_position)
        self.screen.blit(text, text_rect)

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

            if event.type == pygame.KEYDOWN:
                self.start_game()