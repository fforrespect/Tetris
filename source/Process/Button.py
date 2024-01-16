import pygame

from Setup import Constants as c


class Button:
    def __init__(self, loc, size, button_text='Button', onclick_function=None, one_press=True):
        self.x, self.y = loc
        self.width, self.height = size
        self.onclickFunction = onclick_function
        self.onePress = one_press

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = c.SMALL_FONT.render(button_text, True, (20, 20, 20))

        self.alreadyPressed = False

    def process(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        color = self.fillColors['normal']

        if self.buttonRect.collidepoint(mouse_pos):
            color = self.fillColors['hover']

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                color = self.fillColors['pressed']

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        self.buttonSurface.fill((0, 0, 0, 0))
        pygame.draw.rect(self.buttonSurface, color, (0, 0, self.width, self.height), border_radius=10)

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])

        screen.blit(self.buttonSurface, self.buttonRect)
