cont_caracteres = input("Digite uma palavra: ")

frequencia = {}

for i in cont_caracteres:
    if i in frequencia:
        frequencia[i] += 1
    else:
        frequencia[i] = 1

print(cont_caracteres + str(frequencia))