perguntas = ['Telefonou para a vítima?',
            'Esteve no local do crime?',
            'Mora perto da vítima??',
            'Tinha dívidas com a vítima?',
            'Já trabalhou com a vítima?']

count = 0

respostas = False

for i in range(len(perguntas)):
    respostas = bool(int(input('{}\n'.format(perguntas[i]))))     # digite 0 (p/ Não) e 1 (p/ Sim) 
    if(respostas==True):
        count+=1

if(count == 2):
    print("Suspeito")
elif(count == 3 or count == 4):
    print("Cúmplice")
elif (count == 5):
    print("Assassino")
else:
    print("Inocente")