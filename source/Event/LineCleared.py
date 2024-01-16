from Setup import Constants as c, GlobalVars as gv


def process() -> None:
    lines_to_clear: list[list[str]] = []
    for row in gv.game_board.grid:
        if " " not in row:
            lines_to_clear.append(row)

    for line in range(len(lines_to_clear)):
        gv.game_board.grid.remove(lines_to_clear[line])
        gv.game_board.grid.insert(0, c.EMPTY_GRID_LINE)

    gv.tetrises += 1 if len(lines_to_clear) == 4 else 0

    gv.total_lines_cleared += len(lines_to_clear)
    gv.score += c.SCORE_MULTIPLIERS[len(lines_to_clear)] * (gv.current_level + 1)
    gv.current_level = gv.total_lines_cleared // c.LINES_NEEDED_FOR_NEXT_LEVEL
