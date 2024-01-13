import pygame

from Setup import Constants, GlobalVars


def get_printable(grid) -> str:
    return "\n".join(map(str, grid))


class Board:
    def __init__(self):
        self.grid: list[list[str]] = [[" "
                                       for __ in range(Constants.GRID_SIZE[0])]
                                       for _ in range(Constants.GRID_SIZE[1])]
        self.px_size: list[int] = [Constants.MINO_SIZE]*2

        GlobalVars.all_overlays.append(self)

    def __str__(self) -> str:
        return get_printable(self.grid)

    def draw(self, screen: pygame.Surface) -> None:
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                content: str = self.grid[row][col]
                if content != " ":
                    nw_px: list[int] = [(Constants.PLAYBOX_NW[i] + [col, row][i] * Constants.MINO_SIZE) for i in
                                        range(2)]
                    block_image: pygame.image = pygame.image.load(f"{Constants.BLOCK_IMAGES_FP}{content}.png")
                    block_image = pygame.transform.scale(block_image, ([Constants.MINO_SIZE] * 2))
                    screen.blit(block_image, nw_px)

    def get_invalid_positions(self) -> list[list[int]]:
        invalid_positions: list[list[int]] = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] != " ":
                    invalid_positions.append([col, row])
        # for i in range(Constants.GRID_SIZE[1]):
        #     invalid_positions.append([-1, i])
        #     invalid_positions.append([Constants.GRID_SIZE[0], i])
        # for i in range(Constants.GRID_SIZE[0]):
        #     invalid_positions.append([i, Constants.GRID_SIZE[1]])
        return invalid_positions
