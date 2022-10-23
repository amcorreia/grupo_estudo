from random import shuffle

def embaralhapalavra(p):
    p = p.upper()
    p = list(p)
    shuffle(p)
    palavra = ''
    for i in p:
        palavra += i
    print(palavra)

p = input("Informe uma palavra: ")

embaralhapalavra(p)