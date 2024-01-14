import pygame
import numpy as np

from Setup import Constants as c, GlobalVars as gv


def get_printable(grid) -> str:
    return "\n".join(map(str, grid))


class Board:
    def __init__(self):
        self.grid: list[list[str]] = [[" "
                                       for __ in range(c.GRID_SIZE[0])]
                                       for _ in range(c.GRID_SIZE[1])]
        self.px_size: list[float] = [c.MINO_SIZE]*2

        gv.all_overlays.add(self)

    def __str__(self) -> str:
        return get_printable(self.grid)

    def draw(self, screen: pygame.Surface) -> None:
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                content: str = self.grid[row][col]
                if content != " ":
                    nw_px: list[int] = [(c.PLAYBOX_NW[i] + [col, row][i] * c.MINO_SIZE) for i in
                                        range(2)]
                    block_image: pygame.image = pygame.image.load(f"{c.BLOCK_IMAGES_FP}{content}.png")
                    block_image = pygame.transform.scale(block_image, self.px_size)
                    screen.blit(block_image, nw_px)

    def get_invalid_positions(self) -> list[list[int]]:
        invalid_positions: list[list[int]] = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] != " ":
                    invalid_positions.append([col, row])
        return invalid_positions

    def set_pos(self, pos, content) -> None:
        temp_grid: np.ndarray = np.array(self.grid)
        temp_grid[*pos[::-1]] = str(content)
        self.grid = temp_grid.tolist()
