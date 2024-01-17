import pygame

from Display import Window
from Event import GameOver, ToppedOut, Pause
from Game import Tetromino
from Setup import Constants as c, GlobalVars as gv


def run(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.mixer.music.load(c.THEME_TUNE_FP)
    pygame.mixer.music.play(-1)
    if gv.is_music_paused:
        pygame.mixer.music.pause()

    Tetromino.generate_new()

    while gv.game_running:
        clock.tick(c.FPS)
        gv.elapsed_frames += 1

        # Checks if the red x has been pressed, and quits the game if so
        GameOver.quit_pressed(pygame.event.get())
        Pause.check(screen, clock)

        if gv.active_tetromino is not None:
            gv.active_tetromino.move()

        # Finally, draw everything to the screen
        Window.display(screen)

    ToppedOut.run(screen, clock)
