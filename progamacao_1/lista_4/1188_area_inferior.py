n = 12
matriz = [[0]*n for i in range(n)]
tipo = input()
soma = 0
cont = 0

ini_v = int(n//2)+1
ini_he = int(n//2)-1
ini_hd = int(n//2)

for i in range(n):
    for j in range(n):
        matriz[i][j] = float(input())

for i in range(ini_v, n):
    for j in range(ini_he, ini_hd+1):
        soma += matriz[i][j]
        cont += 1
    ini_he -= 1
    ini_hd += 1

if tipo == "S":
    print(f"{format(soma, '.1f')}")
elif tipo == "M":
    print(f"{format(soma/cont, '.1f')}")
