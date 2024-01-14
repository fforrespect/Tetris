import pygame

from Event import GameOver
from Game import Initialise, Loop
from Setup import Constants as c, GlobalVars as gv, Colours


def run(screen: pygame.Surface, clock: pygame.time.Clock):
    print("Topped out!")

    gv.game_running = False
    gv.outro_running = True

    small_font = pygame.font.Font(c.TFF_FP, 16)
    large_font = pygame.font.Font(c.TFF_FP, 38)

    rect: pygame.Rect = pygame.Rect(0, 0, 640, 280)
    rect.center = (c.SCREEN_SIZE[0]/2, c.SCREEN_SIZE[1]/2)

    while gv.outro_running:
        GameOver.quit_pressed(pygame.event.get())

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            break

        pygame.draw.rect(screen, Colours.D_GRAY, rect, border_radius=25)
        pygame.draw.rect(screen, Colours.BORDER, rect, 5, 25)

        title_text = large_font.render(
            "New High Score!" if gv.new_high_score else "Game Over",
            True,
            Colours.WHITE
        )
        title_text_rect = title_text.get_rect()
        title_text_rect.center = (c.SCREEN_SIZE[0]/2, (c.SCREEN_SIZE[1]/2) - 50)
        screen.blit(title_text, title_text_rect)

        secondary_text = small_font.render(
            "Press 'ENTER' to play again.",
            True,
            Colours.WHITE
        )
        secondary_text_rect = secondary_text.get_rect()
        secondary_text_rect.center = (c.SCREEN_SIZE[0]/2, (c.SCREEN_SIZE[1]/2) + 50)
        screen.blit(secondary_text, secondary_text_rect)

        pygame.display.update()

    Initialise.init()
    Loop.run(screen, clock)
