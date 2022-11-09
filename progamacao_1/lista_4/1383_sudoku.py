matriz = [[0]*9 for _ in range(3)]
n = int(input())
instancia = 0


for i in range(n):
    valores = [int(i) for i in input().split()]
    for j in range(len(valores)):
        matriz[i][j] = valores[j]


for _ in range(n):
    instancia += 1
    limpo_x = True
    limpo_y = True
    limpo_grid = True

    i = 0
    j = 0

    for _ in range(9):
        k = 0
        if j != k:
            print(i, j)
            if matriz[i][j] == matriz[i][k]:
                limpo_x = False
        k += 1

        if k == 2:
            i += 1
            j = 0
        else:
            j += 1

    print(limpo_x)
