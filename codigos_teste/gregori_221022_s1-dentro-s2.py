s1 = input('Digite um nome: ')
s2 = input('Digite outro nome:')

meio = len(s1) // 2 

s = s1[:meio] + s2 + s1[meio:]
 
print(s)