import pygame

import constants

SKY_SURF = pygame.image.load("graphics/level/sky.png").convert()
GROUND_SURF = pygame.image.load("graphics/level/ground.png").convert()
game_font = pygame.font.Font(pygame.font.get_default_font(), 50)
score_surf = game_font.render("SCORE?", False, "Black")
score_rect = score_surf.get_rect(center=(400, 50))

player_walk = [
    pygame.image.load("graphics/player/player_walk_1.png").convert_alpha(),
    pygame.image.load("graphics/player/player_walk_2.png").convert_alpha(),
]
player_jump = pygame.image.load("graphics/player/player_jump.png").convert_alpha()
player_surf = player_walk[0]
player_rect = player_surf.get_rect(bottomleft=(25, constants.GROUND_Y))

egg_frames = [
    pygame.image.load("graphics/egg/egg_1.png").convert_alpha(),
    pygame.image.load("graphics/egg/egg_2.png").convert_alpha(),
]
egg_surf = egg_frames[0]
# egg_rect = egg_surf.get_rect(bottomleft=(800, constants.GROUND_Y))

# Menu / transition screens
MENU_BG_COLOR = (94, 129, 162)
MENU_TEXT_COLOR = "#c0e8ec"

title_surf = game_font.render("Dino Game", False, MENU_TEXT_COLOR)
title_rect = title_surf.get_rect(center=(constants.DISPLAY_WIDTH / 2, 80))

start_msg_surf = game_font.render("Press SPACE to start", False, MENU_TEXT_COLOR)
start_msg_rect = start_msg_surf.get_rect(center=(constants.DISPLAY_WIDTH / 2, 330))

menu_player_surf = pygame.transform.rotozoom(player_walk[0], 0, 2)
menu_player_rect = menu_player_surf.get_rect(
    center=(constants.DISPLAY_WIDTH / 2, constants.DISPLAY_HEIGHT / 2)
)

obsticle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obsticle_timer, constants.OBSTACLE_SPAWN_RATE)
