from Setup import GlobalVars


def speed() -> int:
    """
    Source: <https://tetris.fandom.com/wiki/Tetris_(NES,_Nintendo)>
    level   speed (frames/fall)
    0	    48
    1	    43
    2	    38
    3	    33
    4	    28
    5	    23
    6	    18
    7	    13
    8	    8
    9	    6
    10–12	5
    13–15	4
    16–18	3
    19–28	2
    29+	    1

    (simplified)
    level   speed (frames/fall)
    00-08   48 - (5 x level)
    09-21   5 - ( (level - 10) // 3)
    22–28	2
    29+	    1
    """

    match (level := GlobalVars.current_level):
        case _ if 0 <= level <= 8:
            return 48 - (5 * level)
        case _ if 9 <= level <= 21:
            return 5 - ((level - 10) // 3)
        case _ if 22 <= level <= 28:
            return 2
        case _ if level >= 29:
            return 1
