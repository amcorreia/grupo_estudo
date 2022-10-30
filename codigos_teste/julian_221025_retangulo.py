class Retangulo():
    def __init__(self, b, a):
        self.base = b
        self.alt = a

    def area_ret(self):
        return self.base * self.alt
bs = int(input("digite a base: "))
al = int(input("digite a altura: "))

Retangulo2 = Retangulo(bs, al)
print ("a area do retangulo eh: ")
print(Retangulo2.area_ret())