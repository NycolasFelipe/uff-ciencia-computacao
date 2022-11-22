n = int(input())
territorios = [int(i) for i in input().split()]
total = 0
soma = 0
cont = 0

for territorio in territorios:
    total += territorio

for i in range(len(territorios)):
    if soma < total/2:
        soma += territorios[i]
        cont += 1
    else:
        break

print(cont)
