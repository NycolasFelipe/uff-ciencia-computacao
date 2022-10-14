numero = int(input())
numeros = input().split()
numeros = [int(i) for i in numeros]
cont = 0

soma_numero = 0
for i in range(1, numero+1):
    soma_numero += i

soma_numeros = 0
for i in numeros:
    soma_numeros += i

distancia = int((soma_numeros-soma_numero)/numero)
numeros_escada = [i for i in range(distancia+1, numero+distancia+1)]

soma_numeros_escada = 0
for i in numeros_escada:
    soma_numeros_escada += i

if soma_numeros != soma_numeros_escada:
    print(-1)
else:
    escada = numeros[:]
    cont = 0

    while escada != numeros_escada:
        degrau = 0

        for i in range(len(escada)):
            if escada[i] > numeros_escada[i]:
                escada[i] -= 1
                degrau += 1
                cont += 1

        for i in range(len(escada)-1, -1, -1):
            if escada[i] < numeros_escada[i]:
                escada[i] += degrau
                break

    print(cont)

# nao funciona para 1 1 1 1 1
# rever
