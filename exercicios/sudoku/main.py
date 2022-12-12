arquivo = open('matrizes.txt', 'r')
matrizes = arquivo.readlines()
n = int(input())
cont = 0

for m in range(n):
    cont += 1
    print(f"Instancia {cont}")
    print(matrizes)

    matriz = []
    linha = ''
    for i in range(9):
        linha += matrizes[i+(m*8)+(1*m)][0:-1]
        matriz += [linha.split()]
        linha = ''

    num_i = 0
    num_j = 0
    encontrou = False

    while not encontrou:
        if num_i == 8 and num_j == 8:
            break

        if num_j == 9:
            num_j = 0
            num_i += 1

        num = matriz[num_i][num_j]
        grid_i = 0
        grid_j = 0
        grid_i += num_i
        grid_j += num_j

        # checando linha e coluna
        for k in range(9):
            if k != num_j:
                if matriz[num_i][k] == num:
                    encontrou = True

            if k != num_i:
                if matriz[k][num_j] == num:
                    encontrou = True
                    break

        # checando grid
        while grid_i != 2 and grid_i != 5 and grid_i != 8:
            grid_i += 1
        while grid_j != 2 and grid_j != 5 and grid_j != 8:
            grid_j += 1

        for k in range(grid_i-2, grid_i+1):
            for l in range(grid_j-2, grid_j+1):
                if k != num_i and l != num_j:
                    if matriz[k][l] == num:
                        encontrou = True
                        break

        num_j += 1

    if encontrou:
        print("NAO")
    else:
        print("SIM")


arquivo.close()
