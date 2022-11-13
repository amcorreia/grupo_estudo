class retangulo():
    def __init__(self, l, w):
        self.base = int(input("digite a base: "))
        self.alt  = int(input("digite a altura: "))

    def area_ret(self):
        return self.base*self.alt

retangulo2 = retangulo(1, 2)
print(retangulo2.area_ret())

