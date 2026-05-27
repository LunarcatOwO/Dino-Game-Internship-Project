"""Dino Game in Python

A game similar to the famous Chrome Dino Game, built using pygame-ce.
Made by intern: @bassemfarid 🤖
"""

import init
import state
import input_handler
import sprite_handler
import score_handler
import display

if __name__ == "__main__":
    while state.running:
        input_handler.handle_events()

        if state.is_playing:
            sprite_handler.update()
            score_handler.update_score()

            if sprite_handler.check_collision():
                state.is_playing = False

        display.draw_frame()

    init.quit_game()
else:
    raise RuntimeError("The main.py file cannot be imported")
