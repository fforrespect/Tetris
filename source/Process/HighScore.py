from Setup import Constants, GlobalVars


def check() -> None:
    with open(Constants.HIGH_SCORE_FP, "r") as file:
        if GlobalVars.score > int(file.read()):
            _set()


def get() -> int:
    with open(Constants.HIGH_SCORE_FP, "r") as file:
        return int(str(file.read()))


def add_new_score() -> None:
    if GlobalVars.score == 0:
        return
    with open(Constants.ALL_SCORES_FP, "a") as file:
        file.write(str(GlobalVars.score) + "\n")
        check()


def _set() -> None:
    with open(Constants.HIGH_SCORE_FP, "w") as file:
        file.write(str(GlobalVars.score))
