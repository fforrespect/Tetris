from Game import Board
from Process import KeyPresses

current_level: int = 0
score: int = 0
total_lines_cleared: int = 0

new_high_score: bool = False

game_running: bool = True
outro_running: bool = False

elapsed_frames: int = 0

all_objects:  set[object] = set()
all_overlays: set[object] = set()

active_tetromino: object | None = None
held_tetromino: object | None = None
tetromino_queue: list[object] = []

game_board: Board.Board | None = None

tetromino_statistics: list[int] = [0] * 7

keys: KeyPresses.Tracker | None = None
