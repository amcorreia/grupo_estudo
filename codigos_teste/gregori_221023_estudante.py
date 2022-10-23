class estudante:

    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
    pass

estudante1 = estudante('Jao','29','ingles')
estudante2 = estudante('jose','36','mecanico')

print(estudante1.nome, estudante1.idade, estudante1.curso)
print(estudante2.nome, estudante2.idade, estudante2.curso)