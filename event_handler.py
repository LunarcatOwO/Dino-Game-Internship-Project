import random

import pygame

import constants
import state
import assets


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state.running = False
        elif state.is_playing:
            if (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
                or event.type == pygame.MOUSEBUTTONDOWN
            ) and assets.player_rect.bottom >= constants.GROUND_Y:
                state.players_gravity_speed = constants.JUMP_GRAVITY_START_SPEED
            if event.type == assets.obsticle_timer and state.is_playing:
                state.obsticle_rect_list.append(assets.egg_surf.get_rect(bottomleft=(random.randint(900,1100), constants.GROUND_Y)))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                state.is_playing = True
                state.obsticle_rect_list = []
                state.start_time = pygame.time.get_ticks()
                state.players_gravity_speed = 0
                assets.player_rect.bottomleft = (25, constants.GROUND_Y)
