import pygame

from Game import Loop
from Setup import Constants as c, GameInit

# Set up pygame
pygame.init()
screen: pygame.Surface = pygame.display.set_mode(c.SCREEN_SIZE)
clock: pygame.time.Clock = pygame.time.Clock()

# Set up game
GameInit.init()
# Run game
Loop.run(screen, clock)

