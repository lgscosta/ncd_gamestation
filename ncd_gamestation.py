import pygame
import sys
import os

# Inicialização do Pygame
pygame.init()

# Configurações da screen
width = 650
heigth = 800
screen = pygame.display.set_mode((width, heigth))
icon = pygame.image.load("img/gamestation.png")
icon = pygame.transform.scale_by(icon, 0.6)
pygame.display.set_caption("NCD GameStation")
pygame.display.set_icon(icon)

# Cores
purple = "#a2185b"
cor_botao = (50, 50, 50)
yellow = "#f4ad42"
red = "#c73d52"
green = "#bcd246"
blue = "#4b8fbd"
white = "#ffffff"

screen.fill(purple)

cid = pygame.image.load("img/gamestation_cid.png")
cid = pygame.transform.scale_by(cid, 0.3)
cid_frame = cid.get_rect(center=(320,150))
screen.blit(cid, cid_frame)

wordle = pygame.image.load("img/wordle2.png")
wordle = pygame.transform.scale_by(wordle, 0.09)
wordle_frame = wordle.get_rect(center=(325,300))
screen.blit(wordle, wordle_frame)


forca = pygame.image.load("img/forca.png")
forca = pygame.transform.scale_by(forca, 0.09)
forca_frame = forca.get_rect(center=(325,480))
screen.blit(forca, forca_frame)

# font e tamanho
font_normal = pygame.font.Font("font/Montserrat-Black.otf", 36)
font_rules = pygame.font.Font("font/Montserrat-Black.otf", 20)

# Função para desenhar botões
def desenhar_botao(x, y, largura, altura, texto, acao=None):
    if texto == "Regras":
        pygame.draw.rect(screen, white, (x, y, largura, altura))
        texto_surface = font_rules.render(texto, True, purple)
    
    elif texto == "Clássico":
        if y == 350:
            pygame.draw.rect(screen, green, (x, y, largura, altura))
            texto_surface = font_normal.render(texto, True, white)
        else:
            pygame.draw.rect(screen, yellow, (x, y, largura, altura))
            texto_surface = font_normal.render(texto, True, white)

    elif texto == "Multiplayer":
        pygame.draw.rect(screen, red, (x, y, largura, altura))
        texto_surface = font_normal.render(texto, True, white)
    else:
        pygame.draw.rect(screen, blue, (x, y, largura, altura))
        texto_surface = font_normal.render(texto, True, white)

    texto_retangulo = texto_surface.get_rect(center=(x + largura / 2, y + altura / 2))
    screen.blit(texto_surface, texto_retangulo)

    # Verifica se o botão foi clicado
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click, _, _ = pygame.mouse.get_pressed()

    if x < mouse_x < x + largura and y < mouse_y < y + altura:
        if click == 1 and acao:
            acao()

def executar_wordle_classico():
    os.system("python3 regras_wordle_classico.py")

def executar_wordle_dueto():
    os.system("python3 regras_wordle_dueto.py")

# Função para executar wordle2.py
def executar_forca_classico():
    os.system("python3 regras_wordle_classico.py")

# Função para executar regras.py
def executar_forca_dueto():
    os.system("python3 regras_wordle_classico.py")

# Loop principal
while True:
    # screen.fill(purple)

    # Desenha os botões
    desenhar_botao(65, 350, 250, 70, "Clássico", executar_wordle_classico)
    desenhar_botao(335, 350, 250, 70, "Dueto", executar_wordle_dueto)
    desenhar_botao(65, 530, 250, 70, "Clássico", executar_wordle_classico)
    desenhar_botao(335, 530, 250, 70, "Multiplayer", executar_forca_classico)
    desenhar_botao(275, 670, 100, 50, "Regras", executar_forca_dueto)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
