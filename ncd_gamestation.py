from dictionary.words import *
from wordle.wordle import *

while True:
    print("Digite o jogo que você quer:\n1. Wordle Clássico\n2. Forca Clássico\n3. Wordle Desafio\n4. Forca Desafio\n")
    jogo = input()

    if jogo == '1':
        teste = wordle()
        wordle_main(teste)
    elif jogo == '2':
        print("2")
    elif jogo == '3':
        print("3")
    elif jogo == '4':
        print("4")
    else:
        print("vixi")