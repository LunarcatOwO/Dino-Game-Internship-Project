import pygame

import constants

pygame.init()
pygame.display.set_caption("Dino Game")
screen = pygame.display.set_mode((constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT))
clock = pygame.time.Clock()


def quit_game():
    pygame.quit()
