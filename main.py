"""Dino Game in Python

A game similar to the famous Chrome Dino Game, built using pygame-ce.
Made by intern: @bassemfarid, no one or nothing else. 🤖
"""

import pygame

import constants
import state
import functions.init as init
import functions.handlers.input as input_handler
import functions.handlers.screen as screen_handler
import functions.handlers.sprite as sprite_handler
import functions.handlers.score as score_handler

while state.running:
    for event in pygame.event.get():
        input_handler.handle(event)

    if state.is_playing:
        sprite_handler.update_egg()
        sprite_handler.update_player()
        score_handler.update_score()

        if sprite_handler.check_collision():
            state.is_playing = False

    screen_handler.update_screen()

    pygame.display.flip()
    init.clock.tick(constants.FPS_LIMIT)

pygame.quit()
