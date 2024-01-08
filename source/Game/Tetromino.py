import pygame

from Process import Shapes
from Setup import Constants, GlobalVars, Colours


def generate():
    shape: int = -1  # will do the random generation later

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

        self.px_size = (Constants.MINO_SIZE, Constants.MINO_SIZE)
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

    def draw(self, screen):
        for row in range(self.matrix_size):
            for col in range(self.matrix_size):
                if self.matrix[row][col] == 1:
                    nw_px: tuple[int, int] = (Constants.PLAYBOX_NW[0] + ((self.nw_pos[0] + col)*Constants.MINO_SIZE),
                                              Constants.PLAYBOX_NW[1] + ((self.nw_pos[1] + row)*Constants.MINO_SIZE))
                    rect = (nw_px, self.px_size)
                    pygame.draw.rect(screen, self.colour, rect)

    def move(self, l_or_r: int, down: int = 1, rotate: int = 0):

        self.nw_pos[0] += l_or_r
        self.nw_pos[1] += down
