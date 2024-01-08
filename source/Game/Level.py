import math

from Setup import GlobalVars


def speed():
    # match (level := GlobalVars.current_level):
    #     case _ if 0 <= level < 10:
    #         return 1
    #     case _ if 10 <= level < 20:
    #         return 2
    #     case _ if 20 <= level < 30:
    #         return 3
    #     case _ if 30 <= level < 40:
    #         return 4

    # How many times per second a block should fall
    return math.ceil((GlobalVars.current_level+1)/10)
