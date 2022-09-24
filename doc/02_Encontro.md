# Encontro #02


## Expressões aritméticas


| operador  |   | exemplo |
|---|---|----|
| **  |  potência | 4 ** 2 = 16 |
| *  | multiplicação  |  4 * 2 = 8 | 
| /  |  divisão | 10 / 3 = 3.3333 |
| // | divisão inteira | 10 // 3 = 3 |
| %  | resto da divisão | 10 % 3 = 1 |


## Operadores relacionais

|||
|--|--|
| == | igualdade |
| != | diferença |
| > >= | maior, maior igual|
| < <= | menor, menor igual |

## Operadores lógicos

|||
|--|--|
|and | E  |
|or| OU  |
|not| Negação |

## Precedencia das operações:
https://docs.python.org/3/reference/expressions.html#operator-precedence

## Tipos de dados

Declaração de variáveis

variável = expressão
        
    idade = 17


### Int

    idade = 36
type(idade)

### Float
    altura = 1.89

### String
    nome = "Alessandro"
    >>> nome
    'Alessandro'
    >>> nome[3:7]
    'ssan'
    >>> nome[1]
    'l'
    >>> nome[-1]
    'o'
    >>> nome[-2]
    'r'
    >>> nome[-3]
    'd'
    >>> nome[-3:2]
    ''
    >>> nome[2:-3]
    'essan'
    
    
### List

    >>> carro = ['fusca', 'chevette', 'opala', 'corcel']
    >>> type(carro)
    <class 'list'>
    
#### Funções tipo list
.append() # Adiciona elemento ao final da lista
>>> carro.append('kombi')

.pop(0) # Remove elemento do inicio da lista
>>> carro.pop(0)
'chevette'

.len() # Retorna o tamanho da lista
>>> len(carro)
4

.sort() # Ordena a lista in-place
>>> carro.sort()
>>> carro
['chevette', 'corcel', 'fusca', 'opala']

.extend() # adiciona o elementos de outra lista
>>> carro
['chevette', 'corcel', 'fusca', 'opala']
>>> carros_novos
['polo', 'jetta', 'c180']
>>> carro.extend(carros_novos)
>>> carro
['chevette', 'corcel', 'fusca', 'opala', 'polo', 'jetta', 'c180']


#### List comprehension
>>> quadrados = [n ** 2 for n in range(10)]
>>> quadrados
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


