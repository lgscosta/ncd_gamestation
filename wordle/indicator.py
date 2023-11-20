import pygame
from wordle.wordle import wordle
from letter import Letter
# Constantes
width = 650
height = 800

# Cores 
green = "#bcd246"
yellow = "#f4ad42"
red = "#c73d52"
grey = "#787c7e"
outline = "#d3d6da"
blue = "#4b8fbd"

# Definição da fonte usada no NCD
guessed_letter_font = pygame.font.Font("font/Montserrat-Black.otf", 50)
availabe_letter_font = pygame.font.Font("font/Montserrat-Black.otf", 25)

# screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
screen = pygame.display.set_mode((width, height))
wordle = pygame.image.load("img/wordle.png")
wordle = pygame.transform.scale_by(wordle, 0.1)
wordle_frame = wordle.get_rect(center=(318,30))
bg = pygame.image.load("img/background.png")
bg_frame = bg.get_rect(center=(318, 361))

icon = pygame.image.load("img/gameStation.png")
icon = pygame.transform.scale_by(icon, 0.6)
pygame.display.set_caption("Wordle - NCD GameStation")
pygame.display.set_icon(icon)

class Indicator:
        def __init__(self, x, y, letter):
            # Initializes variables such as color, size, position, and letter.
            self.x = x
            self.y = y
            self.text = letter
            self.rect = (self.x, self.y, 40, 40)
            self.bg_color = outline

        def draw(self):
            # Puts the indicator and its text on the screen at the desired position.
            pygame.draw.rect(screen, self.bg_color, self.rect, 0, 3)
            self.text_surface = Letter.availabe_letter_font.render(self.text, True, "white")
            self.text_rect = self.text_surface.get_rect(center=(self.x+20, self.y+20))
            screen.blit(self.text_surface, self.text_rect)
            pygame.display.update()