n = int(input())
teste = 0

while n != 0:
    joao = 0
    zezinho = 0

    teste += 1
    print(f"Teste {teste}")

    for _ in range(n):
        deposito = list(map(int, input().split()))
        joao += deposito[0]
        zezinho += deposito[1]
        print(joao-zezinho)
    print("")

    n = int(input())
