# 04 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso

turnos = {"M": "Bom Dia!", "V": "Boa Tarde!", "N": "Boa Noite!"}

letra_turno = input("Qual seu turno: (M)atutino, (V)espertino ou (N)oturno ? ")

if letra_turno in turnos:
    print(turnos[letra_turno])
else:
    print("Valor Inválido!")

