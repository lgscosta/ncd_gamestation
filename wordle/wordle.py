import pygame

# Inicializa o PyGame
pygame.init()

# Cria uma janela
tela = pygame.display.set_mode((600, 600))

# Define a cor de fundo
cor_fundo = (200, 200, 200)

#  Cria o texto
texto = pygame.font.SysFont("Arial", 20)

# Define a cor dos quadrados
cor_rosa = (255, 105, 180)

# Define a largura da margem
margem = 10

# Cria uma matriz de quadrados
quadrados = []

palavras = []
for i in range(5):
    for j in range(6):
        quadrados.append(pygame.Rect((i * 80 + margem, j * 80 + margem), (80 - 2 * margem, 80 - 2 * margem)))

# Loop principal
while True:
    # Processa os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Se o usuário pressionou `Enter`,
        # lê a string digitada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                for palavra in palavras:
                    palavra = pygame.event.wait().text.strip()

    # Limpa a tela
    tela.fill(cor_fundo)

    # Desenha os quadrados
    for quadrado in quadrados:
        pygame.draw.rect(tela, cor_rosa, quadrado)
#        # Desenha o texto no meio do quadrado
        # tela.blit(texto.render("A", True, (255, 255, 255)), (quadrado.centerx-8, quadrado.centery-10))
        
    # for palavra in palavras:
    #     palavra = pygame.event.wait().text.strip()
        
    for palavra in palavras:
        for i in palavra:
            tela.blit(texto.render(i, True, (255, 255, 255)), (quadrado.centerx-8, quadrado.centery-10))

    # Atualiza a tela
    pygame.display.update()



####################


# import pygame

# # Inicializa o Pygame
# pygame.init()

# # Cria a tela
# tela = pygame.display.set_mode((640, 480))

# # Define a cor de fundo
# tela.fill((0, 0, 0))

# # Cria o quadrado
# quadrado = pygame.Rect((320, 240), (100, 100))

# # Desenha o quadrado
# pygame.draw.rect(tela, (255, 255, 255), quadrado)

# # Cria o texto
# texto = pygame.font.SysFont("Arial", 50)

# # Desenha o texto no meio do quadrado
# tela.blit(texto.render("A", True, (255, 0, 0)), (quadrado.centerx, quadrado.centery))

# # Atualiza a tela
# pygame.display.update()

# # Loop principal
# while True:
#     for event in pygame.event.get():
#         # Verifica se o usuário fechou a janela
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

