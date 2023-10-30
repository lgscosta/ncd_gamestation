import pygame
import sys
import random
from words import * # Dicionário de palavras (versão inicial)

pygame.init()

# Constantes
width = 650
height = 850
screen = pygame.display.set_mode((width, height))
wordle = pygame.image.load("wordle.png")
wordle = pygame.transform.scale_by(wordle, 0.1)
wordle_frame = wordle.get_rect(center=(318,30))
bg = pygame.image.load("camada2.png")
bg_frame = bg.get_rect(center=(318, 361))

icon = pygame.image.load("gameStation.png")
pygame.display.set_caption("Wordle - NCD GameStation")
pygame.display.set_icon(icon)

# Cores 
green = "#bcd246"
yellow = "#f4ad42"
red = "#c73d52"
grey = "#787c7e"
outline = "#d3d6da"
filled_outline = "#4b8fbd"

# Escolha da palavra no dicionário
correct_word = random.choice(WORDS)
print(correct_word) # Print da primeira escolha de palavra, já que não há verificação ainda

# Definição da fonte usada no NCD
guessed_letter_font = pygame.font.Font("Montserrat-Black.otf", 50)
availabe_letter_font = pygame.font.Font("Montserrat-Black.otf", 25)

# Inicialização da tela
screen.fill(filled_outline)
screen.blit(bg, bg_frame)
screen.blit(wordle, wordle_frame)
pygame.display.update()

# Espaçamento e tamanho de letra 
letter_x_spacing = 85
letter_y_spacing = 12
letter_size = 75

# Variáveis Globais
guesses_count = 0
guesses = [[]] * 6
current_guess = []
current_guess_string = ""
current_letter_bg_x = 110
indicators = []
game_result = ""

# Objeto Letra 
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
            pygame.draw.rect(screen, filled_outline, self.bg_rect, 3)
        self.text_surface = guessed_letter_font.render(self.text, True, self.text_color)
        screen.blit(self.text_surface, self.text_rect)
        pygame.display.update()

    # Função que deleta uma letra 
    def delete(self):
        # Fills the letter's spot with the default square, emptying it.
        pygame.draw.rect(screen, "white", self.bg_rect)
        pygame.draw.rect(screen, outline, self.bg_rect, 3)
        pygame.display.update()

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
        pygame.draw.rect(screen, self.bg_color, self.rect)
        self.text_surface = availabe_letter_font.render(self.text, True, "white")
        self.text_rect = self.text_surface.get_rect(center=(self.x+22, self.y+22))
        screen.blit(self.text_surface, self.text_rect)
        pygame.display.update()

def initialize_indicators():
    indicator_x = 103
    indicator_y = 660

    for letter in "QWERTYUIOP":
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators.append(new_indicator)
        new_indicator.draw()
        indicator_x += 43
    indicator_y += 46
    indicator_x = 81

    for letter in "ASDFGHJKL":
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators.append(new_indicator)
        new_indicator.draw()
        indicator_x += 43
    indicator_y += 46
    indicator_x = 136

    for letter in "ZXCVBNM":
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators.append(new_indicator)
        new_indicator.draw()
        indicator_x += 43
    # indicator_y += 51

def check_guess(guess_to_check):
    global current_guess, current_guess_string, guesses_count, current_letter_bg_x, game_result
    game_decided = False
    for i in range(5):
        lowercase_letter = guess_to_check[i].text.lower()
        if lowercase_letter in correct_word:
            if lowercase_letter == correct_word[i]:
                guess_to_check[i].bg_color = green
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = green
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                if not game_decided:
                    game_result = "W"
            else:
                guess_to_check[i].bg_color = yellow
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = yellow
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                game_result = ""
                game_decided = True
        else:
            guess_to_check[i].bg_color = grey
            for indicator in indicators:
                if indicator.text == lowercase_letter.upper():
                    indicator.bg_color = red
                    indicator.draw()
            guess_to_check[i].text_color = "white"
            game_result = ""
            game_decided = True
        guess_to_check[i].draw()
        pygame.display.update()
    
    guesses_count += 1
    current_guess = []
    current_guess_string = ""
    current_letter_bg_x = 110

    if guesses_count == 6 and game_result == "":
        game_result = "L"

def play_again():
    pygame.draw.rect(screen, filled_outline, (10, 660, 1000, 600))
    play_again_font = pygame.font.Font("Montserrat-Black.otf", 40)
    play_again_text = play_again_font.render("Aperte ENTER para jogar!", True, "white")
    play_again_rect = play_again_text.get_rect(center=(width/2, 700))
    screen.blit(play_again_text, play_again_rect)
    pygame.display.update()

def reset():
    # Resets all global variables to their default states.
    global guesses_count, correct_word, guesses, current_guess, current_guess_string, game_result
    screen.fill(filled_outline)
    screen.blit(bg, bg_frame)
    screen.blit(wordle, wordle_frame)
    initialize_indicators()
    guesses_count = 0

    correct_word = random.choice(WORDS)
    print(correct_word)
    
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    pygame.display.update()

def create_new_letter():
    # Creates a new letter and adds it to the guess.
    global current_guess_string, current_letter_bg_x
    current_guess_string += key_pressed
    new_letter = Letter(key_pressed, (current_letter_bg_x, guesses_count*100+letter_y_spacing+60))
    current_letter_bg_x += letter_x_spacing
    guesses[guesses_count].append(new_letter)
    current_guess.append(new_letter)
    for guess in guesses:
        for letter in guess:
            letter.draw()

def delete_letter():
    # Deletes the last letter from the guess.
    global current_guess_string, current_letter_bg_x
    guesses[guesses_count][-1].delete()
    guesses[guesses_count].pop()
    current_guess_string = current_guess_string[:-1]
    current_guess.pop()
    current_letter_bg_x -= letter_x_spacing

initialize_indicators()
while True:
    if game_result != "":
        play_again()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_result != "":
                    reset()
                else:
                    if len(current_guess_string) == 5:
                        check_guess(current_guess)
            elif event.key == pygame.K_BACKSPACE:
                if len(current_guess_string) > 0:
                    delete_letter()
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                    if len(current_guess_string) < 5:
                        create_new_letter()