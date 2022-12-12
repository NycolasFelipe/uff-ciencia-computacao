pares = 0

valores = [int(i) for i in input().split()]
n = valores[0]
i = valores[1]
f = valores[2]

vetores = [int(i) for i in input().split()]

for k in range(len(vetores)):
    for l in range(k, len(vetores)):
        if k != l:
            if i <= vetores[k]+vetores[l] <= f:
                pares += 1

print(pares)
