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
- [ ] O jogo deve mostrar uma mensagem de vitória ou derrota quando o jogador adivinhar a palavra ou esgotar suas tentativas e o significado da palavra.

## Entrega Extra (E4)
- [ ] O jogo deve ter uma versão de dueto, onde tenta-se adivinhar duas palavras simultaneamente.
- [ ] O jogo deve ter dicas.

## Como jogar
O jogo é simples: você tem seis tentativas para adivinhar uma palavra de cinco letras. Cada vez que você insere uma palavra, o jogo fornece feedback sobre a posição e a presença das letras na palavra secreta.

- <b style="color: #bcd246">Verde:</b> A letra está na palavra e na posição correta.
- <b style="color: #f4ad42">Amarelo:</b> A letra está na palavra, mas na posição errada.
- <b style="color: #c73d52">Vermelho:</b> A letra não está na palavra.
Se você adivinhar a palavra corretamente antes de esgotar suas tentativas, você vence!

## Desenvolvedor
- Luana Gabriele de Sousa Costa

### Verificar:
- [ ] Usar a função reset antes de começar o loop principal ao invés de usar cada comando.
- [ ] Usar dicionário ao invés de lista na lista de palavras
- [ ] Não desenhe diretamente na tela, mas em outra superfície. Em seguida, dimensione essa outra superfície para o tamanho da tela e cegue-a na tela. (solução para redmensionar)
- [ ] Bug das letras depois de acertar



íóúéá
êôâ
ç
ãõ