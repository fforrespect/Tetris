import pygame

from Display import Window, Overlays
from Event import GameOver
from Game import Board, Tetromino
from Process import Numbers, KeyPresses
from Setup import Constants as c, GlobalVars as gv

# Set up pygame
pygame.init()
screen: pygame.Surface = pygame.display.set_mode(c.SCREEN_SIZE)
clock: pygame.time.Clock = pygame.time.Clock()

# Set up game
Tetromino.init()
Overlays.init()
Numbers.init()
KeyPresses.init()
gv.game_board = Board.Board()

Tetromino.generate_new()

while gv.game_running:
    # Loop processing #
    clock.tick(c.FPS)

    gv.elapsed_frames += 1

    # Checks if the red x has been pressed, and quits the game if so
    GameOver.quit_pressed(pygame.event.get())
    # End processing #

    # keys: tuple[bool] = pygame.key.get_pressed()

    if gv.active_tetromino is not None:
        gv.active_tetromino.move()

    # Finally, draw everything to the screen
    Window.display(screen)
