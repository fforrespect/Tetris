import sys
import pygame

from Process import HighScore
from Setup import GlobalVars as gv


def quit_all():
    HighScore.add_new_score()

    gv.game_running = False
    gv.outro_running = False

    pygame.quit()
    sys.exit()


# Checks if the window's red x button has been pressed
def quit_pressed(events):
    for event in events:
        if event.type == pygame.QUIT:
            quit_all()


def top_out():
    gv.game_running = False
