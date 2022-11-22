qtd, altura = map(int, input().split())
pinos = [int(i) for i in input().split()]+[0]
cont = 0

for i in range(len(pinos)-1):
    while pinos[i] != altura:
        if pinos[i] < altura:
            pinos[i] += 1
            pinos[i+1] += 1
        else:
            pinos[i] -= 1
            pinos[i+1] -= 1
        cont += 1

print(cont)
