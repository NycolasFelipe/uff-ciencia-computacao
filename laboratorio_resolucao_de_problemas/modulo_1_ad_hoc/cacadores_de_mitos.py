n = int(input())
matriz = [[0]*500 for _ in range(500)]
resposta = 0

while n > 0:
    n -= 1

    x, y = map(int, input().split())
    matriz[x-1][y-1] += 1

    for i in range(500):
        for j in range(500):
            if matriz[i][j] > 1:
                resposta = 1
                break
        if resposta == 1:
            n = 0
            break

print(resposta)
