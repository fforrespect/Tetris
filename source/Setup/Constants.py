# Environment #
SCREEN_SIZE: tuple[int, int] = (1024, 896)

PLAYBOX_NW: tuple[int, int] = (382, 158)
PLAYBOX_SIZE: tuple[int, int] = (320, 640)
MINO_SIZE: int = 32
GRID_SIZE: tuple[int, int] = (10, 20)

# Physics #
FPS: int = 60
MOVE_BUFFER: int = 10

# Grid #
EMPTY_GRID_LINE = [" " for _ in range(GRID_SIZE[0])]

# Files #
_RESOURCES_FP: str = "../Resources/"

IMAGES_FP: str = f"{_RESOURCES_FP}Images/"
