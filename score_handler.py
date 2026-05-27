import pygame

import constants
import state
import assets


def update_score():
    state.current_score = (pygame.time.get_ticks() - state.start_time) / constants.SCORE_DIVIDER
    assets.score_surf = assets.game_font.render(f"SCORE: {state.current_score:.0f}", False, "Black")
    assets.score_rect = assets.score_surf.get_rect(center=(400, 50))
    constants.FPS_LIMIT = 60 + int(state.current_score / 100) * constants.SCORE_FPS_INCREASE_RATE


def store_score():
    with open("score.txt", "w") as file:
        file.write(str(state.current_score))
