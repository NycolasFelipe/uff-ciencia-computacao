x, y = map(int, input().split())
matriz = [[0]*y for _ in range(x)]
encontrou = False

for i in range(x):
    linha = [int(i) for i in input().split()]
    for j in range(y):
        matriz[i][j] = linha[j]

print(matriz)

for i in range(1, x-1):
    for j in range(1, y-1):
        if matriz[i][j] == 42:
            if matriz[i-1][j-1] == 7 and \
                    matriz[i][j-1] == 7 and \
                    matriz[i+1][j-1] == 7 and \
                    matriz[i-1][j] == 7 and \
                    matriz[i+1][j] == 7 and \
                    matriz[i-1][j+1] == 7 and \
                    matriz[i][j+1] == 7 and \
                    matriz[i+1][j+1] == 7:
                encontrou = True
                print(i+1, j+1)
        if encontrou:
            quit()

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
