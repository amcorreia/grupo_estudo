#### 02 - Faça um Programa que leia três números e mostre o maior e o menor deles

# [1] Jeito MUITO TOSCO: modo aprendizagem  ;)
#     Solucao HARD-CODED (engessado pra digitacao FIXA de tres numeros)
#
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

print()  # Pra dar uma espacada entre a digitacao acima e o resultado abaixo

# OBS: me bati um monte por querer tratar o caso de quando tem 2 iguais
#      e 1 diferente, ou todos iguais.
#      Tenho outros ALGORs em mente...

# --- Testando qual eh o MAIOR ---

if n1 == n2 == n3:    # Testando se todos sao iguais
    print("Os 3 numeros sao iguais:", n1)
    # Caindo fora... todos sao iguais, nao tem MAIOR nem MENOR!
    exit(1)
elif n1 >= n2 and n1 >= n3:        # Testando o n1 maior
    print("O maior numero eh", n1)
elif n2 >= n1 and n2 >= n3:        # Testando o n2 ...
    print("O maior numero eh", n2)
elif n3 >= n1 and n3 >= n2:        # Testando o n3
    print("O maior numero eh", n3)
else:
    print("ERR: Tem bug no meu algoritmo!") # situacao impossivel?

# --- Testando qual eh o MENOR ---

# print("O menor numero eh... NAO SEI, esse nao fiz (ainda)")

if n1 <= n2 and n1 <= n3:          # Testando o n1 menor
    print("O menor numero eh", n1)
elif n2 <= n1 and n2 <= n3:        # Testando o n2 ...
    print("O menor numero eh", n2)
elif n3 <= n1 and n3 <= n2:        # Testando o n3
    print("O menor numero eh", n3)

