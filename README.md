# NCD GameStation

## Instalação

Para instalar o jogo, você precisará de uma instalação do Python 3 e da biblioteca Pygame.

Para instalar o Python 3, siga estas etapas:

1. Abra um terminal ou prompt de comando.
2. Execute o seguinte comando:

```python3 -m pip install python```


Para instalar a biblioteca Pygame, siga estas etapas:

1. Abra um terminal ou prompt de comando.
2. Execute o seguinte comando:

```python3 -m pip install pygame```

# Wordle
Um jogo de adivinhação de palavras de cinco letras.

## Executando o Jogo
```python3 ncd_gamestation.py```

## Primeira Entrega (E1)
Versão inicial, contendo apenas as seguintes funcionalidades:
- [x] O jogo deve escolher uma palavra aleatória de cinco letras a partir de um dicionário de palavras pré-definido.
- [x] Uma palavra deve ser exibida em um tabuleiro de 6x5, com cada letra em uma caixa.
- [x] O jogador deve poder inserir uma palavra de cinco letras no tabuleiro.

## Segunda Entrega (E2)
- [x] O jogo deve ter uma interface gráfica completa.
- [x] O feedback deve ser exibido em cada caixa da palavra, indicando se a letra está correta, na posição correta ou na palavra, mas na posição errada.
- [x] O jogo deve conter um mostrador na parte inferior das letras já utilizadas.

## Terceira Entrega (E3)
- [x] O jogo deve ter um dicionário de palavras de 5 letras que tenha conceitos de cidadania digital.
- [x] O jogo deve mostrar uma mensagem de vitória ou derrota quando o jogador adivinhar a palavra ou esgotar suas tentativas e o significado da palavra.

## Entrega Extra (E4)
- [x] O jogo deve ter uma versão de dueto, onde tenta-se adivinhar duas palavras simultaneamente.
- [x] O jogo deve ter uma plataforma de entrada dos modos.

## Como jogar
O jogo é simples: você tem seis tentativas para adivinhar uma palavra de cinco letras. Cada vez que você insere uma palavra, o jogo fornece feedback sobre a posição e a presença das letras na palavra secreta.

- <b style="color: #bcd246">Verde:</b> A letra está na palavra e na posição correta.
- <b style="color: #f4ad42">Amarelo:</b> A letra está na palavra, mas na posição errada.
- <b style="color: #c73d52">Vermelho:</b> A letra não está na palavra.
Se você adivinhar a palavra corretamente antes de esgotar suas tentativas, você vence!

## Desenvolvedor
- Luana Gabriele de Sousa Costa

### Limitações Relevantes:
- O jogo tem problema com acentos.
- O jogo é pesado.
- Os elementos da tela são fixos, não permitindo o redimensionamento da tela.

### Propostas de Melhoria:
- O jogo poderia aceitar caracteres especiais (acentos).
- O jogo poderia ser mais leve, ele utiliza muito do processador.
- O jogo poderia conter dicas, mesmo não sendo algo do jogo original, em contexto educativo seria útil.
- O jogo poderia ter a tela redimensionável.
- O jogo poderia fazer algum tipo de filtro de palavras (no momento só reconhece letras, não sabendo se são palavras ou não).
- O jogo poderia ter uma melhor modularização do código.
- O jogo poderia conter uma interação com os indicadores (teclado) que há embaixo (vários colegas que testaram o jogo tentaram clicar nas letras ao invés de digitar).
- A plataforma poderia conter mais jogos.
- Poderia ser criado um novo modo: quarteto.
- O jogo poderia ter bancos de palavras separados por tema, permitindo a escolha de tema no início.


# Jogo da Forca
Um jogo de adivinhação de palavras de cinco letras.

## Executando o Jogo
```python3 ncd_gamestation.py```

## Primeira Entrega (E1)
Versão inicial, contendo apenas as seguintes funcionalidades:
- [x] O jogo deve escolher uma palavra aleatória a partir de uma pequena lista de palavras.
- [x] A tela de jogo deve ser exibida com as casas das letras, um espaço para letras usadas e a saúde do jogador na forca
- [x] O jogador pode chutar letras, uma a uma.
- [x] Há uma resposta visual para erros e acertos

## Segunda Entrega (E2)
- [x] As palavras são escolhidas a partir de um arquivo banco de palavras.
- [x] Ao ganhar uma partida será exibida a definição formal da palavra.

## Terceira Entrega (E3)
- [ ] jogador pode escolher iniciar um novo jogo sem precisar abrir novamente o programa e há um menu.
- [ ] Serão adicionados novos modos de jogo (casual, contra o tempo, N partidas em sequência)

## Entrega Extra (E4)
- [ ] Há um modo com pontuação e um ranking geral dos melhores jogadores.
- [ ] Há um modo multiplayer local time attack

## Como jogar
O jogo é simples: você tem um numero X de vidas para adivinhar uma palavra. Cada cada erro consome uma vida e ao zerar você perde, o jogo fornece feedback sobre acertos e erros.
Se você adivinhar a palavra corretamente antes de esgotar suas vidas, você vence!

## Desenvolvedor
- Gabriel Luiz de Oliveira Paschoal
