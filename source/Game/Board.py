import pygame

from Setup import Colours, Constants, GlobalVars


class Board:
    def __init__(self):
        self.grid = [[" " for __ in range(Constants.GRID_SIZE[0])] for _ in range(Constants.GRID_SIZE[1])]
        self.px_size: list[int] = [Constants.MINO_SIZE for _ in range(2)]

        GlobalVars.all_overlays.append(self)

    def draw(self, screen: pygame.Surface):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] != " ":
                    nw_px: list[int] = [(Constants.PLAYBOX_NW[i] + [col, row][i]*Constants.MINO_SIZE) for i in range(2)]
                    rect = (nw_px, self.px_size)
                    pygame.draw.rect(screen, Colours.BLUE, rect)


