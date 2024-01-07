import pygame

from Setup import Constants, GlobalVars, Colours


class Grid:
    def __init__(self):
        self.colour: tuple[int, int, int] = Colours.RED

        GlobalVars.all_overlays.append(self)

    def draw(self, screen: pygame.Surface):
        for i in range(Constants.GRID_SIZE[0]-1):
            rect = ((Constants.PLAYBOX_NW[0] + ((i + 1) * Constants.MINO_SIZE),
                     Constants.PLAYBOX_NW[1]),
                    (1,
                     Constants.PLAYBOX_SIZE[1]))
            pygame.draw.rect(screen, self.colour, rect)

        for i in range(Constants.GRID_SIZE[1]-1):
            rect = ((Constants.PLAYBOX_NW[0],
                     Constants.PLAYBOX_NW[1] + ((i + 1) * Constants.MINO_SIZE)),
                    (Constants.PLAYBOX_SIZE[0], 1
                     ))
            pygame.draw.rect(screen, self.colour, rect)
