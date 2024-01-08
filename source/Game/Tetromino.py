import pygame
import random

from Game import Level
from Process import Shapes
from Setup import Constants, GlobalVars, Colours


def generate():
    rand = random.Random()
    shape: int = rand.randint(0, 6)

    GlobalVars.active_tetromino = Tetromino(shape)


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
        all_pos: list[list[int]] = []
        for row in range(self.matrix_size):
            for col in range(self.matrix_size):
                if self.matrix[row][col] == 1:
                    all_pos.append([(self.nw_pos[0] + col), (self.nw_pos[1] + row)])
        return all_pos

    def __adjust_vel_for_collision(self, l_or_r: int, down: int) -> tuple[int, int]:
        # Only runs every Constants.FPS/Level.speed() frames (60 by default)
        l_or_r: int = l_or_r
        down: int = down

        # Hit left or right wall
        for x_pos in map(lambda x: x[0] + l_or_r, self.__get_all_pos()):
            if not (0 <= x_pos < Constants.GRID_SIZE[0]):
                l_or_r = 0

        # Hit floor
        for y_pos in map(lambda x: x[1] + down, self.__get_all_pos()):
            if y_pos >= Constants.GRID_SIZE[1]:
                down = 0
                self.__stick_to_board()

        return l_or_r, down

    def __stick_to_board(self):
        for block in self.__get_all_pos():
            GlobalVars.game_board.grid[block[1]][block[0]] = str(self.shape)

        GlobalVars.all_objects.remove(GlobalVars.active_tetromino)
        GlobalVars.active_tetromino = None
        del self

        generate()
