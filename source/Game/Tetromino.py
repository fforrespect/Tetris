import pygame
import random

from Event import LineCleared, GameOver
from Game import Level
from Process import Shapes
from Setup import Constants, GlobalVars


def init() -> None:
    for _ in range(3):
        make_random_tetromino()


def generate_new() -> None:
    make_random_tetromino()
    GlobalVars.tetromino_queue.pop(0).activate()

    if any(not is_valid_block_position([x, y]) for x, y in GlobalVars.active_tetromino.get_all_pos()):
        GameOver.top_out()


def make_random_tetromino() -> None:
    rand = random.Random()
    shape: int = rand.randint(0, 6)
    GlobalVars.tetromino_queue.append(Tetromino(shape))


def make_set(list_: list) -> set[tuple[tuple]]:
    return set(tuple(map(tuple, list_)))


def is_valid_block_position(pos: list[int]) -> bool:
    set_of_invalid_positions: set[tuple[tuple]] = make_set(GlobalVars.game_board.get_invalid_positions())

    x, y = pos
    return ((0 <= x < Constants.GRID_SIZE[0]) and
            (y < Constants.GRID_SIZE[1]) and
            ((x, y) not in set_of_invalid_positions))


def get_initial_nw_pos(matrix_size: int) -> list[int]:
    match matrix_size:
        case 1:
            return [5, 0]
        case 2 | 3:
            return [4, 0]
        case 4:
            return [3, -1]
        case _:
            raise Exception("Invalid matrix")


