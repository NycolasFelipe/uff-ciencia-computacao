n = int(input())

while n != 0:
    matriz = [[0]*n for _ in range(n)]
    matriz[0][0] = 1

    for i in range(1, n):
        matriz[i][0] = matriz[i-1][0]*2
    for i in range(n):
        for j in range(1, n):
            matriz[i][j] = matriz[i][j-1]*2

    maior = len(str(matriz[n-1][n-1]))

    for i in range(n):
        linha = []
        for j in range(n):
            linha += [str(matriz[i][j])]
        for j in range(n):
            while len(linha[j]) < maior:
                linha[j] = ' ' + linha[j]

        texto = ''
        for j in range(n):
            if j == n-1:
                texto += linha[j]
            else:
                texto += linha[j] + ' '

        print(texto)

    print('')
    n = int(input())
