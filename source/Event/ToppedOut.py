import pygame

from Process import Button
from Event import GameOver, Pause
from Game import Loop
from Setup import Constants as c, GlobalVars as gv, Colours, GameInit

restart: bool = False


def restart_() -> None:
    global restart
    restart = True


def create_buttons() -> None:
    text = ("Restart" , "Quit"           , "x"                  )
    locs = ((-100, 20), (100, 20)        , (0, 90)              )
    func = (restart_  , GameOver.quit_all, Pause.toggle_graphics)
    size = ([(150, 50)] * 2) + [(250, 50)]

    def_loc = (c.SCREEN_SIZE[0]/2, c.SCREEN_SIZE[1]/2)

    for i in range(3):
        Button.Button(
            (def_loc[0]+locs[i][0], def_loc[1]+locs[i][1]),
            size[i],
            text[i],
            func[i]
        )


def run(screen: pygame.Surface, clock: pygame.time.Clock):
    gv.game_running = False
    gv.outro_running = True
    global restart
    restart = False

    rect: pygame.Rect = pygame.Rect(0, 0, 640, 280)
    rect.center = (c.SCREEN_SIZE[0]/2, c.SCREEN_SIZE[1]/2)

    create_buttons()

    while gv.outro_running:
        GameOver.quit_pressed(pygame.event.get())

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            Pause.resume()
        if keys[pygame.K_ESCAPE]:
            restart_()
        if keys[pygame.K_m]:
            pygame.mixer.music.pause() if not gv.is_music_paused else None
            gv.is_music_paused = True

        if restart or not gv.outro_running:
            break

        pygame.draw.rect(screen, Colours.D_GRAY, rect, border_radius=25)
        pygame.draw.rect(screen, Colours.BORDER, rect, 5, 25)

        is_new_high_score: bool = gv.score > gv.prev_high_score

        title_text = c.LARGE_FONT.render(
            "New High Score!" if is_new_high_score else "Game Over",
            True,
            Colours.WHITE
        )
        title_text_rect = title_text.get_rect()
        title_text_rect.center = (c.SCREEN_SIZE[0]/2, (c.SCREEN_SIZE[1]/2) - 70)
        screen.blit(title_text, title_text_rect)

        for button in Button.all_buttons:
            if button.onclickFunction == Pause.toggle_music:
                button.text = "Play Music" if gv.is_music_paused else "Mute Music"
            elif button.onclickFunction == Pause.toggle_graphics:
                button.text = "Modern Blocks" if gv.using_classic_skin else "Classic Blocks"

            button.process(screen)

        pygame.display.update()

    Button.reset()
    GameInit.init()
    Loop.run(screen, clock)
