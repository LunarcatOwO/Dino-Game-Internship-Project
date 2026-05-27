import pygame

import constants
import state
import init
import assets


def draw_frame():
    if state.is_playing:
        init.screen.fill("purple")
        init.screen.blit(assets.SKY_SURF, (0, 0))
        init.screen.blit(assets.GROUND_SURF, (0, constants.GROUND_Y))
        pygame.draw.rect(init.screen, "#c0e8ec", assets.score_rect)
        pygame.draw.rect(init.screen, "#c0e8ec", assets.score_rect, 10)
        init.screen.blit(assets.score_surf, assets.score_rect)
        for obstacle in state.obsticle_rect_list:
            init.screen.blit(assets.egg_surf, obstacle)
        init.screen.blit(assets.player_surf, assets.player_rect)
    else:
        init.screen.fill("black")
        init.screen.blit(assets.score_surf, assets.score_rect)

    pygame.display.flip()
    init.clock.tick(constants.FPS_LIMIT)
