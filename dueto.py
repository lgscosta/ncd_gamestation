import pygame
import sys
import random
from dictionary.words import *

# Espaçamento e tamanho de letra 
letter_x_spacing = 85
letter_y_spacing = 12

# letter_x_spacing2 = 85
# letter_y_spacing2 = 12

letter_size = 75

# Variáveis Globais
guesses_count = 0
guesses_count2 = 0
guesses = [[]] * 6
guesses2 = [[]] * 6
current_guess = []
current_guess2 = []
current_guess_string = ""
current_letter_bg_x = 200
current_letter_bg_x2 = 700
indicators = []
indicators2 = []
game_result = ""
game_result2 = ""


dicty = wordle_dict()

pygame.init()

WORDS = []
MEANNINGS = []

for i in dicty.keys():
    WORDS.append(i)

for i in dicty.values():
    MEANNINGS.append(i)

# Constantes
width = 1300
height = 800

# Cores 
green = "#bcd246"
yellow = "#f4ad42"
red = "#c73d52"
grey = "#787c7e"
outline = "#d3d6da"
blue = "#4b8fbd"
blue2 = "#77c6ff"
blue3 = "#144970"
blue4 = "#0d2b3b"


# Definição da fonte usada no NCD
guessed_letter_font = pygame.font.Font("font/Montserrat-Black.otf", 50)
availabe_letter_font = pygame.font.Font("font/Montserrat-Black.otf", 25)

# screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
screen = pygame.display.set_mode((width, height))
wordle = pygame.image.load("img/wordle.png")
wordle = pygame.transform.scale_by(wordle, 0.1)
wordle_frame = wordle.get_rect(center=(656,30))
bg = pygame.image.load("img/background.png")
bg_frame = bg.get_rect(center=(908, 361))
bg2 = pygame.image.load("img/background.png")
bg2_frame = bg2.get_rect(center=(408, 361))

icon = pygame.image.load("img/w_classico.png")
icon = pygame.transform.scale_by(icon, 0.6)
pygame.display.set_caption("Wordle - NCD GameStation")
pygame.display.set_icon(icon)

# Escolha da palavra no dicionário
correct_word = random.choice(WORDS)
correct_meanning = ""

correct_word2 = random.choice(WORDS)
correct_meanning2 = ""

while correct_word2 == correct_word:
    correct_word2 = random.choice(WORDS)

index = 0
for i in WORDS:
    if i == correct_word:
        correct_meanning = MEANNINGS[index]
        break
    index += 1

index = 0
for i in WORDS:
    if i == correct_word2:
        correct_meanning2 = MEANNINGS[index]
        break
    index += 1
    
# Inicialização da tela
screen.fill(blue)
screen.blit(bg, bg_frame)
screen.blit(bg2, bg2_frame)
screen.blit(wordle, wordle_frame)
pygame.display.update()

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
        self.text_surface = availabe_letter_font.render(self.text, True, "white")
        self.text_rect = self.text_surface.get_rect(center=(self.x+20, self.y+20))
        screen.blit(self.text_surface, self.text_rect)
        pygame.display.update()

def initialize_indicators():
    # primeiro
    indicator_x = 192
    indicator_y = 660

    for letter in "QWERTYUIOP":
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators.append(new_indicator)
        new_indicator.draw()
        indicator_x += 43
    indicator_y += 46
    indicator_x = 212

    for letter in "ASDFGHJKL":
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators.append(new_indicator)
        new_indicator.draw()
        indicator_x += 43
    indicator_y += 46
    indicator_x = 254

    for letter in "ZXCVBNM":
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators.append(new_indicator)
        new_indicator.draw()
        indicator_x += 43

    # segundo
    indicator_x = 694
    indicator_y = 660

    for letter in "QWERTYUIOP":
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators2.append(new_indicator)
        new_indicator.draw()
        indicator_x += 43
    indicator_y += 46
    indicator_x = 714

    for letter in "ASDFGHJKL":
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators2.append(new_indicator)
        new_indicator.draw()
        indicator_x += 43
    indicator_y += 46
    indicator_x = 756

    for letter in "ZXCVBNM":
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators2.append(new_indicator)
        new_indicator.draw()
        indicator_x += 43

