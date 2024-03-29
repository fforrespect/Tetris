import pygame

pygame.init()

# Overlay Sizes and NW Positions #
PLAYBOX_SIZE: tuple[int, int] = (324, 648)
PLAYBOX_NW: tuple[int, int] = (380, 156)

STATS_TB_NW: tuple[int, int] = (52, 296)
STATS_TETRAMINO_NW: tuple[int, int] = (94, 338)
STATS_NUMBERS_NW: tuple[int, int] = (192, 352)
STATS_SPACING: int = 64

LINES_CHARS: int = 3
LINES_TX_NW: tuple[int, int] = (608, 64)

LEVEL_CHARS: int = 3
LEVEL_TX_NW: tuple[int, int] = (124, 94)  # 126)

SCORES_CHARS: int = 6
TOP_TX_NW: tuple[int, int] = (768, 128)
SCORE_TX_NW: tuple[int, int] = (768, 224)

TRT_CHARS: int = 2
TRT_TX_NW: tuple[int, int] = (112, 178)

DROUGHT_CHARS: int = 2
DROUGHT_TX_NW: tuple[int, int] = (246, 178)

NEXT_NW: tuple[int, int] = (764, 416)
HOLD_NW: tuple[int, int] = (764, 638)

# Environment #
SCREEN_SIZE: tuple[int, int] = (1024, 896)

GRID_SIZE: tuple[int, int] = (10, 20)
MINO_SIZE: float = PLAYBOX_SIZE[0]/GRID_SIZE[0]  # ~32 (32.4 by default)
DEFAULT_MINO_SIZE: int = 32
MINI_MINO_SIZE: int = 24

# Physics #
FPS: int = 60
KEY_PRESS_INTERVALS: dict[str, int] = {"left"   : 8,
                                       "right"  : 8,
                                       "r_cw"   : 12,
                                       "r_acw"  : 12,
                                       "s_drop" : 10,
                                       "h_drop" : 15,
                                       "hold"   : 0}  # frames

# Controls #
K_MOVE_LEFT: int = pygame.K_LEFT
K_MOVE_RIGHT: int = pygame.K_RIGHT

K_ROTATE_CW: int = pygame.K_UP
K_ROTATE_ACW: int = pygame.K_c

K_SOFT_DROP: int = pygame.K_DOWN
K_HARD_DROP: int = pygame.K_SPACE

K_HOLD_PIECE: int = pygame.K_z

KEY_INPUTS: dict[str, int] = {"left"   : K_MOVE_LEFT,
                              "right"  : K_MOVE_RIGHT,
                              "r_cw"   : K_ROTATE_CW,
                              "r_acw"  : K_ROTATE_ACW,
                              "s_drop" : K_SOFT_DROP,
                              "h_drop" : K_HARD_DROP,
                              "hold"   : K_HOLD_PIECE}

# Grid #
EMPTY_GRID_LINE = [" "] * GRID_SIZE[0]

# Files #
_RESOURCES_FP: str = "../Resources/"

FONTS_FP: str = f"{_RESOURCES_FP}Fonts/"
SCORES_FP: str = f"{_RESOURCES_FP}Scores/"
IMAGES_FP: str = f"{_RESOURCES_FP}Images/"
AUDIO_FP: str = f"{_RESOURCES_FP}Audio/"

REG_NUM_FP: str = f"{FONTS_FP}Regular/"
SML_NUM_FP: str = f"{FONTS_FP}Small/"

_TFF_FP: str = f"{FONTS_FP}press-start/PressStart2P-vaV7.ttf"
ALL_SCORES_FP: str = f"{SCORES_FP}all_scores.txt"

_BLOCK_IMAGES_FP: str = f"{IMAGES_FP}Blocks/"
_GAME_BOARD_FP: str = f"{IMAGES_FP}Board/"
MODERN_GAME_BOARD_FP: str = f"{_GAME_BOARD_FP}game_board_modern.png"
CLASSIC_GAME_BOARD_FP: str = f"{_GAME_BOARD_FP}game_board_classic.png"

MODERN_BLOCKS_FP: str = f"{_BLOCK_IMAGES_FP}Modern/"
CLASSIC_BLOCKS_FP: str = f"{_BLOCK_IMAGES_FP}Classic/blocks.png"
SML_CLASSIC_BLOCKS_FP: str = f"{_BLOCK_IMAGES_FP}Classic/blocks_small.png"

GAME_OVER_SOUND_FP: str = f"{AUDIO_FP}game_over.wav"
BLOCK_PLACED_AUDIO_FP: str = f"{AUDIO_FP}block_placed.wav"
THEME_TUNE_FP: str = f"{AUDIO_FP}theme.wav"

# Game #
LINES_NEEDED_FOR_NEXT_LEVEL: int = 10
SCORE_MULTIPLIERS: tuple[int, int, int, int, int] = (0, 40, 100, 300, 1200)

# Text #
NUMBER_SIZE: tuple[int, int] = (32, 28)
SMALL_NUMBER_SIZE: tuple[int, int] = (24, 21)

SMALL_FONT = pygame.font.Font(_TFF_FP, 16)
LARGE_FONT = pygame.font.Font(_TFF_FP, 38)
