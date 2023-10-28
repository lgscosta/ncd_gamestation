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
```python3 wordle.py```

## Primeira Entrega (E1)
Versão inicial, contendo apenas as seguintes funcionalidades:
1. O jogo deve escolher uma palavra aleatória de cinco letras a partir de um dicionário de palavras pré-definido.
2. Uma palavra deve ser exibida em um tabuleiro de 6x5, com cada letra em uma caixa.
3. O jogador deve poder inserir uma palavra de cinco letras no tabuleiro.

## Como jogar
O jogo é simples: você tem seis tentativas para adivinhar uma palavra de cinco letras. Cada vez que você insere uma palavra, o jogo fornece feedback sobre a posição e a presença das letras na palavra secreta.

- <b style="color: #bcd246">Verde:</b> A letra está na palavra e na posição correta.
- <b style="color: #f4ad42">Amarelo:</b> A letra está na palavra, mas na posição errada.
- <b style="color: #c73d52">Vermelho:</b> A letra não está na palavra.
Se você adivinhar a palavra corretamente antes de esgotar suas tentativas, você vence!

## Desenvolvedor
- Luana Gabriele de Sousa Costa