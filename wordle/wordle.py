import pygame
import sys
import random
from letter import Letter
from indicator import Indicator

# Variáveis Globais
guesses_count = 0
guesses = [[]] * 6
current_guess = []
current_guess_string = ""
current_letter_bg_x = 110
indicators = []
game_result = ""

def wordle_main(dictionary):
    pygame.init()

    WORDS = []
    MEANNINGS = []

    for i in dictionary.keys():
        WORDS.append(i)

    for i in dictionary.values():
        MEANNINGS.append(i)

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

    # Escolha da palavra no dicionário
    correct_word = random.choice(WORDS)
    correct_meanning = ""

    index = 0
    for i in WORDS:
        if i == correct_word:
            correct_meanning = MEANNINGS[index]
            break
        index += 1
        
    # Inicialização da tela
    screen.fill(blue)
    screen.blit(bg, bg_frame)
    screen.blit(wordle, wordle_frame)
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
        indicator_x = 123

        for letter in "ASDFGHJKL":
            new_indicator = Indicator(indicator_x, indicator_y, letter)
            indicators.append(new_indicator)
            new_indicator.draw()
            indicator_x += 43
        indicator_y += 46
        indicator_x = 165

        for letter in "ZXCVBNM":
            new_indicator = Indicator(indicator_x, indicator_y, letter)
            indicators.append(new_indicator)
            new_indicator.draw()
            indicator_x += 43

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
        pygame.draw.rect(screen, blue, (10, 70, 1000, 800))
        play_again_font = pygame.font.Font("font/Montserrat-Black.otf", 40)
        meanning_font = pygame.font.Font("font/Montserrat-Black.otf", 30)

        play_again_text = play_again_font.render("Aperte ENTER para jogar!", True, "white")
        play_again_rect = play_again_text.get_rect(center=(width/2, 700))

        word_was_text = play_again_font.render(f"The word was {correct_word}!", True, "white")
        word_was_rect = word_was_text.get_rect(center=(width/2, 100))

        meanning_was_text = meanning_font.render(f"The meanning was {correct_meanning}!", True, "white")
        meanning_was_rect = meanning_was_text.get_rect(center=(width/2, 200))
        meanning_was_rect.left = 50

        screen.blit(word_was_text, word_was_rect)
        screen.blit(meanning_was_text, meanning_was_rect)
        screen.blit(play_again_text, play_again_rect)
        pygame.display.update()

    def reset():
        # Resets all global variables to their default states.
        global guesses_count, correct_word, guesses, current_guess, current_guess_string, game_result
        screen.fill(blue)
        screen.blit(bg, bg_frame)
        screen.blit(wordle, wordle_frame)
        initialize_indicators()
        guesses_count = 0
        guesses = [[]] * 6
        current_guess = []
        current_guess_string = ""
        game_result = ""
        pygame.display.update()

    def create_new_letter():
        # Creates a new letter and adds it to the guess.
        global current_guess_string, current_letter_bg_x
        current_guess_string += key_pressed
        new_letter = Letter(key_pressed, (current_letter_bg_x, guesses_count*100+Letter.letter_y_spacing+60))
        current_letter_bg_x += Letter.letter_x_spacing
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
        current_letter_bg_x -= Letter.letter_x_spacing

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
                        correct_word = random.choice(WORDS)
                        index = 0
                        for i in WORDS:
                            if i == correct_word:
                                correct_meanning = MEANNINGS[index]
                                break
                            index += 1
                    else:
                        if len(current_guess_string) == 5:
                            check_guess(current_guess)
                elif event.key == pygame.K_BACKSPACE:
                    if len(current_guess_string) > 0:
                        delete_letter()
                elif event.key == pygame.K_ESCAPE:
                    pygame.display.quit()
                    pygame.quit()
                    return
                else:
                    key_pressed = event.unicode.upper()
                    if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                        if len(current_guess_string) < 5:
                            create_new_letter()