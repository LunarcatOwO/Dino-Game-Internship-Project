if __name__ == "__main__":
    raise RuntimeError(f"The {__file__.split('\\')[-1][:-3]} module should not be run on its own. Please run main.py instead")

import constants
import state
import functions.assets as assets


def update_egg():
    assets.egg_rect.x -= 5
    if assets.egg_rect.right <= 0:
        assets.egg_rect.left = 800


def update_player():
    state.players_gravity_speed -= 1
    assets.player_rect.y -= state.players_gravity_speed
    if assets.player_rect.bottom > constants.GROUND_Y:
        assets.player_rect.bottom = constants.GROUND_Y


def check_collision():
    return assets.egg_rect.colliderect(assets.player_rect)
