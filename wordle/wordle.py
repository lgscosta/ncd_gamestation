import pygame
import random

# Dicionário de palavras
dicionario = [
    "abacaxi",
    "abacate",
    "abóbora",
    "abóbora",
    "abóbora",
]

# Inicializa o Pygame
pygame.init()

# Cria a tela do jogo
tela = pygame.display.set_mode((500, 500))

# Cria o tabuleiro do jogo
tabuleiro = []
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(pygame.Surface((100, 100)))
    tabuleiro.append(linha)

# Gera uma palavra aleatória
palavra_secreta = dicionario[random.randint(0, len(dicionario) - 1)]

# Inicia o jogo
rodada = 1
while True:
    # Desenha o tabuleiro na tela
    for i in range(5):
        for j in range(5):
            tabuleiro[i][j].fill((255, 255, 255))
            tela.blit(tabuleiro[i][j], (i * 100, j * 100))

    # Mostra a mensagem de rodada
    tela.blit(pygame.font.SysFont("Arial", 20).render(f"Rodada {rodada}", True, (0, 0, 0)), (200, 10))

    # Lê a entrada do jogador
    palavra_inserida = input("Digite uma palavra de cinco letras: ")

    # Verifica se a palavra é válida
    if len(palavra_inserida) != 5:
        print("A palavra deve ter cinco letras.")
        continue

    # Verifica se a palavra é correta
    if palavra_inserida == palavra_secreta:
        print("Parabéns! Você acertou a palavra secreta!")
        break

    # Fornece feedback ao jogador
    for i in range(5):
        for j in range(5):
            if palavra_inserida[i] == palavra_secreta[i]:
                tabuleiro[i][j].fill((0, 255, 0))
            elif palavra_inserida[i] in palavra_secreta:
                tabuleiro[i][j].fill((255, 255, 0))
            else:
                tabuleiro[i][j].fill((255, 0, 0))

    # Atualiza a rodada
    rodada += 1

    # Atualiza a tela
    pygame.display.update()

# Finaliza o Pygame
pygame.quit()
