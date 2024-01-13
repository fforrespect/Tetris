import pygame

from Game import Tetromino
from Process import Numbers, HighScore
from Setup import Constants, GlobalVars, Colours


def init() -> None:
    PlayBox()
    GameBoard()
    Score()
    HighScoreO()
    Level()
    Lines()
    NextPiece()


class GameBoard:
    def __init__(self):
        self.NW: tuple[int, int] = (0, 0)
        GlobalVars.all_overlays.append(self)

    def draw(self, screen: pygame.Surface) -> None:
        board_image: pygame.image = pygame.image.load(Constants.GAME_BOARD_OVERLAY_FP)
        screen.blit(board_image, self.NW)


class Score:
    def __init__(self):
        self.NW: tuple[int, int] = Constants.SCORE_TX_NW
        GlobalVars.all_overlays.append(self)

    def draw(self, screen: pygame.Surface) -> None:
        Numbers.draw(screen, GlobalVars.score, self.NW, Constants.SCORES_CHARS)


class HighScoreO:
    def __init__(self):
        self.NW: tuple[int, int] = Constants.TOP_TX_NW
        GlobalVars.all_overlays.append(self)

    def draw(self, screen: pygame.Surface) -> None:
        Numbers.draw(screen, HighScore.get(), self.NW, Constants.SCORES_CHARS)


class Level:
    def __init__(self):
        self.NW: tuple[int, int] = Constants.LEVEL_TX_NW
        GlobalVars.all_overlays.append(self)

    def draw(self, screen: pygame.Surface) -> None:
        Numbers.draw(screen, GlobalVars.current_level, self.NW)


class Lines:
    def __init__(self):
        self.NW: tuple[int, int] = Constants.LINES_TX_NW
        GlobalVars.all_overlays.append(self)

    def draw(self, screen: pygame.Surface) -> None:
        Numbers.draw(screen, GlobalVars.total_lines_cleared, self.NW)


class NextPiece:
    def __init__(self):
        self.NW: tuple[int, int] = Constants.NEXT_NW
        GlobalVars.all_overlays.append(self)

    @staticmethod
    def draw(screen: pygame.Surface) -> None:
        next_tetromino: Tetromino.Tetromino = GlobalVars.tetromino_queue[0]
        next_tetromino.draw(screen, True)


class PlayBox:
    def __init__(self):
        self.rect: pygame.rect = (Constants.PLAYBOX_NW, Constants.PLAYBOX_SIZE)
        self.colour: tuple[int, int, int] = Colours.CYAN
        self.is_filled: bool = False

        GlobalVars.all_overlays.append(self)

    def draw(self, screen: pygame.Surface) -> None:
        return
        # pygame.draw.rect(screen, self.colour, self.rect, not self.is_filled)
