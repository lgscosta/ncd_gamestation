import pygame
import sys
import os

# Inicializa o Pygame
pygame.init()

# Define as dimensões da janela
width = 650
height = 800

# Cria a janela
screen = pygame.display.set_mode((width, height))
icon = pygame.image.load("img/rules.png")
icon = pygame.transform.scale_by(icon, 0.6)
pygame.display.set_icon(icon)
pygame.display.set_caption("Pygame Page")

# Carrega o wallpaper
wallpaper = pygame.image.load("img/regras_f_classico.png")
wallpaper = pygame.transform.scale(wallpaper, (width, height))

# Define a fonte para o texto
font = pygame.font.Font(None, 36)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Executa o arquivo "wordle.py"
                # os.system("python3 wordle.py")
                pygame.quit()
                sys.exit()

    # Renderiza o wallpaper
    screen.blit(wallpaper, (0, 0))

    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
sys.exit()
