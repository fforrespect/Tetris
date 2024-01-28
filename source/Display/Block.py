import pygame

from Setup import Constants as c, GlobalVars as gv

block_images: dict[tuple[int, bool, bool], pygame.image] = {}


def blit_image(screen: pygame.Surface,
               shape: int,
               nw_px: list[int],
               px_size: list[float],
               is_small: bool = False) -> None:

    block_image: pygame.image = __load_image(shape, is_small)

    area: tuple[tuple[int, int]] | None = None
    if gv.using_classic_skin:
        level: int = gv.current_level % 256
        offset: int = int(__get_offset(shape) * px_size[0])
        mino_size: int = c.DEFAULT_MINO_SIZE if not is_small else c.MINI_MINO_SIZE
        x: int = (((level % 10) * 3) * mino_size) + offset
        y: int = 0 if level <= 129 else (level // 10) * mino_size

        area: tuple[tuple[int, int], list[float]] = ((x, y), px_size)
    else:
        block_image = pygame.transform.scale(block_image, px_size)

    screen.blit(block_image, nw_px, area)


def __load_image(shape: int, is_small: bool) -> pygame.Surface:
    key: tuple[int, bool, bool] = (shape, gv.using_classic_skin, is_small)

    if key not in block_images:
        image_path: str
        if not gv.using_classic_skin:
            image_path = f"{c.MODERN_BLOCKS_FP}{shape}.png"
        else:
            image_path = c.SML_CLASSIC_BLOCKS_FP if is_small else c.CLASSIC_BLOCKS_FP
        block_images[key] = pygame.image.load(image_path)
    return block_images[key]


def __get_offset(shape: int) -> int:
    return {
        0: 0, 1: 0, 4: 0,
        2: 1, 6: 1,
        3: 2, 5: 2
    }.get(shape, 2)
