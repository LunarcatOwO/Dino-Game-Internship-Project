import time

FPS_LIMIT = 60
GROUND_Y = 300
JUMP_GRAVITY_START_SPEED = 20
# The seed used for spawning
SEED = time.time()
# Display settings
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 400
# Divides the score by this number to make it less inflated
SCORE_DIVIDER = 100
# The rate at which the FPS limit increases as the score increases (FPS per 100 points). Set to 0 to disable FPS increase.
SCORE_FPS_INCREASE_RATE = 0
# Difficulty (Lower is harder) - SUGGESTED 1500
OBSTACLE_SPAWN_RATE = 1500
# Frames advanced per game tick for sprite animations (higher is faster)
ANIMATION_SPEED = 0.2