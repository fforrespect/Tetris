from Setup import Constants as c, GlobalVars as gv


def check() -> None:
    with open(c.HIGH_SCORE_FP, "r") as file:
        if gv.score > int(file.read()):
            _set()


def get() -> int:
    with open(c.HIGH_SCORE_FP, "r") as file:
        return int(str(file.read()))


def add_new_score() -> None:
    if gv.score == 0:
        return
    with open(c.ALL_SCORES_FP, "a") as file:
        file.write(str(gv.score) + "\n")
        check()


def _set() -> None:
    with open(c.HIGH_SCORE_FP, "w") as file:
        file.write(str(gv.score))
    gv.new_high_score = True
