import pygame
import random

# Define as cores
AMARELO = (255, 255, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
CINZA = (128, 128, 128)
VERMELHO = (255,20,147)

# Define o tamanho da janela
LARGURA = 400
ALTURA = 400

# Inicializa o PyGame
pygame.init()

# Cria a janela
janela = pygame.display.set_mode((LARGURA, ALTURA))

# Define o título da janela
pygame.display.set_caption("Wordle - NCD GameStation")

# Define a fonte
fonte = pygame.font.Font(None, 20)

# Carrega a lista de palavras
palavras = ["ramon", "luana", "seila", "ncdcd", "teste"]

# Gera uma palavra aleatória
palavra_secreta = random.choice(palavras)

# Define as letras da palavra secreta
letras_secretas = []
for letra in palavra_secreta:
    letras_secretas.append("_")

# Define as letras já adivinhadas
letras_adivinhadas = []

# Define o número de tentativas
tentativas = 6

# Loop principal do jogo
while True:
    # Limpa a tela
    janela.fill(CINZA)

    # Desenha a palavra secreta
    for i, letra in enumerate(letras_secretas):
        texto = fonte.render(letra, True, AZUL)
        pygame.draw.rect(janela, AMARELO, (i * 40, 100, 40, 40))
        janela.blit(texto, (i * 40 + 10, 110))

    # Desenha as letras já adivinhadas
    for i, letra in enumerate(letras_adivinhadas):
        texto = fonte.render(letra, True, VERDE)
        pygame.draw.rect(janela, AZUL, (i * 40, 200, 40, 40))
        janela.blit(texto, (i * 40 + 10, 210))

    # Desenha o feedback da última tentativa
    for i, letra in enumerate(letras_secretas):
        if letra in letras_adivinhadas:
            if letra == letras_secretas[i]:
                cor = VERDE
            else:
                cor = AZUL
            texto = fonte.render(letra, True, cor)
            pygame.draw.rect(janela, cor, (i * 40, 300, 40, 40))
            janela.blit(texto, (i * 40 + 10, 310))

    # Verifica se o jogo terminou
    if tentativas == 0 or "_" not in letras_secretas:
        break

    # Captura os eventos do teclado
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif evento.type == pygame.KEYDOWN:
            # Adiciona a letra à lista de letras já adivinhadas
            letras_adivinhadas.append(evento.unicode)
            tentativas -= 1

    # Atualiza a tela
    pygame.display.update()

# # Exibe a mensagem de vitória ou derrota
# if "_" not in letras_secretas:
#     text = "Você venceu!"
#     cor = VERDE
# else:
#     text = "Você perdeu!"
#     cor = VERMELHO
# texto = fonte.render(text, True, cor)
# janela.blit(texto, (100, 400))
# pygame.display.update()

# Aguarda o usuário pressionar uma tecla
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
