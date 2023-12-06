file = open('dictionary/dictionary.txt','r')
linhas = file.read().split("\n")

palavras = []
significados = []

for i  in linhas:
    p, s = i.split(": ")
    palavras.append(p)
    significados.append(s)

dicionario_ncd = dict(zip(palavras, significados))

def wordle_dict():
    palavras_wordle = []
    significados_wordle = []

    for i in dicionario_ncd.keys():
        if len(i) == 5:
            palavras_wordle.append(i)
            significados_wordle.append(dicionario_ncd[i])

    return dict(zip(palavras_wordle, significados_wordle))      