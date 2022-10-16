#### 01 - Crie um programa para calcular o tamanho de uma string. (sem usar o len)

string = input("Digite uma palavra: ")

tamanho = 0
for char in string:
    tamanho = tamanho + 1

print(tamanho)

