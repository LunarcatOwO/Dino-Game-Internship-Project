if __name__ == "__main__":
    raise RuntimeError(f"The {__file__.split('\\')[-1][:-3]} module should not be run on its own. Please run main.py instead")

import time

FPS_LIMIT = 60
GROUND_Y = 300
JUMP_GRAVITY_START_SPEED = 20
# Seed for random generator of enemies but not used for now
SEED = time.time()
# Display settings
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 400
# Divides the score by this number to make it less inflated
SCORE_DIVIDER = 100
# The rate at which the FPS limit increases as the score increases (FPS per 100 points). Set to 0 to disable FPS increase.
SCORE_FPS_INCREASE_RATE = 0