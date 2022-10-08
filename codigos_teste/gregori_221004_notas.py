n1 = int(input("Primeira nota: "))
n2 = int(input("Segunda nota: "))
n3 = int(input("Terceira nota: "))
n4 = int(input("Quarta nota: "))

media = n1 + n2 + n3 + n4 / 4

print("Notas:", n1, n2, n3, n4)

print("Média:",media)

if media >= 195:       # 60 + 60 + 60 + 60/4 = 195
    print("Aprovado")

if media < 195:
    print("Reprovado")    