import pygame

from Setup import Constants as c, GlobalVars as gv


def init():
    gv.keys = Tracker(c.KEY_PRESS_INTERVAL)


class Tracker:
    def __init__(self, interval: int):
        self.interval: int = interval

        self.key_can_be_pressed: dict[str, bool] = {"left"   : True,
                                                    "right"  : True,
                                                    "r_cw"   : True,
                                                    "r_acw"  : True,
                                                    "s_drop" : True,
                                                    "h_drop" : True,
                                                    "hold"   : True}

        self.frame_last_pressed: dict[str, int] = {"left"   : 0,
                                                   "right"  : 0,
                                                   "r_cw"   : 0,
                                                   "r_acw"  : 0,
                                                   "s_drop" : 0,
                                                   "h_drop" : 0,
                                                   "hold"   : 0}

    def press(self, key: str) -> bool:
        """
        :param key:
            "left"      : move left
            "right"     : move right
            "r_cw"      : rotate CW
            "r_acw"     : rotate ACW
            "s_drop"    : soft drop
            "h_drop"    : hard drop
            "hold"      : hold
        :type key: str

        :returns: Whether an input should be processed or not
        :rtype: bool
        """

        kb_input: tuple[bool] = pygame.key.get_pressed()

        if gv.elapsed_frames - self.frame_last_pressed[key] >= self.interval:
            self.key_can_be_pressed[key] = True

        # if left is able to be pressed
        if self.key_can_be_pressed[key]:
            # if it is actually pressed
            if kb_input[c.KEY_INPUTS[key]]:
                self.key_can_be_pressed[key] = False
                self.frame_last_pressed[key] = gv.elapsed_frames
                return True
        return False
