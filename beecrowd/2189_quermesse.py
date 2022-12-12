n = int(input())
teste = 0

while n != 0:
    lista = list(map(int, input().split()))

    teste += 1
    print(f"Teste {teste}")

    for i in range(len(lista)):
        if i+1 == lista[i]:
            print(lista[i])
    print("")

    n = int(input())
