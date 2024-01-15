import sys
import pygame

from Process import HighScore
from Setup import GlobalVars as gv, Constants as c


def quit_all():
    gv.game_running = False
    gv.outro_running = False

    pygame.quit()
    sys.exit()


# Checks if the window's red x button has been pressed
def quit_pressed(events: list[pygame.event.Event]):
    for event in events:
        if event.type == pygame.QUIT:
            HighScore.add_new_score()
            quit_all()


def top_out():
    HighScore.add_new_score()
    gv.game_running = False

    pygame.mixer.music.stop()
    game_over_sound = pygame.mixer.Sound(c.GAME_OVER_SOUND_FP)
    pygame.mixer.Sound.play(game_over_sound)
