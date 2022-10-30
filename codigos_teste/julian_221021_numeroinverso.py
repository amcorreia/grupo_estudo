num = int(input("digite um numero: "))

num_rev = 0

while (num > 0):
    # Logic
    reverso = num % 10
    num_rev = (num_rev * 10) + reverso
    num = num // 10

print("o numero reverso eh : {}".format(num_rev))