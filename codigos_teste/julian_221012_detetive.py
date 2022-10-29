print("responda as perguntas com s ou n")
p1 = int(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
p2 = int(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
p3 = int(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
p4 = int(input("Devia para a vítima? 1/Sim ou 0/Não: "))
p5 = int(input("Já trabalhou com a vítima? 1/Sim ou 0/Não: "))
# soma o número de respostas
soma_respostas = p1 + p2 + p3 + p4 + p5
if (soma_respostas < 2):
 print("Inocente")
elif (soma_respostas == 2):
 print("Suspeito")
elif (3 <= soma_respostas <= 4):
 print("Cúmplice")
elif (soma_respostas == 5):
 print("Assassino")