from Setup import Constants, GlobalVars


def process() -> None:
    lines_to_clear: list[list[str]] = []
    for row in GlobalVars.game_board.grid:
        if " " not in row:
            lines_to_clear.append(row)

    for line in range(len(lines_to_clear)):
        GlobalVars.game_board.grid.remove(lines_to_clear[line])
        GlobalVars.game_board.grid.insert(0, Constants.EMPTY_GRID_LINE)

    GlobalVars.total_lines_cleared += len(lines_to_clear)
    GlobalVars.score += Constants.SCORE_MULTIPLIERS[len(lines_to_clear)] * (GlobalVars.current_level + 1)
    GlobalVars.current_level = (GlobalVars.total_lines_cleared // Constants.LINES_NEEDED_FOR_NEXT_LEVEL) + 1
