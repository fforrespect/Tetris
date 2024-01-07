import pygame

from Setup import Constants, GlobalVars, Colours


class Playbox:
    def __init__(self):
        self.rect: pygame.rect = (Constants.PLAYBOX_NW, Constants.PLAYBOX_SIZE)
        self.colour: tuple[int, int, int] = Colours.CYAN
        self.is_filled: bool = False

        GlobalVars.all_overlays.append(self)

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.colour, self.rect, not self.is_filled)
