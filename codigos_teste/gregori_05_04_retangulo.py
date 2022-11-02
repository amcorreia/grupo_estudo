class Retangulo():

    def base(self):
        self.base  = int(input("Base: "))
    def altura(self):
        self.altura = int(input("Altura: "))
    def Area_retangulo(self):
       print("Área do retangulo: " , self.base * self.altura)

re = Retangulo()
re.base()
re.altura()
re.Area_retangulo()