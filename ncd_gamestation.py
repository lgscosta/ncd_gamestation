from dictionary.words import *
from wordle.wordle import *

print("Digite o jogo que você quer:\n1. Wordle Clássico\n2. Forca Clássico\n3. Wordle Desafio\n4. Forca Desafio\n")
jogo = input()

if jogo == '1':
    teste = wordle()
    wordle_main(teste)