import pygame

from Event import GameOver
from Game import Loop
from Process import Button
from Setup import GlobalVars as gv, Constants as c, Colours, GameInit


def check(screen: pygame.Surface, clock: pygame.time.Clock):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
        run(screen, clock)


def resume():
    gv.pause_running = False


def run(screen: pygame.Surface, clock: pygame.time.Clock):
    gv.game_running = False
    gv.pause_running = True

    restart: bool = False

    rect: pygame.Rect = pygame.Rect(0, 0, 640, 280)
    rect.center = (c.SCREEN_SIZE[0]/2, c.SCREEN_SIZE[1]/2)

    buttons = (
        Button.Button((30, 30), (400, 100), 'Resume', resume),
        Button.Button((30, 30), (400, 100), 'Quit', GameOver.quit_all),

    )

    while gv.pause_running:
        GameOver.quit_pressed(pygame.event.get())

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            break
        if keys[pygame.K_ESCAPE]:
            restart = True
            break
        if keys[pygame.K_m]:
            pygame.mixer.music.unpause() if gv.is_music_paused else None
            gv.is_music_paused = False
        if keys[pygame.K_n]:
            pygame.mixer.music.pause() if not gv.is_music_paused else None
            gv.is_music_paused = True

        pygame.draw.rect(screen, Colours.D_GRAY, rect, border_radius=25)
        pygame.draw.rect(screen, Colours.BORDER, rect, 5, 25)

        title_text = c.LARGE_FONT.render(
            "Paused",
            True,
            Colours.WHITE
        )
        title_text_rect = title_text.get_rect()
        title_text_rect.center = (c.SCREEN_SIZE[0]/2, (c.SCREEN_SIZE[1]/2) - 50)
        screen.blit(title_text, title_text_rect)


        # text2 = c.SMALL_FONT.render(
        #     "Press 'ENTER' to resume",
        #     True,
        #     Colours.WHITE
        # )
        # text2_rect = text2.get_rect()
        # text2_rect.center = (c.SCREEN_SIZE[0]/2, (c.SCREEN_SIZE[1]/2) + 40)
        # screen.blit(text2, text2_rect)
        #
        # text3 = c.SMALL_FONT.render(
        #     "Press 'ESC' to restart",
        #     True,
        #     Colours.WHITE
        # )
        # text3_rect = text3.get_rect()
        # text3_rect.center = (c.SCREEN_SIZE[0]/2, (c.SCREEN_SIZE[1]/2) + 65)
        # screen.blit(text3, text3_rect)
        #
        # text3 = c.SMALL_FONT.render(
        #     "Press '" + ("M' to play" if gv.is_music_paused else "N' to pause") + " the music",
        #     True,
        #     Colours.WHITE
        # )
        # text3_rect = text3.get_rect()
        # text3_rect.center = (c.SCREEN_SIZE[0]/2, (c.SCREEN_SIZE[1]/2) + 90)
        # screen.blit(text3, text3_rect)


        for button in buttons:
            button.process(screen)

        pygame.display.update()

    gv.game_running = True
    gv.pause_running = False

    if restart:
        GameInit.init()
        Loop.run(screen, clock)
