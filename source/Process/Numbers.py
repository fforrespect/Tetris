import pygame

from Setup import Constants

number_images: list[pygame.image]


def init():
    global number_images
    number_images = [pygame.image.load(f"{Constants.FONTS_FP}{i}.png") for i in range(10)]


def _image(number: int) -> pygame.image:
    return number_images[number]


def draw(screen: pygame.Surface, number: int, dest: tuple[int, int], width: int = 3) -> None:
    score: str = str(number).rjust(width, "0")

    for i in range(len(score)):
        dest_i: tuple[int, int] = (dest[0] + (Constants.NUMBER_SIZE[0] * i), dest[1])
        screen.blit(_image(int(score[i])), dest_i)

