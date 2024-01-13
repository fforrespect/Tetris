import pygame

from Setup import Constants, GlobalVars


class Board:
    def __init__(self):
        self.grid = [[" " for __ in range(Constants.GRID_SIZE[0])] for _ in range(Constants.GRID_SIZE[1])]
        self.px_size: list[int] = [Constants.MINO_SIZE for _ in range(2)]

        GlobalVars.all_overlays.append(self)

    def draw(self, screen: pygame.Surface):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                content: str = self.grid[row][col]
                if content != " ":
                    nw_px: list[int] = [(Constants.PLAYBOX_NW[i] + [col, row][i]*Constants.MINO_SIZE) for i in range(2)]
                    block_image: pygame.image = pygame.image.load(f"{Constants.BLOCK_IMAGES_FP}{content}.png")
                    block_image = pygame.transform.scale(block_image, ([Constants.MINO_SIZE]*2))
                    screen.blit(block_image, nw_px)

    def get_filled_pos(self) -> list[list[int]]:
        filled_pos: list[list[int]] = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] != " ":
                    filled_pos.append([col, row])
        return filled_pos
