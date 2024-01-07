from Setup import Constants


class Board:
    def __init__(self):
        self.grid = [[" " for __ in range(Constants.GRID_SIZE[0])] for _ in range(Constants.GRID_SIZE[1])]
