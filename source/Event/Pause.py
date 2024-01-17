import pygame

from Event import GameOver
from Game import Loop
from Process import Button
from Setup import GlobalVars as gv, Constants as c, Colours, GameInit

restart: bool = False

def check(screen: pygame.Surface, clock: pygame.time.Clock) -> None:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
        run(screen, clock)


def resume() -> None:
    gv.pause_running = False
    Button.reset()

def restart_() -> None:
    global restart
    restart = True
    Button.reset()

def toggle_music() -> None:
    pygame.mixer.music.unpause() if gv.is_music_paused else pygame.mixer.music.pause()
    gv.is_music_paused = not gv.is_music_paused

def toggle_graphics() -> None:
    gv.using_classic_skin = not gv.using_classic_skin


def create_buttons() -> None:
    text = ("Resume"   , "Restart", "Quit"           , "x"         , "x"            )
    locs = ((-200, 20) , (0, 20)  , (200, 20)        , (-150, 90)  , (150, 90)      )
    func = (resume     , restart_ , GameOver.quit_all, toggle_music, toggle_graphics)
    size = ([(150, 50)] * 3) + ([(250, 50)] * 2)

    def_loc = (c.SCREEN_SIZE[0]/2, c.SCREEN_SIZE[1]/2)

    for i in range(5):
        Button.Button(
            (def_loc[0]+locs[i][0], def_loc[1]+locs[i][1]),
            size[i],
            text[i],
            func[i]
        )


def run(screen: pygame.Surface, clock: pygame.time.Clock):
    gv.game_running = False
    gv.pause_running = True

    global restart
    restart = False

    rect: pygame.Rect = pygame.Rect(0, 0, 640, 280)
    rect.center = (c.SCREEN_SIZE[0]/2, c.SCREEN_SIZE[1]/2)

    create_buttons()

    while gv.pause_running:
        GameOver.quit_pressed(pygame.event.get())

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            resume()
        if keys[pygame.K_ESCAPE]:
            restart_()
        if keys[pygame.K_m]:
            pygame.mixer.music.pause() if not gv.is_music_paused else None
            gv.is_music_paused = True

        if restart or not gv.pause_running:
            break

        pygame.draw.rect(screen, Colours.D_GRAY, rect, border_radius=25)
        pygame.draw.rect(screen, Colours.BORDER, rect, 5, 25)

        title_text = c.LARGE_FONT.render(
            "Paused",
            True,
            Colours.WHITE
        )
        title_text_rect = title_text.get_rect()
        title_text_rect.center = (c.SCREEN_SIZE[0]/2, (c.SCREEN_SIZE[1]/2) - 70)
        screen.blit(title_text, title_text_rect)

        for button in Button.all_buttons:
            if button.onclickFunction == toggle_music:
                button.text = "Play Music" if gv.is_music_paused else "Mute Music"
            elif button.onclickFunction == toggle_graphics:
                button.text = "Modern Blocks" if gv.using_classic_skin else "Classic Blocks"

            button.process(screen)

        pygame.display.update()

    gv.game_running = True
    gv.pause_running = False

    if restart:
        GameInit.init()
        Loop.run(screen, clock)
