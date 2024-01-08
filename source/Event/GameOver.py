import sys
import pygame

from Setup import GlobalVars


def _quit_all():
    GlobalVars.game_running = False
    pygame.quit()
    sys.exit()


# Checks if the window's red x button has been pressed
def quit_pressed(events):
    for event in events:
        if event.type == pygame.QUIT:
            _quit_all()


def top_out():
    print("Topped out!")
    for i in GlobalVars.game_board.grid:
        print(i)
    _quit_all()
