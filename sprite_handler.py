import constants
import state
import assets


def update():
    update_egg()
    update_player()


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
