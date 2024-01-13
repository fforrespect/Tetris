import pygame

from Process import Number
from Setup import Constants, GlobalVars


class Overlay:
    def __init__(self):
        self.NW: tuple[int, int] = Constants.SCORE_TX_NW
        GlobalVars.all_overlays.append(self)

    def draw(self, screen: pygame.Surface):
        score: str = str(GlobalVars.score).rjust(Constants.SCORES_CHARS, "0")

        for i in range(len(score)):
            dest: tuple[int, int] = (self.NW[0] + (Constants.NUMBER_SIZE[0] * i), self.NW[1])
            screen.blit(Number.image(int(score[i])), dest )
