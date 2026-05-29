import pygame

import constants
import state
import init
import assets


def draw_frame():
    if state.is_playing:
        draw_game()
    else:
        draw_menu()

    pygame.display.flip()
    init.clock.tick(constants.FPS_LIMIT)


def draw_game():
    init.screen.blit(assets.SKY_SURF, (0, 0))
    init.screen.blit(assets.GROUND_SURF, (0, constants.GROUND_Y))
    pygame.draw.rect(init.screen, "#c0e8ec", assets.score_rect)
    pygame.draw.rect(init.screen, "#c0e8ec", assets.score_rect, 10)
    init.screen.blit(assets.score_surf, assets.score_rect)
    for obstacle in state.obsticle_rect_list:
        init.screen.blit(assets.egg_surf, obstacle)
    init.screen.blit(assets.player_surf, assets.player_rect)


def draw_menu():
    init.screen.fill(assets.MENU_BG_COLOR)
    init.screen.blit(assets.menu_player_surf, assets.menu_player_rect)
    init.screen.blit(assets.title_surf, assets.title_rect)

    if state.current_score == 0:
        init.screen.blit(assets.start_msg_surf, assets.start_msg_rect)
    else:
        score_msg_surf = assets.game_font.render(
            f"Your score: {state.current_score:.0f}", False, assets.MENU_TEXT_COLOR
        )
        score_msg_rect = score_msg_surf.get_rect(
            center=(constants.DISPLAY_WIDTH / 2, 330)
        )
        init.screen.blit(score_msg_surf, score_msg_rect)
