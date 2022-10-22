

# Encapsulamento / Heranca / Interface / Polimorfismo

def acelerar_moto():
    print("acelerar moto")

def acelerar_carro():
    print("acelerar carro")

class AutomovelInterface:

    def acelerar(self):
        raise NotImplementedError()

class Carro(AutomovelInterface):

    def __init__(self, modelo, metodo_aceleracao):
        self.modelo = modelo
        self._metodo_aceleracao = metodo_aceleracao

    def acelerar(self):
        self._metodo_aceleracao()

    def frear(self):
        pass

class Moto(AutomovelInterface):
    def __init__(self, modelo, metodo_aceleracao):
        self.modelo = modelo
        self._metodo_aceleracao = metodo_aceleracao

    def acelerar(self):
        self._metodo_aceleracao()


carro1 = Carro("Toyota", acelerar_carro)
moto1 = Moto("Kawasaki", acelerar_moto)


#for auto in [carro1, moto1]:
#    print("veiculo {} => Acelerar {}".format(auto.modelo, auto.acelerar()))


class A:
    x = 10
    z = 10

class B:
    x = 20
    y = 20

class D(A, B):
    z = 30

#i1 = D()

#print(i1.x) # 10
#print(i1.y) # 20
#print(i1.z) # 30

class Dog:
    """Uma doc aqui."""

    tipo = "canino"

    def __init__(self, nome):
        self.nome = nome
        self.nomes = []

    def __add__(self, other):
        self.nomes.append(other.nome)

    def __str__(self):
        return "Dog {} au au..".format(self.nome)


d1 = Dog("maicao")
d2 = Dog("pedro")
d3 = Dog("jukinha")


print(d1.nomes)
d1 + d2
print(d1.nomes)
d1 + d3
print(d1.nomes)

#print(d1.nome)
#print(d2.tipo)
#print(d2.nome)

texto = """
Esse eh um texto que
eu quero manter a formatacao

"""

def func():
    """essa funcao nao faz nada de util."""
    pass
