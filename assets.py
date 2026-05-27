import pygame

import constants

SKY_SURF = pygame.image.load("graphics/level/sky.png").convert()
GROUND_SURF = pygame.image.load("graphics/level/ground.png").convert()
game_font = pygame.font.Font(pygame.font.get_default_font(), 50)
score_surf = game_font.render("SCORE?", False, "Black")
score_rect = score_surf.get_rect(center=(400, 50))

player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(bottomleft=(25, constants.GROUND_Y))
egg_surf = pygame.image.load("graphics/egg/egg_1.png").convert_alpha()
# egg_rect = egg_surf.get_rect(bottomleft=(800, constants.GROUND_Y))

obsticle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obsticle_timer, constants.OBSTACLE_SPAWN_RATE)
