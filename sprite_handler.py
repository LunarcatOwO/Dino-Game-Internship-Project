import constants
import state
import assets


def update():
    update_obstacles()
    update_player()


def update_obstacles():
    for obstacle in state.obsticle_rect_list:
        obstacle.x -= 5
    state.obsticle_rect_list = [obstacle for obstacle in state.obsticle_rect_list if obstacle.x > -100]



def update_player():
    state.players_gravity_speed -= 1
    assets.player_rect.y -= state.players_gravity_speed
    if assets.player_rect.bottom > constants.GROUND_Y:
        assets.player_rect.bottom = constants.GROUND_Y


def check_collision():
    for obstacle in state.obsticle_rect_list:
        if obstacle.colliderect(assets.player_rect):
            return True
    return False
