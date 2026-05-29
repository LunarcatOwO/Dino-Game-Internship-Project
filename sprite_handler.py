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
    animate_obstacles()


def animate_obstacles():
    state.egg_frame_index += constants.ANIMATION_SPEED
    if state.egg_frame_index >= len(assets.egg_frames):
        state.egg_frame_index = 0
    assets.egg_surf = assets.egg_frames[int(state.egg_frame_index)]


def update_player():
    state.players_gravity_speed -= 1
    assets.player_rect.y -= state.players_gravity_speed
    if assets.player_rect.bottom > constants.GROUND_Y:
        assets.player_rect.bottom = constants.GROUND_Y
    animate_player()


def animate_player():
    if assets.player_rect.bottom < constants.GROUND_Y:
        assets.player_surf = assets.player_jump
    else:
        state.player_walk_index += constants.ANIMATION_SPEED
        if state.player_walk_index >= len(assets.player_walk):
            state.player_walk_index = 0
        assets.player_surf = assets.player_walk[int(state.player_walk_index)]


def check_collision():
    for obstacle in state.obsticle_rect_list:
        if obstacle.colliderect(assets.player_rect):
            return True
    return False
