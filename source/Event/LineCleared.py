from Setup import Constants, GlobalVars


def process() -> None:
    lines_to_remove: list[list[str]] = []
    for row in GlobalVars.game_board.grid:
        if " " not in row:
            lines_to_remove.append(row)

    for line in range(len(lines_to_remove)):
        GlobalVars.game_board.grid.remove(lines_to_remove[line])
        GlobalVars.game_board.grid.insert(0, Constants.EMPTY_GRID_LINE)



