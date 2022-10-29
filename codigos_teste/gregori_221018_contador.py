contador = input("Digite uma palavra: ")
quantidade = {}

for i in contador:
    if i in quantidade:
        quantidade[i] += 1
    else: 
        quantidade[i] = 1

print("A palavra tem: " + str(quantidade))