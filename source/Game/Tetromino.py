import pygame
import random

from Game import Level
from Process import Shapes
from Setup import Constants, GlobalVars, Colours


def generate():
    rand = random.Random()
    shape: int = rand.randint(0, 6)

    GlobalVars.active_tetromino = Tetromino(shape)


def make_hashable(list_: list) -> tuple:
    return tuple(map(tuple, list_))


class Tetromino:
    def __init__(self, shape: int, rotation: int = 0):
        """
        :param shape:
           -1: just a dot (debug)
            0: O-piece
            1: I-piece
            2: Z-piece
            3: S-piece
            4: T-piece
            5: J-piece
            6: L-piece
        :type shape: int

        :param rotation: The rotation of the object / 90°
        :type rotation: int
        """

        self.shape: int = shape
        self.rotation: int = rotation

        self.px_size: list[int] = [Constants.MINO_SIZE for _ in range(2)]
        self.matrix: list[list[bool]] = Shapes.matrices[shape][rotation]
        self.matrix_size: int = len(self.matrix)
        self.colour: tuple[int, int, int] = Colours.GREEN  # To be deleted later

        self.nw_pos: list[int, int]
        match self.matrix_size:
            case 1:     self.nw_pos = [5, 0]
            case 2 | 3: self.nw_pos = [4, 0]
            case 4:     self.nw_pos = [3, -1]
            case _:     raise Exception("Invalid matrix")

        GlobalVars.all_objects.append(self)

    def draw(self, screen: pygame.Surface) -> None:
        for position in self.__get_all_pos():
            nw_px: list[int] = [Constants.PLAYBOX_NW[i] + (position[i]*Constants.MINO_SIZE) for i in range(2)]
            rect = (nw_px, self.px_size)
            pygame.draw.rect(screen, self.colour, rect)

    def move(self, keys: tuple[bool]) -> None:
        time_to_move: bool = GlobalVars.elapsed_frames % Constants.MOVE_BUFFER == 0
        l_or_r: int = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT] if time_to_move else 0

        down = 1 \
            if ((GlobalVars.elapsed_frames % round(Constants.FPS / Level.speed()) == 0) or
                (keys[pygame.K_DOWN] and time_to_move)) \
            else 0

        # rotate: int = 0

        l_or_r, down = self.__adjust_vel_for_collision(l_or_r, down)

        self.nw_pos[0] += l_or_r
        self.nw_pos[1] += down

    def __get_all_pos(self) -> list[list[int]]:
        # Iterate over each row and col in self.matrix_size,
        # Check if self.matrix[row][col] is equal to 1,
        # If so, append the adjusted position [self.nw_pos[0] + col, self.nw_pos[1] + row] to the list,
        # Finally, the resulting list of positions is returned
        return [[self.nw_pos[0] + col, self.nw_pos[1] + row]
                for row in range(self.matrix_size)
                for col in range(self.matrix_size)
                if self.matrix[row][col] == 1]

    def __adjust_vel_for_collision(self, l_or_r: int, down: int) -> tuple[int, int]:
        # Only runs every Constants.FPS/Level.speed() frames (60 by default)
        all_pos = self.__get_all_pos()

        # Falls on something
        if set(make_hashable([[x, y + down] for x, y in all_pos])).intersection(
           set(make_hashable(GlobalVars.game_board.get_filled_pos()))) != set() or \
                any(y[1] + down >= Constants.GRID_SIZE[1] for y in all_pos):
            down = 0
            self.__stick_to_board()

        # Hits something while moving l or r
        if set(make_hashable([[x + l_or_r, y] for x, y in all_pos])).intersection(
           set(make_hashable(GlobalVars.game_board.get_filled_pos()))) != set() or \
                any(not (0 <= x[0] + l_or_r < Constants.GRID_SIZE[0]) for x in all_pos):
            l_or_r = 0

        return l_or_r, down

    def __stick_to_board(self):
        for block in self.__get_all_pos():
            GlobalVars.game_board.grid[block[1]][block[0]] = str(self.shape)

        GlobalVars.all_objects.remove(GlobalVars.active_tetromino)
        GlobalVars.active_tetromino = None
        del self

        generate()
