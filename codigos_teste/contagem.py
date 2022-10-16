contagem_str = "grupo de estudo"
res = {i : contagem_str.count(i) for i in set(contagem_str)}
print ("a contagem eh :" +  str(res))