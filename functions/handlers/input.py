if __name__ == "__main__":
    raise RuntimeError(f"The {__file__.split('\\')[-1][:-3]} module should not be run on its own. Please run main.py instead")

import pygame

import constants
import state
import functions.assets as assets


def handle(event):
    if event.type == pygame.QUIT:
        state.running = False
    elif state.is_playing:
        if (
            event.type == pygame.KEYDOWN
            and event.key == pygame.K_SPACE
            or event.type == pygame.MOUSEBUTTONDOWN
            
        ) and assets.player_rect.bottom >= constants.GROUND_Y:
            state.players_gravity_speed = constants.JUMP_GRAVITY_START_SPEED
    else:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            state.is_playing = True
            assets.egg_rect.left = 800
            state.start_time = pygame.time.get_ticks()
            constants.FPS_LIMIT = 60
