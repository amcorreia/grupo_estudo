# 03 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela

notas = []
num_notas = 4

# Digitacao das notas e guardando na lista
for i in range(num_notas):
    nota = int(input("Digite a nota " + str(i+1) + ": ")) # um cast basico!
    notas.append(nota)

# Somatoria das notas e aproveitando o "for" pra mostrar cada uma
i = 1
soma_notas = 0
for nota in notas:
    #soma_notas = soma_notas + nota
    soma_notas += nota
    print("Nota", i, ":", nota)
    i += 1

# Calculo da media
media_notas = soma_notas / num_notas

# Soma vem como debug  ;)
print("Soma das notas :", soma_notas)
print("Media das notas:", media_notas)

