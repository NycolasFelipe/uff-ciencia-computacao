x, y = map(int, input().split())
matriz = [[0]*y for _ in range(x)]
encontrou = False

for i in range(x):
    linha = [int(i) for i in input().split()]
    for j in range(y):
        matriz[i][j] = linha[j]

for i in range(1, x-1):
    for j in range(1, y-1):
        if matriz[i][j] == 42:
            cont = 0
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if matriz[k][l] == 7:
                        cont += 1
            if cont == 8:
                encontrou = True
                print(i+1, j+1)
                break

if not encontrou:
    print('0 0')

# while:
#     if num_i < x-1 and num_j == y-1:
#         num_j = 0
#         num_i += 1
#     else:
#         num_j += 1

#     if num_i == x-1 and num_j == y:
#         break
