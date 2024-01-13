import pygame

from Setup import Constants, GlobalVars


class Overlay:
    def __init__(self):
        self.NW: tuple[int, int] = (0, 0)
        GlobalVars.all_overlays.append(self)

    def draw(self, screen: pygame.Surface) -> None:
        board_image: pygame.image = pygame.image.load(Constants.GAME_BOARD_OVERLAY_FP)
        screen.blit(board_image, self.NW)
