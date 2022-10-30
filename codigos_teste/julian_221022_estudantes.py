class estudante:
  def __init__(self, nome, curso):
    self.nome = nome
    self.curso = curso

p1 = estudante("Chico", "python")
p2 = estudante("Tonho", "Java")

print(p1.nome)
print(p1.curso)
print()
print(p2.nome)
print(p2.curso)