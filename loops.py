# While

#while <expr>: # Enquanto expr for verdadeira, executa
#    <stmt>

#n = 5
#while n > 0:
#    n = n - 1
#    print(n)


#lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]
#while lista:
#    print(lista.pop())


lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# break / continue

# n = 0
# while lista:
#     if n == 3:
#         break
#     n = n + 1
#     print(lista.pop())


# while True:
#     dado = input("Deseja sair (Y/S)? ")
#     if dado in ["y", "Y", "s", "S"]:
#         break

# mostrar numeros pares do indice
# n = len(lista)
# while n > 0:
#     n = n - 1
#     if n % 2:
#         continue
#     print(lista[n])


# FOR

#for key in <colecao/lista/iterador>:
#    <stmt>


#for k in [1, 2, 3, 4, 5]:
#    print(k)

#for s in "joaodocaminhao":
#    print(s)

#lista = ["a", "b", "c"]
#for i in enumerate(lista):
#    print(i)


# usando for
lista_de_quadrados = []
for i in range(10):
    lista_de_quadrados.append(i**2)
print(lista_de_quadrados)

# usando list comprehension
lista_de_quadrados2 = [i**2 for i in range(10)]
print(lista_de_quadrados2)
