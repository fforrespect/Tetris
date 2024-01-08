from Setup import Constants, GlobalVars


class Board:
    def __init__(self):
        self.grid = [[" " for __ in range(Constants.GRID_SIZE[0])] for _ in range(Constants.GRID_SIZE[1])]

    def adjust_velocities_for_collisions(self, l_or_r: int, down: int) -> tuple[int, int]:
        l_or_r: int = l_or_r
        down: int = down

        # Hit left or right wall
        for x_pos in map(lambda x: x[0] + l_or_r, GlobalVars.active_tetromino.get_all_pos()):
            if not (0 <= x_pos < Constants.GRID_SIZE[0]):
                l_or_r = 0

        # Hit floor
        for y_pos in map(lambda x: x[1] + down, GlobalVars.active_tetromino.get_all_pos()):
            if y_pos >= Constants.GRID_SIZE[1]:
                down = 0

        return l_or_r, down
