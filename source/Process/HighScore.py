from Setup import Constants as c, GlobalVars as gv


def init() -> None:
    with open(c.ALL_SCORES_FP, "r") as file:
        scores_list: list[int] = list(map(lambda x: int(x) if x.isdigit() else 0, file.read().split("\n")))
    gv.prev_high_score = max(scores_list)


def get() -> int:
    return gv.prev_high_score


def add_new_score() -> None:
    if gv.score == 0:
        return
    with open(c.ALL_SCORES_FP, "a") as file:
        file.write(str(gv.score) + "\n")
