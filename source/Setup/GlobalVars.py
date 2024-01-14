from Game import Board, Tetromino
from Process import KeyPresses

current_level: int = 0
score: int = 0
total_lines_cleared: int = 0

game_running: bool = True

elapsed_frames: int = 0

all_objects:  set[object] = set()
all_overlays: set[object] = set()

active_tetromino: Tetromino.Tetromino | None = None
held_tetromino: Tetromino.Tetromino | None = None
tetromino_queue: list[Tetromino.Tetromino] = []

game_board: Board.Board | None = None

tetromino_statistics: list[int] = [0] * 7

keys: KeyPresses.Tracker | None = None
