primeiro = int(input('n1: '))
segundo  = int(input('n2 : '))
terceiro = int(input('n3: '))

maior = primeiro

if (segundo > maior):
        maior = segundo     #segundo maior que o primeiro imprime o segundo
if (terceiro > maior):
        maior = terceiro    #terceiro maior que o primeiro imprime o terceiro

print('Maior: ',maior)

menor = primeiro

if (segundo < menor):
        menor = segundo     #segundo menor que o primeiro imprime o segundo
if (terceiro < menor):
        menor = terceiro    #terceiro menor que o primeiro imprime o terceiro

print('Menor: ',menor)
