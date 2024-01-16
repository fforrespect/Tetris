import pygame

from Setup import Constants as c, GlobalVars as gv

block_images: dict[tuple[int, bool], pygame.image] = {}


def blit_image(screen: pygame.Surface, shape: int, nw_px: list[int], px_size: list[float]) -> None:
    block_image: pygame.image = __load_image(shape)

    location: tuple[int, int] | None = None
    if gv.using_classic_skin:
        level: int = gv.current_level % 256
        offset: int = int(__get_offset(shape) * px_size[0])
        x: int = (((level % 10) * 3) * c.DEFAULT_MINO_SIZE) + offset
        y: int = 0 if level <= 129 else (level // 10) * c.DEFAULT_MINO_SIZE
        location = (x, y)
    else:
        block_image = pygame.transform.scale(block_image, px_size)

    area: tuple[tuple[int, int]] | None = (location, [px_size[0] if gv.using_classic_skin else c.DEFAULT_MINO_SIZE]*2) \
                                          if gv.using_classic_skin else None
    block_image = pygame.transform.scale(
        block_image,
        list(map(lambda a: float(a*(px_size[0]/c.MINO_SIZE)), block_image.get_size())),
    ) if gv.using_classic_skin else block_image

    screen.blit(block_image, nw_px, area)

def __load_image(shape: int) -> pygame.Surface:
    key: tuple[int, bool] = (shape, gv.using_classic_skin)
    if key not in block_images:
        image_path: str = f"{c.MODERN_BLOCKS_FP}{shape}.png" if not gv.using_classic_skin else c.CLASSIC_BLOCKS_FP
        block_images[key] = pygame.image.load(image_path)
    return block_images[key]


def __get_offset(shape: int) -> int:
    return {
        0: 0, 1: 0, 4: 0,
        2: 1, 6: 1,
        3: 2, 5: 2
    }.get(shape, 2)