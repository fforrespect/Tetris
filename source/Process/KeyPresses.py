import pygame

from Setup import Constants as c, GlobalVars as gv


def init():
    gv.keys = Tracker(c.KEY_PRESS_DELAY, c.KEY_PRESS_INTERVAL)


class Tracker:
    def __init__(self, delay: int, interval: int):
        self.delay: int = delay
        self.interval: int = interval

        self.move_left_pressed: bool = False
        self.move_right_pressed: bool = False

        self.rotate_cw_pressed: bool = False
        self.rotate_acw_pressed: bool = False

        self.soft_drop_pressed: bool = False
        self.hard_drop_pressed: bool = False

        self.hold_piece_pressed: bool = False

        self.frame_last_pressed: list[int] = [0] * 7

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

        match key:
            case "left":
                return kb_input[c.K_MOVE_LEFT]

            case "right":
                return kb_input[c.K_MOVE_RIGHT]

            case "r_cw":
                return kb_input[c.K_ROTATE_CW]

            case "r_acw":
                return kb_input[c.K_ROTATE_ACW]

            case "s_drop":
                return kb_input[c.K_SOFT_DROP]

            case "h_drop":
                return kb_input[c.K_HARD_DROP]

            case "hold":
                return kb_input[c.K_HOLD_PIECE]

            case _:
                raise ValueError("Incorrect key input")