def check_guess(guess_to_check, guess_to_check2):
    global current_guess, current_guess2, current_guess_string, guesses_count, guesses_count2, current_letter_bg_x, current_letter_bg_x2, game_result, game_result2
    game_decided = False
    game_decided2 = False

    # primeira palavra
    if game_result != "W":
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
    
    # segunda palavra
    if game_result2 != "W":
        for i in range(5):
            lowercase_letter = guess_to_check2[i].text.lower()
            if lowercase_letter in correct_word2:
                if lowercase_letter == correct_word2[i]:
                    guess_to_check2[i].bg_color = green
                    for indicator in indicators2:
                        if indicator.text == lowercase_letter.upper():
                            indicator.bg_color = green
                            indicator.draw()
                    guess_to_check2[i].text_color = "white"
                    if not game_decided2:
                        game_result2 = "W"
                else:
                    guess_to_check2[i].bg_color = yellow
                    for indicator in indicators2:
                        if indicator.text == lowercase_letter.upper():
                            indicator.bg_color = yellow
                            indicator.draw()
                    guess_to_check2[i].text_color = "white"
                    game_result2 = ""
                    game_decided2 = True
            else:
                guess_to_check2[i].bg_color = grey
                for indicator in indicators2:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = red
                        indicator.draw()
                guess_to_check2[i].text_color = "white"
                game_result2 = ""
                game_decided2 = True
            guess_to_check2[i].draw()
            pygame.display.update()

    guesses_count += 1
    guesses_count2 += 1
    current_guess = []
    current_guess2 = []
    current_guess_string = ""
    current_letter_bg_x = 200
    current_letter_bg_x2 = 700

    if guesses_count == 6 and (game_result == "" or game_result2 == ""):
        game_result = "L"
        game_result2 = "L"

def buffer_maker(meanning):
    base = meanning.split(" ")
    buffer = []
    sentence = ""
    first = 0
    last = len(base)

    for i in base:
        if len(i)+len(sentence)+1 <= 32:
            if first == 0:
                sentence = sentence + i
            else:
                sentence = sentence + " " + i
        else:
            buffer.append(sentence)
            sentence = ""
            sentence = sentence + i
        if last == first+1:
            buffer.append(sentence)

        first += 1

    return buffer

def play_again():
    pygame.draw.rect(screen, blue, (10, 70, 1300, 800))
    play_again_font = pygame.font.Font("font/Montserrat-Black.otf", 40)
    meanning_font = pygame.font.Font("font/Montserrat-Black.otf", 30)

    play_again_text = play_again_font.render("Aperte ENTER para jogar!", True, blue2)
    play_again_rect = play_again_text.get_rect(center=(width/2, 700))

    word_was_text = play_again_font.render(f"As palavras eram {correct_word} e {correct_word2}!", True, "white")
    word_was_rect = word_was_text.get_rect(center=(width/2, 410))

    word1_was_text = meanning_font.render(f"{correct_word.upper()}", True, blue4)
    word1_was_rect = word1_was_text.get_rect(center=(width/4, 480))

    word2_was_text = meanning_font.render(f"{correct_word2.upper()}", True, blue4)
    word2_was_rect = word1_was_text.get_rect(center=((3*width)/4, 480))

    meanning_buffer = buffer_maker(correct_meanning)
    count = 0

    for meanning in meanning_buffer:
        meanning_was_text = meanning_font.render(f"{meanning}", True, blue3)
        meanning_was_rect = meanning_was_text.get_rect(center=(width/4, 520+count))
        screen.blit(meanning_was_text, meanning_was_rect)
        count += 40

    # meanning_buffer = [correct_meanning2[i:i+32] for i in range(0, len(correct_meanning2), 32)]
    meanning_buffer = buffer_maker(correct_meanning2)

    count = 0

    for meanning in meanning_buffer:
        meanning_was_text = meanning_font.render(f"{meanning}", True, blue3)
        meanning_was_rect = meanning_was_text.get_rect(center=((3*width)/4, 520+count))
        screen.blit(meanning_was_text, meanning_was_rect)
        count += 40

    if game_result == "W" and game_result2 == "W" :
        won = pygame.image.load("img/won.png")
        won = pygame.transform.scale_by(won, 0.1)
        won_frame = won.get_rect(center=(650, 240))
        screen.blit(won, won_frame)
    else:
        lost = pygame.image.load("img/lost.png")
        lost = pygame.transform.scale_by(lost, 0.1)
        lost_frame = lost.get_rect(center=(650, 250))
        screen.blit(lost, lost_frame)

    screen.blit(word_was_text, word_was_rect)
    screen.blit(word1_was_text, word1_was_rect)
    screen.blit(word2_was_text, word2_was_rect)
    screen.blit(play_again_text, play_again_rect)
    pygame.display.update()

