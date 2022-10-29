# Codigo base do colega Julian, pois nao fiz os exercicios !!

class Retangulo():
    def __init__(self):
        self.base   = int(input("digite a base: "))
        self.altura = int(input("digite a altura: "))

    def area_ret(self):
        return self.base * self.altura

area_retangulo = Retangulo()
print("A area do retangulo eh: " + str(area_retangulo.area_ret()))
