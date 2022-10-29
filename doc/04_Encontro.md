# Encontro #04

## Funcoes

    def <nome>(<argumentos>):
        <corpo>
        [return <alguma coisa>]


## Sem argumentos

	def dizoi():
		print("Ola mundo")

## Com argumentos, e valor default

	def multiplica(x, y=1):
	    return x * y

## Numero variavel de argumentos: Tupla

	def f(*args):
	    print(args)

	f(1, 2, 3, 4)

## Numero variavel de argumentos: Dict

	def f(**args):
	    print(args)

	d = {"param1": 2, "param2": 2)
	f(**d)
	
## Funcao aninhada	

	def funcao1 ():
	    def funcao0 ():
	        ...
	    x = funcao0()


## Funcao lambda

	f = lambda x, y, z: x + y + z
	f(1, 2, 3)


## Resolucao de variaveis: LEGB

####  Local / Enclosing / Global / Builtin



## Importar modulos


	import re

Importa todo o namespace do modulo, precisa usar o caminho completo para usar uma funcao, ex. re.search().

	from re import search

Importa apenas a funcao search do modulo re

		import numpy as np

Importa o modulo usando um apelido.

## Como nao deve importar um modulo

	from re import *

Esse metodo e desencorajado pela comunidade python porque vai importar todas as variaveis e funcoes 