class Tetromino:
    def __init__(self, shape: int, is_active: bool = True, is_small: bool = False):
        """
        :param shape:
           -1: just a dot (debug)
            0: O-piece
            1: I-piece
            2: Z-piece
            3: S-piece
            4: T-piece
            5: J-piece
            6: L-piece
        :type shape: int

        :param is_active: Is the piece currently in the queue, or should it be displayed?
        :type is_active: bool
        """

        self.shape: int = shape
        self.is_inactive: bool = is_active
        self.is_small: bool = is_small

        self.rotation: int = 0
        self.is_being_held: bool = False
        self.has_used_hold: bool = False
        self.px_size: list[float] = [Constants.MINO_SIZE if not self.is_small else Constants.MINI_MINO_SIZE] * 2
        self.matrix: list[list[bool]] = Shapes.matrices[shape][self.rotation]
        self.matrix_size: int = len(self.matrix)

        self.nw_pos: list[int] = get_initial_nw_pos(self.matrix_size)

        GlobalVars.all_objects.add(self)

    def draw(self, screen: pygame.Surface, is_next: bool = False, base_nw: tuple[int, int] = None) -> None:
        if (self.is_inactive and not is_next and not self.is_being_held) or \
                (self.is_small and base_nw is None):
            return

        rotated_matrix: list[list[bool]] = Shapes.matrices[self.shape][1]

        positions = self.get_all_pos(rotated_matrix if self.is_inactive else None)
        x_adj: float = 0; y_adj: float = 0
        if is_next or self.is_being_held:
            x_adj = -(min([pos[0] for pos in positions]) - 1) + (0.5 if self.matrix_size == 4 else 0)
            y_adj = 0.5 if self.matrix_size == 3 else 1
        if base_nw is not None:
            x_adj = -(3.5 + (0.5 if self.shape in (2, 3, 4, 5, 6) else 0))
            y_adj = 0.75 if self.shape == 1 else 0
        adj: tuple[float, float] = (x_adj, y_adj)

        if base_nw is None:
            if is_next:
                base_nw = Constants.NEXT_NW
            elif self.is_being_held:
                base_nw = Constants.HOLD_NW
            else:
                base_nw = Constants.PLAYBOX_NW

        for position in positions:
            nw_px: list[int] = [base_nw[i] + ((position[i] + adj[i]) * self.px_size[0])
                                for i in range(2)]
            block_image: pygame.image = pygame.image.load(f"{Constants.BLOCK_IMAGES_FP}{self.shape}.png")
            block_image = pygame.transform.scale(block_image, self.px_size)
            screen.blit(block_image, nw_px)

    def move(self, keys: tuple[bool]) -> None:
        time_to_move: bool = GlobalVars.elapsed_frames % Constants.MOVE_BUFFER == 0
        l_or_r: int = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT] if time_to_move else 0

        down = 1 \
            if ((GlobalVars.elapsed_frames % Level.speed() == 0) or
                (keys[pygame.K_DOWN] and time_to_move)) \
            else 0

        if keys[pygame.K_DOWN] and time_to_move:
            GlobalVars.score += 1

        new_rotation: int = (self.rotation + (keys[pygame.K_UP] - keys[pygame.K_c])) % 4
        rotated_matrix: list[list[bool]] = Shapes.matrices[self.shape][new_rotation]

        allow_rotation: bool
        l_or_r, down, allow_rotation = self.__adjust_vel_for_collision(
            l_or_r,
            down,
            rotated_matrix
        )

        self.nw_pos[0] += l_or_r
        self.nw_pos[1] += down

        allow_rotation = (allow_rotation and
                          time_to_move and
                          all(is_valid_block_position([x, y])
                              for x, y in self.get_all_pos(rotated_matrix)))

        self.matrix = rotated_matrix if allow_rotation else self.matrix
        self.rotation = new_rotation if allow_rotation else self.rotation

        if keys[pygame.K_SPACE] and time_to_move:
            self.__hard_drop()

        if keys[pygame.K_z] and time_to_move:
            self.__hold()

    def activate(self) -> None:
        self.is_inactive = False
        GlobalVars.tetromino_statistics[self.shape] += 1
        GlobalVars.active_tetromino = self

    def get_all_pos(self, matrix: list[list[int]] | None = None) -> list[list[int]]:
        matrix = self.matrix if matrix is None else matrix
        nw_to_check = get_initial_nw_pos(self.matrix_size) if self.is_being_held else self.nw_pos
        # Iterate over each row and col in self.matrix_size,
        # Check if self.matrix[row][col] is equal to 1,
        # If so, append the adjusted position [self.nw_pos[0] + col, self.nw_pos[1] + row] to the list,
        # Finally, the resulting list of positions is returned
        return [[nw_to_check[0] + col, nw_to_check[1] + row]
                for row in range(len(matrix))
                for col in range(len(matrix[0]))
                if matrix[row][col]]

    def __hard_drop(self) -> None:
        current_pos: list[list[int]] = self.get_all_pos()

        max_drop = Constants.GRID_SIZE[1]
        for x, y in current_pos:
            drop = 0
            while is_valid_block_position([x, y + drop + 1]):
                drop += 1
            max_drop = min(max_drop, drop)

        GlobalVars.score += 2*max_drop

        self.nw_pos[1] += max_drop
        self.__stick_to_board()

    def __hold(self) -> None:
        if GlobalVars.held_tetromino is None:
            GlobalVars.held_tetromino = GlobalVars.active_tetromino
            GlobalVars.tetromino_queue.pop(0).activate()
        else:
            if GlobalVars.active_tetromino.has_used_hold:
                return
            GlobalVars.active_tetromino, GlobalVars.held_tetromino = (
                GlobalVars.held_tetromino, GlobalVars.active_tetromino)

        GlobalVars.active_tetromino.has_used_hold = True

        GlobalVars.held_tetromino.is_being_held = True
        GlobalVars.active_tetromino.is_being_held = False

        GlobalVars.held_tetromino.is_inactive = True
        GlobalVars.active_tetromino.is_inactive = False

        GlobalVars.active_tetromino.nw_pos = get_initial_nw_pos(self.matrix_size)

    def __adjust_vel_for_collision(
            self,
            l_or_r: int,
            down: int,
            rotated_matrix: list[list[bool]]) -> tuple[int, int, bool]:

        current_pos: list[list[int]] = self.get_all_pos()
        able_to_stick: bool = False

        # Falls on something
        if any(not is_valid_block_position([x, y + down])
               for x, y in current_pos):
            down = 0
            able_to_stick = True

        # Hits something while moving l or r
        if any(not is_valid_block_position([x + l_or_r, y])
               for x, y in current_pos):
            l_or_r = 0

        # Check rotation
        rotated_pos: list[list[int]] = self.get_all_pos(rotated_matrix)
        allow_rotation: bool = all(is_valid_block_position(pos)
                                   for pos in rotated_pos)

        if able_to_stick and allow_rotation:
            self.__stick_to_board()

        return l_or_r, down, allow_rotation

    def __stick_to_board(self) -> None:
        print()
        print(self.get_all_pos())
        for block in self.get_all_pos():
            GlobalVars.game_board.set_pos(block, self.shape)

        GlobalVars.all_objects.remove(GlobalVars.active_tetromino)
        GlobalVars.active_tetromino = None

        LineCleared.process()
        generate_new()
