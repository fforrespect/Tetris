from Display import Overlays
from Process import Numbers, HighScore
from Setup import GlobalVars as gv
from Game import Board, Tetromino
from Process import KeyPresses


def init():
    gv.current_level = 0
    gv.score = 0
    gv.total_lines_cleared = 0

    gv.prev_high_score = None
    gv.new_high_score = False

    gv.game_running = True
    gv.outro_running = False
    gv.pause_running = False

    gv.elapsed_frames = 0

    gv.all_objects = []
    gv.all_overlays = []

    gv.active_tetromino = None
    gv.held_tetromino = None
    gv.tetromino_queue = []

    gv.game_boar  = None

    gv.tetromino_statistics = [0] * 7

    gv.keys = None

    # Set up game
    Tetromino.init()
    Overlays.init()
    Numbers.init()
    KeyPresses.init()
    Board.init()
    HighScore.init()
