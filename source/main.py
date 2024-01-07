import sys
import pygame

from Display import Window
from Event import GameOver
from Game import Board
from Process import Overlays
from Setup import Constants, GlobalVars

# Set up pygame
pygame.init()
screen: pygame.Surface = pygame.display.set_mode(Constants.SCREEN_SIZE)
clock: pygame.time.Clock = pygame.time.Clock()

# Set up game
Overlays.initialise()
board = Board.Board()


while GlobalVars.game_running:
    clock.tick(Constants.FPS)

    GlobalVars.elapsed_frames += 1
    GlobalVars.current_frame = GlobalVars.elapsed_frames % Constants.FPS

    # Checks if the red x has been pressed, and quits the game if so
    if GameOver.quit_pressed(pygame.event.get()):
        break

    # keys = pygame.key.get_pressed()

    # Finally, draw everything to the screen
    Window.display(screen)


pygame.quit()
sys.exit()
