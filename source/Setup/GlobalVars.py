from Game import Board, Tetromino

current_level: int = 0

game_running: bool = True

elapsed_frames: int = 0

all_objects:  list[object] = []
all_overlays: list[object] = []

active_tetromino: Tetromino.Tetromino | None = None
game_board: Board.Board | None = None
