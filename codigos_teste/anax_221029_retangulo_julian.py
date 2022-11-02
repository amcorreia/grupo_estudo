#
# Codigo original do colega Julian, onde a entrada das dimensoes eram feitas no "main()".
#
# EDIT: agora, a digitacao foi transferida para dentro da classe e acionada conforme o caso:
#   1.1) Se passar as dimensoes pra classe via argumentos (base, altura), pega dali.
#   1.2) Se nao passar via argumentos (), entao aciona o metodo pra pedir a digitacao ao usuario no terminal.
#   2)   Ao final, calcula a area e retorna o resultado.
#

class Retangulo():
    def __init__(self, *dimensoes):
        if len(dimensoes) == 2:        # 2: base e altura
            #self.base   = dimensoes[0] # acessa arg1 (base)
            #self.altura = dimensoes[1] # acessa arg2 (altura)
            # Acima ta OK, abaixo forma alternativa:
            self.base, self.altura = dimensoes
        else:
            self.le_dimensoes() # dimensoes nao passadas? Pede pro usuario!

    def le_dimensoes(self):
        self.base   = int(input("digite a base: "))
        self.altura = int(input("digite a altura: "))

    def calc_area(self):
        return self.base * self.altura

# OBS: escolha apenas uma das formas abaixo:

# Forma-1: passando as dimensoes por argumento
#
#retangulo_qualquer = Retangulo(2,3)

# Forma-2: nao passando nada, o proprio objeto chama o metodo de digitacao
#
retangulo_qualquer = Retangulo()

# Calcula a area e imprime
area = retangulo_qualquer.calc_area()
print("A area do retangulo eh: " + str(area))

