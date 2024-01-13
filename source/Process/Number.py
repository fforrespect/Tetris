import pygame

from Setup import Constants

number_images: list[pygame.image]


def init():
    global number_images
    number_images = [pygame.image.load(f"{Constants.FONTS_FP}{i}.png") for i in range(10)]


def image(number: int) -> pygame.image:
    return number_images[number]

