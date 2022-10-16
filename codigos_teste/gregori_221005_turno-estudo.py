turno = input("Em qual turno vc estuda? ('M'-matutino 'V'-vespertino 'N'-noturno)    ")

if turno == "M":
    print("Bom dia!")

if turno == "V":
    print("Boa tarde!")
    
if turno == "N":
    print("Boa noite!")
    
while (turno!='M')and(turno!='V')and(turno!='N'):
    print("Valor Inválido!")
    break