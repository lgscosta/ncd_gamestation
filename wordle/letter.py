# Objeto Letra 
import pygame
import sys
import random
from wordle.wordle import wordle

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
guesses_count = 0
guesses = [[]] * 6
current_guess = []
current_guess_string = ""
current_letter_bg_x = 110
indicators = []
game_result = ""
# Definição da fonte usada no NCD
guessed_letter_font = pygame.font.Font("font/Montserrat-Black.otf", 50)
availabe_letter_font = pygame.font.Font("font/Montserrat-Black.otf", 25)

# Espaçamento e tamanho de letra
letter_x_spacing = 85
letter_y_spacing = 12
letter_size = 75

class Letter:
     
    def __init__(self, text, bg_position):
        # Initializes all the variables, including text, color, position, size, etc.
        self.bg_color = "white" # Cor de fundo da letra
        self.text_color = "black" # Cor da letra
        self.bg_position = bg_position # Posição do quadrado em relação ao fundo
        self.bg_x = bg_position[0] # Posição x
        self.bg_y = bg_position[1] # Posição y
        self.bg_rect = (bg_position[0], self.bg_y, letter_size, letter_size) # Quadrado da letra
        self.text = text # Conteúdo ou a letra em si
        self.text_position = (self.bg_x+36, self.bg_position[1]+34) # A posição da letra
        self.text_surface = guessed_letter_font.render(self.text, True, self.text_color) # Renderização da letra
        self.text_rect = self.text_surface.get_rect(center=self.text_position) # Retângulo delimitador

    # Função que aceita uma letra 
    def draw(self):
        pygame.draw.rect(screen, self.bg_color, self.bg_rect)
        if self.bg_color == "white":
            pygame.draw.rect(screen, blue, self.bg_rect, 3)
        self.text_surface = guessed_letter_font.render(self.text, True, self.text_color)
        screen.blit(self.text_surface, self.text_rect)
        pygame.display.update()

    # Função que deleta uma letra 
    def delete(self):
        # Fills the letter's spot with the default square, emptying it.
        pygame.draw.rect(screen, "white", self.bg_rect)
        pygame.draw.rect(screen, outline, self.bg_rect, 3)
        pygame.display.update()