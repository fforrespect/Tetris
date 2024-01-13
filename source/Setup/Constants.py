# Text #
NUMBER_SIZE: tuple[int, int] = (32, 28)

# Overlay Sizes and NW Positions #
PLAYBOX_SIZE: tuple[int, int] = (324, 648)
PLAYBOX_NW: tuple[int, int] = (380, 156)

STATS_TB_SIZE: tuple[int, int] = (280, 516)
STATS_TB_NW: tuple[int, int] = (52, 296)
STATS_TETRAMINO_NW: tuple[int, int] = (94, 338)
STATS_NUMBERS_NW: tuple[int, int] = (192, 352)
STATS_SPACING: int = 64

LINES_CHARS: int = 3
LINES_TX_SIZE: tuple[int, int] = (NUMBER_SIZE[0]*LINES_CHARS, NUMBER_SIZE[1])
LINES_TX_NW: tuple[int, int] = (608, 64)

LEVEL_CHARS: int = 3
LEVEL_TX_SIZE: tuple[int, int] = (NUMBER_SIZE[0]*LEVEL_CHARS, NUMBER_SIZE[1])
LEVEL_TX_NW: tuple[int, int] = (800, 640)

SCORES_CHARS: int = 6
SCORES_TX_SIZE: tuple[int, int] = (NUMBER_SIZE[0]*SCORES_CHARS, NUMBER_SIZE[1])
TOP_TX_NW: tuple[int, int] = (768, 128)
SCORE_TX_NW: tuple[int, int] = (768, 224)

NEXT_NW: tuple[int, int] = (764, 416)
NEXT_SIZE: tuple[int, int] = (132, 132)

# Environment #
SCREEN_SIZE: tuple[int, int] = (1024, 896)

GRID_SIZE: tuple[int, int] = (10, 20)
MINO_SIZE: float = PLAYBOX_SIZE[0]/GRID_SIZE[0]  # ~32 (32.4 by default)
MINI_MINO_SIZE: int = 24

# Physics #
FPS: int = 60
MOVE_BUFFER: int = 10

# Grid #
EMPTY_GRID_LINE = [" "] * GRID_SIZE[0]

# Files #
_RESOURCES_FP: str = "../Resources/"

FONTS_FP: str = f"{_RESOURCES_FP}Fonts/"
SCORES_FP: str = f"{_RESOURCES_FP}Scores/"
IMAGES_FP: str = f"{_RESOURCES_FP}Images/"

ALL_SCORES_FP: str = f"{SCORES_FP}all_scores.txt"
HIGH_SCORE_FP: str = f"{SCORES_FP}high_score.txt"

BLOCK_IMAGES_FP: str = f"{IMAGES_FP}Blocks/"
GAME_BOARD_OVERLAY_FP: str = f"{IMAGES_FP}game_board.png"

# Game #
LINES_NEEDED_FOR_NEXT_LEVEL: int = 10
SCORE_MULTIPLIERS: tuple[int, int, int, int, int] = (0, 40, 100, 300, 1200)
