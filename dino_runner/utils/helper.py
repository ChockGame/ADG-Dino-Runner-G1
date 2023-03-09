import pygame
from dino_runner.utils.constants import FONT_STYLE

def message(message, width_position, height_position,screen):
    font = pygame.font.Font(FONT_STYLE, 32)
    text = font.render(message, True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (width_position, height_position)
    screen.blit(text, text_rect)
