if __name__ == "__main__":
    raise RuntimeError(f"The {__file__.split('\\')[-1][:-3]} module should not be run on its own. Please run main.py instead")

running = True
is_playing = True
players_gravity_speed = 10
start_time = 0
current_score = 0