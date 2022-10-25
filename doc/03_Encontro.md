
# Encontro #03

## Condicionais

	if <expressao>:   # Se a expressao for verdadeira
		<stmt1>       # Executa stmt1
	elif <expr2>:     # senao se expr2 for verdadeira
		<stmt2>       # Executa smt2
	else:             # senao
		<stmt3>       # Executa stmt3

Exemplo if/else

	numero_1 = int(input("Digite um numero: "))  
	if not (numero_1 % 2):  
	    print("Par")  
	else:  
	    print("impar")  

Exemplo completo:

	n1 = int(input("Digite o primeiro numero: "))
	n2 = int(input("Digite o segundo numero: "))

	if n1 > n2:
		print("N1 eh maior que N2: n1: {} n2: {}".format(n1, n2))
	elif n1 < n2:
		print("N1 eh menor que N2: n1: {} n2: {}".format(n1, n2))
	else:
		print("Sao iguais!")
  
 ### One-liner
 
	 debugging = True
	 if debugging: print("chegou nesta linha")

### Ternary

< variavel> = < expr> if < cond_expr> else < expr2>

	 n1 = 7
	 n2 = 30
	 n1_eh_maior = True if n1 > n2 else False

Outra forma

	vai_chover = False  
	print("Vou andar de ", "fusca" if vai_chover else "moto")  
  

## Loops


	while <expr>:    # Enquanto a <expr> for verdadeira
		<stmt>       # executa <stmt>


Exemplo 

	n = 5  
	while n > 0:  
	    n = n - 1  
	    print(n)  
  
 Usando lista
 
	lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]   
	while lista:                 # enquanto tiver elemento na lista
	    print(lista.pop())       # remove o ultimo elemento e imprime   
  
  
## break / continue  
  
  Break: Interrompe a execução do laço

	lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  
	n = 0  
	while lista:  
		if n == 3:  
			break  
		n = n + 1  
	print(lista.pop())  
  
  Exemplo:
  
	while True:  
		dado = input("Deseja sair (Y/S)? ")  
		if dado in ["y", "Y", "s", "S"]:  
			break  
  
 # mostrar numeros pares do indice  

	n = len(lista)  
	while n > 0:  
		n = n - 1  
		if n % 2:  
			continue  
	print(lista[n])  
  
  
# FOR  
  
	for key in <colecao/lista/iterador>:  
	    <stmt>  
  
  
  Exemplo1
  
	for k in [1, 2, 3, 4, 5]:  
	    print(k)  

  Exemplo2
  
	for s in "joaodocaminhao":  
	    print(s)  
  
  Exemplo3

	lista = ["a", "b", "c"]  
	for i in enumerate(lista):  
	    print(i)  
  
  
# usando for  

	lista_de_quadrados = []  
	for i in range(10):  
	    lista_de_quadrados.append(i**2)  
	print(lista_de_quadrados)  
  
  
# usando list comprehension  

	lista_de_quadrados2 = [i**2 for i in range(10)]  
	print(lista_de_quadrados2)

