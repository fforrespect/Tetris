import pygame

from Game import Tetromino
from Process import Numbers, HighScore
from Setup import Constants as c, GlobalVars as gv, Colours


def init() -> None:
    # PlayBox()
    Score()
    HighScoreO()
    Level()
    Lines()
    NextPiece()
    Statistics()
    GameBoard()
    TetrisRate()
    LineBarDrought()


class GameBoard:
    def __init__(self):
        self.NW: tuple[int, int] = (0, 0)
        gv.all_overlays.append(self)

    def draw(self, screen: pygame.Surface) -> None:
        board_image: pygame.image = pygame.image.load(c.GAME_BOARD_OVERLAY_FP)
        screen.blit(board_image, self.NW)


class Score:
    def __init__(self):
        self.NW: tuple[int, int] = c.SCORE_TX_NW
        gv.all_overlays.append(self)

    def draw(self, screen: pygame.Surface) -> None:
        Numbers.draw(screen, gv.score, self.NW, c.SCORES_CHARS)


class HighScoreO:
    def __init__(self):
        self.NW: tuple[int, int] = c.TOP_TX_NW
        gv.all_overlays.append(self)

    def draw(self, screen: pygame.Surface) -> None:
        Numbers.draw(screen, HighScore.get(), self.NW, c.SCORES_CHARS)


class Level:
    def __init__(self):
        self.NW: tuple[int, int] = c.LEVEL_TX_NW
        gv.all_overlays.append(self)

    def draw(self, screen: pygame.Surface) -> None:
        Numbers.draw(screen, gv.current_level, self.NW)


class Lines:
    def __init__(self):
        self.NW: tuple[int, int] = c.LINES_TX_NW
        gv.all_overlays.append(self)

    def draw(self, screen: pygame.Surface) -> None:
        Numbers.draw(screen, gv.total_lines_cleared, self.NW)


class NextPiece:
    def __init__(self):
        self.NW: tuple[int, int] = c.NEXT_NW
        gv.all_overlays.append(self)

    @staticmethod
    def draw(screen: pygame.Surface) -> None:
        next_tetromino: Tetromino.Tetromino = gv.tetromino_queue[0]
        next_tetromino.draw(screen, True)


class Statistics:
    def __init__(self):
        self.tet_NW: tuple[int, int] = c.STATS_TETRAMINO_NW
        self.num_NW: tuple[int, int] = c.STATS_NUMBERS_NW

        self.tetromino_order: tuple = (4, 5, 2, 0, 3, 6, 1)
        self.tetrominoes = [Tetromino.Tetromino(shape, False, True)
                            for shape in self.tetromino_order]

        gv.all_overlays.append(self)

    def draw(self, screen: pygame.Surface) -> None:
        for i, tetromino in enumerate(self.tetrominoes):
            tet_nw_i = (self.tet_NW[0], self.tet_NW[1] + c.STATS_SPACING*i)
            tetromino.draw(screen, base_nw=tet_nw_i)
            Numbers.draw(
                screen,
                gv.tetromino_statistics[tetromino.shape],
                (self.num_NW[0], self.num_NW[1] + c.STATS_SPACING*i)
            )


class TetrisRate:
    def __init__(self):
        self.NW: tuple[int, int] = c.TRT_TX_NW
        gv.all_overlays.append(self)

    def draw(self, screen: pygame.Surface) -> None:
        try:
            trt_pc: int = round((gv.tetrises * 400) / gv.total_lines_cleared)
            trt_pc = 99 if trt_pc == 100 else trt_pc
        except ZeroDivisionError:
            trt_pc: int = 0
        Numbers.draw(screen, trt_pc, self.NW, c.TRT_CHARS, True)


class LineBarDrought:
    def __init__(self):
        self.NW: tuple[int, int] = c.DROUGHT_TX_NW
        gv.all_overlays.append(self)

    def draw(self, screen: pygame.Surface) -> None:
        display = gv.drought if gv.drought < 100 else 99
        Numbers.draw(screen, display, self.NW, c.DROUGHT_CHARS, True)


class PlayBox:
    def __init__(self):
        self.rect: pygame.rect = (c.PLAYBOX_NW, c.PLAYBOX_SIZE)
        self.colour: tuple[int, int, int] = Colours.CYAN
        self.is_filled: bool = False

        gv.all_overlays.append(self)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.colour, self.rect, not self.is_filled)
