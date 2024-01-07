import sys
import pygame

from Setup import Constants, GlobalVars
from Event import GameOver

# Set up pygame
pygame.init()
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
clock = pygame.time.Clock()

while GlobalVars.game_running:
    clock.tick(Constants.FPS)

    GlobalVars.elapsed_frames += 1
    GlobalVars.current_frame = GlobalVars.elapsed_frames % Constants.FPS

    # Checks if the red x has been pressed, and quits the game if so
    if GameOver.quit_pressed(pygame.event.get()):
        break

    keys = pygame.key.get_pressed()

pygame.quit()
sys.exit()
