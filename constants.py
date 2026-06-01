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
# Difficulty (Lower is harder) - SUGGESTED 1500
OBSTACLE_SPAWN_RATE = 1500
# Frames advanced per game tick for sprite animations (higher is faster)
ANIMATION_SPEED = 0.2
SKY_SCROLL_SPEED = 1
STARTING_LIVE_COUNT = 3