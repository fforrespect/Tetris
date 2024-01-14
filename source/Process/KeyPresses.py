import pygame

from Setup import Constants as c, GlobalVars as gv


def init():
    gv.key_tracker = Tracker(c.KEY_PRESS_DELAY, c.KEY_PRESS_INTERVAL)


class Tracker:
    def __init__(self, delay: int, interval: int):
        pass

        # # Logic to make sure only one click is counted at a time
        # check_click = 0
        # click = 0
        #
        # while True:
        #
        #     # Only register a click if in the last frame, a click wasn't registered
        #     # This prevents holding down left click and creating a stream of bullets
        #     if pygame.mouse.get_pressed()[0]:
        #         click = 0 if check_click == 1 else 1
        #         check_click = 1
        #     else:
        #         check_click = 0

