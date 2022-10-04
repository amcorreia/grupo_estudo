n1 = int(input("Primeira nota: "))
n2 = int(input("Segunda nota: "))
n3 = int(input("Terceira nota: "))
n4 = int(input("Quarta nota: "))

media = n1 + n2 + n3 + n4 / 2

print("Notas:", n1, n2, n3, n4)

print("Média:",media)

if media >= 210:       # 60 + 60 + 60 + 60/2 = 210
    print("Aprovado")

if media < 210:
    print("Reprovado")    