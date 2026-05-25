if __name__ == "__main__":
    raise RuntimeError(f"The {__file__.split('\\')[-1][:-3]} module should not be run on its own. Please run main.py instead")
import time

FPS_LIMIT = 60
GROUND_Y = 300
JUMP_GRAVITY_START_SPEED = 20
SEED = time.time()
