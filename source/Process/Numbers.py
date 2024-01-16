import pygame

from Setup import Constants as c

reg_number_images: list[pygame.image]
sml_number_images: list[pygame.image]


def init():
    global reg_number_images
    global sml_number_images
    reg_number_images = [pygame.image.load(f"{c.REG_NUM_FP}{i}.png") for i in range(10)]
    sml_number_images = [pygame.image.load(f"{c.SML_NUM_FP}{i}.png") for i in range(10)]


def _image(number: int, is_small: bool = False) -> pygame.image:
    return reg_number_images[number] if not is_small else sml_number_images[number]


def draw(screen: pygame.Surface,
         number: int,
         dest: tuple[int, int],
         width: int = 3,
         is_small: bool = False) -> None:

    score: str = str(number).rjust(width, "0")
    spacing: int = c.NUMBER_SIZE[0] if not is_small else c.SMALL_NUMBER_SIZE[0]

    for i in range(len(score)):
        dest_i: tuple[int, int] = (dest[0] + (spacing * i), dest[1])
        screen.blit(
            _image(
                int(score[i]),
                is_small),
            dest_i
        )

