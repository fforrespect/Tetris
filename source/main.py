import pygame

from Game import Initialise, Loop
from Setup import Constants as c

# Set up pygame
pygame.init()
screen: pygame.Surface = pygame.display.set_mode(c.SCREEN_SIZE)
clock: pygame.time.Clock = pygame.time.Clock()

# Set up game
Initialise.init()
# Run game
Loop.run(screen, clock)

