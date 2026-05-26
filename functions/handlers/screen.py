if __name__ == "__main__":
    raise RuntimeError(f"The {__file__.split('\\')[-1][:-3]} module should not be run on its own. Please run main.py instead")

import pygame

import constants
import state
import functions.init as init
import functions.assets as assets
import functions.handlers.score as score_handler


def update_screen():
    if state.is_playing:
        init.screen.fill("purple")
        init.screen.blit(assets.SKY_SURF, (0, 0))
        init.screen.blit(assets.GROUND_SURF, (0, constants.GROUND_Y))
        pygame.draw.rect(init.screen, "#c0e8ec", assets.score_rect)
        pygame.draw.rect(init.screen, "#c0e8ec", assets.score_rect, 10)
        init.screen.blit(assets.score_surf, assets.score_rect)
        init.screen.blit(assets.egg_surf, assets.egg_rect)
        init.screen.blit(assets.player_surf, assets.player_rect)
    else:
        init.screen.fill("black")
        init.screen.blit(assets.score_surf, assets.score_rect)