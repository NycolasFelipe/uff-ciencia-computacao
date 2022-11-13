while True:
    try:
        n, m = map(int, input().split())
        matriz = [[0]*m for _ in range(n+1)]
        distancia = 0
        inicio = [0, 0]
        fim = [0, 0]

        for i in range(n):
            linha = [int(i) for i in input().split()]
            for j in range(len(linha)):
                matriz[i][j] = linha[j]
                if linha[j] == 1:
                    inicio[0] = i
                    inicio[1] = j
                elif linha[j] == 2:
                    fim[0] = i
                    fim[1] = j

        while inicio != fim:
            if inicio[0] > fim[0]:
                inicio[0] -= 1
                distancia += 1
            elif inicio[0] < fim[0]:
                inicio[0] += 1
                distancia += 1

            if inicio[1] > fim[1]:
                inicio[1] -= 1
                distancia += 1
            elif inicio[1] < fim[1]:
                inicio[1] += 1
                distancia += 1

        print(distancia)

    except EOFError:
        break