# ok
def reset():
    # Resets all global variables to their default states.
    global guesses_count, guesses_count2, correct_word, correct_word2, guesses, guesses2, current_guess, current_guess2, current_guess_string, game_result, game_result2
    screen.fill(blue)
    screen.blit(bg, bg_frame)
    screen.blit(bg2, bg2_frame)
    screen.blit(wordle, wordle_frame)
    initialize_indicators()
    guesses_count = 0
    guesses_count2 = 0
    guesses = [[]] * 6
    guesses2 = [[]] * 6
    current_guess = []
    current_guess2 = []
    current_guess_string = ""
    game_result = ""
    game_result2 = ""
    pygame.display.update()

# ok
def create_new_letter():
    # Creates a new letter and adds it to the guess.
    global current_guess_string, current_letter_bg_x, current_letter_bg_x2, game_result, game_result2
    current_guess_string += key_pressed

    if game_result != "W":
        new_letter = Letter(key_pressed, (current_letter_bg_x, guesses_count*100+letter_y_spacing+60))
        current_letter_bg_x += letter_x_spacing
        guesses[guesses_count].append(new_letter)
        current_guess.append(new_letter)
        for guess in guesses:
            for letter in guess:
                letter.draw()

    if game_result2 != "W":
        new_letter2 = Letter(key_pressed, (current_letter_bg_x2, guesses_count2*100+letter_y_spacing+60))
        current_letter_bg_x2 += letter_x_spacing
        guesses2[guesses_count2].append(new_letter2)
        current_guess2.append(new_letter2)
        for guess in guesses2:
            for letter in guess:
                letter.draw()

# ok
def delete_letter():
    # Deletes the last letter from the guess.
    global current_guess_string, current_letter_bg_x, current_letter_bg_x2, game_result, game_result2
    
    if game_result != "W":
        guesses[guesses_count][-1].delete()
        guesses[guesses_count].pop()
        current_guess_string = current_guess_string[:-1]
        current_guess.pop()
        current_letter_bg_x -= letter_x_spacing

    if game_result2 != "W":
        guesses2[guesses_count2][-1].delete()
        guesses2[guesses_count2].pop()
        current_guess2.pop()
        current_letter_bg_x2 -= letter_x_spacing

initialize_indicators()

while True:
    if game_result != "" and game_result2 != "":
        play_again()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RETURN:
                if game_result != "" and game_result2 != "":
                    reset()
                    correct_word = random.choice(WORDS)
                    index = 0
                    for i in WORDS:
                        if i == correct_word:
                            correct_meanning = MEANNINGS[index]
                            break
                        index += 1

                    correct_word2 = random.choice(WORDS)

                    while correct_word2 == correct_word:
                        correct_word2 = random.choice(WORDS)
                    
                    index = 0
                    for i in WORDS:
                        if i == correct_word2:
                            correct_meanning2 = MEANNINGS[index]
                            break
                        index += 1
                else:
                    if len(current_guess_string) == 5:
                        check_guess(current_guess, current_guess2)
            elif event.key == pygame.K_BACKSPACE:
                if len(current_guess_string) > 0:
                    delete_letter()
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                    if len(current_guess_string) < 5:
                        create_new_letter()